# Nginx-CentOS安装Nginx

## 安装依赖项
```
yum install -y openssl-devel pcre pcre-devel zlib zlib-devel
```

## 下载
```
wget http://nginx.org/download/nginx-1.18.0.tar.gz
```

## 解压
```
tar zxvf nginx-1.18.0.tar.gz
cd nginx-1.18.0
```

## 安装
```
./configure --prefix=/opt/module/nginx
make && make install
```

## 参考链接
* [Centos7安装Nginx详细步骤](https://www.cnblogs.com/huny/p/13702929.html)
* [centos7 安装nginx并启动](https://blog.csdn.net/fishineye/article/details/106457533)
* [Nginx使用教程](https://blog.csdn.net/duguyuyun12345/article/details/83471821)
