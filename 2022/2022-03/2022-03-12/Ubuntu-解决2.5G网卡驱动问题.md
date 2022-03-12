---
title: Ubuntu-解决2.5G网卡驱动问题
date: 2022/03/12 19:00:00
categories:
 - [Linux进阶之路, Ubuntu]
tags: 
 - Ubuntu
---

## 前言
由于2.5G网卡较新，各linux发行版的通用驱动已不适用，新装的系统会出现无法上网问题，由于国内网络环境去 Realtek 官网很难下载到驱动文件，故本文提供 github 上的 2.5G Ethernet LINUX driver r8125 for kernel up to 5.6 的版本驱动文件 [r8125-9.003.05.tar.bz2](https://github.com/Vito-Tu/r8125) 各位可以自行下载，并结合此教程安装。

## 本机环境
* Ubuntu 18.04

## 安装步骤
1. 准备编译环境
```
sudo apt-get install --reinstall linux-headers-$(uname -r) linux-headers-generic build-essential dkms
```

2. 解压源码到目录 /usr/src
```
sudo tar xvf r8125-9.003.05.tar.bz2 -C /usr/src
```

3. 添加一个 dkms.conf 到 /usr/src/r8125-9.003.05/ 目录
```
# 先进入目录，方便后续操作
cd /usr/src/r8125-9.003.05/
# 创建dkms配置文件
touch dkms.conf
```

4. 编辑 dkms.conf 文件添加如下内容
```
PACKAGE_NAME=Realtek_r8125
PACKAGE_VERSION=9.003.05
 
DEST_MODULE_LOCATION=/updates/dkms
BUILT_MODULE_NAME=r8125
BUILT_MODULE_LOCATION=src/
 
MAKE="'make' -C src/ all"
CLEAN="'make' -C src/ clean"
AUTOINSTALL="yes"
```

5. 编译安装
```
sudo dkms add -m r8125 -v 9.003.05
sudo dkms build -m r8125 -v 9.003.05
sudo dkms install -m r8125 -v 9.003.05
sudo depmod -a
sudo modprobe r8125
```

验证安装结果, 运行如下命令即可看到 enxxx 的有线网接口
```
ifconfig -a
```

后记：这种方法安装完后，后续如果有内核版本升级，仍需重新编译安装，否则驱动无法运行。执行下方代码重新安装
```
sudo dkms remove r8125/9.003.05 --all
```

但每次出问题都去执行代码太过繁琐，建议在安装目录下（本文是/usr/src/r8125-9.003.05/）将命令打包成可执行文件 fixNetworkCard.sh

1. 创建文件，赋予可执行权限，并切链接到用户目录~方便使用
```
# 确保在安装目录
cd /usr/src/r8125-9.003.05/
# 创建文件名授权
touch fixNetWorkCard.sh
chmod 777 fixNetWorkCard.sh
# 回到用户目录创建软连接
cd ~
ln -s /usr/src/r8125-9.003.05/fixNetWorkCard.sh ./
```

2. 编辑 fixNetworkCard.sh 文件粘贴以下内容
```
dkms remove r8125/9.003.05 --all
dkms install -m r8125 -v 9.003.05
depmod -a
modprobe r8125
```

3. 下次网卡驱动失效时，进行快速修复
```
cd ~
sudo ./fixNetworkCard.sh
```

## 可能出现的问题
### modprobe 加载模块时 出现权限不允许提醒；Operation not permitted
这是由于 secure boot 的原因。如果 secure boot 是开启状态，内核不能安装自己定制的模块。

解决方法：我们进入BIOS 把 secure boot 选项关掉；secure boot 大概的作用时为了保护内核的启动安全。

linux secure boot 状态查询：mokutil --sb-state 
![](http://image.aayu.today/2022/03/12/3501b5b09bf75.png)

## 参考链接
* [Ubuntu安装 Realtek R8125 驱动](https://blog.csdn.net/thunder_k/article/details/106494511)
* [解决linux 2.5G网卡驱动问题](https://blog.csdn.net/poorguy_aos/article/details/108250838)
* [modprobe 加载模块时 出现权限不允许提醒；Operation not permitted](https://www.cnblogs.com/xuyaowen/p/linux-secure-boot-disable.html)
