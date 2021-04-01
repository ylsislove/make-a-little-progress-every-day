# webrtc-coturn服务安装

## 环境
* CentOS

## 过程
从 github 上拉取完仓库仓库后，运行 `./configure --prefix=/opt/module/coturn` 命令报错：

```
ERROR: OpenSSL Crypto development libraries are not installed properly in required location
```

```
ERROR: Libevent2 development libraries are not installed properly in required location.
```

## 解决办法
```
yum install openssl-devel libevent-devel mysql-devel mysql-server
```

## 运行
```
bin/turnserver -v -r yaindream.com -a -o -c etc/turnserver.conf
```

## 参考
* [coturn服务器部署](https://blog.csdn.net/w13511069150/article/details/90438614)
* [CentOS下安装coturn+阿里云服务器](https://blog.csdn.net/m0_46453807/article/details/107164699)
* [ERROR: OpenSSL Crypto development libraries are not installed properly in required location](https://superuser.com/questions/1059499/error-openssl-crypto-development-libraries-are-not-installed-properly-in-requir)
