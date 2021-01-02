# Cesium-Viewer参数及属性信息

Viewer是Cesium渲染器的核心功能，直接将地图和场景显示在浏览器中

按需设置

```js
var viewer = new Cesium.Viewer( 'cesiumContainer', {    
    animation : false,          //是否创建动画小器件，左下角仪表    
    baseLayerPicker : false,    //是否显示图层选择器    
    fullscreenButton : false,   //是否显示全屏按钮    
    geocoder : false,   //是否显示geocoder小器件，右上角查询按钮    
    homeButton : false, //是否显示Home按钮    
    infoBox : false,    //是否显示信息框    
    sceneModePicker : false,    //是否显示3D/2D选择器    
    selectionIndicator : false, //是否显示选取指示器组件    
    timeline : false,   //是否显示时间轴    
    navigationHelpButton : false,   //是否显示右上角的帮助按钮    
    scene3DOnly : true, //如果设置为true，则所有几何图形以3D模式绘制以节约GPU资源    
    clock : new Cesium.Clock(),     //用于控制当前时间的时钟对象    
    selectedImageryProviderViewModel : undefined,   //当前图像图层的显示模型，仅baseLayerPicker设为true有意义    
    imageryProviderViewModels : Cesium.createDefaultImageryProviderViewModels(),    //可供BaseLayerPicker选择的图像图层ProviderViewModel数组    
    selectedTerrainProviderViewModel : undefined,   //当前地形图层的显示模型，仅baseLayerPicker设为true有意义    
    terrainProviderViewModels : Cesium.createDefaultTerrainProviderViewModels(),    //可供BaseLayerPicker选择的地形图层ProviderViewModel数组    
    imageryProvider : new Cesium.OpenStreetMapImageryProvider(),//图像图层提供者，仅baseLayerPicker设为false有意义    
    terrainProvider : new Cesium.EllipsoidTerrainProvider(),    //地形图层提供者，仅baseLayerPicker设为false有意义    
    skyBox : new Cesium.SkyBox({    
        sources : {    
            positiveX : 'Cesium-1.7.4/Skybox/px.jpg',    
            negativeX : 'Cesium-1.7.4/Skybox/mx.jpg',    
            positiveY : 'Cesium-1.7.4/Skybox/py.jpg',    
            negativeY : 'Cesium-1.7.4/Skybox/my.jpg',    
            positiveZ : 'Cesium-1.7.4/Skybox/pz.jpg',    
            negativeZ : 'Cesium-1.7.4/Skybox/mz.jpg'    
        }    
    }), //用于渲染星空的SkyBox对象    
    fullscreenElement : document.body,  //全屏时渲染的HTML元素,    
    useDefaultRenderLoop : true,    //如果需要控制渲染循环，则设为true    
    targetFrameRate : undefined,    //使用默认render loop时的帧率    
    showRenderLoopErrors : false,   //如果设为true，将在一个HTML面板中显示错误信息    
    automaticallyTrackDataSourceClocks : true,  //自动追踪最近添加的数据源的时钟设置    
    contextOptions : undefined,                 //传递给Scene对象的上下文参数（scene.options）    
    sceneMode : Cesium.SceneMode.SCENE3D,       //初始场景模式    
    mapProjection : new Cesium.WebMercatorProjection(), //地图投影体系    
    dataSources : new Cesium.DataSourceCollection()     //需要进行可视化的数据源的集合
});
```

小 Tip：

如果设置了 `useDefaultRenderLoop` 为 `true` 以及 `targetFrameRate` 为大于 `0` 的一个整数时，可以控制地图渲染的帧率

> Gets or sets the target frame rate of the widget when <code>useDefaultRenderLoop</code> is true. If undefined, the browser's {@link requestAnimationFrame} implementation determines the frame rate.  If defined, this value must be greater than 0.  A value higher than the underlying requestAnimationFrame implementation will have no effect