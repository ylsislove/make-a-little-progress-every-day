# Zeppelin-快速安装配置

  - [版本选择](#%E7%89%88%E6%9C%AC%E9%80%89%E6%8B%A9)
  - [安装配置](#%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE)

Apache Zeppelin 是一款基于 web 的 notebook（类似于 ipython 的 notebook），支持交互式地数据分析。原生就支持 Spark、Scala、SQL、shell、markdown等。

对于 Zeppelin 而言，并不依赖 Hadoop 集群环境，我们可以部署到单独的节点上进行使用 ~

## 版本选择
zeppelin 每个版本分别对应两种版本：netinst 和 all。

主要区别是：netinst 是 net -install 的简写，就是 Interpreters 自己通过网络安装，具体安装教程可以查阅官方文档。

而 all 版本则是 Interpreters 都集成在压缩包中，无需网络安装了。

这里我选择 0.9.0 的 all 版本进行安装

## 安装配置

1. 下载地址

    [http://zeppelin.apache.org/download.html](http://zeppelin.apache.org/download.html)

    文件比较大，有 1.5 个 G 左右，所以要耐心等待。

2. 上传至服务器并解压

3. 配置环境变量
    ```
    [root@hadoop02 zeppelin-0.9.0-preview1-bin-all]# vim /etc/profile

    # ZEPPELIN_HOME
    export ZEPPELIN_HOME=/opt/module/zeppelin-0.9.0-preview1-bin-all
    export PATH=$PATH:$ZEPPELIN_HOME/bin

    [root@hadoop02 zeppelin-0.9.0-preview1-bin-all]# source /etc/profile
    ```

4. 修改 zeppelin 配置

    对配置文件重命名
    ```bash
    [root@hadoop02 conf]# cp zeppelin-env.sh.template zeppelin-env.sh
    [root@hadoop02 conf]# cp zeppelin-site.xml.template zeppelin-site.xml
    ```

    修改 zeppelin-env.sh。添加路径，注意换成自己的路径
    ```
    export JAVA_HOME=/opt/module/jdk1.8.0_144
    export SPARK_HOME=/opt/module/spark-2.1.1-bin-hadoop2.7
    ```

    修改 zeppelin-site.xml。更改服务器地址和端口，保证端口不被其他进程占用
    ```xml
    <property>
        <name>zeppelin.server.addr</name>
        <value>hadoop02</value>
        <description>Server binding address</description>
    </property>

    <property>
        <name>zeppelin.server.port</name>
        <value>8090</value>
        <description>Server port.</description>
    </property>
    ```

5. 启动
    ```bash
    [root@hadoop02 zeppelin-0.9.0-preview1-bin-all]# zeppelin-daemon.sh start
    ```

    jps 查看
    ```bash
    [root@hadoop02 zeppelin-0.9.0-preview1-bin-all]# jps
    7008 DataNode
    7362 NodeManager
    25939 HMaster
    4873 QuorumPeerMain
    6906 NameNode
    26074 HRegionServer
    35562 Jps
    35340 ZeppelinServer
    ```

6. web 端查看

    ![web页面](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200618204506.png)


接下来就可以很方便的使用 spark 对数据库的数据进行分析了 ~