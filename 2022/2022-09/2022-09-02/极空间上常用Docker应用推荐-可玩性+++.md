---
title: 极空间上常用Docker应用推荐-可玩性+++
date: 2022-09-03 01:28:42
categories:
 - [我的NAS捣鼓笔记, 极空间]
tags: 
 - NAS
 - 极空间
---

## 应用推荐
1. baota（宝塔），可以部署自己的网站 https://aayu.today
2. lsky（兰空图床），基于baota部署，在docker上部署好自己的兰空图床后，写博客时要用到的图片都可以保存到NAS里了，数据在手，天下我有
3. nginx，部署自己的个人博客 https://blog.aayu.today
4. zdir，部署自己的共享云盘 https://pan.aayu.today
5. gitea，部署自己的代码仓库 https://code.aayu.today，可私有可公开，代码保存到自己的NAS里，倍安心~
6. mariadb，本质是mysql8数据库，上面的兰空图床和gitea都要用到mysql数据库
7. qbittorrent 影片资源下载神器
8. frpc 我觉得是最好用的内网穿透工具，配合腾讯云的香港云服务器和自己的域名，便可实现我上述的那些域名外网访问了，香港云服务器峰值带宽30Mb，实测夜间下载我的共享云盘资源能到4MB/s，很爽
9. siyuan（思源笔记），可以把自己的笔记保存到我们的极空间里，而且可配置项很多，笔记的界面可以美化的很好看~
10. qinglong（青龙面板），挂载自动化脚本，可以拿来薅羊毛（蛮复杂的），或练练自己写的自动化脚本，还是蛮不错的
11. komga，一个支持中文，可以看漫画的 Docker 应用

以上就是我目前最常使用的docker应用了，我觉得极大丰富了极空间NAS的可玩性~~

Reader3 我折腾了一下，发现搜书过程响应太慢了，而且书源还很杂很乱，占用资源又挺多的，还不如用极空间 App 自带的极阅读呢，把自己找的资源导进去就可以了，所以 Reader3 我就不折腾了~

## 详细设置
### qbittorrent
* linuxserver/qbittorrent:latest
* 这里推荐 4 个 CPU，内存 4G 应该会更好一点~
* 下面的容器端口只用配置 8999 和 8092 这三个端口就行
* 访问地址：IP地址+端口:8092
* 默认用户名是admin、密码是adminadmin
* 在添加的时候，保存文件的路径，这个`/downloads/`不要删除，我们直接在后面加文件夹名字即可，例如`/downloads/电影`、`/downloads/4K电影`、`/downloads/电视剧`等等

