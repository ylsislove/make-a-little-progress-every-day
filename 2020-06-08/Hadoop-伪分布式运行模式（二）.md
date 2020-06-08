# Hadoop-伪分布式运行模式（二）

  - [配置集群](#%E9%85%8D%E7%BD%AE%E9%9B%86%E7%BE%A4)
  - [启动集群](#%E5%90%AF%E5%8A%A8%E9%9B%86%E7%BE%A4)
  - [集群操作](#%E9%9B%86%E7%BE%A4%E6%93%8D%E4%BD%9C)

上一篇总结了启动 HDFS 并运行 MapReduce 程序。这一篇主要记录启动 YARN 并运行 MapReduce 程序

## 配置集群

1. 配置：`etc/hadoop/yarn-env.sh`。配置 JAVA_HOME 路径
    ```bash
    export JAVA_HOME=/opt/module/jdk1.8.0_144
    ```
2. 配置：`etc/hadoop/yarn-site.xml`
    ```xml
    <!-- Reducer获取数据的方式 -->
    <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
    </property>

    <!-- 指定YARN的ResourceManager的地址 -->
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>0.0.0.0</value>
    </property>
    ```
3. 配置：`etc/hadoop/mapred-env.sh`。配置 JAVA_HOME 路径
    ```bash
    export JAVA_HOME=/opt/module/jdk1.8.0_144
    ```
4. 配置：`etc/hadoop/mapred-site.xml`。这个文件是对 `mapred-site.xml.template` 重命名得到的
    ```xml
    <!-- 指定MR运行在YARN上 -->
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    ```

## 启动集群
1. 启动之前必须保证 NameNode 和 DataNode 已经启动
2. 启动 ResourceManager
    ```bash
    [root@hadoop02 hadoop-2.7.2]# sbin/yarn-daemon.sh start resourcemanager
    ```
3. 启动 NodeManager
    ```bash
    [root@hadoop02 hadoop-2.7.2]# sbin/yarn-daemon.sh start nodemanager
    ```
4. 查看集群是否启动成功
    ```bash
    [root@hadoop02 hadoop-2.7.2]# jps
    12080 DataNode
    13170 NodeManager
    13285 Jps
    12919 ResourceManager
    11976 NameNode
    ```

## 集群操作
1. 在 Web 浏览器查看集群。注意，和 50070 那个端口是不一样的，这个是专门查看 MapReduce 程序运行状况的。记得在服务器上开放 8088 端口
    ```
    http://hadoop02:8088/cluster
    ```
2. 删除文件系统上的 output 文件夹，如果有的话。
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hdfs dfs -rm -r /user/yain/output
    ```
3. 执行 MapReduce 程序
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount /user/yain/input /user/yain/output
    ```
4. 查看执行成功
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hdfs dfs -cat /user/yain/output/p*
    ```
    ![http://hadoop02:50070/explorer.html#/user/yain/output](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200609004054.png)

    ![http://hadoop02:8088/cluster](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200609004438.png)
