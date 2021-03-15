# Hololens2-快速实现一个实时时间显示模块（unity）

  - [前言](#%E5%89%8D%E8%A8%80)
  - [环境](#%E7%8E%AF%E5%A2%83)
  - [创建项目](#%E5%88%9B%E5%BB%BA%E9%A1%B9%E7%9B%AE)
  - [配置项目](#%E9%85%8D%E7%BD%AE%E9%A1%B9%E7%9B%AE)
  - [编写实时时间自动更新脚本](#%E7%BC%96%E5%86%99%E5%AE%9E%E6%97%B6%E6%97%B6%E9%97%B4%E8%87%AA%E5%8A%A8%E6%9B%B4%E6%96%B0%E8%84%9A%E6%9C%AC)
  - [创建 TextMeshPro 对象并挂载脚本](#%E5%88%9B%E5%BB%BA-textmeshpro-%E5%AF%B9%E8%B1%A1%E5%B9%B6%E6%8C%82%E8%BD%BD%E8%84%9A%E6%9C%AC)
  - [让对象跟随头部移动](#%E8%AE%A9%E5%AF%B9%E8%B1%A1%E8%B7%9F%E9%9A%8F%E5%A4%B4%E9%83%A8%E7%A7%BB%E5%8A%A8)
  - [打包、构建和部署](#%E6%89%93%E5%8C%85%E6%9E%84%E5%BB%BA%E5%92%8C%E9%83%A8%E7%BD%B2)
  - [结果展示](#%E7%BB%93%E6%9E%9C%E5%B1%95%E7%A4%BA)

## 前言
补充一些 Unity 开发和 Hololens 开发的基础知识，包括 TextMeshPro 文本更新，对象如何跟随头部移动等。

## 环境
- Hololen2
- Windows 10
- Unity 2019.4.20f1c1
- Visual Studio 2019
- MRTK 2.5.4

## 创建项目
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315202044.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315202044.png)

## 配置项目
1. 在菜单栏“File -> Build Settings”，将平台转换为 `通用Windows平台`

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209002604.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209002604.png)

2. 导入 MRTK 开发工具包，下载链接：[MRTK](https://github.com/microsoft/MixedRealityToolkit-Unity/releases/)
    - 在菜单栏 “Assets -> Import Package -> Custom Package”，选择刚刚下载的 MRTK 工具包（Microsoft.MixedReality.Toolkit.Unity.Foundation.2.5.4.unitypackage）。
    - 选择“All”，然后导入。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315203003.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315203003.png)

3. 在自动打开的 MRTK 项目配置器中，确保所有选项都被选上，如下图，然后点击应用。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209003450.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209003450.png)

    如果 MRTK 项目配置器没有自动打开，可以在在菜单栏“Mixed Reality Toolkit -> Utilities -> Configure Unity Project”手动打开。

4. 在菜单栏“Edit -> Project Settings”打开项目设置
    - 找到“Player -> XR Settings”，勾选 Virtual Reality Supported 复选框。
    - 在自动弹出的 MRTK 项目配置器中，设置空间音频，然后点击应用，如下图。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209004035.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209004035.png)

    - 在 XR Settings 中，设置深度格式为 16-bit 深度，如下

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209004300.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209004300.png)

    - 找到“Player -> Publishing Settings”，设置“Package name”为“HololensTimer”。

5. 在菜单栏“File -> New Scene”新建场景，按“Ctrl S”将新场景保存到 Scenes 文件夹下，场景名为 MainScene

6. 在菜单栏“Mixed Reality Toolkit -> Add to Scene and Configure”添加配置文件。

7. 在菜单栏“Window -> TextMeshPro -> Import TMP Essentail Resources”，点击 All，然后 Import 来导入必要的资源。

## 编写实时时间自动更新脚本
1. 在 Assets 目录下创建 Scripts 文件夹，然后右击创建 C# 脚本，命名为 TimeService。

2. 双击脚本在 VS2019 中打开，然后编写如下代码

```csharp
using System;
using TMPro;
using UnityEngine;

public class TimeService : MonoBehaviour
{
    public TextMeshPro timer;

    // Update is called once per frame
    void Update()
    {
        if (timer != null)
        {
            timer.text = "Time: " + DateTime.Now.ToString("HH:mm:ss");
        }
    }
}
```

3. 保存，返回 Unity 编辑器。

## 创建 TextMeshPro 对象并挂载脚本
1. 在 Hierarchy 上右击，创建 `3D Object -> Text - TextMeshPro` 对象，F2 重命名为 Timer。

2. 在 Inspector 里调整 PosZ 为 1，Width 为 1，Height 为 0.12，Font Size 为 1。`在 Unity 中一个单位长度约对应现实生活中的 1 米`，所以上面的调整将 Timer 放置在眼前 1 米处左右的距离范围。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315205340.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315205340.png)

3. 可以把字体颜色调成红色等比较醒目的颜色。

4. 在 Project 里把 TimeService 脚本拖拽到 Inspector，然后在 Hierarchy 里把 Timer 对象拖拽到 TimeService 脚本的 Timer 属性上，如下图：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315205837.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315205837.png)

    这样就完成了脚本和对象的挂载。

5. 可以点击 Unity 的运行按钮来运行下看看有没有错误，在 Unity 里正常运行如下：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315210158.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315210158.png)

    黄色的警告信息通常可以忽略~

## 让对象跟随头部移动
在 Timer 上点击 Add Component，搜索 RadiaView 并添加，该脚本会自动添加一个 SolverHandler 依赖脚本。我们可以设置 RadiaView 里的 `Min Distance、Max Distance、Min View Degrees 和 Max View Degrees` 值来控制该 Timer 对象跟随头部移动的最小距离、最大距离、最小角度和最大角度。可以将 `Max View Degrees` 从 30 度 改为 1 度，这样我们的头部稍微转动一个角度，Timer 对象也会跟随我们的头部移动了~

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315211507.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315211507.png)

更多信息可以参考官方文档：[如何使对象跟随你？](https://docs.microsoft.com/zh-cn/windows/mixed-reality/out-of-scope/mrtk-101#how-to-make-an-object-follow-you)


## 打包、构建和部署
详细步骤参考我这篇博客：[Hololens2开发笔记-快速入门并实现3D对象手势操作（unity）](https://blog.csdn.net/Apple_Coco/article/details/113765316#%E6%89%93%E5%8C%85%E9%83%A8%E7%BD%B2)

我这里就不再赘述啦~

对了这里多补充一下吧，最后在 VS2019 里构建的时候可以选择 `Master ARM64` 构建，也可以选择 `Release ARM64` 构建，博主都亲自测过都可正常运行。不过博主最近在看 GitHub 上老外开发者们用 `Release ARM64` 构建的居多，所以这里可以区别我那篇博客，选择用 `Release ARM64` 进行构建也可以~

## 结果展示
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315214509.gif)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210315214509.gif)
