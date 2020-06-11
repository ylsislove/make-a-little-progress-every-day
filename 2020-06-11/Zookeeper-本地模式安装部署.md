# Zookeeper-本地模式安装部署

## 环境
* CentOS / 7.3 x86_64 (64bit)
* Java 1.8.0_144

## 安装步骤
1. 下载地址：[官网首页](https://zookeeper.apache.org/)。这里我用的是 3.4.10
2. 使用 scp 命令或其他软件将安装包拷贝服务器上
3. 解压到指定目录
    ```bash
    [root@hadoop02 software]# tar -zxvf zookeeper-3.4.10.tar.gz -C /opt/module/
    ```

## 修改配置
1. 将 `/opt/module/zookeeper-3.4.10/conf` 这个路径下的 `zoo_sample.cfg` 修改为 `zoo.cfg`
    ```bash
    [root@hadoop02 conf]# mv zoo_sample.cfg zoo.cfg
    ```
2. 打开 `zoo.cfg` 文件，修改 `dataDir` 路径
    ```bash
    [root@hadoop02 conf]# vim zoo.cfg
    ```
    修改成如下内容
    ```
    dataDir=/opt/module/zookeeper-3.4.10/zkData
    ```
3. 在 `/opt/module/zookeeper-3.4.10/` 这个目录上创建 `zkData` 文件夹
    ```bash
    [root@hadoop02 zookeeper-3.4.10]# mkdir zkData
    ```

## 配置参数解读
Zookeeper 中的配置文件 zoo.cfg 中参数含义如下：
1. tickTime=2000：通信心跳数，Zookeeper 服务器与客户端心跳时间，单位毫秒

2. initLimit=10：LF初始通信时限<br>
集群中的 Follower 跟随者服务器与 Leader 领导者服务器之间初始连接时能容忍的最多心跳数（tickTime 的数量），用它来限定集群中的 Zookeeper 服务器连接到 Leader 的时限。

3. syncLimit=5：LF同步通信时限<br>
集群中 Leader 与 Follower 之间的最大响应时间单位，假如响应超过 syncLimit * tickTime，Leader 认为 Follwer 死掉，从服务器列表中删除 Follwer。

4. dataDir：数据文件目录+数据持久化路径<br>
主要用于保存 Zookeeper 中的数据。

5. clientPort =2181：客户端连接端口<br>
监听客户端连接的端口。



## 操作Zookeeper
1. 启动 Zookeeper
    ```bash
    [root@hadoop02 zookeeper-3.4.10]# bin/zkServer.sh start
    ```
2. 查看进程是否启动
    ```bash
    [root@hadoop02 zookeeper-3.4.10]# jps
    10186 QuorumPeerMain
    10203 Jps
    ```
3. 查看状态
    ```bash
    [root@hadoop02 zookeeper-3.4.10]# bin/zkServer.sh status
    ZooKeeper JMX enabled by default
    Using config: /opt/module/zookeeper-3.4.10/bin/../conf/zoo.cfg
    Mode: standalone
    ```
    可以看到是单机模式
4. 启动客户端
    ```bash
    [root@hadoop02 zookeeper-3.4.10]# bin/zkCli.sh
    ```
5. 退出客户端
    ```
    [zk: localhost:2181(CONNECTED) 4] quit
    ```
6. 停止 Zookeeper 
    ```bash
    [root@hadoop02 zookeeper-3.4.10]# bin/zkServer.sh stop
    ```