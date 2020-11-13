# Cesium-几种坐标系统及其相互转换

## 获取camera高度
1. 方法一
    ```js
    var ellipsoid = viewer.scene.globe.ellipsoid;
    var height = ellipsoid.cartesianToCartographic(viewer.camera.position).height;
    ```

2. 方法二
    ```js
    var height = viewer.camera.positionCartographic.height;
    ```

## 拾取屏幕中心点的二维坐标，并转换成地理坐标
```js
// 拾取屏幕中心点的二维坐标，并转换成三维坐标
var result = viewer.camera.pickEllipsoid(new Cesium.Cartesian2(viewer.canvas.clientWidth / 2, viewer.canvas
    .clientHeight / 2), viewer.scene.globe.ellipsoid);
// 转换成地理坐标
// 方法一：
var curPosition = Cesium.Ellipsoid.WGS84.cartesianToCartographic(result);
console.log(curPosition.longitude, curPosition.latitude);
// 方法二：
var curPosition2 = viewer.scene.globe.ellipsoid.cartesianToCartographic(result);
console.log(curPosition2.longitude, curPosition2.latitude);
```