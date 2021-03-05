# Hololens2-Unity项目整合Hololens2研究模式

## 环境
* Windows 10 教育版 18363.1379
* Unity 2019.4.20f1c1
* VS2019 16.8.6
* WIN SDK 10.0.18362.0
* Hololens2 内部预览版本 10.0.20301.1000

## 创建项目
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305185610.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305185610.png)

## 切换平台
在菜单栏 `File -> Build Settings` 中切换为 UWP 平台

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305192246.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305192246.png)

## 创建新场景
使用 `Ctrl + N`，`Ctrl + S` 创建新场景并保存为 `StreamingScene`。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305190342.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305190342.png)

## 构建Hololens2研究模式动态链接库
1. 找一个位置 Clone [HoloLens2-Unity-ResearchModeStreamer](https://github.com/ylsislove/HoloLens2-Unity-ResearchModeStreamer) 仓库。
2. 在 VS2019 中打开 `HL2RmStreamUnityPlugin` 解决方案。
3. 选择 `Release, ARM64` 生成解决方案
4. 在 `HL2RmStreamUnityPlugin/ARM64/Release/HL2RmStreamUnityPlugin` 下可以找到 `HL2RmStreamUnityPlugin.dll`。如下图：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305190936.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305190936.png)

## Unity中调用动态链接库
1. 在 Unity 编辑器中，创建 `Assets/Plugins/WSAPlayer/ARM64` 文件夹
2. 拷贝上一步生成的 `HL2RmStreamUnityPlugin.dll` 到刚创建的文件夹中
3. 创建 `Assets/Scripts` 文件夹，然后在文件夹中创建 `StartStreamer` C# 脚本
4. 双击在 VS2019 中打开脚本文件，然后编辑如下：

    ```csharp
    using System.Runtime.InteropServices;
    using UnityEngine;

    public class StartStreamer : MonoBehaviour
    {

    #if ENABLE_WINMD_SUPPORT
        [DllImport("HL2RmStreamUnityPlugin", EntryPoint = "StartStreaming", CallingConvention = CallingConvention.StdCall)]
        public static extern void StartStreaming();
    #endif

        // Start is called before the first frame update
        void Start()
        {
    #if ENABLE_WINMD_SUPPORT
            StartStreaming();
    #endif
        }

        // Update is called once per frame
        void Update()
        {
            
        }
    }
    ```

    保存，返回 Unity 编辑器
5. 可以把脚本挂在到 `Main Camera` 上：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305193308.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305193308.png)

6. 在菜单栏打开 `Edit -> Project Settings`。在 `Player -> Publishing Settings` 确保以下权限被勾上：
    - InternetClient
    - InternetClientServer
    - PrivateNetworkClientServer
    - WebCam
    - SpatialPerception

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305192925.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305192925.png)

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305193014.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305193014.png)
7. `Ctrl + S` 保存项目。打开菜单栏 `File -> Build Settings`，添加场景，然后构建。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305193536.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305193536.png)

## 部署到Hololens2
1. 找到生成的文件夹，在文本编辑器中打开 `UnityHL2RmStreamer\Package.appxmanifest` 文件，并按照如下配置，以确保研究模式被允许：

    - 添加 `xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities"` 到 `Package`
    - 添加 rescap 到 Ignorable Namespaces：`IgnorableNamespaces="... rescap"`
    - 添加 `<rescap:Capability Name="perceptionSensorsExperimental" />` 到 `Capabilities`
    - 保存然后关闭 `Package.appxmanifest`

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305194929.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305194929.png)

2. 在 VS2019 中打开 `UnityHL2RmStreamer.sln` 解决方案，用 `Release, ARM64` 生成解决方案，然后部署到 Hololens2 设备上。

## Python客户端接收Hololens2视频帧
Python 脚本可在此处获得：[hololens2_simpleclient.py](https://github.com/ylsislove/HoloLens2-Unity-ResearchModeStreamer/blob/master/py/hololens2_simpleclient.py)

注意把脚本中的 Host 改成自己 Hololens2 设备的 IP 地址

## 运行结果
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305202315.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305202315.png)

后期我会尝试把研究模式的加速度计、陀螺仪和磁力计流整合进 Unity 项目~

## 致谢
- [HoloLens2-Unity-ResearchModeStreamer](https://github.com/cgsaxner/HoloLens2-Unity-ResearchModeStreamer)
- [Implementation of the IMU inside the StreamRecorder App #67](https://github.com/microsoft/HoloLens2ForCV/issues/67)
- [HoloLens2ForCV](https://github.com/microsoft/HoloLens2ForCV)
