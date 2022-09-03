---
title: 手拉手教你在极空间Docker上安装Gitea并实现SSH提交代码
date: 2022-08-22 17:47:48
categories:
 - [我的NAS捣鼓笔记, 极空间]
tags: 
 - NAS
 - 极空间
 - Gitea
 - SSH
---

## 前言
踩坑不容易啊，终于把这个需求实现了，这样我就可以把我的[博客小站](https://blog.aayu.today/)通过 Git 部署到极空间上了，也可以把自己一些好玩的代码仓库上传到极空间上，再也不用担心 GitHub 的龟速访问，以及 Gitee 莫名其妙的代码审查了~~

注意，本文需要配合内网穿透，实现外网访问后才能解决一些报错问题，有一定难度哦~~

## 安装数据库
Gitea 运行需要数据库，默认为本地 sqlite，不过不推荐这种方式。这里可以参考 kangkang 大佬在极空间论坛里发布的安装 mariadb（mysql）镜像的教程，膜拜大佬~

## 安装Gitea
在极空间 Z4 的 Docker 里选择 `gitea/gitea` 镜像的 `1.9.6-linux-amd64` 版本进行下载，如下图

![](https://image.aayu.today/uploads/2022/08/22/202208221954929.png)

下载完成后可以参考如下配置启动容器

![](https://image.aayu.today/uploads/2022/08/22/202208221955369.png)

![](https://image.aayu.today/uploads/2022/08/22/202208221955658.png)

![](https://image.aayu.today/uploads/2022/08/23/202208230016107.png)

![](https://image.aayu.today/uploads/2022/08/22/202208221956557.png)

其中，数据目录必须挂载，防止数据丢失。USER_UID=1000 USER_GID=1000 也需要设置

其他设置使用默认的就可以啦，设置好以后，就可以启动容器了

## 配置Gitea
容器启动成功后，在浏览器中访问 `http://NAS的内网IP:3000/` 就可以看到 Gitea 的展示界面了，如下

![](https://image.aayu.today/uploads/2022/08/22/202208221959202.png)

点击右上角的注册，就可以进行 Gitea 的初始化配置，配置如下

![](https://image.aayu.today/uploads/2022/08/22/202208222000549.png)

![](https://image.aayu.today/uploads/2022/08/22/202208222301075.png)

![](https://image.aayu.today/uploads/2022/08/22/202208222001352.png)

然后点击安装，耐心等待 10 分钟左右应该就能安装成功了~

安装完成后就会自动跳转到用户的界面，如下图

![](https://image.aayu.today/uploads/2022/08/22/202208222003278.png)

我们可以点击 + 号新建一个仓库来测试下~~

![](https://image.aayu.today/uploads/2022/08/22/202208222008537.png)

注意，这里有点小 bug，就是创建的时候不能勾选 `初始化存储库`，否则会报 500 的异常，这个问题如果有大佬知道怎么解决欢迎留言呀~~

:::info
2022-08-23 更新：博主在查看了日志后发现，当勾选了 `初始化存储库` 再创建仓库，gitea 会尝试用 git 用户去操作 `/tmp` 目录，而 tmp 目录是属于 `root:root` 用户和组的，所以这里就没操作成功，报了没有权限的错误，所以仓库就创建失败，返回 500

知道报错原因后解决办法就很简单啦，我们在极空间里用 root 账号进入 gitea 容器，然后用 `chown -R git:git tmp/` 命令将 tmp 目录设置为 git 用户和组的，再次创建勾选了 `初始化存储库` 的仓库，报错完美解决~
:::

创建成功如下图

![](https://image.aayu.today/uploads/2022/08/22/202208222010015.png)

但是我这边测试直接在本地拉取会报错，但看 kangkang 大佬的[教程](https://www.chenweikang.top/?p=1151)本地拉取就没有报错，有大佬如果知道是怎么回事欢迎给我留言

![](https://image.aayu.today/uploads/2022/08/22/202208222028976.png)

接下来测试下迁移外部仓库。点击左上角选择

![](https://image.aayu.today/uploads/2022/08/22/202208222021979.png)

点击迁移，耐心等待下，便可成功将外部的仓库迁移到极空间里的 Gitea 了，很方便~

![](https://image.aayu.today/uploads/2022/08/22/202208222023397.png)

这里我又测试了一下本地拉取迁移过来的仓库，也是报错了。但别泄气，当后面配置了 frp 内网穿透后，用外网域名访问，以上本地拉取的报错问题就没有啦~

![](https://image.aayu.today/uploads/2022/08/22/202208222031910.png)

## 配置内网穿透
内网穿透的方式太多了，我这里也没办法详细展开介绍，也不是本文的重点

我用的是 `frp + 腾讯云 + 宝塔 + 自己的域名` 方式做的内网穿透，这样做的好处是完全的自我掌控，感兴趣的小伙伴可以去找点教程学习一下，frp 如果你会一点 Linux 命令的话，其实很简单的~~

配置好内网穿透和域名后，就可以在外网用自己的域名访问了，效果如下~

![](https://image.aayu.today/uploads/2022/08/22/202208222049630.png)

成功外网访问后，可以看到仓库的克隆链接那里还是极空间内网的地址，这里就需要再对 Gitea 的配置文件进行修改了

![](https://image.aayu.today/uploads/2022/08/22/202208222051607.png)

在极空间的文件管理中，找到我们挂在的数据目录，找到 `app.ini` 配置文件，这里可以把这个配置文件下载到电脑上，然后用 sublime 或 notepad++ 等编辑器修改，或如果已经把极空间挂载成了网络硬盘，也可以直接在网络硬盘里找到该文件进行修改，或如果熟悉 vi 等编辑器的话，也可以直接打开极空间 Docker 的 SSH，在容器内部修改该配置文件都可以，选择自己熟悉的方式就好啦

配置文件要修改以下地方

![](https://image.aayu.today/uploads/2022/08/23/202208230024987.png)

修改完配置文件后，就要重启 Gitea，这里不需要重启容器，而是直接进到容器内部，然后用 `ps aux | grep gitea` 命令找到 Gitea 进程，如下图

注意要用 git 用户进入容器

![](https://image.aayu.today/uploads/2022/08/22/202208222057259.png)

![](https://image.aayu.today/uploads/2022/08/22/202208222100817.png)

然后用 `kill -9 进程ID` 命令杀死 Gitea 进程即可，杀死后容器会自动重启 Gitea 程序~~

![](https://image.aayu.today/uploads/2022/08/22/202208222103463.png)

注意，这里可以用 `ps aux | grep gitea` 命令多查询几次，看重启后的 Gitea 进程 ID 是否还会变化，如果一直在变化，就表示你的 `app.ini` 设置有误，程序在不断的重启当中。

如果发生了程序在不断重启的情况，不要慌张，可以去 `/data/gitea/log` 目录下找到日志文件，看是什么原因报错然后改正就可以啦

![](https://image.aayu.today/uploads/2022/08/22/202208222105495.png)

修改完配置文件并重启 Gitea 后，可以在 Web 界面的右上角【管理后台】处查看 Gitea 的配置，如下图

![](https://image.aayu.today/uploads/2022/08/22/202208222108037.png)

![](https://image.aayu.today/uploads/2022/08/23/202208230027900.png)

可以看到在配置文件里修改的都已经更新过来了~~

然后打开我们的项目，可以看到克隆链接已经变成公网域名的地址了

![](https://image.aayu.today/uploads/2022/08/22/202208222113401.png)

然后再次在本地克隆仓库，嘿嘿，发现仓库成功拉取下来了。拉取时报了个警告是说我们的仓库是空的，没有内容~

![](https://image.aayu.today/uploads/2022/08/22/202208222115090.png)

那我们就推送个内容上去

![](https://image.aayu.today/uploads/2022/08/22/202208222119098.png)

![](https://image.aayu.today/uploads/2022/08/22/202208222119931.png)

可以看到我们本地的推送测试也是没有问题啦~~

## 配置SSH提交
SSH 需要把我们自己电脑的公钥追加到容器的 `/data/git/.ssh/authorized_keys` 文件中，SSH 的公钥不知如何生成的，可以看我的这篇教程：[]()

注意，有小伙伴可能会注意到个人配置中有配置 SSH 的地方，如下图

![](https://image.aayu.today/uploads/2022/08/22/202208222121300.png)

![](https://image.aayu.today/uploads/2022/08/22/202208222124452.png)

但博主实测，这样的做法不行，首先直接添加会报 500 的错误。就算查阅资料后，在 `app.ini` 配置文件中添加 `START_SSH_SERVER = true` 语句，然后成功在上图位置配置好了个人的 SSH 公钥，后面用 SSH 克隆仓库时还是不行，这里博主踩坑踩得贼累 🥲

所以正确使用 SSH 的做法是什么呢，往下看！

我们需要把自己电脑的公钥追加到容器的 `/data/git/.ssh/authorized_keys` 文件中。具体操作步骤就是先借助极空间把自己电脑的公钥文件上传到容器的 `/data/git` 目录下，然后用 `cat id_rsa.pub > .ssh/authorized_keys` 命令生成 authorized_keys 文件（默认 .ssh 目录下没有这个文件），然后再用 `chmod 600 authorized_keys` 更改文件的权限，就大公告成啦~

![](https://image.aayu.today/uploads/2022/08/23/202208230038774.png)

当成功配置了自己的公钥后，有什么效果呢，看下图

![](https://image.aayu.today/uploads/2022/08/23/202208230041738.png)

发现我们可以在自己的电脑上用 git 用户登录上极空间的 gitea 容器啦，终于达到这一步了，后面我们就可以用 SSH 来拉取代码了

## 用SSH克隆代码
我们现在来尝试将迁移过来的外部仓库用 SSH 的方式克隆到本地，执行 clone 命令一看，卧槽，为啥还报错

![](https://image.aayu.today/uploads/2022/08/23/202208230048808.png)

细细看下报错原因，诶这个原因已经不是登录的问题了！是没有找到我们的 git 仓库。那为什么没找到呢，我们可以看到程序找 git 仓库的路径是 `/ylsislove/test-project.git`，这斜杠开头的路径，是跑去容器的根路径下去找了

那我们仓库的地址是在容器的 `/data/git/repositories/ylsislove/test-project.git` 这个路径下，所以我们就尝试对命令稍加修改 `git clone ssh://git@code.aayu.today:2222/data/git/repositories/ylsislove/test-project.git`，运行，成了！

![](https://image.aayu.today/uploads/2022/08/23/202208230053242.png)

## 尾声
以上就是博主的踩坑过程，踩坑不易，希望能帮助到更多爱折腾的小伙伴~

## 参考链接
* [Gitea官方文档](https://docs.gitea.io/zh-cn/reverse-proxies/)
* [Gitea,一款轻量好用的自托管 Git 服务](https://www.chenweikang.top/?p=1151)
