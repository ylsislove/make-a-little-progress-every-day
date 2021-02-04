# Hololens-构建国际象棋应用（unreal）

  - [前言](#%E5%89%8D%E8%A8%80)
  - [入门](#%E5%85%A5%E9%97%A8)
    - [必备知识](#%E5%BF%85%E5%A4%87%E7%9F%A5%E8%AF%86)
    - [安装 Visual Studio 2019](#%E5%AE%89%E8%A3%85-visual-studio-2019)
  - [初始化你的项目](#%E5%88%9D%E5%A7%8B%E5%8C%96%E4%BD%A0%E7%9A%84%E9%A1%B9%E7%9B%AE)
    - [目标](#%E7%9B%AE%E6%A0%87)
    - [创建新的 Unreal 项目](#%E5%88%9B%E5%BB%BA%E6%96%B0%E7%9A%84-unreal-%E9%A1%B9%E7%9B%AE)
    - [启用所需插件](#%E5%90%AF%E7%94%A8%E6%89%80%E9%9C%80%E6%8F%92%E4%BB%B6)
    - [创建关卡](#%E5%88%9B%E5%BB%BA%E5%85%B3%E5%8D%A1)
    - [导入资产](#%E5%AF%BC%E5%85%A5%E8%B5%84%E4%BA%A7)
    - [添加蓝图](#%E6%B7%BB%E5%8A%A0%E8%93%9D%E5%9B%BE)
    - [使用材质](#%E4%BD%BF%E7%94%A8%E6%9D%90%E8%B4%A8)
    - [填充场景](#%E5%A1%AB%E5%85%85%E5%9C%BA%E6%99%AF)
  - [Mixed Reality 设置](#mixed-reality-%E8%AE%BE%E7%BD%AE)
    - [目标](#%E7%9B%AE%E6%A0%87-1)
    - [添加会话资产](#%E6%B7%BB%E5%8A%A0%E4%BC%9A%E8%AF%9D%E8%B5%84%E4%BA%A7)
    - [创建 Pawn](#%E5%88%9B%E5%BB%BA-pawn)
    - [创建游戏模式](#%E5%88%9B%E5%BB%BA%E6%B8%B8%E6%88%8F%E6%A8%A1%E5%BC%8F)
  - [添加交互性](#%E6%B7%BB%E5%8A%A0%E4%BA%A4%E4%BA%92%E6%80%A7)
    - [目标](#%E7%9B%AE%E6%A0%87-2)
    - [下载混合现实 UX Tools 插件](#%E4%B8%8B%E8%BD%BD%E6%B7%B7%E5%90%88%E7%8E%B0%E5%AE%9E-ux-tools-%E6%8F%92%E4%BB%B6)
    - [生成手势交互 Actor](#%E7%94%9F%E6%88%90%E6%89%8B%E5%8A%BF%E4%BA%A4%E4%BA%92-actor)
    - [附加操控器](#%E9%99%84%E5%8A%A0%E6%93%8D%E6%8E%A7%E5%99%A8)
    - [测试场景](#%E6%B5%8B%E8%AF%95%E5%9C%BA%E6%99%AF)
  - [UI 和函数](#ui-%E5%92%8C%E5%87%BD%E6%95%B0)
    - [目标](#%E7%9B%AE%E6%A0%87-3)
    - [创建重置函数](#%E5%88%9B%E5%BB%BA%E9%87%8D%E7%BD%AE%E5%87%BD%E6%95%B0)
    - [添加按钮](#%E6%B7%BB%E5%8A%A0%E6%8C%89%E9%92%AE)
    - [触发函数](#%E8%A7%A6%E5%8F%91%E5%87%BD%E6%95%B0)
  - [打包和部署](#%E6%89%93%E5%8C%85%E5%92%8C%E9%83%A8%E7%BD%B2)
    - [目标](#%E7%9B%AE%E6%A0%87-4)
    - [[仅设备] 流式传输](#%E4%BB%85%E8%AE%BE%E5%A4%87-%E6%B5%81%E5%BC%8F%E4%BC%A0%E8%BE%93)
    - [通过设备门户打包和部署应用](#%E9%80%9A%E8%BF%87%E8%AE%BE%E5%A4%87%E9%97%A8%E6%88%B7%E6%89%93%E5%8C%85%E5%92%8C%E9%83%A8%E7%BD%B2%E5%BA%94%E7%94%A8)

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
1. 在“内容浏览器”中选择“添加/导入”>“新建文件夹”，然后将其命名为“Blueprints” 。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203048.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203048.png)

    > 如果你不熟悉蓝图，这些蓝图为特殊资产，它们提供基于节点的接口来创建新类型的 Actor 和脚本级别事件。

2. 双击“Blueprints”文件夹，然后右键单击并选择“蓝图类”。
    - 选择“Actor”并将蓝图命名为“Board”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203237.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203237.png)

    新的棋盘蓝图现在显示在“Blueprints”文件夹中，如以下屏幕截图中所示 。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203326.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203326.png)

    你已经准备好开始向创建的对象添加材质。

### 使用材质
你创建的对象默认为灰色，这看上去太过普通。向对象添加材质和网格是本章节中的最后一组任务。
1. 双击“棋盘”以打开蓝图编辑器。
2. 从“组件”面板中选择“添加组件”>“场景组件”，并将其命名为“Root” 。 请注意，“Root”在下面的屏幕截图中显示为 DefaultSceneRoot 的子项：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203543.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203543.png)

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203701.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203701.png)

3. 单击“Root”并将其拖到 DefaultSceneRoot 中，以替换它并在视口中消除球面。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203741.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203741.png)

4. 从“组件”面板中选择“添加组件”>“静态网格体组件”，并将其命名为“SM_Board”。它将在“Root”下显示为子对象。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203901.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204203901.png)

5. 选择“SM_Board”，向下滚动到“细节”面板的“静态网格体”部分，并从下拉列表中选择“棋盘”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204052.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204052.png)

6. 继续在“细节”面板中，展开“材质”部分，然后从下拉列表中选择“新建资产”>“材质”。

    - 将材质命名为“M_ChessBoard”，并将其保存到“ChessAssets”文件夹中。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204158.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204158.png)

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204314.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204314.png)

7. 双击“M_ChessBoard”材质映像以打开材质编辑器。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204402.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204402.png)

8. 在材质编辑器中，单击右键并搜索“纹理示例”。
    - 在“细节”面板中展开“材质表达式纹理Base”部分，然后将“纹理”设置为“ChessBoard_Albedo”。
    - 将“RGB”输出引脚拖至“M_ChessBoard”的“基础颜色”引脚上。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204506.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204506.png)

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204901.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204204901.png)

9. 再重复上述步骤 4 次以再创建四个具有以下设置的“纹理示例”节点：
    - 将“纹理”设置为“ChessBoard_AO”，将“RGB”链接到“环境光遮挡”引脚。
    - 将“纹理”设置为“ChessBoard_Metal”，将“RGB”链接到“Metallic”引脚。
    - 将“纹理”设置为“ChessBoard_Normal”，将“RGB”链接到“Normal”引脚。
    - 将“纹理”设置为“ChessBoard_Rough”，将“RGB”链接到“粗糙度”引脚。
    - 单击“保存”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204205525.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204205525.png)

    在继续之前，请确保材质设置看起来类似于以上屏幕截图。

### 填充场景
如果返回到“棋盘”蓝图，将会看到已应用刚创建的材质。只需设置场景即可！首先，更改以下属性，以确保在场景中放置棋盘时，它的大小和角度正确：
1. 将“比例”设置为“(0.05, 0.05, 0.05)”并将“Z旋转”设置为“90”。
    - 单击顶部工具栏中的“编译”，然后单击“保存”并返回到主窗口。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204205924.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204205924.png)

2. 在右侧世界大纲视图中，右键单击“Cube”>“编辑”>“删除”并将“棋盘”从“内容浏览器”拖至视口中。
    - 将“位置”设置为“X = 80”、“Y = 0”和“Z = -20”。

3. 点击“运行”按钮，查看你所处关卡中的新棋盘。 按 Esc 返回到编辑器。

现在，你将按照与棋盘相同的步骤创建棋子：
1. 转到“蓝图”文件夹，右键单击并选择“蓝图类”，然后选择“Actor”。将 Actor 命名为“WhiteKing”。

2. 双击“WhiteKing”以在蓝图编辑器中将其打开，选择“添加组件”>“场景组件”，并将其命名为“Root”。
    - 将“Root”拖放到 DefaultSceneRoot 中来替换它。

3. 单击“添加组件”>“静态网格体组件”，并将其命名为“SM_King”。
    - 在“细节”面板中，将“静态网格”设置为“Chess_King”，并将“材质”设置为名为“M_ChessWhite”的新材质。

4. 在材质编辑器中打开“M_ChessWhite”，并将以下“纹理示例”节点连接到以下各项：
    - 将“纹理”设置为“ChessWhite_Albedo”并将“RGB”链接到“基本颜色”引脚 。
    - 将“纹理”设置为“ChessWhite_AO”，将“RGB”链接到“环境遮蔽”引脚。
    - 将“纹理”设置为“ChessWhite_Metal”，将“RGB”链接到“金属”引脚。
    - 将“纹理”设置为“ChessWhite_Normal”，将“RGB”链接到“正常”引脚。
    - 将“纹理”设置为“ChessWhite_Rough”，将“RGB”链接到“粗糙度”引脚。
    - 单击“保存”。

在继续之前，“M_ChessKing”材质应与下图类似。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204210841.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204210841.png)

即将完成，只需将新棋子添加到场景中即可：
1. 打开“WhiteKing”蓝图，并将“比例”更改为“(0.05, 0.05, 0.05)”，将“Z旋转”更改为“90”。
    - 编译并保存蓝图，然后返回到主窗口。

2. 将“WhiteKing”拖到视口中，切换到“世界大纲视图”面板，将“WhiteKing”拖到“棋盘”上，使其成为子对象。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204211109.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204211109.png)

3. 在“详细信息”面板中的“变换”下，将 WhiteKing 的“位置”设置为“X = -26”、“Y = 4”、“Z = 0” 。

完成！ 选择“运行”以查看正在运行中的已填充关卡，并在准备好退出时按 Esc。 只是创建一个简单项目就涉及了很多内容，你现在可以进入本系列的下一部分：设置混合现实。

## Mixed Reality 设置
在上一个章节中设置了象棋应用项目。本部分将逐步介绍如何设置此应用，来进行混合现实开发，这意味着要添加 AR 会话。 此任务将使用 ARSessionConfig 数据资产，其中包含有用的 AR 设置，如空间映射和遮挡。可以在 Unreal 的文档中找到有关 ARSessionConfig 资产和 UARSessionConfig 类的更多详细信息。

### 目标
- 使用 Unreal Engine 的 AR 设置
- 使用 ARSessionConfig 数据资产
- 设置 Pawn 和游戏模式

### 添加会话资产
Unreal 中的 AR 会话无法自行发生。要使用会话，需要借助 ARSessionConfig 数据资产，这就是接下来的任务：
1. 单击“内容浏览器”中的“添加/导入 > 其他 > 数据资产”。 请确保自己处于根 Content 文件夹级别。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204212158.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204212158.png)

    - 选择“ARSessionConfig”，单击“选择”，然后将资产命名为“ARSessionConfig”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204212325.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204212325.png)

2. 双击“ARSessionConfig”将其打开，保留所有默认设置，点击“保存”。 返回到主窗口。

完成此操作后，下一步是确保在关卡加载时 AR 会话会启动，而在关卡结束时 AR 会话会停止。幸运的是，Unreal 具有叫做“关卡蓝图”的特殊蓝图，它用作关卡范围的全局事件图。在关卡蓝图中连接 ARSessionConfig 资产，可确保游戏开始时 AR 会话将立即触发。

1. 从编辑器工具栏中单击“蓝图 > 打开关卡蓝图”：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204212520.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204212520.png)

2. 将执行节点（向左箭头图标）拖离“事件开始运行”，随后放开，然后搜索“启动 AR 会话”节点并按 Enter。
    - 单击“会话配置”下的“选择资产”下拉列表，然后选择“ARSessionConfig”资产。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204212839.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204212839.png)

3. 右键单击事件图表中的任意位置，然后创建一个新的 Event EndPlay 节点。 拖动执行脚本，随后放开，然后搜索“停止 AR 会话”节点并按 Enter。 如果在关卡结束时 AR 会话仍在运行，那么在流式传输到头戴显示设备时，如果你重启应用，某些功能可能会停止工作。
    - 点击“编译”和保存”，然后返回到主窗口。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213028.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213028.png)

### 创建 Pawn
此时，项目仍需要一个玩家对象。 在 Unreal 中，Pawn 表示游戏中的用户，但在本例中它将代表 HoloLens 2。
1. 在 Content 根文件夹中单击“添加新项 > 蓝图类”，展开底部的“所有类”部分。

    - 搜索“DefaultPawn”，单击“选择”，将其命名为“MRPawn”，然后双击资产打开它。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213247.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213247.png)

2. 从“组件”面板中单击“添加组件”>“摄像机组件”，然后将其命名为“Camera”。确保“相机”组件是根 (CollisionComponent) 的直接子级。这样，玩家相机就能随 HoloLens 2 设备一起移动。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213404.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213404.png)

    > 默认情况下，Pawn 具有网格和碰撞组件。 在大多数 Unreal 项目中，Pawn 都是可与其他组件碰撞的固体。 在混合现实中 Pawn 与用户相同，因此需要能够在不发生碰撞的情况下传递全息影像。

3. 从“组件”面板中选择“CollisionComponent”，向下滚动到“细节”面板的“碰撞”部分。
    - 单击“碰撞预设”下拉列表，将值更改为“NoCollision”。
    - 对“MeshComponent”执行同样的操作

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213603.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213603.png)

4. 编译并保存蓝图。

从此处完成操作后，返回到主窗口。

### 创建游戏模式
混合现实设置的最后一个部分是游戏模式。 游戏模式决定着游戏或体验的诸多设置，其中包括要使用的默认 Pawn。
1. 在“内容”文件夹中单击“添加/导入”>“蓝图类”，然后选择“游戏模式基础”作为父类 。 将其命名为“MRGameMode”并双击以打开。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213827.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213827.png)

2. 转到“细节”面板中的“类”部分，将“默认 Pawn 类”更改为“MRPawn”。
    - 点击“编译”和保存”，然后返回到主窗口。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213927.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204213927.png)

3. 选择“编辑 > 项目设置”，然后从左侧列表单击“地图和模式”。
    - 展开“默认模式”，将“默认游戏模式”更改为“MRGameMode”。
    - 展开“默认地图”，将“EditorStartupMap”和“GameDefaultMap”都设置为“main”。 当你关闭并重新打开编辑器或玩游戏时，现在将默认选择主地图。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204215917.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204215917.png)

针对混合现实全面设置此项目后，你可以继续学习下一章节，开始将用户输入添加到场景中。

## 添加交互性
在上一个教程中，你添加了 ARSession、Pawn 和游戏模式，以完成针对象棋应用的混合现实设置。本部分重点介绍如何使用开放源代码的混合现实工具包 UX Tools 插件，它提供了使场景具有交互性的工具。本部分结束时，棋子将按照用户输入移动。

### 目标
- 从 GitHub 安装混合现实 UX Tools 插件
- 将手势交互 Actor 添加到指尖
- 创建操控器并将其添加到场景中的对象
- 使用输入模拟来验证项目

### 下载混合现实 UX Tools 插件
在开始使用用户输入之前，需要将插件添加到项目。
1. 在 GitHub 上的混合现实 UX Tools [发布页](https://github.com/microsoft/MixedReality-UXTools-Unreal/releases)上，导航到适用于 Unreal 的 UX Tools v0.11.0 版本并下载 UXTools.0.11.0.zip。 解压缩文件。
   
   > 笔者注：官方文档上所使用的是 UX Tools v0.10.0，对应 UE 版本是 4.25。经笔者实践后，UE 4.26 应该使用 UXTools.0.11.0.zip。

2. 在项目的根文件夹中，创建一个名为“Plugins”的新文件夹。 将解压缩的 UXTools 插件复制到此文件夹中，然后重新启动 Unreal 编辑器。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204225813.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204225813.png)

3. UXTools 插件具有一个“内容”文件夹（带有组件子文件夹，包括“按钮”、“输入模拟”和“指针”），以及一个包含额外代码的“C++ 类”文件夹。

    > 如果在“内容浏览器”中看不到“UXTools 内容”部分，请单击“视图选项”>“显示插件内容” 。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204231042.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204231042.png)

    可以在混合现实 UX Tools [GitHub](https://aka.ms/uxt-unreal) 存储库中找到其他插件文档。

    安装插件后，便可以开始使用它所提供的工具，从手势交互 Actor 开始。

### 生成手势交互 Actor
与 UX 元素的手势交互是使用手势交互 Actor 完成的，这些手势交互 Actor 为近距和远距交互创建并驱动指针和视觉对象。
- 近距交互 - 缩放食指和拇指之间的元素或使用指尖戳元素。
- 远距交互 - 将虚拟手的光线指向元素并同时按住食指和拇指。

在我们的示例中，将手势交互 Actor 添加到 MRPawn 可达到以下目的：
- 将光标添加到 Pawn 的食指指尖。
- 提供可通过 Pawn 操纵的精确手势输入事件。
- 通过从虚拟手的手掌延伸出的手部光线允许远距交互输入事件。

建议在继续之前通读介绍手动交互的[文档](https://microsoft.github.io/MixedReality-UXTools-Unreal/Docs/HandInteraction.html)。

准备就绪后，打开“MRPawn”蓝图，然后转到“事件图”。
1. 将执行引脚从“事件开始运行”拖离然后释放，以放置一个新节点。
    - 选择“从类生成Actor”，单击“类”引脚旁边的下拉列表，并搜索“UXT 手势交互 Actor”。

2. 生成第二个“UXT 手势交互 Actor”，这次会将手势设置为“向右”。事件开始时，将会在每只手上生成 UXT 手势交互 Actor。

事件图应与以下屏幕截图匹配：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204233134.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204233134.png)

两个 UXT 手势交互 Actor 均需要所有者和初始变形位置。 在这种情况下，初始变形并不重要，因为 UX Tools 插件中包含手势交互 Actor，后者可见后便立即跳转到虚拟手。 但是，SpawnActor 函数需要使用变形输入来避免编译器错误，因此你将使用默认值。

1. 从“Spwan Transform”引脚拖拽，然后释放，即可放置一个新节点。
    - 搜索“创建变化”节点，然后将“返回值”拖到另一个手势的“Spwan Transform”，以便连接两个 SpawnActor 节点 。

2. 选择两个 SpawnActor 节点底部的“向下箭头”，以显示“Owner”引脚。
    - 从“Owner”引脚拖拽，然后释放，即可放置一个新节点。
    - 搜索“self”并选择“获得一个对自身的引用”。
    - 在 Self 对象引用节点和另一个手势交互 Actor 的“Own”引脚之间创建连线。

3. 最后，同时选中两个手势交互 Actor 的“在抓取目标上显示近光标”框框。当食指靠近时，光标应出现在抓取目标上，这样就可以看到手指相对于目标的位置。
    - 编译并保存后返回到主窗口。

确保连接与以下屏幕截图匹配，但可随意拖动节点以使蓝图更具可读性。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204235038.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210204235038.png)

可以在 [UX Tools 文档](https://microsoft.github.io/MixedReality-UXTools-Unreal/Docs/HandInteraction.html)中找到有关手动交互 Actor 的详细信息。

现在，项目中的虚拟手可以选择对象，但仍无法对其进行操纵。测试应用之前的最后一个任务是将操控器组件添加到场景中的 Actor。

### 附加操控器
操控器是一个响应精确手动输入的组件，可进行抓取、旋转和平移。 将操控器的变形应用到 Actor 变形可允许进行直接 Actor 操纵。

1. 在“组件”面板中，打开“棋盘”蓝图，单击“添加组件”并搜索“UXT 通用操控器”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205001032.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205001032.png)

2. 展开“细节”面板中的“通用操控器”部分。可以在其中设置单手操纵或双手操纵、旋转模式和平滑模式。可以随意选择所需的模式，然后编译和保存棋盘。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205001508.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205001508.png)

3. 对 WhiteKing Actor 重复以上步骤。

可以在[文档](https://microsoft.github.io/MixedReality-UXTools-Unreal/Docs/Manipulator.html)中找到有关混合现实 UX Tools 插件中提供的操控器组件的详细信息。

### 测试场景
好消息！你已准备好使用其新的虚拟手和用户输入来测试应用。在主窗口中按“运行”，应该会看到两个网格手，且从每个手掌延伸出手部光线。可以按如下所示控制手势及其交互：
- 按住“左 Alt”键以控制左手，按住“左 Shift”键以控制右手。
- 移动鼠标来移动手，并滚动鼠标滚轮，向前或向后移动手 。
- 使用鼠标左键进行缩放，使用鼠标中键执行戳操作。

> 如果你有多个头戴显示设备插入电脑，则输入模拟可能无法正常工作。 如果遇到问题，请尝试拔下其他头戴显示设备。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205002000.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205002000.png)

请尝试使用模拟手来拿起、移动和放下白棋国王并操纵棋盘！ 试验近距交互和远距交互 - 请注意，当手足够靠近可直接抓住棋盘和国王时，食指指尖上的手指光标会取代手部光线。

可以在[文档](https://microsoft.github.io/MixedReality-UXTools-Unreal/Docs/InputSimulation.html)中找到有关 MRTK UX Tools 插件中提供的模拟手功能的详细信息。

现在，你的虚拟手可以与对象交互，接下来可以继续学习下一个教程，并添加用户界面和事件。

## UI 和函数
在上一节中，向棋盘的 Pawn 和操控器组件添加了手势交互 Actor，使它们具有交互性。 在本部分中，你将继续使用混合现实工具包 UX Tools 插件，使用蓝图中的新函数和 Actor 引用构建象棋应用。 本部分结束时，你就可以打包混合现实应用，并将其部署到设备或仿真器中。

### 目标
- 添加交互式按钮
- 创建用于重置棋子位置的函数
- 连接按钮，以在按下时触发此函数

### 创建重置函数
第一个任务是创建一个函数蓝图，来将象棋棋子重置到场景中的原始位置。
1. 打开“WhiteKing”，选择“我的蓝图”中“函数”部分旁的“+”图标，将其命名为“ResetLocation”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205002834.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205002834.png)

2. 从蓝图网格拖动并释放“重置位置”的执行箭头，以创建“SetActorRelativeTransform”节点。
    - 此函数可设置 Actor 相对于其父级的变形（位置、旋转和缩放）。将使用此函数来重置棋盘上国王的位置，即使棋盘已从其原始位置移动也无妨。

3. 在事件图表中右击，选择“创建变化”，然后将其“位置”更改为“X = -26”、“Y = 4”和“Z = 0”。
    - 将其“返回值”连接到“SetActorRelativeTransform”中的“新相对变换”引脚。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205003414.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205003414.png)

编译并保存项目，然后返回到主窗口。

### 添加按钮
正确设置此函数后，接下来的任务是创建一个按钮，以在按它时触发函数。

1. 单击“添加新项”>“蓝图类”，展开“所有类”部分，然后搜索“UxtPressableButtonActor”。
    - 将其命名为“ResetButton”，然后双击以打开蓝图。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205003644.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205003644.png)

2. 确保在“组件”面板中选择了“ResetButton(自身)” 。在“细节”面板中，导航到“按钮”部分。将默认“按钮标签”更改为“Reset”，展开“按钮图标画笔”部分，然后按“打开图标画笔编辑器”按钮。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205003935.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205003935.png)

    图标画笔编辑器随即打开，你可以使用该编辑器为按钮选择新图标。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205004027.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205004027.png)

    为配置按钮，还有很多其他的设置可以进行调整。若要了解有关 UXT 可按按钮组件的详细信息，请参阅[文档](https://microsoft.github.io/MixedReality-UXTools-Unreal/Docs/PressableButton.html)。

3. 单击“组件”面板中的“ButtonComponent(UxtPressableButton)(继承)”，将“细节”面板向下滚动到“事件”部分。
    - 单击“按钮按下时”旁的绿色 + 按钮，向事件图表添加事件，按下按钮时将调用该事件。

此时，需要调用“WhiteKing”的“重置位置”函数，这需要在关卡中引用“WhiteKing”Actor。

4. 在“我的蓝图”面板中，导航到“变量”部分，然后单击 + 按钮，将变量命名为“WhiteKing”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205004334.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205004334.png)

    - 在“详细信息”面板中，选择“变量类型”旁的下拉列表，搜索“WhiteKing”，然后选择“对象引用”。
    - 选中“实例可编辑”旁的框，这使得可从主关卡设置变量。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205004617.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205004617.png)

