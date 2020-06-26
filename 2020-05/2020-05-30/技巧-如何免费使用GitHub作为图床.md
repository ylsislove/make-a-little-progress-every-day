# 技巧-如何免费使用 GitHub 作为图床

可能还有不少人不知道 GitHub 图床的正确用法吧？我来给大家科普下😏
1. 创建一个 GitHub 仓库作为图床仓库，上传提交图片到仓库中
2. 在要使用 GitHub 图床图片的地方将链接换为 `https://cdn.jsdelivr.net/gh/{user}/{repo}/图片路径 `

举个 🌰：比如我的 github 仓库 `make-a-little-progress-every-day` 里 `2020-05-30` 目录下的图片原始访问路径为 [https://raw.githubusercontent.com/ylsislove/make-a-little-progress-every-day/master/2020-05/2020-05-30/orb_result.png](https://raw.githubusercontent.com/ylsislove/make-a-little-progress-every-day/master/2020-05/2020-05-30/orb_result.png) 访问起来贼慢

但是使用 jsDelivr 加速后的地址为：[https://cdn.jsdelivr.net/gh/ylsislove/make-a-little-progress-every-day/2020-05/2020-05-30/orb_result.png](https://cdn.jsdelivr.net/gh/ylsislove/make-a-little-progress-every-day/2020-05/2020-05-30/orb_result.png) 访问速度飞起，享受 jsDelivr 提供的全球 CDN 加速

![aa](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200530225930.png)

jsDelivr 还支持加载指定文件版本和自动压缩 JS，具体用法也可以参考[官方教程](https://www.jsdelivr.com/features)。

---

如果觉得动上传 GitHub 图床仓库太麻烦，这里还有一款开源神器可以推荐，超赞
[https://github.com/Molunerfinn/PicGo](https://github.com/Molunerfinn/PicGo)

这个是软件运行起来的界面

![PicGo](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200530230321.png)

安装方法也很简单，我是 windows 平台用 scoop 包管理工具安装的
```bash
scoop bucket add helbing https://github.com/helbing/scoop-bucket
scoop install picgo
```

安装完成之后，需要去 github 申请一个 [GitHub PAT (Personal access tokens)](https://github.com/settings/tokens)

记得勾选下面这个选项即可
![GitHub PAT](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200530231218.png)

然后在软件里面将刚刚获得的 Token 和其他参数设置好就OK啦
![PicGo设置](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200530231406.png)

是不是很简单，hh 如果这篇文章对您有帮助的话，欢迎为我的 github 项目点一个 ⭐ 哦