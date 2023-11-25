---
title: Rokid 新项目构建过程中，可能遇到的问题及解决方案
math: true
date: 2023-11-25 19:31:42
categories:
 - [Unity3D, Rokid]
tags: 
 - Unity3D
 - Rokid
---

按照开发者文档构建新项目时，可能会碰到如下报错

从报错信息中可以看到一条关键信息 `Could not resolve com.rokid.uxrplugin:rkuxrplugin:2.3.10`

![](https://image.aayu.today/uploads/2023/11/25/202311251932196.png)

在自己浏览器输入下面的网址，发现也能正常打开链接，那自己的网络应该就是没问题的，那为什么会报错呢

原因可能有两个，一个是自己的 Maven 文件没有配置正确，另一个可能就是自己电脑上全局的 gradle.properties 配置文件曾经配置过代理，从而导致 Rokid Maven 仓库访问异常~


关于第一个原因，正确的 Maven 如何配置，可以看[官方文档 2.3.10 版本](https://custom.rokid.com/prod/rokid_web/c88be4bcde4c42c0b8b53409e1fa1701/pc/cn/11f86798dc6c47518e330df49b1b5e65.html?documentId=cdef4b2bea8542deadbe99aca4921b57#3-%E5%8F%91%E5%B8%83%E9%85%8D%E7%BD%AE)

![](https://image.aayu.today/uploads/2023/11/25/202311251932770.png)


这里就有针对不同  Unity 版本的配置文件，直接下载下来，导入到自己的 Unity 项目即可~


至于第二个原因，就是我误打误撞找到了解决办法哈哈，原先我曾经用 Android Studio 开发过 Android 项目，之前开发时为了解决网络环境，就配置了代理，代理设置就被配置在了全局的 gradle.properties 文件中

对于 Windows，这个文件在 `C:\Users\用户名\.gradle` 目录下，对于 Mac 用户的话，这个文件应该在 `~/.gradle/gradle.properties` 这里

配置过代理后的 gradle.properties 应该会有这四行配置

![](https://image.aayu.today/uploads/2023/11/25/202311251933514.png)

而恰巧不巧的是，这里代理用的 socks 版本和我电脑上 v2rayN代理软件 的 socks 版本不匹配，所以在 unity 或 android studio 里构建安卓项目是就会构建不成功

解决办法也很简单，就把第 15、16 行 https 配置注释掉就好，只用 http 代理

修改完后，再次在 unity 里构建项目，构建成功，问题完美解决~


## 参考链接

* [解决 Android Studio 之Cause: dl.google.com:443 failed to respond](https://blog.csdn.net/hzm1475598891/article/details/88530002)
* [解决：Android Studio 之Cause: dl.google.com:443 failed to respond](https://www.jianshu.com/p/8529dc82f812)