5. 将 WhiteKing 变量从“我的蓝图 > 变量”拖放到“‘重置’按钮事件图表”中，然后选择“获取 WhiteKing”。

### 触发函数
剩下的就是，在按下按钮时，正式触发重置函数。

1. 拖动“WhiteKing”输出引脚并释放以放置新节点。 选择“Reset Location”函数。 最后，将传出执行引脚从“按钮按下时”拖放到“重置位置”上的传入执行引脚。编译和保存 ResetButton 蓝图，然后返回到主窗口。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205004834.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205004834.png)

2. 将“ResetButton”拖到视口中，并将其位置设置为“X = 50”、“Y = -25”和“Z = 10”。 将其旋转设置为“Z = 180”。在“默认值”下，将 WhiteKing 变量的值设置为“WhiteKing”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205005047.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205005047.png)

运行应用，将象棋棋子移动到新位置，然后按 HoloLens 2 样式按钮来查看重置逻辑正在运行！

现在，你有了一个混合现实应用，其中包含可交互的棋子和棋盘，以及一个功能齐全的按钮，该按钮可重置棋子的位置。可以在 [GitHub](https://github.com/microsoft/MixedReality-Unreal-Samples/tree/master/ChessApp) 存储库中找到目前完成的该应用程序。请随意阅读本教程以外的内容并设置其余的棋子，以便按下“重置”按钮时重置整个棋盘。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205005208.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205005208.png)

你可以继续学习本教程的最后一部分，你将了解如何将应用打包并部署到设备或仿真器。

> 此时，在将应用程序部署到设备或仿真器之前，应使用建议的 [Unreal 性能设置](https://docs.microsoft.com/zh-cn/windows/mixed-reality/develop/unreal/performance-recommendations-for-unreal)来更新项目。

## 打包和部署
在上一个教程中，你添加了一个简单的按钮，来将象棋棋子重置到原始位置。这是最后一个部分，介绍了如何将此应用准备就绪，以在 HoloLens 2 或仿真器中运行它。 如果你有 HoloLens 2，则可以从计算机进行流式传输，或者打包应用，以便直接在设备上运行。如果没有设备，则打包应用，以便在仿真器上运行它。本部分结束时，你将拥有一个已部署的混合现实应用，你可以通过交互和 UI 充分利用它。

### 目标
- [仅设备] 通过全息应用远程处理流式传输到 HoloLens 2
- 打包应用并将其部署到 HoloLens 2 设备或仿真器

### [仅设备] 流式传输
[全息远程处理](https://docs.microsoft.com/zh-cn/windows/mixed-reality/add-holographic-remoting)是指将数据从电脑或独立 UWP 设备流式传输到 HoloLens 2，而非切换通道。远程处理主机应用从 HoloLens 接收输入数据流，在虚拟沉浸式视图中呈现内容，并通过 Wi-Fi 将内容帧流式传输回 HoloLens。通过流式处理，可以将远程沉浸式视图添加到现有的台式电脑软件中，并可访问更多系统资源。

如果要将此方法用于该象棋应用，需要完成以下事项：
1. 在 HoloLens 2 上从 Microsoft Store 安装并运行“全息远程处理播放器”。请注意应用中显示的 IP 地址。
    - 转到“编辑”>“项目设置”，确保 Windows“默认 RHI”设置为“默认值”或“D3D11”：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205005813.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205005813.png)

2. 返回到 Unreal 编辑器，转到“编辑”>“项目设置”，然后选中“全息远程处理”部分中的“启用远程处理”。

3. 重启编辑器，然后输入设备的 IP 地址（如全息远程处理播放器应用中所示），然后单击“连接”。

连接后，单击“开始”按钮右侧的下拉箭头，然后选择“VR 预览”。此应用将在“VR 预览”窗口中运行，该窗口将流式传输到 HoloLens 头戴显示设备。

### 通过设备门户打包和部署应用

> 如果这是你第一次为 HoloLens 打包 Unreal 应用，则需要从 Epic Launcher 下载支持文件。详情参考第一部分：初始化你的项目

1. 转到“编辑”>“项目设置”。
    - 在“项目 > 描述 > 关于 > 项目命名”下，添加项目名称。
    - 在“项目 > 描述 > 发行商 > 公司识别名”下，添加“CN=YourCompanyName”。
    - 在“项目 > 描述 > 设置”下，选择“以 VR 启动”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205010400.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205010400.png)

    > 如果将这些字段中的任一字段留空，那么当你在步骤 3 中尝试生成新证书时将遇到错误。

    > 不选择“在 VR 中启动”将导致应用程序尝试在平板中启动

2. 在“平台 > 全息透镜”下，选择“Build for Hololens Emulation” 或 “Build for Hololens Device”。

3. 单击“打包”部分（在“签名证书”旁）中的“生成新内容” 。

    > 如果使用的是已生成的证书，证书的发布者名称则必须与应用程序的发布者名称相同。 否则，会导致“找不到签名密钥。 无法对应用进行数字签名。” error。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205010744.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205010744.png)

