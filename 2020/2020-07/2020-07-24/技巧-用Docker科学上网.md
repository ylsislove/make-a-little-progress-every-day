# 技巧-用Docker科学上网

## 2022-04-10 更新
这篇教程已过时！经过博主亲在尝试，目前腾讯云的香港云服务器管理的很严，小飞机刚开就会被封，封几次后整个IP就会被墙了，所以本篇教程已不适用！

目前博主用的是搬瓦工的云服务器和 x-ray 这个服务端软件，客户端软件用的是 v2rayN，后面看情况，有时间的话会出一篇新的教程哒~~

## 2021-07-21 更新
shadowsocks Windows 和 安卓版的客户端都可以通过 [https://github.com/shadowsocks](https://github.com/shadowsocks) 这个网址下载，如果有小伙伴无法上 GitHub 的话，也可以联系我的邮箱，给你们发送这两个客户端软件~

可能有些小伙伴碰到开启小飞机后，用 `git push` 命令后依然提交失败的情况，这个可能就是由于没有给 git 设置代理导致的，可以按照如下命令设置
```
git config --global http.proxy 'socks5://127.0.0.1:54285'
git config --global https.proxy 'socks5://127.0.0.1:54285'
```

这样就可以在 `~/.gitconfig` 文件中添加上对应的代理设置，再次使用 `git push` 命令时只要打开小飞机，就可以让 git 走代理的道路啦，再也不用担心道路不同了嘿嘿~

Git 设置代理参考：[git设置代理和一些git常用命令](https://www.cnblogs.com/johnzhu/p/6582538.html)

## 2021-01-24 更新
目前腾讯云的轻量应用服务器已经有香港地区的了，通过香港来访问外网还是要比硅谷的快很多哦，所以地域选择香港是最好的~
最近想抽个时间把手机科学上网的教程也更新下，敬请期待吧~

## 前言
最近蓝灯真的是好不稳定，👴真的吐了。还是自己买一个国外的服务器自己搭个梯子吧，自己动手，丰衣足食。我购买的是腾讯云的轻量应用服务器（主要考虑带宽大，每月的流量也足够，关键钱还便宜），每个月也就 24 块钱，把自己续费腾讯视频会员的钱拿出来就足够啦。话不多说，开始配置吧~

哦对，购买的轻量应用服务器的地域是硅谷的哦，既然要科学上网，那肯定不能买国内的呀 hh。

## 安装 Docker
1. 查看内核版本。docker 官方建议内核版本 3.10 以上
    ```bash
    [root@yaindream ~]# uname -a
    Linux yaindream 3.10.0-514.26.2.el7.x86_64 #1 SMP Tue Jul 4 15:04:05 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
    ```

2. 更新 yum 包
    ```bash
    [root@yaindream ~]# yum update
    ```

3. 安装 docker 
    ```bash
    [root@yaindream ~]# yum install docker
    ```

4. 启动 docker 并加入开机启动
    ```bash
    [root@yaindream ~]# systemctl start docker
    [root@yaindream ~]# docker version
    [root@yaindream ~]# systemctl enable docker
    Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
    ```

## 安装 ShadowSocks
1. 拉取 docker-shadowsocks 镜像
    ```bash
    sudo docker pull oddrationale/docker-shadowsocks
    ```

    安装完成后，显示如下：

    ![安装完成](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200724160217.png)

2. 配置 docker-shadowsocks
    ```bash
    sudo docker run -d -p 54285:54285 oddrationale/docker-shadowsocks -s 0.0.0.0 -p 54285 -k yourpasswd -m aes-256-cfb
    ```

    ![参数说明](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200724160337.png)

3. 客户端配置 ip 和端口

    这个客户端是 Shadowsocks，我是通过 scoop 包管理工具安装的。这个包管理工具是专门针对 windows 用户的，也是一个神器，有时间我也会出一篇使用教程。（哦应该是 vpn，手快打错了，懒得重新截图了）

    ![客户端配置](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200724160447.png)

4. 服务器安全组开放端口（腾讯云轻量应用服务器）

    ![服务器安全组开放端口](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200724160703.png)

5. 愉快的玩耍

    ![](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200724161033.png)
