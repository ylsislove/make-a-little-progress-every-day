# Cesium-Geometry and Appearances 几何图形和外观

本教程将向您介绍提供使用 Primitive API 的几何图形和外观系统。这是一个高级主题，用于扩展具有自定义网格、形状、体积和外观的 CesiumJS，而不是面向通用的 Cesium 用户。如果您有兴趣学习如何在地球上绘制各种形状和体积，请查看创建实体教程。CesiumJS 可以使用实体（如多边形和椭圆体）创建不同的几何类型。例如，将以下代码复制并粘贴到 [Hello World Sandcastle](https://cesiumjs.org/Cesium/Build/Apps/Sandcastle/index.html) 示例中，以在球体上创建具有点模式的矩形：

```js
var viewer = new Cesium.Viewer('cesiumContainer');

viewer.entities.add({
    rectangle : {
        coordinates : Cesium.Rectangle.fromDegrees(-100.0, 20.0, -90.0, 30.0),
        material : new Cesium.StripeMaterialProperty({
            evenColor: Cesium.Color.WHITE,
            oddColor: Cesium.Color.BLUE,
            repeat: 5
        })
    }
});
```

在本教程中，我们将深入到遮光罩下，查看构成它们的几何图形和外观类型。几何图形定义了 Primitive 结构，即构成基本体的三角形、线或点。外观定义了 Primitive 的着色，包括其完整的 GLSL 顶点和面片着色，以及渲染状态。

