# HBase-HBase安装部署

  - [环境](#%E7%8E%AF%E5%A2%83)
  - [Zookeeper正常部署](#zookeeper%E6%AD%A3%E5%B8%B8%E9%83%A8%E7%BD%B2)
  - [Hadoop正常部署](#hadoop%E6%AD%A3%E5%B8%B8%E9%83%A8%E7%BD%B2)
  - [HBase解压](#hbase%E8%A7%A3%E5%8E%8B)
  - [HBase的配置文件](#hbase%E7%9A%84%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)
  - [HBase服务的启动](#hbase%E6%9C%8D%E5%8A%A1%E7%9A%84%E5%90%AF%E5%8A%A8)

## 环境
在之前完成 Hadoop 完全分布式安装和部署的服务器上继续完成 HBase 的安装和部署，不了解的朋友可看：
* [Hadoop-完全分布式运行模式（一）](../2020-06-09/Hadoop-完全分布式运行模式（一）.md)
* [Zookeeper-分布式安装部署](../2020-06-11/Zookeeper-分布式安装部署.md)

## Zookeeper正常部署
首先保证 Zookeeper 集群正常部署并启动之：
```bash
[root@hadoop02 zookeeper-3.4.10]# zkServer.sh start
[root@hadoop03 zookeeper-3.4.10]# zkServer.sh start
[root@hadoop04 zookeeper-3.4.10]# zkServer.sh start
```

## Hadoop正常部署
Hadoop 集群的正常部署并启动：
```bash
[root@hadoop02 hadoop-2.7.2]# start-dfs.sh
Starting namenodes on [hadoop02]
hadoop02: starting namenode, logging to /opt/module/hadoop-2.7.2/logs/hadoop-root-namenode-hadoop02.out
hadoop02: starting datanode, logging to /opt/module/hadoop-2.7.2/logs/hadoop-root-datanode-hadoop02.out
hadoop03: starting datanode, logging to /opt/module/hadoop-2.7.2/logs/hadoop-root-datanode-hadoop03.out
hadoop04: starting datanode, logging to /opt/module/hadoop-2.7.2/logs/hadoop-root-datanode-hadoop04.out
Starting secondary namenodes [hadoop04]
hadoop04: starting secondarynamenode, logging to /opt/module/hadoop-2.7.2/logs/hadoop-root-secondarynamenode-hadoop04.out

[root@hadoop03 hadoop-2.7.2]# start-yarn.sh 
starting yarn daemons
starting resourcemanager, logging to /opt/module/hadoop-2.7.2/logs/yarn-root-resourcemanager-hadoop03.out
hadoop03: starting nodemanager, logging to /opt/module/hadoop-2.7.2/logs/yarn-root-nodemanager-hadoop03.out
hadoop02: starting nodemanager, logging to /opt/module/hadoop-2.7.2/logs/yarn-root-nodemanager-hadoop02.out
hadoop04: starting nodemanager, logging to /opt/module/hadoop-2.7.2/logs/yarn-root-nodemanager-hadoop04.out
```
注意：YARN 需要在 hadoop03 服务器上启动，因为 resourcemanager 部署在 hadoop03 上。

## HBase解压
```bash
[root@hadoop02 software]# tar -zxvf hbase-1.3.1-bin.tar.gz -C /opt/module/
```

## HBase的配置文件
修改 hbase 对应的配置文件
1. conf/hbase-env.sh 修改内容
```
# 第27行
export JAVA_HOME=/opt/module/jdk1.8.0_144

# 下面这两行原本是打开的，用 # 将它们注释
#export HBASE_MASTER_OPTS="$HBASE_MASTER_OPTS -XX:PermSize=128m -XX:MaxPermSize=128m"
#export HBASE_REGIONSERVER_OPTS="$HBASE_REGIONSERVER_OPTS -XX:PermSize=128m -XX:MaxPermSize=128m"

# 第128行
export HBASE_MANAGES_ZK=false
```

2. conf/hbase-site.xml 修改内容
```xml
<configuration>
        <property>
            <name>hbase.rootdir</name>
            <value>hdfs://hadoop02:9000/HBase</value>
        </property>

        <property>
            <name>hbase.cluster.distributed</name>
            <value>true</value>
        </property>

        <!-- 0.98 后的新变动，之前版本没有.port,默认端口为 60000 -->
        <property>
            <name>hbase.master.port</name>
            <value>16000</value>
        </property>

        <property>
            <name>hbase.zookeeper.quorum</name>
            <value>hadoop02,hadoop03,hadoop04</value>
        </property>

        <property>
            <name>hbase.zookeeper.property.dataDir</name>
            <value>/opt/module/zookeeper-3.4.10/zkData</value>
        </property>
</configuration>
```

3. 修改 conf/regionservers
```
hadoop02
hadoop03
hadoop04
```

4. 软连接 hadoop 配置文件到 HBase：
```bash
[root@hadoop02 module]# ln -s /opt/module/hadoop-2.7.2/etc/hadoop/core-site.xml /opt/module/hbase-1.3.1/conf/core-site.xml
[root@hadoop02 module]# ln -s /opt/module/hadoop-2.7.2/etc/hadoop/hdfs-site.xml /opt/module/hbase-1.3.1/conf/hdfs-site.xml
```

5. 配置文件同步到其他集群
```bash
[root@hadoop02 hbase-1.3.1]# xsync conf/
```

## HBase服务的启动
1. 启动方式一：单节点启动
```bash
[root@hadoop02 hbase-1.3.1]# bin/hbase-daemon.sh start master
starting master, logging to /opt/module/hbase-1.3.1/bin/../logs/hbase-root-master-hadoop02.out
[root@hadoop02 hbase-1.3.1]# bin/hbase-daemon.sh start regionserver
starting regionserver, logging to /opt/module/hbase-1.3.1/bin/../logs/hbase-root-regionserver-hadoop02.out

[root@hadoop02 hbase-1.3.1]# jps
20084 HMaster
20340 HRegionServer
20424 Jps
19500 NodeManager
11037 QuorumPeerMain
19261 DataNode
19133 NameNode
```
可以看到服务正常启动。也可以访问 web 界面
```
http://hadoop02:16010/master-status
```
![web界面](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200612223259.png)

注意：如果集群之间的节点时间不同步，会导致 regionserver 无法启动，抛出 ClockOutOfSyncException 异常。解决办法是同步服务器的时间

2. 启动方式二：群起
```bash
[root@hadoop02 hbase-1.3.1]# bin/start-hbase.sh
```
对应的停止服务
```bash
[root@hadoop02 hbase-1.3.1]# bin/stop-hbase.sh
```