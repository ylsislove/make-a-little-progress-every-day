# Hololens2-MixedReality-WebRTC的使用问题

很可惜，目前 [MixedReality-WebRTC](https://github.com/microsoft/MixedReality-WebRTC/tree/master) 和 [HoloLens2ForCV](https://github.com/microsoft/HoloLens2ForCV) 不能同时在一个 Unity 项目使用。因为 MixedReality-WebRTC 只支持 ARM 构建，而 HoloLens2 的研究模式只能在 ARM64 下构建：[ARM Support](https://github.com/microsoft/HoloLens2ForCV/issues/22)。GitHub 关于这些问题的讨论如下：

## mrwebrtc could not be found on HL2 / Unable to load DLL 'mrwebrtc'
关于此问题的相关讨论
* [mrwebrtc could not be found on HL2](https://github.com/microsoft/MixedReality-WebRTC/issues/574)
* [Unable to load DLL 'mrwebrtc'](https://github.com/microsoft/MixedReality-WebRTC/issues/569)
* [Unity3D + Hololens 2: Unable to load DLL 'mrwebrtc.dll': The specified module could not be found](https://github.com/microsoft/MixedReality-WebRTC/issues/591)
* [now working on ARM64 build](https://github.com/microsoft/MixedReality-WebRTC/issues/235)

这里提供了 MixedReality-WebRTC 对 ARM64 支持的概述和路线图的相关讨论
* [ARM64 support progress](https://github.com/microsoft/MixedReality-WebRTC/issues/414)

持续关注，希望未来能有更多的进度。

放一张在 ARM 构建下成功运行的截图吧

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210311151916.jpg)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210311151916.jpg)
