# HBase-API操作之与MR交互（一）

  - [准备工作](#%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C)
  - [官方案例一：统计 Student 表中有多少行数据](#%E5%AE%98%E6%96%B9%E6%A1%88%E4%BE%8B%E4%B8%80%E7%BB%9F%E8%AE%A1-student-%E8%A1%A8%E4%B8%AD%E6%9C%89%E5%A4%9A%E5%B0%91%E8%A1%8C%E6%95%B0%E6%8D%AE)
  - [官方案例二：使用 MapReduce 将本地数据导入到 HBase](#%E5%AE%98%E6%96%B9%E6%A1%88%E4%BE%8B%E4%BA%8C%E4%BD%BF%E7%94%A8-mapreduce-%E5%B0%86%E6%9C%AC%E5%9C%B0%E6%95%B0%E6%8D%AE%E5%AF%BC%E5%85%A5%E5%88%B0-hbase)

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


## 官方案例二：使用 MapReduce 将本地数据导入到 HBase

1. 在本地创建一个 tsv 格式的文件：fruit.tsv。分隔符必须是 `\t`
    ```
    1001    Apple   Red 
    1002    Pear    Yellow 
    1003    Pineapple       Yellow
    ```

2. 将文件上传到 hdfs 里
    ```bash
    [root@hadoop02 hbase-1.3.1]# hadoop fs -put fruit.tsv /
    ```

3. 创建 Hbase 表
    ```
    hbase(main):002:0> create 'fruit','info'
    ```

4. 执行 MapReduce 命令，将 fruit.tsv 文件导入到 HBase 的 fruit 表中
    ```bash
    /opt/module/hadoop-2.7.2/bin/yarn jar lib/hbase-server-1.3.1.jar importtsv -Dimporttsv.columns=HBASE_ROW_KEY,info:name,info:color fruit hdfs://hadoop02:9000/fruit.tsv
    ```

5. 运行结果
![运行结果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200615182153.png)
![运行结果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200615182311.png)

