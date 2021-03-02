# Hololens2-重刷系统（正常发布版本和内部预览版本）

  - [刷机：正常发布版本](#%E5%88%B7%E6%9C%BA%E6%AD%A3%E5%B8%B8%E5%8F%91%E5%B8%83%E7%89%88%E6%9C%AC)
  - [刷机：内部预览版本](#%E5%88%B7%E6%9C%BA%E5%86%85%E9%83%A8%E9%A2%84%E8%A7%88%E7%89%88%E6%9C%AC)

这个过程心情真的是大起大落，真不容易。感兴趣的可以看看我的[踩坑记录](./心情-又一次体会到了努力的回报，自己把Hololens搞好了.md)~

回归正传，这里给出 HoloLens2 两个版本的刷机教程：正常发布版本和内部预览版本（内部预览版本就是对应 Windows Hololens 的预览体验计划）。需要注意的是，刷内部预览版本的前提是要先刷正常发布版本，只有当正常发布版本刷成功后，进入 Hololens 系统的设置界面，在更新与安全处加入 Windows 预览计划成功后，再刷内部预览版本，才能刷机成功，否则就会失败，博主血的教训555

如果在刷机过程中看到以下报错：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210302225121.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210302225121.png)

就是因为没有在 Hololens 的 系统设置 -> 更新与安全 处加入 Windows 预览计划，直接就刷内部预览版本，才会报错的。官方对这个地方已经说明了，如下图：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210302225405.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210302225405.png)

以上就是你可能会碰到的问题，也是博主惨痛的亲身经历。

## 刷机：正常发布版本
参考文档：[重启、重置或恢复 HoloLens 2](https://docs.microsoft.com/zh-cn/hololens/hololens-recovery)

1. 下载正常发布版本的最新 Hololens2 系统镜像

    就像是给 PC 重装系统，肯定要有个系统镜像才能重装。Hololens 也是一样，可以在这个链接（[https://aka.ms/hololens2download](https://aka.ms/hololens2download)）处下载最新镜像。这个链接也可以在官方文档的这个地方找到：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210302230102.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210302230102.png)

    注意：这个过程可能对网络有点要求，如果因为网络问题下载不成功的，可以私信我要百度网盘链接（但这就不是最新的系统镜像了哦），或者也可以参考我的[这篇文章](./../../../2020/2020-07/2020-07-24/技巧-用Docker科学上网.md)来解决网络问题。

2. 在 Microsoft Store 处下载安装 ARC（[Advanced Recovery Companion](https://www.microsoft.com/store/productId/9P74Z35SFRS8)，高级恢复助手）

3. 在以上两个步骤都完成后，就可以按照官方文档的步骤说明，[对设备进行干净重刷](https://docs.microsoft.com/zh-cn/hololens/hololens-recovery#%E5%AF%B9%E8%AE%BE%E5%A4%87%E8%BF%9B%E8%A1%8C%E5%B9%B2%E5%87%80%E9%87%8D%E5%88%B7)了。

4. 根据 ARC 的提示走，直接选择刚刚下载的镜像文件，不出意外，正常发布版本的刷机应该是没问题的~

## 刷机：内部预览版本

前提条件：Hololens 系统可以正常进入（不管原本就可以正常进入，还是再重刷了正常发布的版本后可以正常进入，都行）

以下教程也可适用于：Hololens2 系统内部下载安装 预览版本 的速度过慢；害怕 Hololens2 在内部更新完后无法启动，直接变成板砖（博主亲身经历）的小伙伴，直接刷机吧，以上两个问题通通解决。

1. 下载内部预览版本的最新 Hololens2 系统镜像

    下载链接：[https://aka.ms/hololenspreviewdownload](https://aka.ms/hololenspreviewdownload)

    在下载过程中可能也会遇到网络困难，需要的可以私信我要百度网盘链接（非最新），也可以自己想办法解决网络问题~

2. 注册加入 Windows Hololens 内部预览体验计划，没有这步是刷机不成功的，官方说明如下：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210302232044.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210302232044.png)

3. 注册加入重启设备之后，就可以按照[对设备进行干净重刷](https://docs.microsoft.com/zh-cn/hololens/hololens-recovery#%E5%AF%B9%E8%AE%BE%E5%A4%87%E8%BF%9B%E8%A1%8C%E5%B9%B2%E5%87%80%E9%87%8D%E5%88%B7)里的正常程序，选择刚刚下载好的最新预览版本系统镜像，对 Hololens 进行重刷了，不出意外，刷机成功后，你的设备系统就是内部预览版本的啦

4. 进入预览版本后，就可以对 Hololens2 的研究模式（Research Mode）好好的捣鼓捣鼓了！
