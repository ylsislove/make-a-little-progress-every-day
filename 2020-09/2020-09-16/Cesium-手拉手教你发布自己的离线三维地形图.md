# Cesium-手拉手教你发布自己的离线三维地形图

## 最终效果展示
![最终效果展示](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200915171801.png)


## 软件准备
1. LocaSpaceViewer 4

    - 下载地址：[http://www.locaspace.cn/LSV.jsp](http://www.locaspace.cn/LSV.jsp)
    - 说明：这个地图数据下载软件真的是蛮好用的，可以**免费**、**方便**的下载到卫星影像数据和 DEM 高程数据。作为同类型的软件还有 BigeMap，下载高程数据要收费，果断放弃。。

2. cesiumlab

    - 下载地址：[http://www.cesiumlab.com/](http://www.cesiumlab.com/)
    - 说明：很棒的一个软件。通过这个软件我们可以将高程数据转换成地形切片数据，也可以将卫星影像数据转换成瓦片数据，这样就可以在 cesium 中直接加载自己的数据了，很方便。


## 下载高程数据和卫星影像数据
### 下载高程数据
1. 首先在 LocaSpaceViewer 4 的**编辑**菜单中选择**绘制矩形**，绘制完成后如下图所示

    ![绘制矩形](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910111512.png)

2. 在地形下载中选择**选择面**，选中我们之前绘制的矩形。同理，下载级别越高，文件越大，根据自身情况选择。温馨提示，这个高程数据下载速度很慢，请耐心等待

    ![下载高程数据](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910113312.png)

3. 等待下载完成即可。


### 下载卫星影像数据（**瓦片**）
1. 选中绘制的矩形，在矩形上右击，选择**数据下载**，在弹出的框框中选择**选择面**，下载配置如下所示

    ![下载配置](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200925135642.png)

2. 点击开始下载，选择保存路径即可。


## 通过 cesiumlab 将高程数据转换为地形切片数据
1. 打开 cesiumlab 登录自己的账号，选择 数据处理 -> 地形切片，如下所示

    ![地形切片](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200925140454.png)

2. 输入文件那里，点击添加，选择刚刚下载的高程数据，存储类型选择**散列文件**，输出文件设置保存路径，其余可以不用设置，如下所示

    ![设置](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200925140952.png)

3. 点击确认即可。

## 在 Cesium 框架中加载自己的地形数据和卫星瓦片数据

脚本如下

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Use correct character set. -->
    <meta charset="utf-8" />
    <!-- Tell IE to use the latest, best version. -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <!-- Make the application on mobile take up the full browser screen and disable user scaling. -->
    <meta name="viewport"
        content="width=device-width, initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no" />
    <title>三维地图</title>
    <script type="text/javascript" src="Build/Cesium/Cesium.js"></script>
    <style>
        @import url(Build/Cesium/Widgets/widgets.css);

        html,
        body,
        #cesiumContainer {
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
    </style>
</head>

<body>
    <div id="cesiumContainer" class="fullSize"></div>
    <script>

        var terrainProvider = new Cesium.CesiumTerrainProvider({
            url: "Assets/muli/muli_dem_tile"
        });

        var imageryProvider = new Cesium.UrlTemplateImageryProvider({
            url: "Assets/muli/muli_tile/{z}/{x}/{y}.png",
            maximumLevel: 19,
            // 设置边界
            rectangle: new Cesium.Rectangle(
                Cesium.Math.toRadians(102.145299911499),    // west
                Cesium.Math.toRadians(27.757043838501),     // south
                Cesium.Math.toRadians(102.348546981812),    // east
                Cesium.Math.toRadians(27.8943729400635)     // north
            )
        });

        var viewer = new Cesium.Viewer("cesiumContainer", {
            terrainProvider: terrainProvider,
            imageryProvider: imageryProvider,
            homeButton: true,
            baseLayerPicker: false,
            animation: false,
            timeline: false,
            navigationHelpButton: false,
            geocoder: false,
            sceneModePicker: false
        });

        // 隐藏版权信息
        viewer._cesiumWidget._creditContainer.style.display = "none";

        // 添加一个图层
        var layers = viewer.scene.imageryLayers;
        var globalImagery = layers.addImageryProvider(new Cesium.SingleTileImageryProvider({
            url: 'Assets/global.png'
        }));
        // 移动到底层
        layers.lower(globalImagery);
        // 调整透明度 0.0 is transparent.  1.0 is opaque.
        globalImagery.alpha = 0.5;

        // 设置相机初始位置
        var homeCameraView = {
            destination: Cesium.Cartesian3.fromDegrees(
                102.145299911499,
                27.757043838501,
                10000
            ),
            orientation: {
                heading: Cesium.Math.toRadians(0),
                pitch: Cesium.Math.toRadians(-45),
                roll: Cesium.Math.toRadians(0),
            },
        };
        viewer.camera.setView(homeCameraView);

        // 设置 Home 按钮
        viewer.homeButton.viewModel.command.beforeExecute.addEventListener(function (e) {
            e.cancel = true;
            viewer.camera.setView(homeCameraView);
        });

    </script>
</body>

</html>
```

部署在 Tomcat 中即可。