# OpenCV-npm安装opencv4nodejs（Windows）

  - [前言](#%E5%89%8D%E8%A8%80)
  - [官方指南](#%E5%AE%98%E6%96%B9%E6%8C%87%E5%8D%97)
  - [踩坑指南](#%E8%B8%A9%E5%9D%91%E6%8C%87%E5%8D%97)
    - [安装好 git 和 cmake](#%E5%AE%89%E8%A3%85%E5%A5%BD-git-%E5%92%8C-cmake)
    - [安装 windows-build-tools](#%E5%AE%89%E8%A3%85-windows-build-tools)
    - [安装 opencv4nodejs](#%E5%AE%89%E8%A3%85-opencv4nodejs)
  - [安装成功](#%E5%AE%89%E8%A3%85%E6%88%90%E5%8A%9F)
  - [参考链接](#%E5%8F%82%E8%80%83%E9%93%BE%E6%8E%A5)

## 前言
深夜踩坑真的是太难了，呜呜

OpenCV 可以说是很早就接触了，之前用过 Python 版本的和 C++ 版本的。最近在学习前端方面的知识，做 WebGIS 和图像处理方面的开发，顺理成章就希望能将 OpenCV 用在前端上。查阅了一些资料，发现已经有大神做了将 OpenCV 用于 NodeJS 上的开发，其名为 opencv4nodejs。既然已经有了前辈探路，我们也就可以大胆开干了。万万没想到，踩坑之路已悄然开始，呜呜

npm 安装 opencv4nodejs 国内只有零星的几篇 Blog 有介绍，但是坑又没有踩完，所以想将自己踩坑成功后的经历记录下来，方便后面的小伙伴们~

## 官方指南
> https://www.npmjs.com/package/opencv4nodejs#how-to-install

![官方指南](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201101131636.png)

在官方安装指南中，我们可以看到，安装命令只有简简单单的两条，甚至一条（之前有用过 Visual Studio，所以安装过相关依赖库，就不需要第二条命令了）。但是，想要安装成功，这些应该是远远不够的。

## 踩坑指南
### 安装好 git 和 cmake
这两个是必须一定要安装的，因为在安装 opencv4nodejs 的过程中，会先用 git 从 GitHub 上拉取 opencv 和 openc_contrib 这两个仓库，之后会用 cmake 进行编译，所以这两个工具一定要安装好，需要在 terminal 中能直接查看到 git 和 cmake 的版本才可以哦。查看命令如下

```bash
git --version
cmake --version
```

![git和cmake](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201101132846.png)

这里我推荐使用 Scoop 包管理工具，像 CentOS 上的 yum 和 Ubuntu 上的 apt-get 等，Scoop 是专门应用于 Windows 的包管理工具，两条命令即可安装好 git 和 cmake，并自动配置好环境变量，简直不要太方便

啊还有一件事要注意，众所周知，从 GitHub 上拉取仓库的速度是极其慢的。。opencv 有 50M 左右的大小，openc_contrib 有 80M 左右，如果在网络上没有一些特殊手段的话，这两个仓库就别想拉取下来了。想解决网络问题，可以参考我的[这篇文章](../../2020-07/2020-07-24/技巧-用Docker科学上网.md)，当然，有其他解决办法也是没问题的。

### 安装 windows-build-tools
根据官方指南，需要用 npm 安装一下 Windows 构建工具包，如果之前有用过 Virual Studio，这个包应该就不用安装了，但安装了也没啥问题，亲测。安装命令

```bash
npm install --global windows-build-tools
```

需要注意的是，安装这个包需要有管理员权限，所以用有管理员权限的 PowerShell 安装即可。

### 安装 opencv4nodejs
这就是最后一步，也是最关键一步啦

首先需要注意的是，你的项目路径中，不能包含空格、中文等特殊字符，不然后面是编译不过的。但是 `_` 和 `-` 这两个字符可以包含，亲测有效

如果前面的步骤都没问题，首先进入你自己的项目根目录下，然后运行安装命令

```bash
npm install --save opencv4nodejs
```

应该就能看到打印出来的一步步安装日志了。

![安装日志](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201101140021.png)

在网络没有问题的情况下，安装程序会按照 拉取仓库 -> 设置编译配置项 -> 开始编译 -> 编译完成 -> 安装成功 这个步骤进行下去

最大一个坑要发生了，在编译的过程中，可能会报找不到文件的错误，直接就是最严重的那种错误，然后安装进程直接就终止了。报错如下

![](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201101142014.png)

根据报错文件提示的路径，猜想问题应该就出现在该路径下缺失了几个必要的文件。问度娘，果然在手动编译 OpenCV 的过程中会有缺失文件的问题，缺失文件如下

![](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201101140711.png)

那么解决办法就很显然易见了，我们需要在 GitHub 仓库拉取完成之后，手动把缺失的文件放到指定的路径下，这样在编译的过程中，编译器就能找到了。缺失的文件在网上都能找到，这里我也提供一个百度云链接，需要的自取

链接：https://pan.baidu.com/s/1Gxg6c-tBDNXKafIGdHIjDg 
提取码：unxi

这里的细节是，在 opencv 和 openc_contrib 这两个仓库拉取完成之后，找到 `node_modules\opencv-build\opencv\opencv_contrib\modules\xfeatures2d\src\` 这个目录，注意是 opencv_contrib 相关目录下，会发现这个目录下确实没有那几个文件，所以手动将缺失的文件拷贝到这里，问题解决！

## 安装成功
最后放一张安装成功的截图吧~~

![安装成功](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201101142557.png)

## 参考链接
- [opencv4nodejs](https://www.npmjs.com/package/opencv4nodejs#how-to-install)
- [opencv4nodejs安装](https://blog.csdn.net/qq_37385726/article/details/80448322)
- [编译OpenCV以及openc_contrib提示缺少boostdesc_bgm.i文件出错的解决](https://blog.csdn.net/u011736771/article/details/85960300)
- [编译OpenCV时错误，缺少boostdesc_bgm.i文件的问题（附带资源）](https://blog.csdn.net/qq_35498696/article/details/106434799)