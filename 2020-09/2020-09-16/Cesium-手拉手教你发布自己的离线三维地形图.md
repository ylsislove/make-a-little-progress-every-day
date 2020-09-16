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


未完待更~~~