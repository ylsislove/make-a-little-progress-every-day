# Cesium-Geometry and Appearances 几何图形和外观

  - [Geometry types 几何图形类型](#geometry-types-%E5%87%A0%E4%BD%95%E5%9B%BE%E5%BD%A2%E7%B1%BB%E5%9E%8B)
  - [组合几何图形](#%E7%BB%84%E5%90%88%E5%87%A0%E4%BD%95%E5%9B%BE%E5%BD%A2)
  - [Picking 拾取](#picking-%E6%8B%BE%E5%8F%96)
  - [Geometry instances 几何实例](#geometry-instances-%E5%87%A0%E4%BD%95%E5%AE%9E%E4%BE%8B)
  - [Updating per-instance attributes 更新实例属性](#updating-per-instance-attributes-%E6%9B%B4%E6%96%B0%E5%AE%9E%E4%BE%8B%E5%B1%9E%E6%80%A7)
  - [外观](#%E5%A4%96%E8%A7%82)
  - [Geometry and appearance compatibility 几何图形和外观兼容](#geometry-and-appearance-compatibility-%E5%87%A0%E4%BD%95%E5%9B%BE%E5%BD%A2%E5%92%8C%E5%A4%96%E8%A7%82%E5%85%BC%E5%AE%B9)
  - [Resources 资源](#resources-%E8%B5%84%E6%BA%90)

Cesium中文网：[http://cesiumcn.org/](http://cesiumcn.org/) | 国内快速访问：[http://cesium.coinidea.com/](http://cesium.coinidea.com/)

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

使用几何图形和外观的好处是：
* Performance(性能)：在绘制大量Primitive（如美国每个邮政编码的多边形）时，使用几何图形直接允许我们将它们组合成单个几何图形，以减少CPU开销并更好地利用GPU。组合Primitive是在Web worker上完成的，以保持UI的响应性。
* Flexibility(灵活)：Primitive结合了几何图形和外观。通过分离它们，我们可以独立地修改每一个。我们可以添加与许多不同外观兼容的新几何图形，反之亦然。
* Low-level access（低层级访问）：外观提供接近金属的渲染访问，无需担心直接使用Renderer的所有细节。外观使下列情况变得容易：
  * 写所有GLSL的顶点和面片着色器
  * 使用自定义渲染状态

当然也会有一些缺点：
* 直接使用几何图形和外观需要更多的代码和对图形更深入的理解。实体处于适合映射应用程序的抽象级别；几何图形和外观的抽象级别更接近于**传统的3D引擎**。
* 组合几何图形对静态数据有效，对动态数据不一定有效。

让我们使用几何图形和外观重写初始代码示例：
```js
var viewer = new Cesium.Viewer('cesiumContainer');
var scene = viewer.scene;

// original code
//viewer.entities.add({
//    rectangle : {
//        coordinates : Cesium.Rectangle.fromDegrees(-100.0, 20.0, -90.0, 30.0),
//        material : new Cesium.StripeMaterialProperty({
//            evenColor: Cesium.Color.WHITE,
//            oddColor: Cesium.Color.BLUE,
//            repeat: 5
//        })
//    }
//});

var instance = new Cesium.GeometryInstance({
  geometry : new Cesium.RectangleGeometry({
    rectangle : Cesium.Rectangle.fromDegrees(-100.0, 20.0, -90.0, 30.0),
    vertexFormat : Cesium.EllipsoidSurfaceAppearance.VERTEX_FORMAT
  })
});

scene.primitives.add(new Cesium.Primitive({
  geometryInstances : instance,
  appearance : new Cesium.EllipsoidSurfaceAppearance({
    material : Cesium.Material.fromType('Stripe')
  })
}));
```

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123173744.png)

我们使用Primitive（**Primitive**）代替矩形实体，它结合了几何图形和外观。现在，我们将不区分 **Geometry** 和 **GemometryInstance**。实例不仅是几何图形的实例，更是其的容器。

为了创建矩形的几何图形，即覆盖矩形区域的三角形和适合球体曲率的三角形，我们创建了一个RectangleGeometry。

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123173828.png)

因为它在表面上，所以我们可以使用 **EllipsoidSurfaceAppearance**。这通过假设几何图形在曲面上或在椭球体上方的恒定高度来节省内存。

## Geometry types 几何图形类型
CesiumJS提供下列几何图形：

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123173907.png)

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123174121.png)

## 组合几何图形
当我们使用一个 Primitive 绘制多个静态几何图形时，我们看到了性能优势。例如，在一个 Primitive 中绘制两个矩形。

```js
var viewer = new Cesium.Viewer('cesiumContainer');
var scene = viewer.scene;

var instance = new Cesium.GeometryInstance({
  geometry : new Cesium.RectangleGeometry({
    rectangle : Cesium.Rectangle.fromDegrees(-100.0, 20.0, -90.0, 30.0),
    vertexFormat : Cesium.EllipsoidSurfaceAppearance.VERTEX_FORMAT
  })
});

var anotherInstance = new Cesium.GeometryInstance({
  geometry : new Cesium.RectangleGeometry({
    rectangle : Cesium.Rectangle.fromDegrees(-85.0, 20.0, -75.0, 30.0),
    vertexFormat : Cesium.EllipsoidSurfaceAppearance.VERTEX_FORMAT
  })
});

scene.primitives.add(new Cesium.Primitive({
  geometryInstances : [instance, anotherInstance],
  appearance : new Cesium.EllipsoidSurfaceAppearance({
    material : Cesium.Material.fromType('Stripe')
  })
}));
```

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123175936.png)

我们用不同的矩形创建了另一个实例，然后将这两个实例提供给 Primitive。这将以相同的外观绘制两个实例。

有些外观允许每个实例提供唯一的属性。例如，我们可以使用 **PerinstanceColorAppearance** 对每个实例使用不同的颜色进行着色。

```js
var viewer = new Cesium.Viewer('cesiumContainer');
var scene = viewer.scene;

var instance = new Cesium.GeometryInstance({
  geometry : new Cesium.RectangleGeometry({
    rectangle : Cesium.Rectangle.fromDegrees(-100.0, 20.0, -90.0, 30.0),
    vertexFormat : Cesium.PerInstanceColorAppearance.VERTEX_FORMAT
  }),
  attributes : {
    color : new Cesium.ColorGeometryInstanceAttribute(0.0, 0.0, 1.0, 0.8)
  }
});

var anotherInstance = new Cesium.GeometryInstance({
  geometry : new Cesium.RectangleGeometry({
    rectangle : Cesium.Rectangle.fromDegrees(-85.0, 20.0, -75.0, 30.0),
    vertexFormat : Cesium.PerInstanceColorAppearance.VERTEX_FORMAT
  }),
  attributes : {
    color : new Cesium.ColorGeometryInstanceAttribute(1.0, 0.0, 0.0, 0.8)
  }
});

scene.primitives.add(new Cesium.Primitive({
  geometryInstances : [instance, anotherInstance],
  appearance : new Cesium.PerInstanceColorAppearance()
}));
```

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123180137.png)

每个实例都有一个**颜色**属性。Primitive 是用 PerinstanceColorAppearance 构造的，它使用每个实例的颜色属性来确定着色。

组合几何图形可以使 CesiumJS 有效地绘制许多几何图形。下面的示例绘制 2592 个颜色独特的矩形。

```js
var viewer = new Cesium.Viewer('cesiumContainer');
var scene = viewer.scene;

var instances = [];

for (var lon = -180.0; lon < 180.0; lon += 5.0) {
  for (var lat = -85.0; lat < 85.0; lat += 5.0) {
    instances.push(new Cesium.GeometryInstance({
      geometry : new Cesium.RectangleGeometry({
        rectangle : Cesium.Rectangle.fromDegrees(lon, lat, lon + 5.0, lat + 5.0),
        vertexFormat: Cesium.PerInstanceColorAppearance.VERTEX_FORMAT
      }),
      attributes : {
        color : Cesium.ColorGeometryInstanceAttribute.fromColor(Cesium.Color.fromRandom({alpha : 0.5}))
      }
    }));
  }
}

scene.primitives.add(new Cesium.Primitive({
  geometryInstances : instances,
  appearance : new Cesium.PerInstanceColorAppearance()
}));
```

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123180743.png)

## Picking 拾取
实例合并后可以独立访问。为实例分配一个 ID，并使用它来确定是否使用 Scene.Pick 拾取该实例。

下面的示例创建一个带id的实例，并在单击该实例时将消息写入控制台。

```js
var viewer = new Cesium.Viewer('cesiumContainer');
var scene = viewer.scene;

var instance = new Cesium.GeometryInstance({
  geometry : new Cesium.RectangleGeometry({
    rectangle : Cesium.Rectangle.fromDegrees(-100.0, 30.0, -90.0, 40.0),
    vertexFormat: Cesium.PerInstanceColorAppearance.VERTEX_FORMAT
  }),
  id : 'my rectangle',
  attributes : {
    color : Cesium.ColorGeometryInstanceAttribute.fromColor(Cesium.Color.RED)
  }
});

scene.primitives.add(new Cesium.Primitive({
  geometryInstances : instance,
  appearance : new Cesium.PerInstanceColorAppearance()
}));

var handler = new Cesium.ScreenSpaceEventHandler(scene.canvas);
handler.setInputAction(function (movement) {
    var pick = scene.pick(movement.position);
    if (Cesium.defined(pick) && (pick.id === 'my rectangle')) {
      console.log('Mouse clicked rectangle.');
    }
  }, Cesium.ScreenSpaceEventType.LEFT_CLICK);
```

使用 id 避免了在内存中，在 Primitive 构造之后，对整个实例的引用，包括几何图形。

## Geometry instances 几何实例
实例可用于在场景的不同部分定位、缩放和旋转相同的几何体。这是可能的，因为多个实例可以引用相同的 Geometry，并且每个实例可以具有不同的 modelMatrix。这允许我们只计算一次几何图形，并多次重复使用它。

以下示例创建一个 **EllipsoidGeometry** 和两个实例。每个实例引用相同的椭球几何体，但使用不同的 modelMatrix 放置它，导致一个椭球位于另一个椭球之上。

```js
var viewer = new Cesium.Viewer('cesiumContainer');
var scene = viewer.scene;

var ellipsoidGeometry = new Cesium.EllipsoidGeometry({
    vertexFormat : Cesium.PerInstanceColorAppearance.VERTEX_FORMAT,
    radii : new Cesium.Cartesian3(300000.0, 200000.0, 150000.0)
});

var cyanEllipsoidInstance = new Cesium.GeometryInstance({
    geometry : ellipsoidGeometry,
    modelMatrix : Cesium.Matrix4.multiplyByTranslation(
        Cesium.Transforms.eastNorthUpToFixedFrame(Cesium.Cartesian3.fromDegrees(-100.0, 40.0)),
        new Cesium.Cartesian3(0.0, 0.0, 150000.0),
        new Cesium.Matrix4()
    ),
    attributes : {
        color : Cesium.ColorGeometryInstanceAttribute.fromColor(Cesium.Color.CYAN)
    }
});

var orangeEllipsoidInstance = new Cesium.GeometryInstance({
    geometry : ellipsoidGeometry,
    modelMatrix : Cesium.Matrix4.multiplyByTranslation(
        Cesium.Transforms.eastNorthUpToFixedFrame(Cesium.Cartesian3.fromDegrees(-100.0, 40.0)),
        new Cesium.Cartesian3(0.0, 0.0, 450000.0),
        new Cesium.Matrix4()
    ),
    attributes : {
        color : Cesium.ColorGeometryInstanceAttribute.fromColor(Cesium.Color.ORANGE)
    }
});

scene.primitives.add(new Cesium.Primitive({
    geometryInstances : [cyanEllipsoidInstance, orangeEllipsoidInstance],
    appearance : new Cesium.PerInstanceColorAppearance({
        translucent : false,
        closed : true
    })
}));
```

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123181403.png)

## Updating per-instance attributes 更新实例属性
将几何图形添加到 Primitive 后，更新几何图形的每个实例属性以更改可视化效果。每个实例的属性包括：
- Color: ColorGeometryInstanceAttribute 决定了颜色实例。Primitive必须具有 PerInstanceColorAppearance。
- Show：boolean类型决定实例是否可见。所有实例都具有该属性。

下列展示了如何改变几何实例的颜色：
```js
var viewer = new Cesium.Viewer('cesiumContainer');
var scene = viewer.scene;

var circleInstance = new Cesium.GeometryInstance({
    geometry : new Cesium.CircleGeometry({
        center : Cesium.Cartesian3.fromDegrees(-95.0, 43.0),
        radius : 250000.0,
        vertexFormat : Cesium.PerInstanceColorAppearance.VERTEX_FORMAT
    }),
    attributes : {
        color : Cesium.ColorGeometryInstanceAttribute.fromColor(new Cesium.Color(1.0, 0.0, 0.0, 0.5))
    },
    id: 'circle'
});
var primitive = new Cesium.Primitive({
    geometryInstances : circleInstance,
    appearance : new Cesium.PerInstanceColorAppearance({
        translucent : false,
        closed : true
    })
});
scene.primitives.add(primitive);

setInterval(function() {
    var attributes = primitive.getGeometryInstanceAttributes('circle');
    attributes.color = Cesium.ColorGeometryInstanceAttribute.toValue(Cesium.Color.fromRandom({alpha : 1.0}));
},2000);
```

几何图形实例的属性可以被 primitive 使用 primitive.getGeometryInstanceAttributes 检索。attirbutes 的属性可以直接被改变。

## 外观
几何定义结构。primitive 的另一个关键属性，appearance，定义了 primitive 的纹理，即单个像素的颜色。primitive 可以有多个几何实例，但只能有一个外观。根据外观的类型，外观将具有定义着色的主体的 **material**。

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123193243.png)

