# Cesium-GeoJson数据的显示和隐藏

  - [结果展示](#%E7%BB%93%E6%9E%9C%E5%B1%95%E7%A4%BA)
  - [相关代码](#%E7%9B%B8%E5%85%B3%E4%BB%A3%E7%A0%81)

## 结果展示
![结果展示](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200927115636.gif)

## 相关代码
```js
// -------------------------- 加载GeoJson数据 ------------------------------

var fireLayer = null;
var borderLayer = null;
var roadLayer = null;

viewer.dataSources.add(Cesium.GeoJsonDataSource.load('Assets/muli/muli_geojson/fire.geojson', {
    stroke: Cesium.Color.RED.withAlpha(0.5),
    strokeWidth: 2.3,
    fill: Cesium.Color.RED.withAlpha(0.1),
    clampToGround: true
})).then(data => {
    fireLayer = data;
});

viewer.dataSources.add(Cesium.GeoJsonDataSource.load('Assets/muli/muli_geojson/road.geojson', {
    stroke: Cesium.Color.CORAL.withAlpha(0.5),
    strokeWidth: 2.3,
    fill: Cesium.Color.CORAL.withAlpha(0.4),
    clampToGround: true
})).then(data => {
    roadLayer = data;
});

viewer.dataSources.add(Cesium.GeoJsonDataSource.load('Assets/muli/muli_geojson/border.geojson', {
    stroke: Cesium.Color.RED.withAlpha(0.5),
    strokeWidth: 2.3,
    fill: Cesium.Color.RED.withAlpha(0.5),
    clampToGround: true
})).then(data => {
    borderLayer = data;
});

// ------------------------- 图层的显式控制 ----------------------------------
checkboxFire = document.getElementById("checkboxFire");
checkboxFire.checked = true;
checkboxFire.addEventListener("click", () => {
    fireLayer.show = checkboxFire.checked;
    borderLayer.show = checkboxFire.checked;
});

checkboxRoad = document.getElementById("checkboxRoad");
checkboxRoad.checked = true;
checkboxRoad.addEventListener("click", () => {
    roadLayer.show = checkboxRoad.checked;
});
```