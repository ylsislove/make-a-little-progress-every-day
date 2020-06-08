# Hadoop-伪分布式运行模式（三）

昨天总结了如何启动 YAIN 并运行 MapReduce 程序。这一篇主要总结如何配置历史服务器和日志的聚集。

## 配置历史服务器
为了查看程序的历史运行情况，需要配置一下历史服务器。具体配置步骤如下
1. 配置：`etc/hadoop/mapred-site.xml`。在文件里增加如下配置
    ```xml
    <!-- 历史服务器端地址 -->
    <property>
        <name>mapreduce.jobhistory.address</name>
        <value>0.0.0.0:10020</value>
    </property>

    <!-- 历史服务器web端地址 -->
    <property>
        <name>mapreduce.jobhistory.webapp.address</name>
        <value>0.0.0.0:19888</value>
    </property>
    ```
2. 启动历史服务器
    ```bash
    [root@hadoop02 hadoop-2.7.2]# sbin/mr-jobhistory-daemon.sh start historyserver
    ```
3. 查看历史服务器是否启动成功
    ```bash
    [root@hadoop02 hadoop-2.7.2]# jps
    12080 DataNode
    13873 JobHistoryServer
    13170 NodeManager
    13906 Jps
    12919 ResourceManager
    11976 NameNode
    ```
4. Web 端查看。记得开放 19888 端口
    ```
    http://hadoop02:19888/jobhistory
    ```
    ![http://hadoop02:19888/jobhistory](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200609005636.png)

## 配置日志聚集
日志聚集概念：应用运行完成以后，将程序运行日志信息上传到HDFS系统上。

日志聚集功能好处：可以方便的查看到程序运行详情，方便开发调试。

注意：开启日志聚集功能，需要重新启动 NodeManager、ResourceManager 和 HistoryManager。
1. 配置：`etc/hadoop/yarn-site.xml`。在该文件里增加如下配置
    ```xml
    <!-- 日志聚集功能使能 -->
    <property>
        <name>yarn.log-aggregation-enable</name>
        <value>true</value>
    </property>

    <!-- 日志保留时间设置7天 -->
    <property>
        <name>yarn.log-aggregation.retain-seconds</name>
        <value>604800</value>
    </property>
    ```
2. 关闭 NodeManager 、ResourceManager 和 HistoryManager
    ```bash
    [root@hadoop02 hadoop-2.7.2]# sbin/yarn-daemon.sh stop resourcemanager
    [root@hadoop02 hadoop-2.7.2]# sbin/yarn-daemon.sh stop nodemanager
    [root@hadoop02 hadoop-2.7.2]# sbin/mr-jobhistory-daemon.sh stop historyserver
    ```
3. 启动 NodeManager 、ResourceManager 和 HistoryManager
    ```bash
    [root@hadoop02 hadoop-2.7.2]# sbin/yarn-daemon.sh start resourcemanager
    [root@hadoop02 hadoop-2.7.2]# sbin/yarn-daemon.sh start nodemanager
    [root@hadoop02 hadoop-2.7.2]# sbin/mr-jobhistory-daemon.sh start historyserver
    ```
4. 删除 HDFS 上已经存在的输出文件，如果有的话
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hdfs dfs -rm -r /user/yain/output
    ```
5. 执行 WordCount 程序
    ```bash
    [root@hadoop02 hadoop-2.7.2]# bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount /user/yain/input /user/yain/output
    ```
6. 查看日志
    ```
    http://hadoop02:19888/jobhistory
    ```
    ![总览](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200609013002.png)

    ![详情一](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200609013100.png)

    ![详情二](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200609013145.png)


## 配置文件说明
Hadoop 配置文件分两类：默认配置文件和自定义配置文件，只有用户想修改某一默认配置值时，才需要修改自定义配置文件，更改相应属性值。

1. 默认配置文件：

    | 要获取的默认文件 | 文件存放在Hadoop的jar包中的位置 |
    | -------- | -------- |
    | [core-default.xml] | hadoop-common-2.7.2.jar/ core-default.xml   |
    | [hdfs-default.xml] | hadoop-hdfs-2.7.2.jar/ hdfs-default.xml   |
    | [yarn-default.xml] | hadoop-yarn-common-2.7.2.jar/ yarn-default.xml |
    | [mapred-default.xml] | hadoop-mapreduce-client-core-2.7.2.jar/ mapred-default.xml |

2. 自定义配置文件

    core-site.xml、hdfs-site.xml、yarn-site.xml、mapred-site.xml 四个配置文件存放在 `$HADOOP_HOME/etc/hadoop` 这个路径上，用户可以根据项目需求重新进行修改配置。