CesiumJS具有下列外观：

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123193320.png)

外观定义了绘制 Primitive 时在 GPU 上执行的完整 GLSL 顶点和面片着色器。外观还定义了完整的渲染状态，它控制绘制 primitvie 时 GPU 的状态。我们可以直接定义渲染状态，也可以使用更高级的属性，如“闭合(**closed**)”和“半透明(**translucent**)”，外观将转换为渲染状态。例如：
```js
// Perhaps for an opaque box that the viewer will not enter.
//  - Backface culled and depth tested.  No blending.

var appearance  = new Cesium.PerInstanceColorAppearance({
  translucent : false,
  closed : true
});

// This appearance is the same as above
var anotherAppearance  = new Cesium.PerInstanceColorAppearance({
  renderState : {
    depthTest : {
      enabled : true
    },
    cull : {
      enabled : true,
      face : Cesium.CullFace.BACK
    }
  }
});
```

创建外观后，不能更改其 renderState 属性，但可以更改其 material。我们还可以更改 primitive 的 appearnace 属性。

大多数外观还具有 **flat** 和 **faceForward** 属性，这些属性间接控制GLSL着色器。

- flat：平面阴影。不要考虑照明。
- faceForward：照明时，翻转法线，使其始终面向观众。回避背面的黑色区域，例如墙的内侧。

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123193812.png)

