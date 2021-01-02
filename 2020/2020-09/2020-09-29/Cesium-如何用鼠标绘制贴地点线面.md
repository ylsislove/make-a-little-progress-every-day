# Cesium-如何用鼠标绘制贴地点线面

## 绘制线
### 效果展示
![效果展示](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200929142454.gif)

### 相关代码
```js
// 定义当前场景的画布元素的事件处理
var handler = new Cesium.ScreenSpaceEventHandler(viewer.canvas);
// 去除双击选择实体的事件
viewer.cesiumWidget.screenSpaceEventHandler.removeInputAction(Cesium.ScreenSpaceEventType.LEFT_DOUBLE_CLICK);
viewer.cesiumWidget.screenSpaceEventHandler.removeInputAction(Cesium.ScreenSpaceEventType.LEFT_CLICK);

// 鼠标绘图
var activeShapePoints = [];
var activeShape;
var floatingPoint;

// 绘制点
function createPoint(worldPosition) {
    var point = viewer.entities.add({
        position: worldPosition,
        point: {
            color: Cesium.Color.WHITE,
            pixelSize: 5,
            heightReference: Cesium.HeightReference.CLAMP_TO_GROUND
        }
    });
    return point;
}

// 初始化为线
var drawingMode = 'line';
// 绘制图形
function drawShape(positionData) {
    var shape;
    if (drawingMode === 'line') {
        shape = viewer.entities.add({
            polyline: {
                positions: positionData,
                clampToGround: true,
                width: 3
            }
        });
    }
    return shape;
}

// 鼠标左键
handler.setInputAction(function (event) {
    // We use `viewer.scene.pickPosition` here instead of `viewer.camera.pickEllipsoid` so that
    // we get the correct point when mousing over terrain.
    // scene.pickPosition只有在开启地形深度检测，且不使用默认地形时是准确的。
    var earthPosition = viewer.scene.pickPosition(event.position);
    // `earthPosition` will be undefined if our mouse is not over the globe.
    if (Cesium.defined(earthPosition)) {
        // 记录当前位置
        activeShapePoints.push(earthPosition);
        // 创建一个浮动点
        if (activeShapePoints.length === 1) {
            floatingPoint = createPoint(earthPosition);
            activeShapePoints.push(earthPosition);
            // 这是drawShape函数positions属性的回调函数，含义就是当positions属性发生改变时，重新绘制线
            var dynamicPositions = new Cesium.CallbackProperty(function () {
                return activeShapePoints;
            }, false);
            // 把回调函数赋值给drawShape函数positions属性
            activeShape = drawShape(dynamicPositions); //绘制动态图
        }
    }
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);

//鼠标移动
handler.setInputAction(function (event) {
    if (Cesium.defined(floatingPoint)) {
        var newPosition = viewer.scene.pickPosition(event.endPosition);
        if (Cesium.defined(newPosition)) {
            // 浮动点随鼠标移动而移动
            floatingPoint.position.setValue(newPosition);
            // 更新数组
            activeShapePoints.pop();
            activeShapePoints.push(newPosition);
        }
    }
}, Cesium.ScreenSpaceEventType.MOUSE_MOVE);

// Redraw the shape so it's not dynamic and remove the dynamic shape.
// 重新绘制形状使其不是动态的并删除动态形状。
function terminateShape() {
    activeShapePoints.pop(); // 去除最后一个动态点位置
    if (activeShapePoints.length > 1) {
        drawShape(activeShapePoints); // 绘制最终图（不会再随鼠标移动而变化）
    }
    viewer.entities.remove(floatingPoint);  // 去除动态点图形（当前鼠标点）
    viewer.entities.remove(activeShape);    // 去除动态图形（移除之前有回调函数的那个图形）
    floatingPoint = undefined;
    activeShape = undefined;
    activeShapePoints = [];
}

handler.setInputAction(function (event) {
    terminateShape();
}, Cesium.ScreenSpaceEventType.RIGHT_CLICK);

// 开启地形深度检测，如果鼠标指针和点不重合，这个选项设置为true试试。
viewer.scene.globe.depthTestAgainstTerrain = true;
```


后续待更。。。