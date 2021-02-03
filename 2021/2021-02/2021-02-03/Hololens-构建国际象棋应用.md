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

笔者注：笔者使用的是 Unreal Engine 4.26 版本，对应的后面下载的 UX Tools 插件的版本也和原文有所不同。如果版本不匹配，最后的打包部署步骤就会失败。具体情况后面会详细说明。

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

