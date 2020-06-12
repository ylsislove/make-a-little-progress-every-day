# Zookeeper-客户端命令行操作

  - [基本命令](#%E5%9F%BA%E6%9C%AC%E5%91%BD%E4%BB%A4)
  - [实战演练](#%E5%AE%9E%E6%88%98%E6%BC%94%E7%BB%83)

## 基本命令
| 命令基本语法 | 功能描述 |
| - | - |
| help | 显示所有操作命令 |
| ls path [watch] | 使用ls命令来查看当前znode中所包含的内容 |
| ls2 path [watch] | 查看当前节点数据并能看到更新次数等数据 |
| create | 普通创建<br>-s 包含序列<br>-e 临时节点（重启或超时就消失） |
| get path [watch] | 获得节点的值 |
| set | 设置节点的具体值 |
| stat | 查看节点状态 |
| delete | 删除节点 |
| rmr | 递归删除节点 |


## 实战演练
1. 启动客户端
```
[root@hadoop02 ~]# zkCli.sh
```
2. 显示所有操作命令
```
[zk: localhost:2181(CONNECTED) 1] help
ZooKeeper -server host:port cmd args
        stat path [watch]
        set path data [version]
        ls path [watch]
        delquota [-n|-b] path
        ls2 path [watch]
        setAcl path acl
        setquota -n|-b val path
        history 
        redo cmdno
        printwatches on|off
        delete path [version]
        sync path
        listquota path
        rmr path
        get path [watch]
        create [-s] [-e] path data acl
        addauth scheme auth
        quit 
        getAcl path
        close 
        connect host:port
```
3. 查看当前znode中所包含的内容
```
[zk: localhost:2181(CONNECTED) 2] ls /
[zookeeper]
```
4. 查看当前节点的详细数据
```
[zk: localhost:2181(CONNECTED) 3] ls2 /
[zookeeper]
cZxid = 0x0
ctime = Thu Jan 01 08:00:00 CST 1970
mZxid = 0x0
mtime = Thu Jan 01 08:00:00 CST 1970
pZxid = 0x0
cversion = -1
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 0
numChildren = 1
```
5. 分别创建两个普通节点
```
[zk: localhost:2181(CONNECTED) 4] create /servers "servers"
Created /servers
[zk: localhost:2181(CONNECTED) 5] create /servers/server01 "hadoop02"
Created /servers/server01
```
6. 获得节点的值
```
[zk: localhost:2181(CONNECTED) 7] get /servers/server01
hadoop02
cZxid = 0x100000003
ctime = Fri Jun 12 20:21:35 CST 2020
mZxid = 0x100000003
mtime = Fri Jun 12 20:21:35 CST 2020
pZxid = 0x100000003
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 8
numChildren = 0
```
7. 创建短暂节点
    1. 创建
    ```
    [zk: localhost:2181(CONNECTED) 8] create -e /servers/server02 "hadoop03"
    Created /servers/server02
    ```    
    2. 在当前客户端可以查看到
    ```
    [zk: localhost:2181(CONNECTED) 9] ls /servers
    [server02, server01]
    ```
    3. 退出当前客户端然后再重启客户端
    ```
    [zk: localhost:2181(CONNECTED) 10] quit
    [root@hadoop02 ~]# zkCli.sh
    ```
    4. 再次查看根目录下短暂节点已经删除
    ```
    [zk: localhost:2181(CONNECTED) 0] ls /servers
    [server01]
    ```
8. 创建带序号的节点
```
[zk: localhost:2181(CONNECTED) 0] ls /servers
[server01]
[zk: localhost:2181(CONNECTED) 1] create -s /servers/server02 "hadoop03"
Created /servers/server020000000002
[zk: localhost:2181(CONNECTED) 2] create -s /servers/server03 "hadoop04"
Created /servers/server030000000003
[zk: localhost:2181(CONNECTED) 3] ls /servers
[server020000000002, server01, server030000000003]
```
如果原来没有序号节点，则序号从0开始依次递增。如果原节点下已经有2个节点，则再排序时从2开始，依次类推。

9. 修改节点数据值
```
[zk: localhost:2181(CONNECTED) 4] set /servers/server01 "hadoop01"
cZxid = 0x100000003
ctime = Fri Jun 12 20:21:35 CST 2020
mZxid = 0x10000000a
mtime = Fri Jun 12 20:33:55 CST 2020
pZxid = 0x100000003
cversion = 0
dataVersion = 1
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 8
numChildren = 0
```
10. 监听节点的值变化
    1. 在 hadoop02 主机上注册监听 /servers 节点数据变化
    ```
    [zk: localhost:2181(CONNECTED) 8] get /servers watch
    ```
    2. 在 hadoop03 主机上修改 /servers 节点的数据
    ```
    [zk: localhost:2181(CONNECTED) 5] set /servers "update"
    ```
    3. 观察 hadoop02 主机上收到数据变化的监听
    ```
    [zk: localhost:2181(CONNECTED) 9] 
    WATCHER::

    WatchedEvent state:SyncConnected type:NodeDataChanged path:/servers
    ```
    注意，监听数据变化的命令是一次性的，监听到之后，命令便失效了。

11. 节点的子节点变化监听（路径变化）
    1. 在 hadoop03 主机上注册监听 /servers 节点的子节点变化
    ```
    [zk: localhost:2181(CONNECTED) 8] ls /servers watch
    ```
    2. 在 hadoop02 主机 /servers 节点上创建子节点
    ```
    [zk: localhost:2181(CONNECTED) 9] create /servers/server04 "test"
    ```
    3. 观察 hadoop03 主机上收到子节点变化的监听
    ```
    [zk: localhost:2181(CONNECTED) 9] 
    WATCHER::

    WatchedEvent state:SyncConnected type:NodeChildrenChanged path:/servers
    ```
    同样，监听命令是一次性的，监听到之后，命令便失效了。

12. 删除节点
```
[zk: localhost:2181(CONNECTED) 10] delete /servers/server04
```
13. 递归删除节点
```
[zk: localhost:2181(CONNECTED) 12] rmr /servers
[zk: localhost:2181(CONNECTED) 13] ls /
[zookeeper]
```
14. 查看节点状态
```
[zk: localhost:2181(CONNECTED) 14] stat /
cZxid = 0x0
ctime = Thu Jan 01 08:00:00 CST 1970
mZxid = 0x0
mtime = Thu Jan 01 08:00:00 CST 1970
pZxid = 0x100000011
cversion = 1
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 0
numChildren = 1
```