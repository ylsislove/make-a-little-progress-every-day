# Hololens2-Unity项目获取IMU传感器数据

## 前言
在仔细捣鼓了 HoloLens2 研究模式的 API 文档后，借鉴了官方案例 [SensorVisualization](https://github.com/microsoft/HoloLens2ForCV/tree/main/Samples/SensorVisualization) 和这位哥们的代码 [HoloLens2-Unity-ResearchModeStreamer](https://github.com/cgsaxner/HoloLens2-Unity-ResearchModeStreamer)，终于成功的把传感器 IMU 相关的 API 构建成了 DLL，可以在 Unity 项目中进行调用，获取到高帧率的 IMU 数据。

## 使用指南
1. 下载本仓库：[HoloLens2-ResearchMode-UnityPlugin](https://github.com/ylsislove/HoloLens2-ResearchMode-UnityPlugin)
2. 在 Visual Studio 中打开 `HL2RmUnityPlugin`
3. 用 `Release, ARM64` 方式构建解决方案
4. 在 Unity 项目中，创建 `Assets/Plugins/HL2RmUnityPlugin` 文件夹
5. 将构建生成的 `HL2RmUnityPlugin.dll` 复制到 `Assets/Plugins/HL2RmUnityPlugin` 文件夹
6. 在 Unity 脚本中调用 DLL 函数，参考 [IMUMamager.cs](https://github.com/ylsislove/HoloLens2-ResearchMode-UnityPlugin/blob/main/HL2RmUnityDemo/Assets/Scripts/IMUManager.cs) 脚本
7. 在菜单栏打开 `Edit -> Project Settings`。在 `Player -> Publishing Settings` 确保以下权限被勾上：
    - InternetClient
    - InternetClientServer
    - PrivateNetworkClientServer
    - WebCam
    - SpatialPerception
8. 构建 Unity 项目
9. 在生成的文件夹中找到 `Package.appxmanifest`，确保以下代码被添加：
```xml
<?xml version="1.0" encoding="utf-8"?>
<Package ... IgnorableNamespaces="... rescap" xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities">
  ...
  <Capabilities>
    <rescap:Capability Name="perceptionSensorsExperimental" />
    <Capability Name="internetClient" />
    <Capability Name="internetClientServer" />
    <Capability Name="privateNetworkClientServer" />
    <uap2:Capability Name="spatialPerception" />
    <DeviceCapability Name="webcam" />
    <DeviceCapability Name="backgroundSpatialPerception" />
  </Capabilities>
</Package>
```
9. 在 Visual Studio 打开生成文件夹，用 `Release, ARM64` 方式构建解决方案并部署到 Hololens2

## 运行结果
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210308220110.gif)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210308220110.gif)

欢迎给本插件提 Issues ~
