# Cesium-通过Shader添加圆形扩散效果

  - [实验效果](#%E5%AE%9E%E9%AA%8C%E6%95%88%E6%9E%9C)
  - [代码](#%E4%BB%A3%E7%A0%81)
    - [自定义GLSL代码](#%E8%87%AA%E5%AE%9A%E4%B9%89glsl%E4%BB%A3%E7%A0%81)
    - [外部调用](#%E5%A4%96%E9%83%A8%E8%B0%83%E7%94%A8)
  - [总结](#%E6%80%BB%E7%BB%93)
  - [参考链接](#%E5%8F%82%E8%80%83%E9%93%BE%E6%8E%A5)

## 实验效果
![实验效果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201030163125.gif)

## 代码
### 自定义GLSL代码
```js
const DynamicCircle = `
uniform sampler2D colorTexture;    //颜色纹理
uniform sampler2D depthTexture;    //深度纹理
varying vec2 v_textureCoordinates; //纹理坐标
uniform vec4 u_scanCenterEC;       //扫描中心
uniform vec3 u_scanPlaneNormalEC;  //扫描平面法向量
uniform float u_radius;            //扫描半径
uniform vec4 u_scanColor;          //扫描颜色

// 根据二维向量和深度值 计算距离camera的向量
vec4 toEye(in vec2 uv, in float depth) {
    vec2 xy = vec2((uv.x * 2.0 - 1.0), (uv.y * 2.0 - 1.0));
    // 看看源码中关于此函数的解释是，cesium系统自动生成的4*4的反投影变换矩阵
    // 从clip坐标转为眼睛坐标，clip坐标是指顶点着色器的坐标系统gl_position输出的
    vec4 posInCamera = czm_inverseProjection * vec4(xy, depth, 1.0);
    posInCamera = posInCamera / posInCamera.w; //将视角坐标除深度分量
    return posInCamera;
}

// 点在平面上的投影，输入参数为 平面法向量，平面起始点，测试点
vec3 pointProjectOnPlane(in vec3 planeNormal, in vec3 planeOrigin, in vec3 point) {
    // 计算测试点与平面起始点的向量
    vec3 v01 = point - planeOrigin;
    // 平面法向量与 测试点与平面上的点 点积  点积的几何意义，b在a上的投影长度，
    // 即v01在平面法向量上的长度
    float d = dot(planeNormal, v01);
    // planeNormal * d 即为v01在平面法向量上的投影向量
    // 根据三角形向量相加为0的原则 即可得点在平面上的投影
    return (point - planeNormal * d);
}

// 获取深度值，根据纹理坐标获取深度值
float getDepth(in vec4 depth) {
    float z_window = czm_unpackDepth(depth);  //源码解释将一个vec4向量还原到0，1内的一个数
    z_window = czm_reverseLogDepth(z_window); // czm_reverseLogDepth解开深度
    float n_range = czm_depthRange.near;      //
    float f_range = czm_depthRange.far;
    return (2.0 * z_window - n_range - f_range) / (f_range - n_range);
}

void main() {
    gl_FragColor = texture2D(colorTexture, v_textureCoordinates);          //片元颜色
    float depth = getDepth(texture2D(depthTexture, v_textureCoordinates)); //根据纹理获取深度值
    vec4 viewPos = toEye(v_textureCoordinates, depth);                     //根据纹理坐标和深度值获取视点坐标
    // 点在平面上的投影，平面法向量，平面中心，视点坐标
    vec3 prjOnPlane = pointProjectOnPlane(u_scanPlaneNormalEC.xyz, u_scanCenterEC.xyz, viewPos.xyz);
    // 计算投影坐标到视点中心的距离
    float dis = length(prjOnPlane.xyz - u_scanCenterEC.xyz);
    // 如果在扫描半径内，则重新赋值片元颜色
    if (dis < u_radius) {
        // 计算与扫描中心的距离并归一化
        float f = dis / u_radius;
        // 原博客如下，实际上可简化为上式子
        // float f = 1.0 -abs(u_radius - dis) / u_radius;
        // 四次方
        f = pow(f, 2.0);
        // mix(x, y, a): x, y的线性混叠， x(1-a)  y*a;,
        // 效果解释：在越接近扫描中心时，f越小，则片元的颜色越接近原来的，相反则越红
        gl_FragColor = mix(gl_FragColor, u_scanColor, f);
    }
}
`

export function createDynamicCircleStage(viewer, Cesium, cartographicCenter, maxRadius, scanColor, duration) {
    // 中心点
    var _Cartesian3Center = Cesium.Cartographic.toCartesian(cartographicCenter);
    var _Cartesian4Center = new Cesium.Cartesian4(_Cartesian3Center.x, _Cartesian3Center.y, _Cartesian3Center.z, 1);

    // 中心点垂直高度上升500m的坐标点，目的是为了计算平面的法向量
    var _CartographicCenter1 = new Cesium.Cartographic(cartographicCenter.longitude, cartographicCenter.latitude, cartographicCenter.height + 500);
    var _Cartesian3Center1 = Cesium.Cartographic.toCartesian(_CartographicCenter1);
    var _Cartesian4Center1 = new Cesium.Cartesian4(_Cartesian3Center1.x, _Cartesian3Center1.y, _Cartesian3Center1.z, 1);

    // 当前时间
    var _time = (new Date()).getTime();

    // 转换成相机参考系后的中心点，上升高度后的中心点以及平面法向量
    var _scratchCartesian4Center = new Cesium.Cartesian4();
    var _scratchCartesian4Center1 = new Cesium.Cartesian4();
    var _scratchCartesian3Normal = new Cesium.Cartesian3();

    // 自定义PostProcessStage
    var dynamicCircle = new Cesium.PostProcessStage({
        fragmentShader: DynamicCircle,
        uniforms: {
            // 将中心点坐标转化到相机参考系
            u_scanCenterEC: function () {
                return Cesium.Matrix4.multiplyByVector(viewer.camera._viewMatrix, _Cartesian4Center, _scratchCartesian4Center);
            },
            // 计算相机参考系下的平面法向量
            u_scanPlaneNormalEC: function () {
                var temp = Cesium.Matrix4.multiplyByVector(viewer.camera._viewMatrix, _Cartesian4Center, _scratchCartesian4Center);
                var temp1 = Cesium.Matrix4.multiplyByVector(viewer.camera._viewMatrix, _Cartesian4Center1, _scratchCartesian4Center1);
                _scratchCartesian3Normal.x = temp1.x - temp.x;
                _scratchCartesian3Normal.y = temp1.y - temp.y;
                _scratchCartesian3Normal.z = temp1.z - temp.z;

                Cesium.Cartesian3.normalize(_scratchCartesian3Normal, _scratchCartesian3Normal);
                return _scratchCartesian3Normal;
            },
            // 动态半径
            u_radius: function () {
                return maxRadius * (((new Date()).getTime() - _time) % duration) / duration;
            },
            u_scanColor: scanColor
        }
    });
    return dynamicCircle;
}
```

### 外部调用
```js
var lng = 117.90365282568267
var lat = 40.16773126252592
var cartographicCenter = new Cesium.Cartographic(Cesium.Math.toRadians(lng), Cesium.Math.toRadians(lat), 0)
var scanColor = new Cesium.Color(1.0, 0.0, 0.0, 1)
// 创建自定义的 PostProcessStage
var dynamicCircle = createDynamicCircleStage(viewer, Cesium, cartographicCenter, 1500, scanColor, 4000)
// 添加进场景
viewer.scene.postProcessStages.add(dynamicCircle)
```

## 总结
实现该效果的原理就是：判断片元与圆心的距离是否大于半径，如果小于半径，则更改该片元的颜色，否则使用原来的片元颜色。

我们看到的是一个圆形，实际上，该圆形也是由若干个片元构成的~

## 参考链接
[cesium着色器学习系列7- PostProcessStage渲染 后处理，以圆形扩散为例](https://blog.csdn.net/A873054267/article/details/105365862)