---
title: Mac使用体验～
date: 2025-06-23 01:54:03
categories:
 - [清风明月, 心情]
tags: 
 - 心情
 - MacBook
---

最近趁着国补的优惠力度很大，入手了一台 M4 的 MacBook Air，和 Windows 的感受确实很不一样，不需要考虑电脑的续航、关机和重启等

也成功在 Mac 上配置了 blog 编译环境，终于想拾起自己久违的 blog 记录了哈哈

后面会在此记录下来 Mac 的一些使用体验，坚持记录自己的生活吧～

在 Mac 上运行不同架构的 docker 容器
```bash
yuwang@YudeMacBook-Air github-actions-demo % uname -a
Darwin YudeMacBook-Air.local 24.6.0 Darwin Kernel Version 24.6.0: Mon Jul 14 11:30:40 PDT 2025; root:xnu-11417.140.69~1/RELEASE_ARM64_T8132 arm64
yuwang@YudeMacBook-Air github-actions-demo % 
yuwang@YudeMacBook-Air github-actions-demo % 
yuwang@YudeMacBook-Air github-actions-demo % docker run --rm --platform linux/amd64 alpine uname -m
Unable to find image 'alpine:latest' locally
latest: Pulling from library/alpine
2d35ebdb57d9: Pull complete 
Digest: sha256:4b7ce07002c69e8f3d704a9c5d6fd3053be500b7f1c69fc0d80990c2ad8dd412
Status: Downloaded newer image for alpine:latest
x86_64
yuwang@YudeMacBook-Air github-actions-demo % docker run --rm --platform linux/arm64 alpine uname -m
Unable to find image 'alpine:latest' locally
latest: Pulling from library/alpine
6b59a28fa201: Pull complete 
Digest: sha256:4b7ce07002c69e8f3d704a9c5d6fd3053be500b7f1c69fc0d80990c2ad8dd412
Status: Image is up to date for alpine:latest
aarch64
```

在 Mac 上的体验是真不错哇，期间一直没更新博客，有很大一部分原因是因为我在 GitHub 上的 Action 失效了，导致文章 Push 到 GitHub 上不能自动部署

期间工作内容也比较多，所以断断续续的一直修复不了这个问题

在 1 月 18 号周日来公司，整个公司真安静啊，终于能静下心来好好的搞一搞 hexo-action 失效的问题了

用 Mac 电脑借助 Deepseek 把问题修复后，是真爽啊哈哈，博客终于也能继续搞起来了

修复过程记录在下篇文章中，冲冲冲～

## MAC实用技巧
### 访达
* 按住 shift + command + G 可以通过路径跳转到文件夹
* 使用 command + N 可以快速新建访达窗口
* command + i 打开文件详情，然后把照片拖上去后可以更换封面图。如果要恢复成默认，就点击图标后，再点击删除
* 