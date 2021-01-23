# 技巧-用Docker科学上网

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
