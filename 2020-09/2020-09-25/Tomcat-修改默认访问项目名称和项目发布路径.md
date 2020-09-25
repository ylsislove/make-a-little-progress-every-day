# Tomcat-修改默认访问项目名称和项目发布路径

  - [修改项目发布路径](#%E4%BF%AE%E6%94%B9%E9%A1%B9%E7%9B%AE%E5%8F%91%E5%B8%83%E8%B7%AF%E5%BE%84)
  - [修改默认访问项目](#%E4%BF%AE%E6%94%B9%E9%BB%98%E8%AE%A4%E8%AE%BF%E9%97%AE%E9%A1%B9%E7%9B%AE)

## 修改项目发布路径
tomcat默认的而发布路径为 `tomcat/webapps/` 目录，但是这个目录下有一些默认的项目，在 tomcat 启动的时候会跟着一起加载。如果不想删除这些项目，可以把 tomcat 发布的路径修改到其他地方。

找到 `tomcat/conf/server.xml` 文件，修改里面这一行的 `appBase` 为其他路径即可。

```xml
<Host name="localhost"  appBase="/root/webfile/webapps" unpackWARs="true" autoDeploy="true">
```

其中：
* name 是虚拟主机名，对应目录 /conf/Catalina/localhost
* unpackWARs 为是否自动解压 war 文件，如果设置为 true，表示把 war 文件先展开再运行。如果为 false 则直接运行 war 文件
* autoDeploy，默认为true，表示如果有新的 WEB 应用放入 appBase 并且 Tomcat 在运行的情况下，自动载入应用

这里既可以用相对路径，也可以用绝对路径。相对路径默认tomcat目录为根目录。

## 修改默认访问项目
最简单的，可以直接把项目名称修改为 `ROOT`，放在 `tomcat/webapps/` 目录即可。

如果不想修改。那么在第 1 步中的

```xml
<Host name="localhost"  appBase="/root/webfile/webapps" unpackWARs="true" autoDeploy="true">
```

下面加上下面这句即可

```xml
<!-- 设置默认项目名称 -->
<Context path="" docBase="/root/webfile/web" reloadable="true"/> 
```

其中：
* path 代表用浏览器访问的时候的的路径，如 http://localhost:8080/web 来访问 path="/web"
* docBase 为你的项目的路径，这里同样既可以用相对路径，也可以用绝对路径。设置好了之后就会把项目自动映射到 ROOT
* reloadable，如果这个属性设为 true，tomcat 服务器在运行状态下会监视在 WEB-INF/classes 和 WEB-INF/lib 目录下 class 文件的改动，如果监测到有 class 文件被更新的，服务器会自动重新加载 Web 应用