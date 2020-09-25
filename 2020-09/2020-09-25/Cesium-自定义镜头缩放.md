# Cesium-自定义镜头缩放

原理很简单，通过 Cesium 提供的 `viewer.camera.zoomIn()` 和 `viewer.camera.zoomOut` API 即可。

代码如下：

```js
// 定义当前场景的画布元素的事件处理
var handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);
// 设置鼠标滚动事件的处理函数，这里负责对相机高度进行控制
handler.setInputAction(function (e) {

    // 获取当前镜头位置的笛卡尔坐标
    let cameraPos = viewer.camera.position;
    // 获取当前坐标系标准
    let ellipsoid = viewer.scene.globe.ellipsoid;
    // 根据坐标系标准，将笛卡尔坐标转换为地理坐标
    let cartographic = ellipsoid.cartesianToCartographic(cameraPos);
    // 获取镜头的高度
    let height = cartographic.height;

    // 滚轮往前滚，镜头拉近
    if (e > 0) {
        // 镜头拉近
        viewer.camera.zoomIn(height / 3);
    } else {
        // 镜头远离
        viewer.camera.zoomOut(height * 1.2);
    }

}, Cesium.ScreenSpaceEventType.WHEEL)
```

进一步处理，如果想让相机镜头平滑的进行缩放，可以用 `viewer.camera.flyTo()` API。

代码如下：

```js
// 根据上面当前镜头的位置，获取该中心位置的经纬度坐标
let centerLon = parseFloat(Cesium.Math.toDegrees(cartographic.longitude).toFixed(8));
let centerLat = parseFloat(Cesium.Math.toDegrees(cartographic.latitude).toFixed(8));

// 镜头拉近
viewer.camera.flyTo({
    destination: Cesium.Cartesian3.fromDegrees(centerLon, centerLat, height / 1.8),
    duration: 1.0
});

// 镜头拉远
viewer.camera.flyTo({
    destination: Cesium.Cartesian3.fromDegrees(centerLon, centerLat, height * 1.8),
    duration: 1.0
});
```