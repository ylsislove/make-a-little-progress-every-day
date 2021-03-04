# Hololens2-运行研究模式官方案例（StreamRecorder）

注意看本案例的 README 文件，里面给出了很多有用的信息。

构建没啥问题，用的是 Release 版本，构建成功如下图：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304214348.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304214348.png)

在 Hololens2 上成功运行截图：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304214425.jpg)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304214425.jpg)

按照 README 文件的说明，可以用 `StreamRecorderConverter/` 文件夹下的 Python 脚本对保存在 Hololens 上的数据进行后期处理。

可能遇到的问题：
1. 运行 `recorder_console.py` 脚本报错：urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1076)>

    很显然，这个问题是由于缺少安全证书导致的。每次用浏览器访问 Hololens 设备门户的时候，如果没有安全证书，就会出现此连接不安全，是否继续的界面。用脚本访问同样就会出现这个问题。

    解决方法也很简单，按照[官方文档说明](https://docs.microsoft.com/zh-cn/windows/mixed-reality/develop/platform-capabilities-and-apis/using-the-windows-device-portal#security-certificate)，下载证书并导入即可，截图如下，这里就不详细说明了。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304215313.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304215313.png)

    注意：如果对设备进行了重刷系统，需要再次执行此过程。重刷系统教程可参考：[Hololens2-重刷系统（正常发布版本和内部预览版本）](./../2021-03-02/Hololens2-重刷系统（正常发布版本和内部预览版本）.md)

    导入完证书后，再次用浏览器访问设备门户，就不会再出现那个不安全的界面了。

    然后再次运行 `recorder_console.py` 脚本，哦很不幸，这个问题还是没有解决（捂脸哭）。看了下 GitHub 的 Issues，很幸运，这里有人提出了这个 Issue：[Can't download StreamRecorder data #4](https://github.com/microsoft/HoloLens2ForCV/issues/4)，并给出了解决方法，如下：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304220823.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304220823.png)

    把那两行代码添加进 `recorder_console.py` 脚本文件中，然后在设备门户中取消勾选 `SSL connection` 复选框，如下：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304221212.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210304221212.png)

2. 运行 `recorder_console.py` 脚本报错：urllib.error.HTTPError: HTTP Error 401: Unauthorized

    解决完第一个问题，你可能还会碰到这个问题，比如博主（捂脸）。用户名和密码都输入正确的情况下，为什么脚本还是会报错呢，脑阔疼

    暂时还未寻求到解决办法。后续继续更新。

    2021-03-05 01:03:08 更新：

    解决了。我注意到在这个脚本中，使用的 Hololens 设备门户的 IP 地址默认是 `http://127.0.0.1:10080`，但是我把这个地址输入到浏览器后，它会重定向到 `https://127.0.0.1:10443/`。所以我直接在脚本中把 `self.url` 写成 `https://127.0.0.1:10443/`，如下：

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305010642.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305010642.png)

    再次运行这个脚本，终于不报错了，完美解决！

    进一步思考，这个问题或许是由于我使用的是 USB 连接的 Hololens 设备门户，如果用 WiFi 连接可能就不会引起这个错误。后面有时间再验证吧~

数据后期处理截图：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305013947.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210305013947.png)
