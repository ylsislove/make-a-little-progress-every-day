# winrtc-MyFirstWinRtc官方案例Nuget包还原失败解决方法

按照官方的 [README](https://github.com/microsoft/winrtc/blob/master/samples/README.md)，打开示例程序，导航到NuGet程序包管理器，会看到需要还原 Nuget 包的警告。点击还原后还原失败，无法下载 Microsoft.WinRTC.libwebrtc.uwp 84.0.14170001-alpha 包。在 [Issues](https://github.com/microsoft/winrtc/issues/116) 上找到了解决方案。该包的版本已被 84.0.14370001-beta.1 代替。

所以需要更改 `samples\Microsoft.WinRTC.Simple.VideoConferencing\packages.config` 文件，将 Microsoft.WinRTC.libwebrtc.uwp 包的版本替换为 84.0.14370001-beta.1。如下

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210331162653.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210331162653.png)

重新打开解决方案，再次点击还原，问题解决。
