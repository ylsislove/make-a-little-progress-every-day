# Hololens2-运行研究模式官方案例（SensorVisualization）

参考：[Hololens2初入——调用深度相机和前置摄像头的Demo](https://blog.csdn.net/scy261983626/article/details/108685000)

可能碰到的问题：
1. 生产解决方案失败：The max version tested value must not be less than the min version value.

    原因：自己安装 VS2019 时指定的 Win SDK 版本是 10.0.18362.0，而 SensorVisualization 这个官方 Demo 里配置的 Win SDK 版本是 19041.1.191206，所以就会导致那个报错。

    解决方法：很简单，我们手动把官方 Demo 里的 Win SDK 版本指定成我们自己的版本就好了，详情如下：

    1. 在解决方案上右击，点击 `属性`：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304045747.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304045747.png)

    2. 在 `目标平台最低版本` 里选择我们有的 SDK 版本，如下：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304045921.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304045921.png)

    然后点击确定

    3. `生成 -> 清理解决方案`，然后再 `生成 -> 生成解决方案`，完美解决这个报错问题

    4. 点击部署到设备，即可在设备上运行这个官方 Demo 了。最后放一张成功运行的截图吧

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304050155.jpg)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304050155.jpg)

