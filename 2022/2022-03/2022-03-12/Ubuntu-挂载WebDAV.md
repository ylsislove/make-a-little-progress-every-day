---
title: Ubuntu挂载WebDAV
date: 2022/03/12 19:15:00
categories:
 - [Linux进阶之路, Ubuntu]
tags: 
 - Ubuntu
---

## 前言
WebDAV 是个好东西，尤其是配个自己的 NAS 使用，熟悉以后就再也离不开它啦，这篇博客教小伙伴们如何在 Ubuntu 18.04 下挂载 WebDAV~

## 本机环境
* Ubuntu 18.04

## 操作步骤
1. 安装 davfs2
```
apt-get -y install davfs2
```

2. 安装完 davfs2 之后执行
```bash
sed -i 's/# use_locks       1/use_locks       0/g' /etc/davfs2/davfs2.conf
echo "你的WebDAV地址 用户名 密码" >> /etc/davfs2/secrets #保存用户名密码，以后可以直接免密码挂载
mount.davfs 你的WebDAV地址 你想要挂载到的目录
```

即可成功挂载

注意 1：挂载目录必须提前创建好！
注意 2：如果你不执行第二句保存用户名密码，那么你以后挂载的时候都会要求输入用户名密码！

## 开机自动挂载
如果想要开机自动挂载，则再执行
```
echo "mount.davfs 你的WebDAV地址 你想要挂载到的目录" >> /etc/rc.local
```

执行完此句之后检查一下 `/etc/rc.local` 文件，看看是否有 `exit 0` 这句。如果有的话，要手动把上面命令添加进去的语句放到 `exit 0` 之前。

## 参考链接
* [[WebDAV] 如何在各个平台下挂载WebDAV](https://moe.best/linux-memo/mount-webdav.html)