4. 当系统提示你创建私钥密码时，出于测试目的，请单击“None”。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205010818.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210205010818.png)

5. 关闭项目设置，转到“文件”>“包项目”并选择“HoloLens”。

    - 创建新文件夹 Package 以保存包，并单击“选择文件夹”。

6. 打包应用后，请打开 [Windows 设备门户](https://docs.microsoft.com/zh-cn/windows/mixed-reality/using-the-windows-device-portal)，转到“视图 > 应用”，并找到“部署应用”部分。

7. 单击“浏览...”，转到“ChessApp.appxbundle”文件，然后单击“打开”。
    - 如果这是你第一次在设备上安装应用，请选中“允许我选择框架包”旁的复选框。
    - 在下一个对话框中，包含相应的 VCLibs 和 appx 文件（arm64 用于设备，而 x64 用于仿真器）。在保存包的文件夹中，可以从 HoloLens 下找到相应文件。

8. 单击“安装”
    - 安装完成后，带上Hololens，在“所有应用”，点击新安装的应用来运行它，或者直接从 Windows 设备门户启动应用。

9. 愉快的玩耍~

恭喜！ 你的 HoloLens 混合现实应用程序已完成，并且可随时运行。但是，这一体验过程并未就此结束。MRTK 有许多独立功能，你可以将其添加到项目中，其中包括空间映射、凝视和语音输入甚至 QR 码。有关这些功能的详细信息，请参阅 [Unreal 开发概述](https://docs.microsoft.com/zh-cn/windows/mixed-reality/unreal-development-overview)。
