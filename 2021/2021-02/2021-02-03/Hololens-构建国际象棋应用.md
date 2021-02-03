# Hololens-构建国际象棋应用

## 前言
本文取自微软 Hololens [官方开发文档](https://docs.microsoft.com/zh-cn/windows/mixed-reality/)，笔者实践后，将其中过时的步骤和图片进行更新，并在此记录下来，希望能对其他热衷于 Hololens 开发的小伙伴们有所帮助~

## 入门
无论你是混合现实新手还是经验丰富的专业人员，都可以使用 HoloLens2 和 Unreal Engine 开始你的体验之旅。 本系列教程将为你提供有关如何使用 UX Tools 插件构建交互式象棋应用的分步指南，该插件是 Unreal 混合现实工具包的一部分。 该插件将帮助你通过代码、蓝图和示例将常见的 UX 功能添加到项目中。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203221424.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203221424.png)

在本系列文章结束时，你将拥有以下方面的经验：
- 开始新项目
- 设置混合现实
- 使用用户输入
- 添加按钮
- 在模拟器或设备上播放

### 必备知识
在开始之前，请确保已安装以下项：
* Windows 10 1809 或更高版本
* Windows 10 SDK 10.0.18362.0 或更高版本
* Unreal Engine 4.25 或更高版本
* 针对开发配置的 Microsoft HoloLens 2 设备，或仿真器
* 具有以下工作负载的 Visual Studio 2019

> 笔者注：笔者使用的是 Unreal Engine 4.26 版本，对应的后面下载的 UX Tools 插件的版本也和原文有所不同。如果版本不匹配，最后的打包部署步骤就会失败。具体情况后面会详细说明。

### 安装 Visual Studio 2019
首先，确保使用所有必需的 Visual Studio 包进行设置：
1. 安装最新版本的 Visual Studio 2019
2. 安装以下工作负载：
    - 使用 C++ 的桌面开发
    - .NET 桌面开发
    - 通用 Windows 平台开发
3. 展开“通用 Windows 平台开发”并选择：
    - USB 设备连接性
    - C++ (v142) 通用 Windows 平台工具
4. 安装以下组件：
    - 编译器、生成工具和运行时 > MSVC v142 - VS 2019 C++ ARM64 生成工具（最新版本）

可使用以下图片确认安装

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203222151.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203222151.png)

就这么简单！ 一切准备就绪，现在可以开始象棋项目了。

## 初始化你的项目
在本章节，你将开始从一个新 Unreal 项目着手，需启用 HoloLens 插件、创建和点亮关卡，以及添加棋子。 你可将我们预制的资产用于所有 3D 对象和材质，因此不必担心需自行建模的问题。 本章节结束时，你会有一个可用于混合现实的空白画布。

> 重要：请确保满足入门中的所有先决条件。

### 目标
- 为 HoloLens 开发配置 Unreal 项目
- 导入资产和设置场景
- 使用蓝图创建 Actor 和脚本级别事件

### 创建新的 Unreal 项目
首先需要一个待处理的项目。 如果你是刚接触的 Unreal 开发人员，则需要从 Epic Launcher 下载支持文件。步骤如下：
- 转到“编辑器首选项”>“常规”>“源代码”>“源代码编辑器”，然后检查是否已选择 Visual Studio 2019。
- 转到 Epic Games Launcher 的“库”选项卡，选择“启动”旁的下拉箭头，然后单击“选项”。
- 在“目标平台”下，选择“HoloLens 2”，然后单击“应用”。

  [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203230109.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203230109.png)

1. 启动 Unreal Engine
2. 在“新项目类别”中选择“游戏”，然后单击“下一步” 。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203230316.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203230316.png)

3. 选择“空白”模板，然后单击“下一步” 。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203230451.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203230451.png)

4. 在项目设置中选择“C++”、“可缩放的 3D 或 2D”、“移动/平板电脑”和“非初学者内容”，然后选择保存位置并单击“创建项目” 。

    > 为了生成 UX Tools 插件，必须选择 C++ 项目而不是 Blueprint 项目，你稍后将在第 4 节中对此进行设置

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203230557.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203230557.png)

项目应在 Unreal 编辑器中自动打开，这意味着你已准备好进入下一部分。

### 启用所需插件
你需要启用两个插件，然后才能开始向场景添加对象。
1. 打开“编辑”>“插件”，并从内置选项列表中选择“增强现实”。
    - 向下滚动到“HoloLens”并选中“已启用”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203231259.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203231259.png)

2. 从内置选项列表中选择“虚拟现实”。
    - 向下滚动到“Microsoft Windows Mixed Reality”，选择“已启用”，然后重启编辑器 。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203231515.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203231515.png)

> 这两个插件都是 HoloLens 2 开发所必需的。

### 创建关卡
下一个任务是创建具有可供参考和缩放的起点和立方体的玩家设置。
1. 选择“文件”>“新建关卡”>“空关卡”。 视口中的默认场景现在应为空。
2. 从“模式”选项卡中选择“基础”，并将“玩家出生点”拖到场景中。
    - 在“详细信息”选项卡中，将“位置”设置为“X = 0”、“Y = 0”和“Z = 0”，以便在应用启动时将用户设置到场景的中心。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203232358.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203232358.png)

3. 将“立方体”从“基本”选项卡拖到场景中。
    - 将“位置”设置为“X = 50”、“Y = 0”和“Z = 0” 。 在启动时将立方体放在距离玩家 50 厘米的位置。
    - 将“比例”更改为“X = 0.2”、“Y = 0.2”和“Z = 0.2”以缩小立方体。
4. 切换到“模式”面板上的“光源”选项卡，然后将“定向光源”拖到场景中。将光源置于“玩家出生点”上方，以便可以看到该光源。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203232847.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203232847.png)

5. 转到“文件”>“保存当前关卡”，将关卡命名为“main”，然后选择“保存”。

设置场景后，按工具栏中的“开始”，以查看正在运行的立方体！ 完成工作后，按 Esc 停止应用程序。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203233140.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203233140.png)

设置场景后，便可以开始在棋盘和棋子中进行添加以构成应用程序环境。

### 导入资产
场景目前看起来非常空，但通过将现成的资产导入到项目中，将解决此问题。
1. 使用 7-zip 下载并解压缩 [GitHub](https://github.com/microsoft/MixedReality-Unreal-Samples/blob/master/ChessApp/ChessAssets.7z) 资产文件夹。
2. 从“内容浏览器”中选择“新增”>“新建文件夹”，然后将其命名为“ChessAssets”。
    - 双击新文件夹，这是导入 3D 资产的位置。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203233446.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203233446.png)

3. 从“内容浏览器”中选择“导入”，选择解压缩的资产文件夹中的所有项目，然后单击“打开”。
    - 资产包括棋盘和棋子的 3D 对象网格（采用 FBX 格式）和用于材质的纹理映射（采用 TGA 格式）。
4. 弹出“FBX 导入选项”窗口后，展开“材质”部分，并将“材质导入方法”更改为“不创建材质” 。
    - 选择“全部导入”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203233707.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210203233707.png)

资产只需执行这些操作。接下来的一组任务是使用蓝图创建应用程序的构建基块。

### 添加蓝图
待更
