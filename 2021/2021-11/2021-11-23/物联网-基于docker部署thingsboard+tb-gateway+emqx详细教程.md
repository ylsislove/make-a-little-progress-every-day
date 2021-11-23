# 物联网-基于docker部署thingsboard+tb-gateway+emqx详细教程

  - [前言](#%E5%89%8D%E8%A8%80)
  - [环境](#%E7%8E%AF%E5%A2%83)
  - [安装 postgres 数据库](#%E5%AE%89%E8%A3%85-postgres-%E6%95%B0%E6%8D%AE%E5%BA%93)
  - [启动 thingsboard 镜像](#%E5%90%AF%E5%8A%A8-thingsboard-%E9%95%9C%E5%83%8F)
  - [安装 tb-gateway](#%E5%AE%89%E8%A3%85-tb-gateway)
  - [安装 emqx](#%E5%AE%89%E8%A3%85-emqx)
  - [参考文章](#%E5%8F%82%E8%80%83%E6%96%87%E7%AB%A0)

## 前言
这篇教程其实拖了好久了，十月份的时候经过连续几个晚上的踩坑，终于把整个流程跑通啦。但后面由于自己太懒了，一直没能抽时间把这篇教程记录下来，于是便拖到了现在 (。・ω・。)

拒绝拖延，从我做起。记录下这篇博客，希望能帮到有需要的小伙伴~

## 环境
* 1 核 2G Centos 腾讯云服务器
* postgres 13.0 数据库
* thingsboard 3.2.1
* tb-gateway 最新版
* emqx 4.0

这里需要注意一下，经过博主测试，1 核 2G 的配置是最低最低的极限配置，实际上，在该配置下用 docker 起四个体积不小的容器，打开网页已经能感受到明显的卡顿了。所以建议有条件的小伙伴升级到 2 核 4G 的配置比较好，这里博主就用 1 核 2G 的配置进行演示。

## 安装 postgres 数据库
根据 [thingsboard](https://thingsboard.io/docs/user-guide/install/docker/) 的官方文档，thingsboard 的 docker 镜像里是带了 postgres 数据库的，如下图

![thingsboard的docker镜像](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123145809.png)

因此理论上是不需要单独在安装 postgres 的。但博主在尝试的过程中，碰到了 postgres 的权限问题，即用 thingsboard 镜像里面自带的 postgres 数据库，数据库的初始化总是失败。导致后面 thingsboard 在启动过程中因为在数据库中找不到对应的表，直接就启动失败，退出了。

在查询了很多资料后，在 stackoverflow 上找到了解决办法。

[ThingsBoard Docker container deploy resulting in `PSQLException`](https://stackoverflow.com/questions/64659110/thingsboard-docker-container-deploy-resulting-in-psqlexception)

![stackoverflow上的解决办法](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123151921.png)

解决办法就是不用 thingsboard 镜像内自带的 postgres 数据库，在环境变量中将连接的数据库地址指向我们自己创建的 postgres 数据库。所以第一步就是用 docker 去创建一个 postgres 数据库。

拉取指定版本的 postgres 镜像
```
docker pull postgres:13.0
```

![拉取最新的 postgres 镜像](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123162009.png)

拉取完后查看镜像
```
docker images
```

![拉取完后查看镜像](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123162053.png)

创建并启动容器
```
docker run --name postgres13 -e POSTGRES_PASSWORD=postgres -p 5432:5432 -v /root/thingsboard/pgdata:/var/lib/postgresql/data -d postgres:13.0
```
下面解释下这些参数的意思
- --name：将容器命名为一个好记的名字
- -e：设置环境变量。这里设置数据库的密码是 postgres
- -p：进行端口映射。左边是服务器的端口，右边是容器内的端口
- -v：进行目录映射。即将服务器的 `/root/thingsboard/pgdata` 与容器内部的 `/var/lib/postgresql/data` 的目录进行关联，而容器内部的那个目录即为储存数据的目录，这样就相当于将数据备份到本地了。同理，在服务器的对应目录下对数据库配置文件进行修改也能反映到
- -d：让容器后台运行

注意：postgres 镜像默认的用户名为 postgres

使用 `docker ps` 查看容器状态

![查看容器状态](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123162757.png)

进入服务器的 `/root/thingsboard/pgdata` 目录下，可以看到该目录下已经有数据了

![数据目录](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123162852.png)

下面可以在我们自己的电脑上用 pgadmin 工具连接一下云端的 postgres 数据库。注意服务器要放开 5432 端口哦

创建一个 server

![创建一个 server](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123163127.png)

填写数据库连接的参数，密码就是创建时设的 `postgres`，点击确定后，没啥问题应该就能顺利连接上啦

接下来，在 pgadmin 里创建一个 `thingsboard` 数据库，这样到时 thingsboard 镜像启动时，会连接这个数据库，对数据库进行初始化

![创建一个 `thingsboard` 数据库](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123163619.png)

输入数据库名称后，点击确定

![输入数据库名称](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123163713.png)

做完这一步，数据库相关的工作就基本完成了，下一步就是启动 thingsboard 镜像了

## 启动 thingsboard 镜像
根据 [thingsboard](https://thingsboard.io/docs/user-guide/install/docker/) 官方文档，想启动 thingsboard 镜像，除了需要安装 `docker`，还需要再安装 `docker compose`，如下图

![安装必要条件](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123164333.png)

根据 [docker compose](https://docs.docker.com/compose/install/) 的文档，运行如下命令安装 `docker compose`

下载二进制可执行文件
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

赋予可执行权限
```
sudo chmod +x /usr/local/bin/docker-compose
```

![docker compose安装步骤](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123165111.png)

运行下列命令测试安装是否成功
```
docker-compose --version
```

![测试安装是否成功](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123165344.png)

按照 [thingsboard](https://thingsboard.io/docs/user-guide/install/docker/) 官方文档，接下来就是创建一个 `docker-compose.yml` 文件了，这里该文件的内容和官方文档里的就有些差别了。因为官方文档里的默认是用内部的 postgres 数据库，经过博主的惨烈踩坑后，发现这种方式行不通，所以 `docker-compose.yml` 文件里的内容按照我的来编辑

```yml
version: '2.2'
services:
  mytb:
    restart: always
    image: "thingsboard/tb-postgres:3.2.1"
    ports:
      - "8080:9090"
      - "1884:1883"
      - "7070:7070"
      - "5683-5688:5683-5688/udp"
    environment:
      - TB_QUEUE_TYPE=in-memory
      - SPRING_DATASOURCE_URL=jdbc:postgresql://xxx.xxx.xxx.xxx:5432/thingsboard
      - SPRING_DATASOURCE_USERNAME=postgres
      - SPRING_DATASOURCE_PASSWORD=postgres
```

可以看到和官方文档里的主要区别就是在环境变量里指定了外部 postgres 数据库的地址，注意把地址换成你自己云服务器的地址

哦对，还有一个主要区别，注意到 `1884:1883` 了吗，官方文档里是 `1883:1883`，这里和官方文档不一样是因为我后面还需要用 docker 启动 `emqx`，而 `emqx` 也需要用 1883 端口，所以我这里把 thingsboard 的 1883 端口映射为服务器的 1884 端口，这里是一个重点哦~

这里可以把 `docker-compose.yml` 文件放到 `/root/thingsboard/` 目录下，然后我们在该目录下运行

```
docker-compose pull
docker-compose up
```

来拉取镜像并启动镜像。

这里我镜像指定的是 `3.2.1` 版本的，如果想用最新版的，可以把后面的 `3.2.1` 去掉，但最新版的可能会有新的问题，这里博主还没有去踩新坑

数据库地址配置正确的话，可以在启动过程中看到正在初始化数据库

![初始化数据库](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123171835.png)

下图表示数据库初始化成功，数据库初始化成功的话，后面就应该不会有啥问题了

![数据库初始化成功](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123171857.png)

下图就是正常启动的输出日志

![下图就是正常启动的输出日志](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123172316.png)

在服务器的防火墙中放开 `8080`、`1884`、`7070`、`5683-5688` 这几个端口，然后再浏览器中访问 `ip地址:8080`，就可以看到 thingsboard 的登陆界面了，如下图

![thingsboard 的登陆界面](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123183411.png)

官方文档也给出了默认的系统管理员账号和密码，如下图

![默认的系统管理员账号和密码](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123183536.png)

我们再打开 pgadmin，可以看到 thingsboard 数据库中已经多出了很多表，这些都是在数据库初始化时自动生成的

![数据库](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123183720.png)

至此，用 docker 启动 thingsboard 就成功啦~

## 安装 tb-gateway
可以直接参考官方文档：[Install ThingsBoard IoT Gateway using Docker.](https://thingsboard.io/docs/iot-gateway/install/docker-installation/)

```
docker run -it -v ~/.tb-gateway/logs:/thingsboard_gateway/logs -v ~/.tb-gateway/extensions:/thingsboard_gateway/extensions -v ~/.tb-gateway/config:/thingsboard_gateway/config --name tb-gateway --restart always thingsboard/tb-gateway
```

![官方文档](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123184621.png)

通过 `-v` 挂载目录后，就可以直接在 `~/.tb-gateway/config` 修改 tb-gateway 的配置文件了，非常的方便

接下来可以参考 [Thingsboard 3.0 通过 tb-gateway 网关接入 MQTT 设备教程](https://www.cnblogs.com/iotschool/p/13065330.html) 这篇博客对 `tb-gateway` 进行配置

## 安装 emqx
这个好像也没啥好写的，直接看官方文档就行了：[通过 Docker 运行 (包含简单的 docker-compose 集群)](https://docs.emqx.cn/broker/v4.3/getting-started/install.html#%E9%80%9A%E8%BF%87-docker-%E8%BF%90%E8%A1%8C-%E5%8C%85%E5%90%AB%E7%AE%80%E5%8D%95%E7%9A%84-docker-compose-%E9%9B%86%E7%BE%A4)

```
docker pull emqx/emqx:v4.0.0
$ docker run -d --name emqx -p 1883:1883 -p 8081:8081 -p 8083:8083 -p 8883:8883 -p 8084:8084 -p 18083:18083 emqx/emqx:v4.0.0
```

![安装 emqx](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123185652.png)

注意在防火墙放开 `1883`、`8081`、`8083`、`8883`、`8084`、`18083` 这几个端口

启动成功后，访问 `ip地址:18083`，就可以看到 emqx 的界面了，如下图

默认用户名是 `admin`，密码是 `public`

![emqx](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211123190407.png)

剩下的就可以参考 [Thingsboard 3.0 通过 tb-gateway 网关接入 MQTT 设备教程](https://www.cnblogs.com/iotschool/p/13065330.html) 这篇博客接入 MQTT 设备啦

教程写到这里就要结束啦，这篇教程浓缩了博主踩了好几个晚上的坑，都是博主的血和泪555，如果对你们有帮助的话，记得点个赞支持一下博主呀 (✿◡‿◡)

## 参考文章
* [Installing ThingsBoard using Docker (Linux or Mac OS)](https://thingsboard.io/docs/user-guide/install/docker/)
* [ThingsBoard Docker container deploy resulting in `PSQLException`](https://stackoverflow.com/questions/64659110/thingsboard-docker-container-deploy-resulting-in-psqlexception)
* [Thingsboard 3.0 通过 tb-gateway 网关接入 MQTT 设备教程](https://www.cnblogs.com/iotschool/p/13065330.html)
