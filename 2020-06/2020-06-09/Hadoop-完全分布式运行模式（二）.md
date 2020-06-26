# Hadoop-完全分布式运行模式（二）

  - [集群基本测试](#%E9%9B%86%E7%BE%A4%E5%9F%BA%E6%9C%AC%E6%B5%8B%E8%AF%95)
  - [集群启动 / 停止方式总结](#%E9%9B%86%E7%BE%A4%E5%90%AF%E5%8A%A8--%E5%81%9C%E6%AD%A2%E6%96%B9%E5%BC%8F%E6%80%BB%E7%BB%93)


## 集群基本测试
1. 上传小文件到集群
    ```bash
    [root@hadoop02 hadoop-2.7.2]# hdfs dfs -put wcinput/wc.input /
    ```
2. 上传大文件到集群
    ```bash
    [root@hadoop02 hadoop-2.7.2]# hdfs dfs -put /opt/software/hadoop-2.7.2.tar.gz /
    ```
    ![上传结果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200609222116.png)
3. 查看文件存放的位置
    ```bash
    [root@hadoop02 subdir0]# pwd
    /opt/module/hadoop-2.7.2/data/tmp/dfs/data/current/BP-56315598-123.56.156.127-1591685988349/current/finalized/subdir0/subdir0
    [root@hadoop02 subdir0]# ll
    total 194552
    -rw-r--r-- 1 root root        79 Jun  9 22:15 blk_1073741825
    -rw-r--r-- 1 root root        11 Jun  9 22:15 blk_1073741825_1001.meta
    -rw-r--r-- 1 root root 134217728 Jun  9 22:17 blk_1073741826
    -rw-r--r-- 1 root root   1048583 Jun  9 22:17 blk_1073741826_1002.meta
    -rw-r--r-- 1 root root  63439959 Jun  9 22:17 blk_1073741827
    -rw-r--r-- 1 root root    495635 Jun  9 22:17 blk_1073741827_1003.meta
    ```

## 集群启动 / 停止方式总结
1. 各个服务组件逐一启动 / 停止
    ```bash
    # 分别启动 / 停止HDFS组件
    hadoop-daemon.sh  start / stop  namenode / datanode / secondarynamenode

    # 分别启动 / 停止YARN
    yarn-daemon.sh  start / stop  resourcemanager / nodemanager
    ```
2. 各个模块分开启动 / 停止（前提是 ssh 要配置好） 常用
    ```bash
    # 整体启动 / 停止HDFS
    start-dfs.sh / stop-dfs.sh

    # 整体启动 / 停止YARN
    start-yarn.sh / stop-yarn.sh
    ```
