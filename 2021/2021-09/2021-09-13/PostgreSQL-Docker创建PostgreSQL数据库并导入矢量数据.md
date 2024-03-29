# PostgreSQL-Docker创建PostgreSQL数据库并导入矢量数据

## 前言
涉及到 PostgreSQL 10.0 数据库和 postgis 2.4 数据库扩展，基于 docker 安装，在此进行总结和记录~

## 创建命令
```
docker run --name postgis -d -e POSTGRES_USER=postgres -e POSTGRES_PASS=postgres -e POSTGRES_DBNAME=gis -e ALLOW_IP_RANGE=0.0.0.0/0 -p 5432:5432 -v /home/wy/postgre_data:/var/lib/postgresql -v /home/wy/server/cityscene/data:/data --restart=always kartoza/postgis:10.0-2.4
```

参数说明：
- --name postgis：告诉 docker 新建一个镜像，命名为 postgis
- -d：让容器后台运行
- -e：设置容器内环境变量。`POSTGRES_USER` 设置超级用户；`POSTGRES_PASS` 设置用户密码；`POSTGRES_DBNAME` 设置初始化空间数据库的名字；`ALLOW_IP_RANGE` 允许任何客户端连接当前用户
- -p：设置端口。冒号左边是本机向外暴露的端口，冒号右边是容器内部数据库服务端口
- -v：创建数据卷，使数据持久化存储。冒号左边是本机路径，冒号右边是想要存储的容器内部数据
- --restart=always 创建一条自动启动的规则，告诉 Docker ， 每次启动的时候 postgis 容器自动启动

Note：实际上，第二个 `-v` 不是必要的，我这里添加只是因为我开发的应用程序有这个需求

命令运行完后，用 `docker ps` 和 `docker logs postgis` 查看容器是否创建成功，以及创建过程中的日志

## 用 pgAdmin 连接数据库
下载链接：[pgAdmin](https://www.pgadmin.org/download/)

安装完成后打开，首先会让你设置一个 pgAdmin 的访问密码，可以设置为 `postgres` 好记

然后点击添加新服务，输入别名，在 Connection 中输入 ip 地址和其他信息，点击保存，不报错表示连接成功

## 通过 PostGIS Shapefile Import/Export Manager 导入矢量数据
这个工具是矢量 Shapefile 文件的导入工具。下载链接：[PostGIS](http://download.osgeo.org/postgis/windows/pg10/)，可以下载最新版本的 3.1.4

安装 PostGIS Shapefile Import/Export Manager 这个工具之前需要在本地安装 PostgreSQL 10，安装过程参考：[PostgreSQL 10 安装详细步骤](https://blog.csdn.net/antma/article/details/83579920)

因为我们并不需要本地的数据库，所以安装时可以只勾选 server 和 command line 这两项即可。

安装完成后，就可以安装刚刚下载的 Shapefile 文件导入工具了，安装过程可以参考 [PostGIS 2.5.0 安装详细步骤](https://blog.csdn.net/antma/article/details/83580859)

同理，因为我们不使用本地的 PostgreSQL 数据库，所以安装过程中可以选择不安装 spatial database 空间数据库。最后安装完成

打开 PostGIS Shapefile Import/Export Manager，点击 `view connection detail`，输入连接信息，如下图

![连接docker数据库](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210924103213.png)

点击 OK 后，下面输出 success，表示连接成功

![docker数据库连接成功](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210924103344.png)

接下来就是导入矢量数据了，我们从网上下载一份全国 62 个城市建筑物的矢量数据，下载链接：[全国62个城市建筑物轮廓矢量数据](https://www.sohu.com/a/324288814_100020239)，我们解压个武汉的建筑物数据，然后把解压出来的数据放到一个没有中文字符的路径下，路径也不要过长，同时全部选中，按 F2 将中文名称改成英文的，如下图

![规范路径和名称](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210924110802.png)

然后在导入工具中点击 Add File，选择刚刚解压出来的 `wuhan.shp`，就可以看到在 Import List 里出现了我们选择的文件，可以在这里更改表名等信息，确定无误后点击下方的 Import 按钮，如下图

![Import](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210924111102.png)

可以看到下方的输出框中出现 import completed，表示导入成功。

我们还可以在 pgAdmin 中查看到刚刚导入的数据，如下图

![pgAdmin查看导入的数据](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210924111720.png)

## 通过 QGIS 导入矢量数据
上面那个方法必须要在本机上安装 PostgreSQL 数据库，才能安装 PostGIS 导入工具，即使我们用不到本机的数据库，所以第二种导入方式就是通过 QGIS 连接 Docker 容器内的 PostgreSQL 数据库并导入数据，这样就不需要在本机上安装 PostgreSQL 和 PostGIS 了。

后续待更~

## 相关链接
- [PostgreSQL中文社区](http://www.postgres.cn/v2/document)
- [pgAdmin](https://www.pgadmin.org/download/)
- [在 Docker 上搭建 PostGIS 数据库实现空间数据存储及可视化](https://blog.csdn.net/weixin_33694172/article/details/89733112)
