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
yum install openssl-devel
yum install libevent-devel
```

## 参考
* [编译安装coturn小记](https://blog.csdn.net/righteousness/article/details/90732368)
* [ERROR: OpenSSL Crypto development libraries are not installed properly in required location](https://superuser.com/questions/1059499/error-openssl-crypto-development-libraries-are-not-installed-properly-in-requir)
