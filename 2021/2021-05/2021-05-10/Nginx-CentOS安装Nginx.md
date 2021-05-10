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

## 配置静态资源文件目录
* [nginx学习：搭建静态资源服务器](https://blog.csdn.net/happysong8783/article/details/80665530)
* [nginx静态资源文件无法访问，403 forbidden错误](https://blog.csdn.net/ngcsnow/article/details/39394991)
* [Nginx静态文件路径配置](https://www.cnblogs.com/azhqiang/p/9772089.html)

## 参考链接
* [Centos7安装Nginx详细步骤](https://www.cnblogs.com/huny/p/13702929.html)
* [centos7安装nginx并启动](https://blog.csdn.net/fishineye/article/details/106457533)
* [Nginx使用教程](https://blog.csdn.net/duguyuyun12345/article/details/83471821)
