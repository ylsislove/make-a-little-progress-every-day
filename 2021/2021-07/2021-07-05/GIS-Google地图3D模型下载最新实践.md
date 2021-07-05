# GIS-Google地图3D城市模型下载最新实践

  - [前言](#%E5%89%8D%E8%A8%80)
  - [环境](#%E7%8E%AF%E5%A2%83)
    - [Google Chrome](#google-chrome)
    - [RenderDoc](#renderdoc)
    - [Blender](#blender)
    - [Maps Models Importer](#maps-models-importer)
    - [百度网盘打包下载](#%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98%E6%89%93%E5%8C%85%E4%B8%8B%E8%BD%BD)
  - [具体实践](#%E5%85%B7%E4%BD%93%E5%AE%9E%E8%B7%B5)
    - [1. 修改 Chrome 运行方式](#1-%E4%BF%AE%E6%94%B9-chrome-%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F)
    - [2. 关闭所有的 Chrome 浏览器窗口，然后双击刚刚修改的快捷方式](#2-%E5%85%B3%E9%97%AD%E6%89%80%E6%9C%89%E7%9A%84-chrome-%E6%B5%8F%E8%A7%88%E5%99%A8%E7%AA%97%E5%8F%A3%E7%84%B6%E5%90%8E%E5%8F%8C%E5%87%BB%E5%88%9A%E5%88%9A%E4%BF%AE%E6%94%B9%E7%9A%84%E5%BF%AB%E6%8D%B7%E6%96%B9%E5%BC%8F)
    - [3. 打开 RenderDoc 软件](#3-%E6%89%93%E5%BC%80-renderdoc-%E8%BD%AF%E4%BB%B6)
    - [4. 捕获 Google 地图的 3D 城市模型](#4-%E6%8D%95%E8%8E%B7-google-%E5%9C%B0%E5%9B%BE%E7%9A%84-3d-%E5%9F%8E%E5%B8%82%E6%A8%A1%E5%9E%8B)
    - [5. 在 Blender 中查看捕获的 3D 城市模型](#5-%E5%9C%A8-blender-%E4%B8%AD%E6%9F%A5%E7%9C%8B%E6%8D%95%E8%8E%B7%E7%9A%84-3d-%E5%9F%8E%E5%B8%82%E6%A8%A1%E5%9E%8B)
    - [6. 将模型导出成 FBX 格式](#6-%E5%B0%86%E6%A8%A1%E5%9E%8B%E5%AF%BC%E5%87%BA%E6%88%90-fbx-%E6%A0%BC%E5%BC%8F)

## 前言
最近接触到 RenderDoc 工具，可以下载到 Google Map 的 3D 城市模型。经过一番踩坑后，终于实践成功啦，在此记录下来，方便后面的小伙伴进行学习~

最终下载的 3D 城市模型效果如下（香港区域的城市模型）：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705114915.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705114915.png)

## 环境
### Google Chrome
Chrome 浏览器是必须的。我看到网上有些教程说需要使用老版本的 Chrome，但经过我长达一天的折腾后，发现老版本的 Chrome 下载的 3D 城市模型始终有问题（捂脸），可能是我电脑的原因，下载的模型无法导入 Blender。在最后之际，又重新安装了最新版的 Chrome，惊喜的发现成功了，真是开心哈哈

我用的 Chrome 是当前时间（2021-07-05）的最新版 `91.0.4472.101`，后面尝试的小伙伴也可以尝试将 Chrome 升级到最新版，不一定要全按网上教程所说的，实践是检验真理的唯一标准哈哈

### RenderDoc
RenderDoc 是我们下载 Google 地图 3D 城市模型的主要工具，这里我使用的版本是 `1.13`

注意不要使用 `1.13` 以上的版本，因为以上版本移除了我们捕获模型所要使用的 `Inject into Process` 功能

RenderDoc 下载连接：[https://renderdoc.org/builds](https://renderdoc.org/builds)

### Blender
Blender 是一个 3D 模型展示软件，我们可以使用该软件查看下载的 3D 城市模型，并导出成其他的格式，如 FBX 格式。

我用的 Blender 版本是 `2.93.1`，下载链接如下

Blender 下载连接：[https://www.blender.org/download/](https://www.blender.org/download/)

### Maps Models Importer
安装好后的 Blender 导入选项没有 Google Map 导入，所以我们还需要安装 Maps Models Importer 插件扩展其功能

我用的 Maps Models Importer 版本是 `0.4.1 - RC1`，下载链接如下

Maps Models Importer 下载链接：[https://github.com/eliemichel/MapsModelsImporter/releases](https://github.com/eliemichel/MapsModelsImporter/releases)

### 百度网盘打包下载
如果有小伙伴懒得去以上网址下载软件，这里提供一个百度网盘的链接，需要的可以自取哈哈

链接：https://pan.baidu.com/s/1PhQbZoP_Hud-cHtlDqRyWQ 
提取码：63b9 

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705115708.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705115708.png)

## 具体实践
### 1. 修改 Chrome 运行方式
在 Chrome 快捷方式上右击 `属性`，编辑 `目标` 为如下字符串：`C:\Windows\System32\cmd.exe /c "SET RENDERDOC_HOOK_EGL=0 && START "" ^"D:\scoop\apps\googlechrome\current\chrome.exe^" --disable-gpu-sandbox --gpu-startup-dialog"`，如下图所示

注意修改 `D:\scoop\apps\googlechrome\current\chrome.exe` 为你自己 Chrome 的安装路径

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705104317.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705104317.png)

然后点击 `应用`，然后 `确定`。修改后的快捷方式变成如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705104525.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705104525.png)

### 2. 关闭所有的 Chrome 浏览器窗口，然后双击刚刚修改的快捷方式
这时界面会弹出一个小弹窗，如下图所示

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705105051.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705105051.png)

注意，这个小弹窗先 `不要点击确定`，切记哈，只需记住 pid 号即可

### 3. 打开 RenderDoc 软件
打开刚刚安装好的 RenderDoc 软件。然后在菜单栏 File 里点击 `Inject into Process` 选项，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705105344.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705105344.png)

在面板里输入刚刚 Chrome 弹窗里的那个 pid 号，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705105519.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705105519.png)

然后双击搜索出来的那个进程，显示如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705105616.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705105616.png)

这时，我们点击 Chrome 小弹窗上的确认按钮，可以看到 RenderDoc 面板上的 API 状态变成了 `D3D11`，右边的按钮也由灰色变成可点击的状态，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705105910.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705105910.png)

这时再跳转到 Chrome 浏览器，可以看到浏览器左上角出现了一个状态栏，这是正常哒

这时，我们可以在浏览器地址栏输入以下网址，打开 Google Map

`https://www.google.com/maps/place/香港/@22.3147582,114.1649326,1059a,35y,350.39h/data=!3m1!1e3!4m5!3m4!1s0x3403e2eda332980f:0xf08ab3badbeac97c!8m2!3d22.3193039!4d114.1693611`

按 `F11` 进入全屏状态，鼠标移动到左下角 `图层` 上，点击 `更多`，取消标签显示，如下图所示

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705111139.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705111139.png)

### 4. 捕获 Google 地图的 3D 城市模型
完成以上步骤后，跳转到 RenderDoc 软件，点击 `Capture Frame(s) Immediately` 按钮，然后再跳转到 Chrome 界面，微微拖动下地图，可以发现当前界面的 3D 城市模型已经被捕获到 RenderDoc 里啦，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705111802.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705111802.png)

注意捕获的模型大小，一般模型大小会有四五十兆，如果模型大小只有一二十兆，那应该是这次捕获失败了。不要担心，右击把这次捕获的模型删除，然后按上面步骤重新捕获一次就好啦

双击捕获的模型，打开 Texture Viewer 面板，选择 `Colour Pass #1`，可以看到一连串的 `DrawIndexed`，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705112051.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705112051.png)

点击第一个 `DrawIndexed`，然后按住键盘方向键的 `↓` 键，可以看到 Texture Viewer 面板里城市模型被一点点显示出来，如下图，这就说明这次捕获是成功的~

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705113004.gif)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705113004.gif)

鼠标选中列表的 `Colour Pass #1`，然后点击菜单栏中的 `File`，点击 `Save Capture As`，将刚刚捕获的模型保存成 `.rdc` 文件

### 5. 在 Blender 中查看捕获的 3D 城市模型
打开 Blender 软件，将界面中默认的物体选中，按 Delete 删除。

默认安装的 Blender 软件 `Google Map Capture` 的导入选项的，这时就需要安装之前下载好的 Blender 插件了。

点击菜单栏 `Edit`，点击 `Preferences`，在打开的界面上选择 `Add-ons`，然后点击 `Install`，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705113704.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705113704.png)

在打开的界面选择我们已下载好的 `MapsModelsImporter-0.4.1-rc1.zip` 文件，然后点击安装。

安装完成后，还需要将插件启用，勾选插件前面的单选框即可，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705113924.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705113924.png)

然后我们就可以导入 Google Map 文件啦

点击菜单栏的 `File`，点击 `Import`，最下面就出现了 `Google Map Capture` 选项了，点击，选择刚刚保存的 `.rdc` 文件，稍等片刻，模型便被显示在 Blender 里啦。默认没有显示材质贴图，我们可以点击界面右上角的这个按钮，打开贴图渲染，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705114342.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705114342.png)

打开贴图的效果如下

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705114426.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210705114426.png)

### 6. 将模型导出成 FBX 格式
这时我们可以用鼠标框选住所有的模型，然后按 `Ctrl + j` 键，将模型合并成一个模型。

然后选中模型，点击菜单栏的 `File`，点击 `Export`，选择 `FBX` 格式，就可以将这个 3D 城市模型导出成 FBX 格式的啦。

以上就是教程的全部内容，感谢阅读~

