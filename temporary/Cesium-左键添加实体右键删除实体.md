# Cesium-左键添加实体右键删除实体


```js
// 得到当前三维场景
var scene = viewer.scene;
var uid = 1;
var laberConnection = [];

// 得到当前三维场景的椭球体，即地球
var ellipsoid = scene.globe.ellipsoid;
var longitudeString = null;
var latitudeString = null;
var cartesian = null;

var timer = null;
// 设置鼠标点击事件的处理函数，这里负责监听x, y坐标值变化
handler.setInputAction(function (movement) {
    // 通过指定的椭球或者地图对应的坐标系，将鼠标的二维坐标转换为对应椭球体三维坐标
    cartesian = viewer.camera.pickEllipsoid(movement.position, ellipsoid);
    // 将笛卡尔坐标转换为地理坐标
    var cartographic = ellipsoid.cartesianToCartographic(cartesian);
    // 将弧度转换为度的十进制表示
    longitudeString = Cesium.Math.toDegrees(cartographic.longitude);
    latitudeString = Cesium.Math.toDegrees(cartographic.latitude);

    // 清除第一次的单击事件
    clearTimeout(timer);
    // 指定时间之后运行点击事件
    timer = setTimeout(function () {
        var a = viewer.entities.add({
            id: 'billboard' + uid,
            position: cartesian,
            label: {
                text: '(' + longitudeString + ', ' + latitudeString + ')',
                font: '18px monospace',
                style: Cesium.LabelStyle.FILL_AND_OUTLINE,
                outlineWidth: 2,
                verticalOrigin: Cesium.VerticalOrigin.BOTTOM,
                pixelOffset: new Cesium.Cartesian2(0, 0) // +左下 ， -右上 ， （x,y）
            }
        });
        uid++;
        laberConnection.push(a);
        copyText(longitudeString + ', ' + latitudeString);
    }, 200);
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);

// 设置鼠标右击事件的处理函数，这里负责删除实体
handler.setInputAction(function (movement) {
    laberConnection.forEach(item => {
        viewer.entities.remove(item);
    });
}, Cesium.ScreenSpaceEventType.RIGHT_CLICK);


// -----------------------------------------------------------------------------------
// 复制经纬度到剪切板
const copyTempElement = document.createElement('textarea');
copyTempElement.setAttribute('style', 'margin:0;padding:0;width:0;height:0;position:absolute;');
document.body.appendChild(copyTempElement);
function copyText(text) {
    let succeeded;
    try {
        copyTempElement.value = text;
        copyTempElement.select();
        succeeded = document.execCommand('copy');
    } catch (err) {
        succeeded = false;
    }
    return succeeded;
}
```