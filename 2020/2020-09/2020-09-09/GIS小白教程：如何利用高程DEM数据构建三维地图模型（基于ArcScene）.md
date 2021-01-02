# GIS小白教程：如何利用高程DEM数据构建三维地图模型（基于ArcScene）

  - [最终效果展示](#%E6%9C%80%E7%BB%88%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA)
  - [软件准备](#%E8%BD%AF%E4%BB%B6%E5%87%86%E5%A4%87)
  - [下载数据](#%E4%B8%8B%E8%BD%BD%E6%95%B0%E6%8D%AE)
    - [下载卫星影像数据](#%E4%B8%8B%E8%BD%BD%E5%8D%AB%E6%98%9F%E5%BD%B1%E5%83%8F%E6%95%B0%E6%8D%AE)
    - [下载高程数据](#%E4%B8%8B%E8%BD%BD%E9%AB%98%E7%A8%8B%E6%95%B0%E6%8D%AE)
  - [对数据进行预处理](#%E5%AF%B9%E6%95%B0%E6%8D%AE%E8%BF%9B%E8%A1%8C%E9%A2%84%E5%A4%84%E7%90%86)
    - [对高程数据预处理](#%E5%AF%B9%E9%AB%98%E7%A8%8B%E6%95%B0%E6%8D%AE%E9%A2%84%E5%A4%84%E7%90%86)
    - [对卫星影像数据进行预处理](#%E5%AF%B9%E5%8D%AB%E6%98%9F%E5%BD%B1%E5%83%8F%E6%95%B0%E6%8D%AE%E8%BF%9B%E8%A1%8C%E9%A2%84%E5%A4%84%E7%90%86)
  - [在 ArcScene 中构建三维地图模型](#%E5%9C%A8-arcscene-%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%89%E7%BB%B4%E5%9C%B0%E5%9B%BE%E6%A8%A1%E5%9E%8B)

## 最终效果展示
![最终效果展示](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910141850.png)


## 软件准备
1. LocaSpaceViewer 4

    - 下载地址：[http://www.locaspace.cn/LSV.jsp](http://www.locaspace.cn/LSV.jsp)
    - 说明：这个地图数据下载软件真的是蛮好用的，可以**免费**、**方便**的下载到卫星影像数据和 DEM 高程数据。作为同类型的软件还有 BigeMap，下载高程数据要收费，果断放弃。。

2. global mapper

    - 下载地址：[http://www.bigemap.com/Uploads/file/20150804/globalmapper14.rar](http://www.bigemap.com/Uploads/file/20150804/globalmapper14.rar)
    - 说明：很好用的一款地理坐标系统转换软件，后面我们会用此软件将经纬度坐标系转换为投影坐标系。

3. ARCGIS 10.2

    - 下载、安装及破解地址：[http://www.bigemap.com/helps/doc2018011754.html](http://www.bigemap.com/helps/doc2018011754.html)
    - 说明：这个应该是 GIS 开发人员必备的软件，我就不多介绍了。。


## 下载数据

首先我们需要在 LocaSpaceViewer 4 上下载卫星影像数据以及高程数据，详细步骤如下

### 下载卫星影像数据
1. 首先在 LocaSpaceViewer 4 的**编辑**菜单中选择**绘制矩形**，绘制完成后如下图所示

    ![绘制矩形](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910111512.png)

2. 选中绘制的矩形，在矩形上右击，选择**数据下载**，在弹出的框框中选择**选择面**，如下图所示

    ![选择面](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910112002.png)

3. 配置下载参数，下载级别越高，卫星影像越清晰，但文件体积就越大，根据自己情况选择

    ![配置下载参数](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910112333.png)

4. 点击开始下载，选择保存路径，即可进行下载。

### 下载高程数据
1. 首先在 LocaSpaceViewer 4 的**下载**菜单中选择**谷歌地形（90米）**，注意**不是**选择**提取高程**哦，如下图所示

    ![选择谷歌地形（90米）](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910112825.png)

2. 在地形下载中选择**选择面**，选中我们之前绘制的矩形。同理，下载级别越高，文件越大，根据自身情况选择。温馨提示，这个高程数据下载速度很慢，请耐心等待

    ![下载高程数据](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910113312.png)

3. 等待下载完成即可。


## 对数据进行预处理

这一部分主要是通过 global mapper 将影像数据和高程数据的坐标系都转换为平面投影坐标系，并将高程数据导出成 DEM 格式文件。

### 对高程数据预处理
1. 在 global mapper 中打开之前下载的高程数据（默认保存位置是 LocaSpaceViewer 目录下的 download 文件夹，找到 TIF 后缀且大小正确的文件，就是我们的高程数据）

2. 在弹出的对话框中选择**是**，如下图

    ![加载高程数据](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910114703.png)

3. 在菜单中选择**工具**，**设置**，然后选择**投影**，配置投影坐标系参数，如下图所示

    ![配置平面投影坐标系](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910115028.png)

4. 保存成 DEM 格式的文件。在菜单栏中选择**文件 -> 输出 -> 输出海拔网格格式**，然后选择 **DEM**

    ![输出DEM文件格式](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910115557.png)

5. 填写图幅名称，垂直单位选择米，点击确定，即可将高程数据保存为 DEM 格式的文件~

    ![](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910115834.png)

### 对卫星影像数据进行预处理
1. 在 global mapper 中打开之前下载的卫星影像数据

    ![卫星影像数据](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910132810.png)

2. 按照同样的步骤将影像的数据转换到平面投影坐标系下，如下图

    ![转换到平面投影坐标系](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910133117.png)

3. 将图像保存成 TIF 格式。在菜单栏中选择**文件 -> 输出 -> 输出光栅/图像格式**，选择输出格式为 **GeoTIFF**，如下

    ![将图像保存成 TIF 格式](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910133441.png)

4. 保持参数方面如果不清楚的话，就保持原样就好了，点击最下面的确认按钮即可。（如果发现最下面的确认按钮看不到的话，可以将电脑的缩放比例调成 100%，就能看见确认按钮了(oﾟ▽ﾟ)o  ）

    ![确认按钮](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910134123.png)


## 在 ArcScene 中构建三维地图模型

1. 打开 ArcScene，将卫星影像数据拖拽进 ArcScene 即可加载图像

2. 是否创建金字塔选择**否**即可，这样就可以不生成一些额外的文件。

3. 在左侧图层中的图像名称上右击，点击**属性**，然后选择**基本高度**，选择在自定义表面浮动，加载上一步中得到的 DEM 高程数据，如下图所示

    ![加载DEM高程数据](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910140938.png)

4. 如果觉得高度差不明显，可以将下面的系数调大，然后点击确定。最终效果展示如下图~

    ![最终效果展示](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200910141850.png)