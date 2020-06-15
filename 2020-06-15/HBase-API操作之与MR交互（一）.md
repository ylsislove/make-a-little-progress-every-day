# HBase-API操作之与MR交互（一）

## 准备工作
1. 查看 HBase 的 MapReduce 任务执行时的 ClassPath
    ```bash
    [root@hadoop02 hbase-1.3.1]# hbase mapredcp
    SLF4J: Class path contains multiple SLF4J bindings.
    SLF4J: Found binding in [jar:file:/opt/module/hbase-1.3.1/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: Found binding in [jar:file:/opt/module/hadoop-2.7.2/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
    SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
    /opt/module/hbase-1.3.1/lib/zookeeper-3.4.6.jar:/opt/module/hbase-1.3.1/lib/guava-12.0.1.jar:/opt/module/hbase-1.3.1/lib/metrics-core-2.2.0.jar:/opt/module/hbase-1.3.1/lib/protobuf-java-2.5.0.jar:/opt/module/hbase-1.3.1/lib/hbase-common-1.3.1.jar:/opt/module/hbase-1.3.1/lib/hbase-protocol-1.3.1.jar:/opt/module/hbase-1.3.1/lib/htrace-core-3.1.0-incubating.jar:/opt/module/hbase-1.3.1/lib/hbase-client-1.3.1.jar:/opt/module/hbase-1.3.1/lib/hbase-hadoop-compat-1.3.1.jar:/opt/module/hbase-1.3.1/lib/netty-all-4.0.23.Final.jar:/opt/module/hbase-1.3.1/lib/hbase-server-1.3.1.jar:/opt/module/hbase-1.3.1/lib/hbase-prefix-tree-1.3.1.jar
    ```
2. 在环境变量中进行配置
    1. 在 /etc/profile 中要配置如下语句
        ```
        # HBASE_HOME
        export HBASE_HOME=/opt/module/hbase-1.3.1
        
        # HADOOP_HOME
        export HADOOP_HOME=/opt/module/hadoop-2.7.2
        ```
    2. 在 hadoop-env.sh 中配置 `hbase mapredcp` 命令所打印出来的 ClassPath。注意在 for 循环之后配置，保证不破坏原本的 ClassPath
        ```
        export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:/opt/module/hbase-1.3.1/lib/zookeeper-3.4.6.jar:/opt/module/hbase-1.3.1/lib/guava-12.0.1.jar:/opt/module/hbase-1.3.1/lib/metrics-core-2.2.0.jar:/opt/module/hbase-1.3.1/lib/protobuf-java-2.5.0.jar:/opt/module/hbase-1.3.1/lib/hbase-common-1.3.1.jar:/opt/module/hbase-1.3.1/lib/hbase-protocol-1.3.1.jar:/opt/module/hbase-1.3.1/lib/htrace-core-3.1.0-incubating.jar:/opt/module/hbase-1.3.1/lib/hbase-client-1.3.1.jar:/opt/module/hbase-1.3.1/lib/hbase-hadoop-compat-1.3.1.jar:/opt/module/hbase-1.3.1/lib/netty-all-4.0.23.Final.jar:/opt/module/hbase-1.3.1/lib/hbase-server-1.3.1.jar:/opt/module/hbase-1.3.1/lib/hbase-prefix-tree-1.3.1.jar
        ```
    3. 分发到其他集群
        ```bash
        [root@hadoop02 hbase-1.3.1]# xsync /opt/module/hadoop-2.7.2/etc/hadoop/hadoop-env.sh
        ```
    4. 重启 hbase，hadoop 服务
        ```bash
        [root@hadoop02 hbase-1.3.1]# stop-hbase.sh
        # 注意 YARN 要在部署了 ResourceManager 的机器上启动和关闭
        [root@hadoop03 hbase-1.3.1]# stop-yarn.sh
        [root@hadoop02 hbase-1.3.1]# stop-dfs.sh

        [root@hadoop02 hbase-1.3.1]# start-dfs.sh
        # 注意 YARN 要在部署了 ResourceManager 的机器上启动和关闭
        [root@hadoop03 hbase-1.3.1]# start-yarn.sh
        # 等待半分钟，等待 hadoop 退出安全模式了在启动 hbase。安全模式状态可在 hadoop 的 web 端查看
        [root@hadoop02 hbase-1.3.1]# start-hbase.sh
        ```
    5. 查看服务是否正常启动
        ```bash
        [root@hadoop02 hbase-1.3.1]# jps
        ```

## 官方案例一：统计 Student 表中有多少行数据

运行命令
```bash
[root@hadoop02 hbase-1.3.1]# /opt/module/hadoop-2.7.2/bin/yarn jar lib/hbase-server-1.3.1.jar rowcounter student
```

运行结果
![运行结果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200615020701.png)

