# GeoMesa-快速安装（基于HBase）

  - [下载](#%E4%B8%8B%E8%BD%BD)
  - [配置环境变量](#%E9%85%8D%E7%BD%AE%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)
  - [下载依赖插件](#%E4%B8%8B%E8%BD%BD%E4%BE%9D%E8%B5%96%E6%8F%92%E4%BB%B6)
  - [部署 jar 包](#%E9%83%A8%E7%BD%B2-jar-%E5%8C%85)
  - [注册协处理器](#%E6%B3%A8%E5%86%8C%E5%8D%8F%E5%A4%84%E7%90%86%E5%99%A8)
  - [设置命令行工具](#%E8%AE%BE%E7%BD%AE%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%B7%A5%E5%85%B7)

GeoMesa 是一个运行在分布式计算系统上，支持大规模时空矢量数据查询和分析的开源工具。

## 下载
从 [GitHub](https://github.com/locationtech/geomesa/releases) 上下载最新的发行版本，上传至服务器，并解压到相关目录

![下载地址](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200618174846.png)


## 配置环境变量
注意把路径替换成自己的路径
```
export HADOOP_HOME=/path/to/hadoop
export HBASE_HOME=/path/to/hbase
export GEOMESA_HBASE_HOME=/opt/geomesa
export PATH="${PATH}:${GEOMESA_HOME}/bin"
```

GeoMesa 推荐在 geomesa-hbase_2.11-$VERSION/conf/geomesa-env.sh 文件中设置以上环境变量，也可以在 .bashrc 或 /etc/profile 中设置

## 下载依赖插件
由于许可的原因，需要手动执行以下命令，安装两个插件：
```bash
[root@hadoop02 geomesa-hbase_2.11-2.4.1]# bin/install-jai.sh
[root@hadoop02 geomesa-hbase_2.11-2.4.1]# bin/install-jline.sh
```

如果因为网络原因一直下载不成功，可以按照控制台打印的网址手动下载，然后上传到 lib 目录下

## 部署 jar 包
GeoMesa for HBase 需要使用本地过滤器来加速查询，因此需要将 GeoMesa 的 runtime JAR 包，拷贝到 HBase 的库目录下
```bash
[root@hadoop02 geomesa-hbase_2.11-2.4.1]# cp dist/hbase/geomesa-hbase-distributed-runtime_2.11-2.4.1.jar /opt/module/hbase-1.3.1/lib/
```

注意：如果是分布式环境，需要将其复制到每一个节点。
```bash
[root@hadoop02 geomesa-hbase_2.11-2.4.1]# xsync /opt/module/hbase-1.3.1/lib/geomesa-hbase-distributed-runtime_2.11-2.4.1.jar
```

## 注册协处理器
注册的过程其实就是使 HBase 在运行时能够访问到 geomesa-hbase-distributed-runtime 的 jar 包。官网给出了几种方法实现这一目标，最方便的是在 HBase 的配置文件 hbase-site.xml 添加如下内容
```xml
<property>
    <name>hbase.coprocessor.user.region.classes</name>
    <value>org.locationtech.geomesa.hbase.coprocessor.GeoMesaCoprocessor</value>
</property>
```

注意：如果是分布式环境，需要在每一个节点都添加相同的内容。
```bash
[root@hadoop02 hbase-1.3.1]# xsync conf/hbase-site.xml
```

## 设置命令行工具
在完成以上设置后，GeoMesa 的主要部分就安装完成了。可以使用 bin/geomesa-hbase 命令调用 GeoMesa 的命令行工具，执行一系列的功能。

这里要额外设置的是使用如下命令，将 HBase 配置文件 hbase-site.xml 打包进 geomesa-hbase-datastore_2.11-$VERSION.jar 中
```bash
[root@hadoop02 geomesa-hbase_2.11-2.4.1]# zip -r lib/geomesa-hbase-datastore_2.11-2.4.1.jar /opt/module/hbase-1.3.1/conf/hbase-site.xml
```

这一步的目的是确保在 MapReduce 任务中，GeoMesa 能够顺利访问到该文件。

下一篇会介绍将 GDELT 数据通过 GeoMesa 上传到 HBase ~