## Geometry and appearance compatibility 几何图形和外观兼容
并非所有外观都适用于所有几何图形。例如，EllipsoidSurfaceAppearance 外观不适用于 WallGeometry 几何图形，因为墙不在球体的表面上。

要使外观与几何图形兼容，它们必须具有匹配的顶点格式，这意味着几何图形必须具有外观所期待的输入数据。创建几何图形时可以提供 **vertexFormat**。

![img](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201123194100.png)

几何图形的 vertexFormat 确定它是否可以与其他几何图形组合。两个几何图形不必是相同的类型，但它们需要匹配的顶点格式。

为方便起见，外观要么具有 vertexFormat 属性，要么具有可作为几何体选项传入的 VERTEX_FORMAT 静态常量。

```js
var geometry = new Ceisum.RectangleGeometry({
  vertexFormat : Ceisum.EllipsoidSurfaceAppearance.VERTEX_FORMAT
  // ...
});

var geometry2 = new Ceisum.RectangleGeometry({
  vertexFormat : Ceisum.PerInstanceColorAppearance.VERTEX_FORMAT
  // ...
});

var appearance = new Ceisum.MaterialAppearance(/* ... */);
var geometry3 = new Ceisum.RectangleGeometry({
  vertexFormat : appearance.vertexFormat
  // ...
});
```

## Resources 资源
参考文档：
- [All geometries](https://cesiumjs.org/Cesium/Build/Documentation/index.html?filter=Geometry)
- [All appearances](https://cesiumjs.org/Cesium/Build/Documentation/index.html?filter=Appearance)
- [Primitive](https://cesiumjs.org/Cesium/Build/Documentation/Primitive.html)
- [GeometryInstance](https://cesiumjs.org/Cesium/Build/Documentation/GeometryInstance.html)

更多材料请访问：[Fabric](https://github.com/AnalyticalGraphicsInc/cesium/wiki/Fabric) 更多未来计划，请访问：[Geometry and Appearances Roadmap](https://github.com/AnalyticalGraphicsInc/cesium/issues/766)
