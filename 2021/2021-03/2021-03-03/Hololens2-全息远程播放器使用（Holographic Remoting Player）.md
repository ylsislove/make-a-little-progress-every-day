# Hololens2-全息远程播放器使用（Holographic Remoting Player）

## 可能碰到的问题
1. Disconnect:Transport connection was closed due to the requested video format not being available

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304000013.jpg)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304000013.jpg)

    GitHub 关于此问题的讨论：[https://github.com/microsoft/MixedRealityToolkit-Unity/issues/8214](https://github.com/microsoft/MixedRealityToolkit-Unity/issues/8214)

    在这个链接处查看自己的 GPU 是否支持 H265 编码：[https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new)

    我的显卡是 NVIDIA GeForce GTX 960M，驱动版本是 378.66，如下

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304011617.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304011617.png)

    在官网查看自己的显卡不支持 H265 编码，呜呜

    尝试将自己的驱动版本更新到最新，最新的驱动版本可以在 Nvidia 官网处下载到，链接：[https://www.nvidia.com/Download/index.aspx](https://www.nvidia.com/Download/index.aspx)

    更新完成后驱动版本为 461.72，如下：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304011834.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304011834.png)

    在 Unity 中尝试全息远程处理，还是报同样的错误，呜呜，难道我只能像 Github 中讨论的那样，买一台更牛逼的显卡的电脑辣吗？

    不行，我要再尝试尝试其他的方法！

    TNND，按照[官方教程](https://docs.microsoft.com/en-us/windows/mixed-reality/develop/platform-capabilities-and-apis/holographic-remoting-troubleshooting#h265-video-codec-not-available)，尝试在 PC 上安装 `HEVC Video Extensions`，要花七块软妹币购买不说，安装完成后还是不能在 Unity 上连接 Hololens2 上的全息远程播放器，哭死。难道，难道真的只能换一台更好的电脑了吗呜呜呜

    又尝试在 Hololens2 上安装了 `HEVC Video Extensions`，因为我看到它也是适用于 Hololens 设备的。安装没问题，但还是在 Unity 上连不上 Hololens 啊啊啊啊啊啊

    我最后又尝试了一下[官方文档](https://docs.microsoft.com/en-us/azure/remote-rendering/resources/troubleshoot#h265-codec-not-available)这里所给出的方法：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304024339.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304024339.png)

    完全是按照文档上的步骤来执行的，但最终，还是失败了。我的 Unity 项目就死活连不上 Hololens2 的全息远程播放器呗，心真的累了。。

    至此，除了换一台更好的电脑，我真的没其他的办法。。。

    如果有其他的小伙伴和我一样也遇到了这个问题，但最终解决的，一定要给我说声解决办法啊，呜呜呜心累。
