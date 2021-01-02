# Cesium-通过Shader添加雨雪天气效果

  - [前言](#%E5%89%8D%E8%A8%80)
  - [实验效果](#%E5%AE%9E%E9%AA%8C%E6%95%88%E6%9E%9C)
  - [代码](#%E4%BB%A3%E7%A0%81)
    - [自定义GLSL代码](#%E8%87%AA%E5%AE%9A%E4%B9%89glsl%E4%BB%A3%E7%A0%81)
    - [外部调用](#%E5%A4%96%E9%83%A8%E8%B0%83%E7%94%A8)
  - [总结](#%E6%80%BB%E7%BB%93)
  - [参考链接](#%E5%8F%82%E8%80%83%E9%93%BE%E6%8E%A5)

## 前言
作为一个三维地球，在场景中来点雨雪效果，貌似可以增加一点真实感。Cesium 官网 [Demo](https://sandcastle.cesium.com/index.html?src=Particle%20System%20Weather.html) 中有天气系统的实例，用的是 Cesium 中的粒子系统做的。效果如下图所示，粒子系统的本质是向场景中添加了很多物体，用 BillBoard 技术展现。这种实现方式有一个麻烦的地方就是当视角变化(拉近、拉远、平移、旋转)时，粒子就会变化，甚至会消失，很影响体验。考虑用 shader 的方式直接模拟雨雪效果，恰好发现了 Catzpaw 大神写的模拟雨雪的 shader，果断增添到 Cesium 中。

![](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201030142218.png)

## 实验效果
![雪](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201030143549.gif)

![雨](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201030145003.gif)

## 代码
### 自定义GLSL代码
```js
/**
 * 后期处理控制类
 * postProcessController.js
 */

const Snow = `
uniform sampler2D colorTexture; //输入的场景渲染照片
varying vec2 v_textureCoordinates;

float snow(vec2 uv, float scale) {
    float time = czm_frameNumber / 60.0;
    float w = smoothstep(1., 0., -uv.y * (scale / 10.));
    if (w < .1)
        return 0.;
    uv += time / scale;
    uv.y += time * 2. / scale;
    uv.x += sin(uv.y + time * .5) / scale;
    uv *= scale;
    vec2 s = floor(uv), f = fract(uv), p;
    float k = 3., d;
    p = .5 + .35 * sin(11. * fract(sin((s + p + scale) * mat2(7, 3, 6, 5)) * 5.)) - f;
    d = length(p);
    k = min(d, k);
    k = smoothstep(0., k, sin(f.x + f.y) * 0.01);
    return k * w;
}

void main(void) {
    vec2 resolution = czm_viewport.zw;
    vec2 uv = (gl_FragCoord.xy * 2. - resolution.xy) / min(resolution.x, resolution.y);
    vec3 finalColor = vec3(0);
    // float c=smoothstep(1.,0.3,clamp(uv.y*.3+.8,0.,.75));
    float c = 0.0;
    c += snow(uv, 30.) * .0;
    c += snow(uv, 20.) * .0;
    c += snow(uv, 15.) * .0;
    c += snow(uv, 10.);
    c += snow(uv, 8.);
    c += snow(uv, 6.);
    c += snow(uv, 5.);
    finalColor = (vec3(c));                                                                      //屏幕上雪的颜色
    gl_FragColor = mix(texture2D(colorTexture, v_textureCoordinates), vec4(finalColor, 1), 0.5); //将雪和三维场景融合
}
`

const Rain = `
uniform sampler2D colorTexture; //输入的场景渲染照片
varying vec2 v_textureCoordinates;

float hash(float x) { return fract(sin(x * 133.3) * 13.13); }

void main(void) {

    float time = czm_frameNumber / 60.0;
    vec2 resolution = czm_viewport.zw;

    vec2 uv = (gl_FragCoord.xy * 2. - resolution.xy) / min(resolution.x, resolution.y);
    vec3 c = vec3(.6, .7, .8);

    float a = -.4;
    float si = sin(a), co = cos(a);
    uv *= mat2(co, -si, si, co);
    uv *= length(uv + vec2(0, 4.9)) * .3 + 1.;

    float v = 1. - sin(hash(floor(uv.x * 100.)) * 2.);
    float b = clamp(abs(sin(20. * time * v + uv.y * (5. / (2. + v)))) - .95, 0., 1.) * 20.;
    c *= v * b; //屏幕上雨的颜色

    gl_FragColor = mix(texture2D(colorTexture, v_textureCoordinates), vec4(c, 1), 0.5); //将雨和三维场景融合
}
`

export function createSnowStage(Cesium) {
    var snow = new Cesium.PostProcessStage({
        name: 'czm_snow',
        fragmentShader: Snow
    });
    return snow;
}

export function createRainStage(Cesium) {
    var rain = new Cesium.PostProcessStage({
        name: 'czm_rain',
        fragmentShader: Rain
    });
    return rain;
}
```

生成雨和雪的 glsl 代码很神奇，就是单纯的数学计算，意识到学好数学还是很重要的，再次向大神膜拜 ○|￣|_

### 外部调用
```js
// 开启后期处理
var collection = viewer.scene.postProcessStages;
var snow = createSnowStage(Cesium)
// var rain = createRainStage(Cesium)
// collection.add(rain)
collection.add(snow)
viewer.scene.skyAtmosphere.hueShift = -0.8;
viewer.scene.skyAtmosphere.saturationShift = -0.7;
viewer.scene.skyAtmosphere.brightnessShift = -0.33;
viewer.scene.fog.density = 0.001;
viewer.scene.fog.minimumBrightness = 0.8;
```

最终效果就如上图展示的那样~

## 总结
通过 Shader 这种方式模拟雨雪可以不受视点位置的影响，相当于是一个全屏的后处理，当然在效果模拟上还有可以增强的地方。本文描写的步骤可以作为大家在 Cesium 上添加后期处理效果步骤的一个参考~

## 参考链接
[Cesium应用篇--添加雨雪天气](https://www.cnblogs.com/webgl-angela/p/9846990.html)