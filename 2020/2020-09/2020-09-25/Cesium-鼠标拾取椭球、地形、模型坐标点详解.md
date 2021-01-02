# Cesium-鼠标拾取椭球、地形、模型坐标点详解

  - [前言](#%E5%89%8D%E8%A8%80)
  - [获取椭球体表面的经纬度坐标（方法一）](#%E8%8E%B7%E5%8F%96%E6%A4%AD%E7%90%83%E4%BD%93%E8%A1%A8%E9%9D%A2%E7%9A%84%E7%BB%8F%E7%BA%AC%E5%BA%A6%E5%9D%90%E6%A0%87%E6%96%B9%E6%B3%95%E4%B8%80)
  - [获取椭球体表面的经纬度坐标（方法二）](#%E8%8E%B7%E5%8F%96%E6%A4%AD%E7%90%83%E4%BD%93%E8%A1%A8%E9%9D%A2%E7%9A%84%E7%BB%8F%E7%BA%AC%E5%BA%A6%E5%9D%90%E6%A0%87%E6%96%B9%E6%B3%95%E4%BA%8C)
  - [获取地形表面的经纬度高程坐标（方法一）](#%E8%8E%B7%E5%8F%96%E5%9C%B0%E5%BD%A2%E8%A1%A8%E9%9D%A2%E7%9A%84%E7%BB%8F%E7%BA%AC%E5%BA%A6%E9%AB%98%E7%A8%8B%E5%9D%90%E6%A0%87%E6%96%B9%E6%B3%95%E4%B8%80)
  - [获取地形表面的经纬度高程坐标（方法二）](#%E8%8E%B7%E5%8F%96%E5%9C%B0%E5%BD%A2%E8%A1%A8%E9%9D%A2%E7%9A%84%E7%BB%8F%E7%BA%AC%E5%BA%A6%E9%AB%98%E7%A8%8B%E5%9D%90%E6%A0%87%E6%96%B9%E6%B3%95%E4%BA%8C)
  - [获取模型表面的经纬度高程坐标（此方法借鉴于官方示例）](#%E8%8E%B7%E5%8F%96%E6%A8%A1%E5%9E%8B%E8%A1%A8%E9%9D%A2%E7%9A%84%E7%BB%8F%E7%BA%AC%E5%BA%A6%E9%AB%98%E7%A8%8B%E5%9D%90%E6%A0%87%E6%AD%A4%E6%96%B9%E6%B3%95%E5%80%9F%E9%89%B4%E4%BA%8E%E5%AE%98%E6%96%B9%E7%A4%BA%E4%BE%8B)

## 前言
Cesium 中的三维坐标可分为三种情况：椭球表面、地形和模型。

## 获取椭球体表面的经纬度坐标（方法一）
```js
var handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);  
handler.setInputAction(function(evt) { 
    var cartesian = viewer.camera.pickEllipsoid(evt.position, viewer.scene.globe.ellipsoid);  
    var cartographic = Cesium.Cartographic.fromCartesian(cartesian);  
    var lng = Cesium.Math.toDegrees(cartographic.longitude); // 经度值  
    var lat = Cesium.Math.toDegrees(cartographic.latitude); // 纬度值  
    var mapPosition = {
        x: lng, 
        y: lat,
        z: cartographic.height // cartographic.height 的值始终为零
    };
}, Cesium.ScreenSpaceEventType.LEFT_CLICK); 
```

获取相机高度可以通过此法获得：
```js
// 获取相机的高度
height = Math.ceil(viewer.camera.positionCartographic.height);
```

## 获取椭球体表面的经纬度坐标（方法二）
```js
var handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);
// 设置鼠标移动事件的处理函数，这里负责监听x, y坐标值变化
handler.setInputAction(function(evt) {
    // 得到当前三维场景的椭球体，即地球
    var ellipsoid = scene.globe.ellipsoid;
    // 通过指定的椭球或者地图对应的坐标系，将鼠标的二维坐标转换为对应椭球体三维坐标
    cartesian = viewer.camera.pickEllipsoid(evt.endPosition, ellipsoid);
    // 将笛卡尔坐标转换为地理坐标
    var cartographic = ellipsoid.cartesianToCartographic(cartesian);
    // 将弧度转换为度的十进制表示
    lng = Cesium.Math.toDegrees(cartographic.longitude);
    lat = Cesium.Math.toDegrees(cartographic.latitude);

}, Cesium.ScreenSpaceEventType.MOUSE_MOVE)

```

## 获取地形表面的经纬度高程坐标（方法一）
```js
var handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);  
handler.setInputAction(function(evt) {  
    var ray = viewer.camera.getPickRay(evt.position);  
    var cartesian = viewer.scene.globe.pick(ray, viewer.scene); 
    var cartographic = Cesium.Cartographic.fromCartesian(cartesian); 
    var lng = Cesium.Math.toDegrees(cartographic.longitude); // 经度值  
    var lat = Cesium.Math.toDegrees(cartographic.latitude); // 纬度值  
    var mapPosition = {
        x: lng,
        y: lat,
        z: cartographic.height // cartographic.height的值为地形高度 
    }; 
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);
```

## 获取地形表面的经纬度高程坐标（方法二）
```js
var handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);  
handler.setInputAction(function(evt) {  
    var ray = viewer.camera.getPickRay(evt.position);  
    var cartesian = viewer.scene.globe.pick(ray, viewer.scene);  
    var cartographic = Cesium.Cartographic.fromCartesian(cartesian);  
    var lng = Cesium.Math.toDegrees(cartographic.longitude); // 经度值  
    var lat = Cesium.Math.toDegrees(cartographic.latitude); // 纬度值  
    // height 结果与 cartographic.height 相差无几，注意：cartographic.height 可以为 0，也就是说，可以根据经纬度计算出高程。  
    var height = viewer.scene.globe.getHeight(cartographic);  
    var mapPosition = {
        x: lng,
        y: lat,
        z: height.height // height 的值为地形高度
    };
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);
```

## 获取模型表面的经纬度高程坐标（此方法借鉴于官方示例）
```js
var handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);  
handler.setInputAction(function(evt) {  
    var scene = viewer.scene;  
    if (scene.mode !== Cesium.SceneMode.MORPHING) {  
        var pickedObject = scene.pick(evt.position);  
        if (scene.pickPositionSupported && Cesium.defined(pickedObject) && pickedObject.node) {  
            var cartesian = viewer.scene.pickPosition(evt.position);  
            if (Cesium.defined(cartesian)) {  
                var cartographic = Cesium.Cartographic.fromCartesian(cartesian);  
                var lng = Cesium.Math.toDegrees(cartographic.longitude);  
                var lat = Cesium.Math.toDegrees(cartographic.latitude);  
                var height = cartographic.height; // 模型高度  
                mapPosition = {
                    x: lng,
                    y: lat,
                    z: height
                } 
            }  
        }  
    }  
}, Cesium.ScreenSpaceEventType.LEFT_CLICK); 
```