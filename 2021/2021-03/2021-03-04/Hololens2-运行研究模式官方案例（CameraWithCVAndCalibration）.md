# Hololens2-运行研究模式官方案例（CameraWithCVAndCalibration）

这个 Demo 用到了 OpenCV 库，预感在构建的过程中可能会出现一些其他的问题，果然哈哈

可能出现的问题：
1. 错误	LNK1107	文件无效或损坏: 无法在 0x86 处读取	CameraWithCVAndCalibration。问题截图如下：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304200443.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304200443.png)

    GitHub 上关于此问题的讨论：[OpenCV lib corrupt #66](https://github.com/microsoft/HoloLens2ForCV/issues/66)

    这个问题可能由两个原因引起的：
    1. 直接下载仓库的 ZIP 文件，而不是直接 Clone 获取该仓库；
    2. 没有运行 `git lfs install` 命令。

    实际上，在 `CameraWithCVAndCalibration` 这个 Demo 的 README 文件中就指出了 `git lfs` 是必须的，如下：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304202214.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304202214.png)

    所以，解决办法也很简单：
    1. 先在 PowerShell 里面按[文档](https://git-lfs.github.com/)所说的运行 `git lfs install` 命令；
    2. 重新用 `git clone` 命令获取 `HoloLens2ForCV` 仓库。

    对比用 ZIP 下载的仓库的 `Samples\CameraWithCVAndCalibration\OpenCvInstallArm64-412d\x64\vc15\staticlib` 里的文件大小，和运行了 `git lfs` 命令后 clone 下的仓库的文件大小，可以很明显的看出 ZIP 里的 OpenCV 链接库文件明显是不对的。如下：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304203151.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304203151.png)

    在新仓库下的 `CameraWithCVAndCalibration` Demo 中生成解决方案，报错解决~

2. 其他可能的错误参考我的前几篇文章~

成功运行的截图：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304204946.jpg)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304204946.jpg)

好家伙，不得不说，运行这个程序后，CPU 直接飙满，界面卡的一批。用 Hololens 来做计算机视觉研究和开发还任重道远呀~
