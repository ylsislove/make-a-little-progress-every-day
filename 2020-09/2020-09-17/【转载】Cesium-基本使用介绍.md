# 【转载】Cesium-基本使用介绍

发现一篇总结的很棒的关于 Cesium 基本使用的文章，必须在此记录下来。

  - [原文链接](#%E5%8E%9F%E6%96%87%E9%93%BE%E6%8E%A5)
  - [前言](#%E5%89%8D%E8%A8%80)
  - [Cesium简介](#cesium%E7%AE%80%E4%BB%8B)
  - [Cesium简单使用](#cesium%E7%AE%80%E5%8D%95%E4%BD%BF%E7%94%A8)
    - [安装及测试](#%E5%AE%89%E8%A3%85%E5%8F%8A%E6%B5%8B%E8%AF%95)
    - [Viewer和地图图层](#viewer%E5%92%8C%E5%9C%B0%E5%9B%BE%E5%9B%BE%E5%B1%82)
      - [Viewer](#viewer)
      - [图层介绍](#%E5%9B%BE%E5%B1%82%E4%BB%8B%E7%BB%8D)
      - [默认图层设置](#%E9%BB%98%E8%AE%A4%E5%9B%BE%E5%B1%82%E8%AE%BE%E7%BD%AE)
    - [地形](#%E5%9C%B0%E5%BD%A2)
      - [STK World Terrain](#stk-world-terrain)
      - [Small Terrain](#small-terrain)
    - [坐标转换](#%E5%9D%90%E6%A0%87%E8%BD%AC%E6%8D%A2)
      - [坐标系](#%E5%9D%90%E6%A0%87%E7%B3%BB)
      - [二维屏幕坐标系到三维坐标系的转换](#%E4%BA%8C%E7%BB%B4%E5%B1%8F%E5%B9%95%E5%9D%90%E6%A0%87%E7%B3%BB%E5%88%B0%E4%B8%89%E7%BB%B4%E5%9D%90%E6%A0%87%E7%B3%BB%E7%9A%84%E8%BD%AC%E6%8D%A2)
      - [三维坐标到地理坐标的转换](#%E4%B8%89%E7%BB%B4%E5%9D%90%E6%A0%87%E5%88%B0%E5%9C%B0%E7%90%86%E5%9D%90%E6%A0%87%E7%9A%84%E8%BD%AC%E6%8D%A2)
      - [地理坐标到经纬度坐标的转换](#%E5%9C%B0%E7%90%86%E5%9D%90%E6%A0%87%E5%88%B0%E7%BB%8F%E7%BA%AC%E5%BA%A6%E5%9D%90%E6%A0%87%E7%9A%84%E8%BD%AC%E6%8D%A2)
      - [经纬度坐标转地理坐标（弧度）](#%E7%BB%8F%E7%BA%AC%E5%BA%A6%E5%9D%90%E6%A0%87%E8%BD%AC%E5%9C%B0%E7%90%86%E5%9D%90%E6%A0%87%E5%BC%A7%E5%BA%A6)
      - [经纬度坐标转世界坐标](#%E7%BB%8F%E7%BA%AC%E5%BA%A6%E5%9D%90%E6%A0%87%E8%BD%AC%E4%B8%96%E7%95%8C%E5%9D%90%E6%A0%87)
      - [计算两个三维坐标系之间的距离](#%E8%AE%A1%E7%AE%97%E4%B8%A4%E4%B8%AA%E4%B8%89%E7%BB%B4%E5%9D%90%E6%A0%87%E7%B3%BB%E4%B9%8B%E9%97%B4%E7%9A%84%E8%B7%9D%E7%A6%BB)
    - [加载3D对象（Entity）](#%E5%8A%A0%E8%BD%BD3d%E5%AF%B9%E8%B1%A1entity)
      - [直接添加](#%E7%9B%B4%E6%8E%A5%E6%B7%BB%E5%8A%A0)
      - [添加primitives](#%E6%B7%BB%E5%8A%A0primitives)
    - [加载GeoJson、KML、CZML数据](#%E5%8A%A0%E8%BD%BDgeojsonkmlczml%E6%95%B0%E6%8D%AE)
      - [GeoJson](#geojson)
      - [KML](#kml)
      - [CZML](#czml)
    - [加载3D Tile](#%E5%8A%A0%E8%BD%BD3d-tile)
      - [加载](#%E5%8A%A0%E8%BD%BD)
      - [tileset.json文件](#tilesetjson%E6%96%87%E4%BB%B6)
      - [支持的格式](#%E6%94%AF%E6%8C%81%E7%9A%84%E6%A0%BC%E5%BC%8F)
      - [Style](#style)
  - [总结](#%E6%80%BB%E7%BB%93)

## 原文链接
Cesium基础使用介绍
> https://www.cnblogs.com/shoufengwei/p/7998468.html#commentform

## 前言
最近折腾了一下三维地球，本文简单为大家介绍一款开源的三维地球软件——Cesium，以及如何快速上手Cesium。当然三维地球重要的肯定不是数据显示，这只是数据可视化的一小部分，重要的应该是背后的数据生成及处理等。本文先为大家介绍这简单的部分。

## Cesium简介
Github地址：[https://github.com/AnalyticalGraphicsInc/cesium](https://github.com/AnalyticalGraphicsInc/cesium)。官方介绍如下：

> An open-source JavaScript library for world-class 3D globes and maps.

非常简洁：Cesium是一款开源的基于JS的3D地图框架。具体这里也不多做介绍，各位可以自行浏览其网站。其实他就是一个地图可视化框架，与Leaft-let以及OpenLayer等没有本质的区别，只是Cesium支持三维场景，做的更漂亮。

## Cesium简单使用
### 安装及测试
最简单的安装方式，就是普通的JS文件加载，只需要从Github中下载其js代码，放到自己的项目中，在html页面中引用即可。如下：

![安装](https://images2017.cnblogs.com/blog/704456/201712/704456-20171207115107925-414517475.png)

当然如果要直接使用其示例等，还是需要按照其文档使用nodejs一步步安装。安装完之后，新建html页面并引用Cesium.js，如下：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello 3D Earth</title>
    <script src="CesiumUnminified/Cesium.js"></script>
    <style>
        @import url(CesiumUnminified/Widgets/widgets.css);
        html, body, #cesiumContainer {
            width: 100%; height: 100%; margin: 0; padding: 0; overflow: hidden;
        }
    </style>
</head>
<body>
    <div id="cesiumContainer"></div>
    <script src="app.js"></script>
</body>
</html>
```

app.js只需要一行代码即可，内容如下：

```js
viewer = new Cesium.Viewer('cesiumContainer');
```

其中cesiumContainer为html中的地图显示div的id。就是这么简单，浏览器打开上述html页面，便可看到一个三维地球。底图为微软影像只是加载到了三维地球上，包含放大、缩小、平移等基本在线地图功能，同时还包含了时间轴等与时间有关的控件，这是Cesium的一个特色，其地图、对象以及场景等能与时间相关联。

![cesium](https://images2017.cnblogs.com/blog/704456/201712/704456-20171207115404253-2111916653.png)

### Viewer和地图图层
#### Viewer
Viewer是Cesium的核心，上面的一行代码实现了基本框架的加载，我们可以为其添加参数，实现不同类型的地图加载，如下：

```js
var viewer = new Cesium.Viewer("cesiumContainer", {
    animation: true, //是否显示动画控件(左下方那个)
    baseLayerPicker: true, //是否显示图层选择控件
    geocoder: true, //是否显示地名查找控件
    timeline: true, //是否显示时间线控件
    sceneModePicker: true, //是否显示投影方式控件
    navigationHelpButton: false, //是否显示帮助信息控件
    infoBox: true, //是否显示点击要素之后显示的信息
});
```

这里面设置了地图浏览中几个控件的显示与否。这里主要介绍baseLayerPicker项，他可以设置图层选择空间是否可见，如果设置不可见，则需要设置自定义图层作为默认图层。当然设置可见之后也可以更改其中的图层为自定义图层。

#### 图层介绍
Cesium中的图层分为两种：一种是普通图层，包含影像、线划等普通显示图层；还有一种是地形图层，用于真实的模拟地球表面的场景，Cesium会根据加载到的地形瓦片以三维的方式显示出山川、大海等。

那么首先来介绍一下在Cesium中如何创建一个图层。

第一种方式可以直接在基本图层上添加一个图层，如注记等等。方式如下：

```js
//全球影像中文注记服务
var my_layer = viewer.imageryLayers.addImageryProvider(new Cesium.WebMapTileServiceImageryProvider({
    url: "http://t0.tianditu.com/cia_w/wmts?service=wmts&request=GetTile&version=1.0.0&LAYER=cia&tileMatrixSet=w&TileMatrix={TileMatrix}&TileRow={TileRow}&TileCol={TileCol}&style=default.jpg",
    layer: "tdtAnnoLayer",
    style: "default",
    format: "image/jpeg",
    tileMatrixSetID: "GoogleMapsCompatible",
    show: false
}));
```

这段代码实现在影像的基础上叠加天地图注记层。当然也可以添加其他已知商业地图的图层或者自定义地图，但是需要做好CORS，详细请参考[geotrellis使用（三十五）Cesium加载geotrellis TMS瓦片](http://www.cnblogs.com/shoufengwei/p/7901428.html)。

第二种方式大同小异，如下：

```js
var my_layer = viewer.scene.imageryLayers.addImageryProvider(
    new Cesium.UrlTemplateImageryProvider({
        url : 'http://my_url/{z}/{x}/{y}',
        format: "image/png"
    })
);
```

区别在于不是直接加载到viewer的imageryLayers而是scene的imageryLayers，但是查看Cesium的源代码你会发现二者是一致的，viewer.imageryLayers返回的正是viewer.scene.imageryLayers。所以二者都可以通过下述方式设置透明度和亮度，防止压盖等。

```js
//50%透明度
my_layer.alpha = 0.5;
//两倍亮度
my_layer.brightness = 2.0;
```

这里就已经介绍了Cesium的两种图层对象：UrlTemplateImageryProvider、WebMapTileServiceImageryProvider，其还有Cesium.createTileMapServiceImageryProvider、SingleTileImageryProvider等等好几种，只是url的组织方式不同，可以根据需要自行查阅相关源码即可。

#### 默认图层设置
上文已经说了可以设置baseLayerPicker为false或true来控制图层选择控件是否可见，当设置为false的时候可以在创建viewer时添加一项来设置默认显示的底图，否则仍然显示微软的默认影像。与添加图层的方式基本一致，如下：

```js
imageryProvider : new Cesium.WebMapTileServiceImageryProvider({
    url: "http://t0.tianditu.com/vec_w/wmts?service=wmts&request=GetTile&version=1.0.0&LAYER=vec&tileMatrixSet=w&TileMatrix={TileMatrix}&TileRow={TileRow}&TileCol={TileCol}&style=default&format=tiles",
    layer: "tdtVecBasicLayer",
    style: "default",
    format: "image/jpeg",
    tileMatrixSetID: "GoogleMapsCompatible",
    show: false
})
```

当baseLayerPicker设置为true的时候，我们也可以修改里面的默认图层为我们想要的图层。只需要在创建viewer时再添加一项即可，如下：

```js
imageryProviderViewModels: imageryLayers//设置影像图列表
terrainProviderViewModels: terrainLayers//设置地形图列表
```

其中imageryLayers为影像（普通）图层数组，terrainLayers为地形图层数组，有关地图图层在下面介绍。

### 地形
Cesium中的地形系统是一种由流式瓦片数据生成地形mesh的技术，厉害指出在于其可以自动模拟出地面、海洋的三维效果。创建地形图层的方式如下：

```js
var terrainProvider = new Cesium.CesiumTerrainProvider({
    url : 'https://assets.agi.com/stk-terrain/v1/tilesets/world/tiles', // 默认立体地表
    // 请求照明
    requestVertexNormals: true,
    // 请求水波纹效果
    requestWaterMask: true
});
viewer.terrainProvider = terrainProvider;
```

Cesium支持两种类型的地形，STK World Terrain和Small Terrain。

#### STK World Terrain
STK World Terrain是高分辨率, 基于quantized mesh的地形。这是一种基于网格的地形，可充分利用GL中的Shader来渲染，效果相当逼真。STK World Terrain使用了多种数据源，分别适应不同地区和不同精度时的情形。比如对于美国本土使用National Elevation Dataset (NED)的高程，精度3-30米；对于欧洲使用EU-DEM高程，精度30米；对于澳洲使用Australia SRTM-derived 1 Second DEM高程，精度30米；对于-60至60纬度段使用CGIAR SRTM高程，精度90米；对于整个地球使用GTOPO30，精度1000米。STK World Terrain地形是怎样生成的是不公开的，如需应用于封闭的局域网时，则需购买AGI的STK terrain server。但是AGI提供了一个webapi可供因特网上调用，并提供了这种地形的格式细节。就是上面的url

#### Small Terrain
Small Terrain是中等高分辨率基于heightmap的地形，渲染出的地形效果不如quantized mesh的地形，但也基本能接受。可以由DEM数据生成这种规范的.terrain文件。生成工具见https://groups.google.com/forum/#!topic/cesium-dev/rBieaEBJHi，需要gdal库和numpy。

> 我有话说：由 DEM 数据生成这种规范的 .terrain 文件可以通过 CesiumLab 软件很方便的实现。详情可以看我的这篇文章 [Cesium-手拉手教你发布自己的离线三维地形图](../2020-09-16/Cesium-手拉手教你发布自己的离线三维地形图.md)

### 坐标转换
Cesium其实是一个封装好的WebGL库，当然这里面就牵扯到好几套坐标问题：屏幕坐标、三维空间坐标、投影坐标。而且坐标转换肯定是我们在开发任何地理信息系统中经常会碰到的问题，也比较复杂，简单总结了几种转换方式：

#### 坐标系
```js
new Cesium.Cartesian2(1,1) //表示一个二维笛卡尔坐标系，也就是直角坐标系（屏幕坐标系）
new Cesium.Cartesian3(1,1,1) //表示一个三维笛卡尔坐标系，也是直角坐标系(就是真实世界的坐标系)
```

#### 二维屏幕坐标系到三维坐标系的转换
```js
var pick1= scene.globe.pick(viewer.camera.getPickRay(pt1), scene) //其中pt1为一个二维屏幕坐标
```

#### 三维坐标到地理坐标的转换
```js
var geoPt1= scene.globe.ellipsoid.cartesianToCartographic(pick1) //其中pick1是一个Cesium.Cartesian3对象。
```

#### 地理坐标到经纬度坐标的转换
```js
var point1=[geoPt1.longitude / Math.PI * 180,geoPt1.latitude / Math.PI * 180]; //其中geoPt1是一个地理坐标。
```

#### 经纬度坐标转地理坐标（弧度）
```js
var cartographic = Cesium.Cartographic.fromDegree(point) //point是经纬度值
var coord_wgs84 = Cesium.Cartographic.fromDegrees(lng, lat, alt);//单位：度，度，米
```

#### 经纬度坐标转世界坐标
```js
var cartesian = Cesium.Cartesian3.fromDegree(point)
```

#### 计算两个三维坐标系之间的距离
```js
var d = Cesium.Cartesian3.distance(
    new Cesium.Cartesian3(pick1.x, pick1.y, pick1.z), 
    new Cesium.Cartesian3(pick3.x, pick3.y, pick3.z)
); //pick1、pick3都是三维坐标系
```

### 加载3D对象（Entity）
通过Cesium可以很清楚的将一个三维模型加载到地球中。有两种方式可以实现此功能。

#### 直接添加
```js
var entity = viewer.entities.add({ 
    position : Cesium.Cartesian3.fromDegrees(-123.0744619, 44.0503706), 
    model : { uri : '../Apps/SampleData/models/CesiumGround/Cesium_Ground.gltf' }
});
viewer.trackedEntity = entity; // 镜头追踪，将镜头固定在对象上
```

清晰明了，不做过多介绍。

#### 添加primitives
```js
// 这种方式会以最大最小值为缩放边界，采用entity的方式会完全根据地图进行缩放
var scene = viewer.scene;
var modelMatrix = Cesium.Transforms.eastNorthUpToFixedFrame(Cesium.Cartesian3.fromDegrees(-123.0745725, 44.0503706));
var model = scene.primitives.add(Cesium.Model.fromGltf({
    url: 'data/Cesium_Ground.gltf',
    //以下这些信息也均可在entity中设置
    color : Cesium.Color.fromAlpha(Cesium.Color.RED, parseFloat(0.5)),//模型颜色，透明度
    silhouetteColor : Cesium.Color.fromAlpha(Cesium.Color.GREEN, parseFloat(0.5)),//轮廓线
    colorBlendMode : Cesium.ColorBlendMode.MIX,//模型样式['Highlight', 'Replace', 'Mix']
    modelMatrix: modelMatrix,
    minimumPixelSize : 256, // 最小的缩放尺寸，256个像素，就是一个瓦片的尺寸。
    maxiumScale: 2 // 最大的缩放倍数
}));
```

其中modelMatrix定义了对象的位置，第一种添加方式模型会自动按照gltf设置好的动画进行播放，第二种方式则需要添加下述代码设置动画。

```js
//添加动画
Cesium.when(model.readyPromise).then(function (model) {
    model.activeAnimations.addAll({
        loop: Cesium.ModelAnimationLoop.REPEAT,//控制重复
        speedup: 0.5, // 速度，相对于clock
        reverse: true // 动画反转
    })
});
```

![演示](https://images2017.cnblogs.com/blog/704456/201712/704456-20171207115747378-319643942.png)

### 加载GeoJson、KML、CZML数据
这几类数据归为一类都是矢量数据，所以这里要介绍的就是如何加载矢量数据，当然数据量特别大的时候就需要考虑矢量瓦片，Cesium也正在开发矢量瓦片相关版本，之前看到一个折中方法是先读取矢量瓦片而后转换成GeoJson进行加载，这里不做过多介绍。那么这三类数据虽然都是矢量数据，但稍微有些不同，下面逐一介绍。

#### GeoJson
GeoJson是较为通用的一种网络矢量数据传输方案。其加载方式如下：

```js
viewer.dataSources.add(Cesium.GeoJsonDataSource.load('mydata.geojson', {
        stroke: Cesium.Color.BLUE.withAlpha(0.8),
        strokeWidth: 2.3,
        fill: Cesium.Color.RED.withAlpha(0.3),
        clampToGround : true
    }
));
```

Cesium.GeoJsonDataSource.load函数即为加载geojson数据，并配置相关属性。通过这种方式就可将数据加载到三维地球中，并设置边线以及填充等，clampToGround用于设置对象是否贴着地形，如为true则对象会随地势起伏而变化。当然我们可以为geojson中的各个要素设置不同的渲染方式，如下：

```js
Cesium.Math.setRandomNumberSeed(0);

var promise = Cesium.GeoJsonDataSource.load('data/county3.geojson'); // load完之后即为一个promise对象
promise.then(function(dataSource) { // 此处类似于添加3D对象中的动画。
    viewer.dataSources.add(dataSource); // 先添加对象

    var entities = dataSource.entities.values; // 获取所有对象

    var colorHash = {};
    for (var i = 0; i < entities.length; i++) { // 逐一遍历循环
        var entity = entities[i];
        var name = entity.properties.GB1999; // 取出GB1999属性内容
        var color = colorHash[name]; // 如果GB1999属性相同，则赋同一个颜色。
        if (!color) {
            color = Cesium.Color.fromRandom({
                alpha : 1.0
            });
            colorHash[name] = color;
        }
        entity.polygon.material = color; // 设置polygon对象的填充颜色
        entity.polygon.outline = false; // polygon边线显示与否

        entity.polygon.extrudedHeight = entity.properties.POPU * 1000; // 根据POPU属性设置polygon的高度
    }
});
viewer.zoomTo(promise);
```

此种方式实现原理为先load数据，而后逐一设置load后数据的entity。geojson中的对象的属性可以通过entity.properties.GB1999的方式取出，其中GB1999表示属性名称。注意数据最好是84投影经纬度坐标，下同。

![演示](https://images2017.cnblogs.com/blog/704456/201712/704456-20171207115620988-1276898145.png)

#### KML
KML是Google Earth定义的一种矢量数据组织方式，其加载方式与GeoJson基本相同，如下：

```js
var promise = Cesium.KmlDataSource.load('data.kml');
```

剩下的处理方式与GeoJson相同。

#### CZML
CZML是Cesium中很重要的一个概念，也是一个亮点，CZML使得cesium很酷很炫地展示动态数据成为可能。CZML是一种JSON格式的字符串，用于描述与时间有关的动画场景，CZML包含点、线、地标、模型、和其他的一些图形元素，并指明了这些元素如何随时间而变化。某种程度上说, Cesium 和 CZML的关系就像 Google Earth 和 KML。

CZML的一个典型结构如下

```js
[
    // packet one
    {
        "id": "GroundControlStation"
        "position": { "cartographicDegrees": [-75.5, 40.0, 0.0] },
        "point": {
            "color": { "rgba": [0, 0, 255, 255] },
        }
    },
    // packet two
    {
        "id": "PredatorUAV",
        // ...
    }
]
```

CZML可以记录对象与时间的关系，其时间序列相关属性如下：

```js
{
    // ...  
    "someInterpolatableProperty": {  
        "cartesian": [  
            "2012-04-30T12:00Z", 1.0, 2.0, 3.0, //表示当时间为2012-04-30T12:00Z，坐标为(1,2,3)
            "2012-04-30T12:01Z", 4.0, 5.0, 6.0, //表示当时间为2012-04-30T12:01Z，坐标为(4,5,6)
            "2012-04-30T12:02Z", 7.0, 8.0, 9.0  //表示当时间为2012-04-30T12:02Z，坐标为(7,8,9)
        ]  
    }  
}
{  
    // ...  
    "someInterpolatableProperty": {  
        "epoch": "2012-04-30T12:00Z", //表示时间起点为2012-04-30T12:00：00 
        "cartesian": [  
            0.0, 1.0, 2.0, 3.0,  //从起点开始，第0秒时坐标为(1,2,3)
            60.0, 4.0, 5.0, 6.0, //从起点开始，第60秒时坐标为(4,5,6) 
            120.0, 7.0, 8.0, 9.0 //从起点开始，第120秒时坐标为(7,8,9) 
        ]  
    }  
}
{  
    // ...  
    "someInterpolatableProperty": {  
        "epoch": "2012-04-30T12:00Z",  
        "cartesian": [  
            0.0, 1.0, 2.0, 3.0,  
            60.0, 4.0, 5.0, 6.0,  
            120.0, 7.0, 8.0, 9.0  
        ],  
        "interpolationAlgorithm": "LAGRANGE",  //插值算法为LAGRANGE，还有HERMITE,GEODESIC
        "interpolationDegree": 5 //1为线性插值，2为平方插值
    },  
}
```

具体的可以查阅相关资料。将CZML数据载入场景的方式与前两者一致，加载完后处理方式也基本一致，如下：

```js
dataSource = new Cesium.CzmlDataSource();
var czml = 'data/Vehicle.czml';
dataSource.load(czml);
viewer.dataSources.add(dataSource);
```

### 加载3D Tile
3D瓦片可以显示建筑物、地标乃至森林广告牌等等以及其对应的属性信息。每个3D瓦片就是一个3D对象，具体的数据范围等等信息在tileset.json中定义。

#### 加载
```js
var tileSet = viewer.scene.primitives.add(new Cesium.Cesium3DTileset({
    // 同样url只定义编号前面的部分，具体的编号（数字或者非数字都有可能）在此URL下的tileset.json文件中定义，包括此3d瓦片图层的范围等等。
    url: 'https://beta.cesium.com/api/assets/1461?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiMTBjN2E3Mi03ZGZkLTRhYmItOWEzNC1iOTdjODEzMzM5MzgiLCJpZCI6NDQsImlhdCI6MTQ4NjQ4NDM0M30.B3C7Noey3ZPXcf7_FXBEYwirct23fsUecRnS12FltN8&v=1.0'
}));

tileSet.readyPromise.then(function (tileset) {
    viewer.camera.viewBoundingSphere(tileset.boundingSphere, new Cesium.HeadingPitchRange(0, -0.5, 0));
    viewer.camera.lookAtTransform(Cesium.Matrix4.IDENTITY);
});
```

#### tileset.json文件
不同分辨率显示不同3D瓦片，全靠此文件定义。

```js
{
  "asset": {
    "version": "1.0"
  },
  "geometricError": 500,
  "root": {
    "transform": [
      96.86356343768793,
      24.848542777253734,
      0,
      0,
      -15.986465724980844,
      62.317780594908875,
      76.5566922962899,
      0,
      19.02322243409411,
      -74.15554020821229,
      64.3356267137516,
      0,
      1215107.7612304366,
      -4736682.902037748,
      4081926.095098698,
      1
    ],
    "boundingVolume": {
      "box": [
        0,
        0,
        0,
        7.0955,
        0,
        0,
        0,
        3.1405,
        0,
        0,
        0,
        5.0375
      ]
    },
    "geometricError": 100,
    "refine": "REPLACE",
    "content": {
      "url": "dragon_low.b3dm"
    },
    "children": [
      {
        "boundingVolume": {
          "box": [
            0,
            0,
            0,
            7.0955,
            0,
            0,
            0,
            3.1405,
            0,
            0,
            0,
            5.0375
          ]
        },
        "geometricError": 10,
        "content": {
          "url": "dragon_medium.b3dm"
        },
        "children": [
          {
            "boundingVolume": {
              "box": [
                0,
                0,
                0,
                7.0955,
                0,
                0,
                0,
                3.1405,
                0,
                0,
                0,
                5.0375
              ]
            },
            "geometricError": 0,
            "content": {
              "url": "dragon_high.b3dm"
            }
          }
        ]
      }
    ]
  }
}
```

其中boundingVolume.region 属性是包含六个元素的数组对象，用于定义边界地理区域，格式是[west,
south, east, north, minimum height, maximum height]。经度和维度以弧度为单位，高度以米为单位（高于或低于WGS84椭球体）除了 region，也有其他边界体可以用，比如 box 和 sphere。其余各个字段包含信息可以查阅官方手册。

#### 支持的格式
- b3dm： Batched 3D Model 用于展示城市建筑等大规模的3D对象
- l3dm： Instanced 3D Model 用于展示模型等。
- pnts： Point Cloud 用于展示大量的3D点。
- vctr： Vector Data 用于展示矢量元素，代替KML（那么CZML呢？动画？）
- cmpt： Composite 用于合并异构3D瓦片，如将城市建筑的b3dm和树的i3dm合在一起展示。

#### Style
可以根据对象的属性信息进行不同的可视化处理，包括颜色、显示与否等等。

```js
var styleJson = {
    color : {
        conditions : [
            ["${height} > 70.0", "rgb(0, 0, 255)"],
            ["${height} > 50.0", "rgb(0, 255, 0)"],
            ["${height} > 30.0", "rgb(0, 255, 255)"],
            ["${height} > 10.0", "color('purple', 1)"],
            ["${height} > 1.0", "color('gray', 0.5)"],
            ["true", "color('blue')"] // conditions 
        ]
    },
    show : '${height} > 0',
    meta : {
        description : '"Building id ${id} has height ${height}."'
    }
};
tileSet.style = new Cesium.Cesium3DTileStyle(styleJson);
```

注意conditions中条件必须闭合，不能出现分类不完整，所以一般最后会加一个true项，相当于default。

## 总结
本文简单介绍了Cesium三维数据可视化框架以及其简单的使用，比较笼统细节也并未深究可能也有错漏，感兴趣的可以自行查阅相关资料，随着学习的深入我也会增加些详细信息。总之，Cesium是一款不错的3D地图数据可视化引擎，值得拥有。