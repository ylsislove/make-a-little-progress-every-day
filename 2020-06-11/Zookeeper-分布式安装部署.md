# Zookeeper-分布式安装部署

  - [集群规划](#%E9%9B%86%E7%BE%A4%E8%A7%84%E5%88%92)
  - [安装和部署](#%E5%AE%89%E8%A3%85%E5%92%8C%E9%83%A8%E7%BD%B2)
  - [配置参数解读](#%E9%85%8D%E7%BD%AE%E5%8F%82%E6%95%B0%E8%A7%A3%E8%AF%BB)
  - [集群操作](#%E9%9B%86%E7%BE%A4%E6%93%8D%E4%BD%9C)

## 集群规划
在之前部署过分布式 Hadoop 的服务器上继续部署 Zookeeper。完全分布式部署 Hadoop 详情可看 [Hadoop-完全分布式运行模式（一）](../2020-06-09/Hadoop-完全分布式运行模式（一）.md)。

在 hadoop02、hadoop03、hadoop04 三个节点上分布式部署 Zookeeper。

## 安装和部署
1. 解压 Zookeeper 安装包到 /opt/module/ 目录下
    ```bash
    [root@hadoop02 software]# tar -zxvf zookeeper-3.4.10.tar.gz -C /opt/module/
    ```
2. 同步 /opt/module/zookeeper-3.4.10 目录内容到 hadoop03、hadoop04 上。同步工具在之前的文章 [Hadoop-完全分布式运行模式（一）](../2020-06-09/Hadoop-完全分布式运行模式（一）.md) 已经介绍过了。
    ```bash
    [root@hadoop02 module]# xsync zookeeper-3.4.10/
    ```
3. 在 /opt/module/zookeeper-3.4.10/ 这个目录下创建 zkData
    ```bash
    [root@hadoop02 zookeeper-3.4.10]# mkdir zkData
    ```
4. 在 /opt/module/zookeeper-3.4.10/zkData 目录下创建一个 myid 的文件
    ```bash
    [root@hadoop02 zkData]# touch myid
    ```
5. 编辑 myid 文件。在文件中添加与 server 对应的编号。除了编号不要有其他的内容
    ```bash
    [root@hadoop02 zkData]# vim myid
    ```
    ```
    2
    ```
6. 将配置好的文件拷贝到其他服务器上。注意：在 hadoop03 和 hadoop04 上修改 myid 文件中的内容为 3 和 4
    ```bash
    [root@hadoop02 zookeeper-3.4.10]# xsync zkData/
    ```
注意：在 hadoop03 和 hadoop04 上修改 myid 文件中的内容为 3 和 4

7. 将 `/opt/module/zookeeper-3.4.10/conf` 这个路径下的 `zoo_sample.cfg` 修改为 `zoo.cfg`
    ```bash
    [root@hadoop02 conf]# mv zoo_sample.cfg zoo.cfg
    ```
8. 打开 zoo.cfg 文件。修改数据存储路径，并增加如下配置
    ```
    # 修改数据存储路径
    dataDir=/opt/module/zookeeper-3.4.10/zkData

    # 增加如下配置
    #######################cluster##########################
    server.2=hadoop02:2888:3888
    server.3=hadoop03:2888:3888
    server.4=hadoop04:2888:3888
    ```
9. 同步 zoo.cfg 配置文件
    ```bash
    [root@hadoop02 conf]# xsync zoo.cfg
    ```

## 配置参数解读
在 zoo.cfg 文件中，在最后添加了集群信息，形式为 `server.A=B:C:D`。ABCD 的含义如下：

A 是一个数字，表示这个是第几号服务器；集群模式下配置一个文件 myid，这个文件在 dataDir 目录下，这个文件里面有一个数据就是 A 的值，Zookeeper 启动时读取此文件，拿到里面的数据与 zoo.cfg 里面的配置信息比较从而判断到底是哪个 server。

B 是这个服务器的 ip 地址

C 是这个服务器与集群中的 Leader 服务器交换信息的端口

D 是万一集群中的 Leader 服务器挂了，需要一个端口来重新进行选举，选出一个新的 Leader，而这个端口就是用来执行选举时服务器相互通信的端口

## 集群操作
1. 分别启动 Zookeeper
    ```bash
    [root@hadoop02 zookeeper-3.4.10]# zkServer.sh start
    [root@hadoop03 zookeeper-3.4.10]# zkServer.sh start
    [root@hadoop04 zookeeper-3.4.10]# zkServer.sh start
    ```
2. 查看状态
    ```bash
    [root@hadoop02 zookeeper-3.4.10]# zkServer.sh status
    ZooKeeper JMX enabled by default
    Using config: /opt/module/zookeeper-3.4.10/bin/../conf/zoo.cfg
    Mode: follower

    [root@hadoop03 zookeeper-3.4.10]# zkServer.sh status
    ZooKeeper JMX enabled by default
    Using config: /opt/module/zookeeper-3.4.10/bin/../conf/zoo.cfg
    Mode: leader

    [root@hadoop04 zookeeper-3.4.10]# zkServer.sh status
    ZooKeeper JMX enabled by default
    Using config: /opt/module/zookeeper-3.4.10/bin/../conf/zoo.cfg
    Mode: follower
    ```
    可以看到我们第二个启动 zookeeper 的服务器 hadoop03 称为了 leader。这个就是 zookeeper的选举机制。