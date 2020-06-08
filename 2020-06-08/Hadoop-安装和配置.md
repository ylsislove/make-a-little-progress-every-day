# Hadoop-安装和配置

  - [环境](#%E7%8E%AF%E5%A2%83)
  - [安装 Hadoop](#%E5%AE%89%E8%A3%85-hadoop)
  - [Hadoop 的目录结构](#hadoop-%E7%9A%84%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84)

## 环境
* CentOS / 7.3 x86_64 (64bit)
* Java 1.8.0_144

## 安装 Hadoop
1. 下载地址[https://archive.apache.org/dist/hadoop/common/hadoop-2.7.2/](https://archive.apache.org/dist/hadoop/common/hadoop-2.7.2/)
2. 使用 scp 命令或其他传输工具将 hadoop-2.7.2.tar.gz 上传至服务器的 /opt/software 目录下
3. 进入到 Hadoop 安装包目录下
    ```bash
    cd /opt/software/
    ```
4. 解压安装文件到 /opt/module 目录下（没有这个目录可以事先创建）
    ```bash
    [root@hadoop02 software]# tar -zxvf hadoop-2.7.2.tar.gz -C /opt/module/
    ```
5. 查看解压是否成功
    ```bash
    [root@hadoop02 ~]# ls /opt/module/
    hadoop-2.7.2  jdk1.8.0_144
    ```
6. 将 Hadoop 添加进环境变量
    1. 打开 /etc/profile 文件
        ```bash
        [root@hadoop02 ~]# vim /etc/profile
        ```
    2. 在 profile 文件末尾添加 Hadoop 路径（shift + g）
        ```bash
        # HADOOP_HOME
        export HADOOP_HOME=/opt/module/hadoop-2.7.2
        export PATH=$PATH:$HADOOP_HOME/bin
        export PATH=$PATH:$HADOOP_HOME/sbin
        ```
    3. 让修改后的文件生效
        ```bash
        [root@hadoop02 ~]# source /etc/profile
        ```
    4. 查看 Hadoop 版本
        ```bash
        [root@hadoop02 ~]# hadoop version
        Hadoop 2.7.2
        ```

## Hadoop 的目录结构
```bash
[root@hadoop02 hadoop-2.7.2]# ll
total 76
drwxr-xr-x 2 root root  4096 Apr 15 03:04 bin
drwxr-xr-x 3 root root  4096 Apr 15 03:04 data
drwxr-xr-x 3 root root  4096 Apr 15 03:04 etc
drwxr-xr-x 2 root root  4096 Apr 15 03:04 include
drwxr-xr-x 2 root root  4096 Apr 15 03:25 input
drwxr-xr-x 3 root root  4096 Apr 15 03:25 lib
drwxr-xr-x 2 root root  4096 Apr 15 03:25 libexec
-rw-r--r-- 1 root root 15429 Apr 15 03:04 LICENSE.txt
drwxr-xr-x 3 root root  4096 Apr 15 03:04 logs
-rw-r--r-- 1 root root   101 Apr 15 03:25 NOTICE.txt
drwxr-xr-x 2 root root  4096 Apr 15 03:25 output
-rw-r--r-- 1 root root  1366 Apr 15 03:25 README.txt
drwxr-xr-x 2 root root  4096 Apr 15 03:25 sbin
drwxr-xr-x 4 root root  4096 Apr 15 03:04 share
drwxr-xr-x 2 root root  4096 Apr 15 03:25 wcinput
drwxr-xr-x 2 root root  4096 Apr 15 03:04 wcoutput
```
其中有些目录，像 data、wcinput、wcoutput 是运行起来后一些操作生成的，不用管它。

重要目录有以下几个：
* bin 目录：存放对 Hadoop 相关服务（HDFS,YARN）进行操作的脚本
* etc 目录：Hadoop 的配置文件目录，存放 Hadoop 的配置文件
* lib 目录：存放 Hadoop 的本地库（对数据进行压缩解压缩功能）
* sbin 目录：存放启动或停止 Hadoop 相关服务的脚本
* share 目录：存放 Hadoop 的依赖 jar 包、文档、和官方案例
