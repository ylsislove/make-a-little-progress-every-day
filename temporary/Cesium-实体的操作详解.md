# Cesium-实体的操作详解

## 添加实体
```js
var redBox = viewer.entities.add({
    id:'Box',
    position : Cesium.Cartesian3.fromDegrees(108, 34,0),
    box : {
        dimensions : new Cesium.Cartesian3(4000, 3000, 5000),
        material : Cesium.Color.RED.withAlpha(0.5),
        outline : true,
        outlineColor : Cesium.Color.BLACK
    }
})
```

## 添加模型
```js
var entity = viewer.entities.add({
    // 加载飞机模型
    model: {
        uri: 'Assets/SampleData/models/CesiumAir/Cesium_Air.glb',
        minimumPixelSize: 64
    },
    position: Cesium.Cartesian3.fromDegrees(102.23292685840103, 27.825718192817853, 2500.0)
});
```

## 获取实体
```js
var getByIdBox = viewer.entities.getById('Box');
console.log(getByIdBox)
```

## 删除实体
```js
//方法一（针对性删除某一个）
viewer.entities.remove(redBox);
    
//方法二（通过id删除）
viewer.entities.remove(getByIdBox);

//方法三（删除所有实体）
viewer.entities.removeAll();
```