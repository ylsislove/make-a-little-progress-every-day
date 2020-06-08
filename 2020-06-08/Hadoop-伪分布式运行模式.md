# Hadoop-伪分布式运行模式

  - [配置集群](#%E9%85%8D%E7%BD%AE%E9%9B%86%E7%BE%A4)
  - [启动集群](#%E5%90%AF%E5%8A%A8%E9%9B%86%E7%BE%A4)
  - [查看集群](#%E6%9F%A5%E7%9C%8B%E9%9B%86%E7%BE%A4)
  - [操作集群](#%E6%93%8D%E4%BD%9C%E9%9B%86%E7%BE%A4)
  - [注意事项](#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)

## 配置集群

1. 配置：`etc/hadoop/hadoop-env.sh`。修改 JAVA_HOME 路径
    ```bash
    export JAVA_HOME=/opt/module/jdk1.8.0_144
    ```

2. 配置：`etc/hadoop/core-site.xml`
    ```xml
    <!-- 指定HDFS中NameNode的地址 -->
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>

    <!-- 指定Hadoop运行时产生文件的存储目录 -->
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/opt/module/hadoop-2.7.2/data/tmp</value>
    </property>
    ```

3. 配置：`etc/hadoop/hdfs-site.xml`
    ```xml
    <!-- 指定HDFS副本的数量 -->
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    ```

## 启动集群
1. 格式化 NameNode（第一次启动时格式化，以后就不要总格式化）
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hdfs namenode -format
    ```
2. 启动 NameNode
    ```bash
    [root@hadoop02 hadoop-2.7.2]# sbin/hadoop-daemon.sh start namenode
    ```
3. 启动 DataNode
    ```bash
    [root@hadoop02 hadoop-2.7.2]# sbin/hadoop-daemon.sh start datanode
    ```

## 查看集群
1. 查看是否启动成功
    ```bash
    [root@hadoop02 hadoop-2.7.2]# jps
    12080 DataNode
    11976 NameNode
    12152 Jps
    ```
    注意：jps 是 JDK 中的命令，不是 Linux 命令。不安装 JDK 不能使用 jps

2. Web 端查看 HDFS 文件系统
    ```
    http://hadoop02:50070/dfshealth.html#tab-overview
    ```
    注意：记得开放服务器相关端口
3. 查看产生的 Log 日志。查看 Log 日志是排除的重要手段
    ```
    [root@hadoop02 hadoop-2.7.2]# ll logs/
    total 92
    -rw-r--r-- 1 root root 23736 Jun  8 23:04 hadoop-root-datanode-hadoop02.log
    -rw-r--r-- 1 root root   715 Jun  8 23:04 hadoop-root-datanode-hadoop02.out
    -rw-r--r-- 1 root root 56186 Jun  8 23:04 hadoop-root-namenode-hadoop02.log
    -rw-r--r-- 1 root root   715 Jun  8 23:01 hadoop-root-namenode-hadoop02.out
    -rw-r--r-- 1 root root   715 Jun  8 22:58 hadoop-root-namenode-hadoop02.out.1
    -rw-r--r-- 1 root root     0 Jun  8 22:58 SecurityAuth-root.audit
    ```

## 操作集群
1. 在 HDFS 文件系统上创建一个 input 文件夹
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hdfs dfs -mkdir -p /user/yain/input
    ```
2. 将测试文件内容上传到文件系统上。wcinput/wc.input是一个文本文件，里面随便放一些单词即可，用来测试 WordCount 程序
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hdfs dfs -put wcinput/wc.input /user/yain/input
    ```
3. 查看上传的文件是否正确
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hdfs dfs -ls /user/yain/input
    Found 1 items
    -rw-r--r--   1 root supergroup         79 2020-06-08 23:31 /user/yain/input/wc.input

    [root@hadoop02 hadoop-2.7.2]# bin/hdfs dfs -cat /user/yain/input/wc.input
    ```
    注意：也可以在 Web 端看到刚刚上传的文件

4. 运行 MapReduce 程序
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount /user/yain/input /user/yain/output
    ```
5. 查看输出结果
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hdfs dfs -cat /user/yain/output/p*
    ```
6. 将测试文件下载到本地
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hdfs dfs -get /user/yain/output/part-r-00000 ./wcoutput/
    ```
7. 删除输出结果
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hdfs dfs -rm -r /user/yain/output
    ```

## 注意事项
1. 为什么不能一直格式化 NameNode，格式化 NameNode 要注意什么？
    ```bash
    [root@hadoop02 hadoop-2.7.2]# cat data/tmp/dfs/name/current/VERSION
    clusterID=CID-525d4809-c836-48f3-bf25-8fa1583d2393

    [root@hadoop02 hadoop-2.7.2]# cat data/tmp/dfs/data/current/VERSION
    clusterID=CID-525d4809-c836-48f3-bf25-8fa1583d2393
    ```
    格式化 NameNode，会产生新的集群 id,导致 NameNode 和DataNode 的集群 id 不一致，集群找不到已往数据。所以，格式 NameNode 时，首先 jps 查看进程是否已经关闭，然后一定要先删除 data 数据和 log 日志，然后再格式化 NameNode。