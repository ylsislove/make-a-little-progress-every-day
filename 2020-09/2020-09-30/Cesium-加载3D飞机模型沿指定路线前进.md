# Cesium-加载3D飞机模型沿指定路线前进

## 最终效果
话不多说，先上效果

![最终效果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200930105416.gif)


## 相关知识点
主要用到 CZML 相关知识

CZML 是一种用来描述动态场景的JSON架构的语言，主要用于 Cesium 在浏览器中的展示。它可以用来描述点、线、布告板、模型以及其他的图元，同时定义他们是怎样随时间变化的。

详情可看：[CZML介绍](https://blog.csdn.net/wgf1997/article/details/103064450)

我这里就不过多赘述了。

## 主要代码
```js
var czml = [
    {
        id: "document",
        name: "CZML Path",
        version: "1.0",
        clock: {
            interval: "2020-09-30T10:00:00Z/2020-09-30T10:01:20Z",
            currentTime: "2012-08-04T10:00:00Z",
            multiplier: 10,
        },
    },
    {
        id: "path",
        name: "path with GPS flight data",
        description: "Created by wangyu",
        availability: "2020-09-30T10:00:00Z/2020-09-30T10:01:20Z",
        path: {
            material: {
                polylineOutline: {
                    color: {
                        rgba: [255, 0, 255, 127],
                    },
                    outlineColor: {
                        rgba: [255, 0, 255, 127],
                    },
                    outlineWidth: 3,
                },
            },
            width: 5,
            leadTime: 10,
            trailTime: 1000,
            resolution: 5,
        },
        model: {
            gltf: "Assets/SampleData/models/CesiumAir/Cesium_Air.glb",
            scale: 2.0,
            minimumPixelSize: 128,
        },
        position: {
            epoch: "2020-09-30T10:00:00Z",
            cartographicDegrees: [
                0, 102.23404378554466, 27.825736605050523, 2500,
                10, 102.23691954070244, 27.82887625908256, 2500,
                20, 102.23908610745147, 27.830920963237897, 2500,
                30, 102.24222708893987, 27.834251845778994, 2500,
                40, 102.24483684219396, 27.837156939755058, 2500,
                50, 102.24821756517042, 27.838973119832243, 2500,
                60, 102.2497304631213, 27.843805668815058, 2500,
                70, 102.25017946873977, 27.849726810753346, 2500,
                80, 102.24597936406548, 27.852179959795592, 2500
            ],
        },
    },
];

var airModel;
viewer.dataSources.add(Cesium.CzmlDataSource.load(czml)).then(function (ds) {
    airModel = ds.entities.getById("path");
    airModel.orientation = new Cesium.VelocityOrientationProperty(airModel.position);
    airModel.model.alignedAxis = new Cesium.VelocityVectorProperty(airModel.position, true)
});
```
