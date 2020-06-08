# Hadoop-完全分布式运行模式

## 环境准备
目前能以学生优惠购买的云服务器有：
* 腾讯云一台
* 阿里云一台
* 华为云一台
* 百度云一台

学生身份能免费领取的云服务器有：
* 阿里云抗疫特惠云服务器一台

因为腾讯云和华为云的服务器有其他用途，所以剩余的三台用来实现 Hadoop 完全分布式运行模式，勉强够用。

云服务器环境如下：
* CentOS / 7.3 x86_64 (64bit)
* Java 1.8.0_144
* Hadoop 2.7.2

## 编写集群分发脚本
想要实现通过一个脚本将指定文件循环复制到所有节点的相同目录下。
1. 在 /root 目录下创建 bin 目录，并在 bin 目录下创建文件 xsync
    ```bash
    [root@hadoop02 bin]# mdkir bin
    [root@hadoop02 bin]# cd bin/
    [root@hadoop02 bin]# touch xsync
    [root@hadoop02 bin]# vim xsync
    ```
2. 在文件中编写如下代码
    ```bash
    #!/bin/bash
    #1 获取输入参数个数，如果没有参数，直接退出
    pcount=$#
    if((pcount==0)); then
    echo no args;
    exit;
    fi

    #2 获取文件名称
    p1=$1
    fname=`basename $p1`
    echo fname=$fname

    #3 获取上级目录到绝对路径
    pdir=`cd -P $(dirname $p1); pwd`
    echo pdir=$pdir

    #4 获取当前用户名称
    user=`whoami`

    #5 循环
    for((host=3; host<5; host++)); do
        echo ------------------- hadoop$host --------------
        rsync -rvl $pdir/$fname $user@hadoop0$host:$pdir
    done
    ```
    注意：记得要把服务器地址和域名配置到 /etc/hosts 文件中

3. 修改 xsync 具有执行权限
    ```bash
    [root@hadoop02 bin]# chmod 755 xsync
    ```
4. 调用脚本测试：将 /root/bin 目录复制到其他节点
    ```bash
    [root@hadoop02 bin]# xsync /root/bin
    ```

## SSH 无密登录配置
无密登录原理

具体操作如下：
1. 生成公钥和私钥
    ```bash
    [root@hadoop02 .ssh]# ssh-keygen -t rsa
    ```
    然后敲（三个回车），就会生成两个文件 `id_rsa（私钥）`、 `id_rsa.pub（公钥）`

2. 将公钥拷贝到要免密登录的目标机器上
    ```bash
    [root@hadoop02 .ssh]# ssh-copy-id hadoop02
    [root@hadoop02 .ssh]# ssh-copy-id hadoop03
    [root@hadoop02 .ssh]# ssh-copy-id hadoop04
    ```
3. 测试一哈
    ```bash
    [root@hadoop02 .ssh]# ssh hadoop03
    ```
    无密登录的感觉是不是很爽哈哈。退出 ssh 用 exit 命令即可

注意了，还需要在 hadoop03 上采用 root 账号配置一下无密登录到 hadoop02、hadoop03、hadoop04 服务器上。为后面的集群群起做准备。

### .ssh 文件夹下（~/.ssh）的文件功能解释
| 文件名 | 功能 |
| -------- | -------- |
| known_hosts | 记录ssh访问过计算机的公钥（public key）|
| id_rsa | 生成的私钥 |
| id_rsa.pub | 生成的公钥 |
| authorized_keys | 存放授权过得无密登录服务器公钥 |


## 集群配置

### 集群规划部署
|  | hadoop02 | hadoop03 | hdoop04 |
| -------- | -------- | -------- | -------- |
| HDFS |  NameNode<br>DataNode | DataNode | SecondaryNameNode<br>DataNode |
| YARN | NodeManager | ResourceManager<br>NodeManager | NodeManager |

### 配置集群