![](https://image.aayu.today/uploads/2022/09/03/202209030007797.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030009238.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030014797.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030016077.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030059310.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030101665.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030101798.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030102482.png)
{.gallery data-height="150"}

### baota
* kangkang223/baota:latest
* 文件夹映射没必要映射`/home`，当时只是测试用的
* 端口映射后面的`8890-8899`随意设置，这是为以后宝塔内的应用预留的备用端口
* 宝塔启动成功后，进入SSH，用`bt`命令重置用户名和密码就行
* 可以是不是的备份宝塔配置，这样以后迁移时就能直接恢复配置了，注意要把宝塔备份数据下载下来
* 要搭建兰空图床的PHP-8.0的配置详见我这篇博客：[手拉手教你在极空间Docker宝塔上搭建兰空图床（Lsky）](https://blog.aayu.today/nas/zspace/20220822/)

:::warning  
注意：在搭建图床那篇博客中需要变通的是，不能用宝塔内部的 MySQL 数据库，因为我实测，用了一两天就自己给崩了，再也启动不了，所以解决办法就是用下面我要介绍的 `Mariadb` 镜像，该 Docker 镜像就是 MySQL8 数据库，不能用宝塔内部的数据库，一定要注意呀，不管用哪个数据库，也要经常做备份~
:::

![](https://image.aayu.today/uploads/2022/09/03/202209030137635.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030138132.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030140784.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030141848.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030142449.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030144588.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030145938.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030150748.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030151260.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030414585.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030416891.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030418283.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030420696.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030421764.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030422381.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030424566.png)
{.gallery data-height="150"}

### frpc
* oldiy/frpc:latest
* 除了设置文件夹路径外，其余设置都保持默认就好

![](https://image.aayu.today/uploads/2022/09/03/202209030213306.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030214380.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030215126.png)
{.gallery data-height="150"}

### mariadb
* kangkang223/centos-mariadb:latest
* 在环境这里记得设置 root 密码
* 如果是初次运行镜像，进入容器后，运行 `sh /init_db.sh`，有报错的话就再运行一次，应该就没有报错了
* 容器内连接数据库：`/usr/local/mariadb/bin/mysql -u root`
* 记得数据库要常做备份呀！

![](https://image.aayu.today/uploads/2022/09/03/202209030217415.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030217487.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030218084.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030218742.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030219962.png)
{.gallery data-height="150"}

### gitea
* gitea/gitea/1.9.6-linux-amd64
* 注意，这里在环境这里设置了 git 作为程序的运行用户，同时指定了 UID 和 GID 都为 1000，这个设置很重要，因为后面用 Nginx 映射博客静态文件时，只有 UID 保持一直，才不会导致博客文件权限混乱
* gitea 的其他配置可以详见：[手拉手教你在极空间Docker上安装Gitea并实现SSH提交代码](https://blog.aayu.today/nas/zspace/20220822-2/)

:::primary
如果配合 Hexo 博客框架，想实现把博客静态文件提交到 gitea 上，需要参考 [hexo部署到云服务器上](https://blog.csdn.net/weixin_43886632/article/details/106457873) 这篇文章，设置一下 `GIT HOOKS`，在 `post-receive` 添加如下内容（注意按自己实际情况适当修改静态文件保存的路径）

```
git --work-tree=/data/www/blog --git-dir=/data/git/repositories/ylsislove/blog.git checkout -f
```

注意提前创好`/data/www/blog`目录，并用`chown -R git:git /data/www/blog`设置成 git 用户和组
:::

app.ini 部分配置供参考
```
[server]
APP_DATA_PATH    = /data/gitea
SSH_DOMAIN       = code.aayu.today
HTTP_PORT        = 3000
ROOT_URL         = https://code.aayu.today/
DISABLE_SSH      = false
SSH_PORT         = 2222
LFS_START_SERVER = true
LFS_CONTENT_PATH = /data/git/lfs
DOMAIN           = code.aayu.today
OFFLINE_MODE     = false
LANDING_PAGE	 = explore

[picture]
AVATAR_UPLOAD_PATH            = /data/gitea/avatars
REPOSITORY_AVATAR_UPLOAD_PATH = /data/gitea/repo-avatars
DISABLE_GRAVATAR              = true
ENABLE_FEDERATED_AVATAR       = false

[attachment]
PATH = /data/gitea/attachments
ALLOWED_TYPES = */*
MAX_SIZE  = 50
MAX_FILES = 10

[service]
DISABLE_REGISTRATION              = true
REQUIRE_SIGNIN_VIEW               = false
REGISTER_EMAIL_CONFIRM            = false
ENABLE_NOTIFY_MAIL                = false
ALLOW_ONLY_EXTERNAL_REGISTRATION  = false
ENABLE_CAPTCHA                    = false
DEFAULT_KEEP_EMAIL_PRIVATE        = false
DEFAULT_ALLOW_CREATE_ORGANIZATION = true
DEFAULT_ENABLE_TIMETRACKING       = true
NO_REPLY_ADDRESS                  = noreply.example.org
```

![](https://image.aayu.today/uploads/2022/09/03/202209030229974.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030230543.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030230993.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030231483.png)
{.gallery data-height="150"}

### zdir
* linuxserver/nginx:latest
* 注意配置下要映射的 80 端口
* 除了文件夹路径和端口设置下，其他设置默认就可以啦

![](https://image.aayu.today/uploads/2022/09/03/202209030254768.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030255280.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030255097.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030256144.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030257806.png)
{.gallery data-height="150"}

### blog
* linuxserver/nginx:latest
* 注意博客的文件夹路径映射，是从 gitea 创建的 /data/www/blog 那里映射过来的
* 所以在环境配置那里要多加条配置`USER`，`git`
* 同样注意配置下要映射的 80 端口

:::warning
这里我的配置还是有问题的，因为我就算设置了`USER`、`USER_UID`和`USER_GID`，容器启动后，依然把 `/data/www/blog` 这个目录的用户和组变成了 911，变成 911 后，博客访问虽然没问题，但用 Hexo 部署博客到 gitea 就会报错，因为 git 用户没有 911 用户的权限，我这个小菜鸟目前也不知道该怎么解决啦，如果有熟悉 docker 的，欢迎给我点指导 🙈
:::

:::primary
2022-09-03 更新：博客这里的权限问题解决了，需要设置`PUID`和`PGID`为 1000，就可以了。因为 gitea 容器的环境是 git 用户，而 git 用户的 ID 就是 1000，但和 gitea 容器的区别是，这里要用`PUID`和`PGID`指定 nginx 启动用户的 ID 号，只要设置了，就可以和 gitea 那边保持同样的用户 ID 了，问题解决~
:::

![](https://image.aayu.today/uploads/2022/09/03/202209030258911.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030258706.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030259805.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030332199.png)
{.gallery data-height="150"}

### siyuan
* zsource/siyuan:latest
* 思源笔记配置比较简单，环境那里可以配置下授权码配置`ACCESSAUTHCODE`，这样笔记就必须输入授权码才能查看啦，这里忘设置了也没关系，可以进入界面后在笔记里设置
* 思源笔记美化教程资源：[思源笔记美化教程](https://github.com/langzhou/siyuan-note)

:::primary
要是配置了内网穿透，然后用反向代理设置了 HTTPS，需要在反向代理的配置文件里添加如下两行，进行 WebSocket 反代，详情可参考：[群晖docker安装，配置反向代理，https访问提示“内核连接中断...v2.0.11](https://github.com/siyuan-note/siyuan/issues/4959)

```
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection 'Upgrade';
```
:::

![](https://image.aayu.today/uploads/2022/09/03/202209030339604.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030340122.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030340469.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030341131.png)
{.gallery data-height="150"}

### qinglong
* whyour/qinglong:latest
* 文件夹映射还蛮多的，青龙面板用来练练自己写的自动化任务还是蛮不错的
* 用青龙面板薅羊毛感觉好复杂，后面有时间再研究吧

![](https://image.aayu.today/uploads/2022/09/03/202209030355859.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030355501.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030356578.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030356433.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030358002.png)
{.gallery data-height="150"}

### komga
* gotson/komga:latest
* 一个支持中文，可以看漫画的 Docker 应用，但说实话，我还不咋常用，最主要的原因可能是漫画资源不好找哇 😖
* 貌似占用资源很多，如果有小伙伴常用的话，可以取消性能限制

![](https://image.aayu.today/uploads/2022/09/03/202209030404198.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030405788.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030405832.png)
![](https://image.aayu.today/uploads/2022/09/03/202209030405492.png)
{.gallery data-height="150"}

## 尾记
迁移 Docker 前记得备份下 mariadb 数据库
