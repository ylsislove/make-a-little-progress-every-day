# Cesium-坐标系统详解

  - [Cesium中几个重要的坐标对象](#cesium%E4%B8%AD%E5%87%A0%E4%B8%AA%E9%87%8D%E8%A6%81%E7%9A%84%E5%9D%90%E6%A0%87%E5%AF%B9%E8%B1%A1)
    - [世界坐标（Cartesian3：笛卡尔空间直角坐标系）](#%E4%B8%96%E7%95%8C%E5%9D%90%E6%A0%87cartesian3%E7%AC%9B%E5%8D%A1%E5%B0%94%E7%A9%BA%E9%97%B4%E7%9B%B4%E8%A7%92%E5%9D%90%E6%A0%87%E7%B3%BB)
    - [经纬度坐标（Degrees）](#%E7%BB%8F%E7%BA%AC%E5%BA%A6%E5%9D%90%E6%A0%87degrees)
    - [弧度（Cartographic）](#%E5%BC%A7%E5%BA%A6cartographic)
  - [相互转换](#%E7%9B%B8%E4%BA%92%E8%BD%AC%E6%8D%A2)
    - [经纬度（Degrees）转换为世界坐标（Cartesian3）](#%E7%BB%8F%E7%BA%AC%E5%BA%A6degrees%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%B8%96%E7%95%8C%E5%9D%90%E6%A0%87cartesian3)
    - [世界坐标（Cartesian3）转换为经纬度（Degrees）](#%E4%B8%96%E7%95%8C%E5%9D%90%E6%A0%87cartesian3%E8%BD%AC%E6%8D%A2%E4%B8%BA%E7%BB%8F%E7%BA%AC%E5%BA%A6degrees)
    - [弧度（Cartographic）和经纬度（Degrees）](#%E5%BC%A7%E5%BA%A6cartographic%E5%92%8C%E7%BB%8F%E7%BA%AC%E5%BA%A6degrees)
    - [屏幕坐标（Cartesian2）和世界坐标（Cartesian3）相互转换](#%E5%B1%8F%E5%B9%95%E5%9D%90%E6%A0%87cartesian2%E5%92%8C%E4%B8%96%E7%95%8C%E5%9D%90%E6%A0%87cartesian3%E7%9B%B8%E4%BA%92%E8%BD%AC%E6%8D%A2)

## Cesium中几个重要的坐标对象
### 世界坐标（Cartesian3：笛卡尔空间直角坐标系）
```js
new Cesium.Cartesian3(x, y, z)
```

![世界坐标](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200924110015.png)

可以看作，以椭球中心为原点的空间直角坐标系中的一个点的坐标。

### 经纬度坐标（Degrees）
地理坐标系，坐标原点在椭球的质心。

经度：参考椭球面上某点的大地子午面与本初子午面间的两面角。东正西负。

纬度 ：参考椭球面上某点的法线与赤道平面的夹角。北正南负。

Cesuim中没有具体的经纬度对象，要得到经纬度首先需要计算为弧度，再进行转换。

![经纬度坐标](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200924110248.jpg)


### 弧度（Cartographic）
```js
new Cesium.Cartographic(longitude, latitude, height)
```

这里的参数也叫做，longitude，latitude，即经度和纬度。

但是是用弧度表示的经纬度，经纬度其实就是角度，可以看上面的解释。弧度即角度对应弧长是半径的倍数。

角度转弧度 π / 180 × 角度

弧度变角度 180 / π × 弧度

![弧度](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200924110516.png)


## 相互转换
### 经纬度（Degrees）转换为世界坐标（Cartesian3）
第一种方法：直接转换
```js
Cesium.Cartesian3.fromDegrees(longitude, latitude, height, ellipsoid, result) 
```

第二种方法：先转换成弧度再转换，借助 ellipsoid 对象
```js
var ellipsoid=viewer.scene.globe.ellipsoid;
var cartographic=Cesium.Cartographic.fromDegrees(lng,lat,alt);
var cartesian3=ellipsoid.cartographicToCartesian(cartographic);
```

### 世界坐标（Cartesian3）转换为经纬度（Degrees）
```js
var ellipsoid=viewer.scene.globe.ellipsoid;
var cartesian3=new Cesium.cartesian3(x,y,z);
var cartographic=ellipsoid.cartesianToCartographic(cartesian3);
var lat=Cesium.Math.toDegrees(cartograhphic.latitude);
var lng=Cesium.Math.toDegrees(cartograhpinc.longitude);
var alt=cartographic.height;
```

同理，得到弧度还可以用
```js
Cartographic.fromCartesian
```

### 弧度（Cartographic）和经纬度（Degrees）
经纬度转弧度
```js
Cesium.Math.toRadians(degrees) 
```

弧度转经纬度
```js
Cesium.Math.toDegrees(radians) 
```

### 屏幕坐标（Cartesian2）和世界坐标（Cartesian3）相互转换
屏幕坐标转世界坐标
```js
var pick1= new Cesium.Cartesian2(0, 0);
var cartesian = viewer.scene.globe.pick(viewer.camera.getPickRay(pick1),viewer.scene);
```

注意这里屏幕坐标一定要在球上，否则生成出的 cartesian 对象是 undefined

世界坐标转屏幕坐标
```js
Cesium.SceneTransforms.wgs84ToWindowCoordinates(scene, Cartesian3);
```

结果是 Cartesian2 对象，取出 X, Y 即为屏幕坐标。