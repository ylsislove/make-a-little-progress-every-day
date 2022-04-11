# 物联网-thingsboard源码编译安装踩坑记录

  - [前言](#%E5%89%8D%E8%A8%80)
  - [从 GitHub 上 Clone 下源码后运行 Mavan 报错](#%E4%BB%8E-github-%E4%B8%8A-clone-%E4%B8%8B%E6%BA%90%E7%A0%81%E5%90%8E%E8%BF%90%E8%A1%8C-mavan-%E6%8A%A5%E9%94%99)
  - [Cannot resolve com.sun:tools:1.4.2](#cannot-resolve-comsuntools142)
  - [org.postgresql.util.PSQLException: 不支援 10 验证类型。请核对您已经组态 pg_hba.conf 文件包含客户端的IP位址或网路区段，以及驱动程序所支援的验证架构模式已被支援](#orgpostgresqlutilpsqlexception-%E4%B8%8D%E6%94%AF%E6%8F%B4-10-%E9%AA%8C%E8%AF%81%E7%B1%BB%E5%9E%8B%E8%AF%B7%E6%A0%B8%E5%AF%B9%E6%82%A8%E5%B7%B2%E7%BB%8F%E7%BB%84%E6%80%81-pg_hbaconf-%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB%E5%AE%A2%E6%88%B7%E7%AB%AF%E7%9A%84ip%E4%BD%8D%E5%9D%80%E6%88%96%E7%BD%91%E8%B7%AF%E5%8C%BA%E6%AE%B5%E4%BB%A5%E5%8F%8A%E9%A9%B1%E5%8A%A8%E7%A8%8B%E5%BA%8F%E6%89%80%E6%94%AF%E6%8F%B4%E7%9A%84%E9%AA%8C%E8%AF%81%E6%9E%B6%E6%9E%84%E6%A8%A1%E5%BC%8F%E5%B7%B2%E8%A2%AB%E6%94%AF%E6%8F%B4)
  - [参考链接](#%E5%8F%82%E8%80%83%E9%93%BE%E6%8E%A5)
  - [附录](#%E9%99%84%E5%BD%95)

## 前言
深夜踩坑真艰难，但获得的成就感也是最开心的~

## 从 GitHub 上 Clone 下源码后运行 Mavan 报错
如果运行 `mvn clean install -DskipTests --settings D:\scoop\apps\maven\current\conf\thingsboardSettings.xml` 命令后编译报错，最大的可能就是 jdk 的版本和仓库的版本不符，目前仓库最新的代码（thingsboard-3.3.1）用的 jdk 是 jdk11，而我电脑上安装的是 jdk8，所以这肯定就编译不过了。解决办法就是去 [GitHub Release](https://github.com/thingsboard/thingsboard/releases) 找到 `ThingsBoard 3.2.1 Release` 下载，注意选择源码版本下载，如下图。3.2.1 版本的 thingsboard 是用的 jdk8，然后在运行 mvn 命令就不会报编译错误了。

![ThingsBoard 3.2.1 Release](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210926012001.png)

thingsboardSettings.xml 文件内容放到文章附录，需要的自取。注意将文件中的 `<localRepository>D:\RepMaven</localRepository>` 改成自己的路径

## 报错 The unauthenticated git protocol on port 9418 is no longer supported.
报错如下图

![](http://image.aayu.today/2022/04/11/3eadd16f755fe.png)

哎，这个就是由于[最新版本的 git 提升安全性加入了新特性（2022.1.11）](https://github.blog/2021-09-01-improving-git-protocol-security-github/#no-more-unauthenticated-git)导致的

解决办法就是在 `.gitconfig` 文件中加入如下语句 

```xml
[url "https://"]
  insteadOf = ssh://
[url "https://"]
  insteadOf = git://
```

然后重新进行编译即可~~

参考链接：[The unauthenticated git protocol on port 9418 is no longer supported. ](https://www.cnblogs.com/procorosso/p/16121047.html)

## Cannot resolve com.sun:tools:1.4.2
![报错图](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210925231719.png)

这个问题真是太坑了，因为我的 jdk8 是通过 scoop 安装的，而这个工具安装的 jdk8 没有配置 CLASSPATH 环境变量，导致找不到 com.sun:tools

解决办法就是在环境变量里配置一下 CLASSPATH 为 `.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar`，如下图。

![配置环境变量](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210925231601.png)

配置完成后再在 IDEA 里打开项目，点击侧边栏 Maven 下方的刷新按钮，刷新完成后项目就不再报错啦~

![项目就不再报错啦](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210925232100.png)

## org.postgresql.util.PSQLException: 不支援 10 验证类型。请核对您已经组态 pg_hba.conf 文件包含客户端的IP位址或网路区段，以及驱动程序所支援的验证架构模式已被支援

运行数据库初始化脚本 `install_dev_db.bat` 报错。感谢这位老哥的[帖子](https://blog.csdn.net/qq_35377323/article/details/112979532)给出了解决方案

解决办法：找到 pgsql 的安装目录下的 pg_hba.conf 文件，如下图

![pg_hba.conf](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210925232625.png)

用文本编辑器打开后做如下修改

```
# "local" is for Unix domain socket connections only
local   all             all                           trust
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 trust
```

![修改示意图](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210925232925.png)

修改完成后，再次运行 `install_dev_db.bat` 脚本就不会报错啦~

![数据库初始化成功](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210925233049.png)

## 参考链接
* [ThingsBoard开源物联网平台学习记录](https://www.bilibili.com/video/BV12f4y147UX)
* [pgsql在连接的时候报：不支援 10 验证类型。请核对您已经组态。。。](https://blog.csdn.net/qq_35377323/article/details/112979532)
* [Thingsboard入门教程：本地环境搭建和源码编译安装，献给thingsboard编译失败的同学，教程不断优化](https://www.iotschool.com/wiki/tbinstall)

## 附录
```xml
<?xml version="1.0" encoding="UTF-8"?>

<!--
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
-->

<!--
 | This is the configuration file for Maven. It can be specified at two levels:
 |
 |  1. User Level. This settings.xml file provides configuration for a single user,
 |                 and is normally provided in ${user.home}/.m2/settings.xml.
 |
 |                 NOTE: This location can be overridden with the CLI option:
 |
 |                 -s /path/to/user/settings.xml
 |
 |  2. Global Level. This settings.xml file provides configuration for all Maven
 |                 users on a machine (assuming they're all using the same Maven
 |                 installation). It's normally provided in
 |                 ${maven.conf}/settings.xml.
 |
 |                 NOTE: This location can be overridden with the CLI option:
 |
 |                 -gs /path/to/global/settings.xml
 |
 | The sections in this sample file are intended to give you a running start at
 | getting the most out of your Maven installation. Where appropriate, the default
 | values (values used when the setting is not specified) are provided.
 |
 |-->
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">
  <!-- localRepository
   | The path to the local repository maven will use to store artifacts.
   |
   | Default: ${user.home}/.m2/repository
  <localRepository>/path/to/local/repo</localRepository>
  -->
<localRepository>D:\RepMaven</localRepository>
  <!-- interactiveMode
   | This will determine whether maven prompts you when it needs input. If set to false,
   | maven will use a sensible default value, perhaps based on some other setting, for
   | the parameter in question.
   |
   | Default: true
  <interactiveMode>true</interactiveMode>
  -->

  <!-- offline
   | Determines whether maven should attempt to connect to the network when executing a build.
   | This will have an effect on artifact downloads, artifact deployment, and others.
   |
   | Default: false
  <offline>false</offline>
  -->

  <!-- pluginGroups
   | This is a list of additional group identifiers that will be searched when resolving plugins by their prefix, i.e.
   | when invoking a command line like "mvn prefix:goal". Maven will automatically add the group identifiers
   | "org.apache.maven.plugins" and "org.codehaus.mojo" if these are not already contained in the list.
   |-->
  <pluginGroups>
    <!-- pluginGroup
     | Specifies a further group identifier to use for plugin lookup.
    <pluginGroup>com.your.plugins</pluginGroup>
    -->
  </pluginGroups>

  <!-- proxies
   | This is a list of proxies which can be used on this machine to connect to the network.
   | Unless otherwise specified (by system property or command-line switch), the first proxy
   | specification in this list marked as active will be used.
   |-->
  <proxies>
    <!-- proxy
     | Specification for one proxy, to be used in connecting to the network.
     |
    <proxy>
      <id>optional</id>
      <active>true</active>
      <protocol>http</protocol>
      <username>proxyuser</username>
      <password>proxypass</password>
      <host>proxy.host.net</host>
      <port>80</port>
      <nonProxyHosts>local.net|some.host.com</nonProxyHosts>
    </proxy>
    -->
  </proxies>

  <!-- servers
   | This is a list of authentication profiles, keyed by the server-id used within the system.
   | Authentication profiles can be used whenever maven must make a connection to a remote server.
   |-->
  <servers>
    <!-- server
     | Specifies the authentication information to use when connecting to a particular server, identified by
     | a unique name within the system (referred to by the 'id' attribute below).
     |
     | NOTE: You should either specify username/password OR privateKey/passphrase, since these pairings are
     |       used together.
     |
    <server>
      <id>deploymentRepo</id>
      <username>repouser</username>
      <password>repopwd</password>
    </server>
    -->

    <!-- Another sample, using keys to authenticate.
    <server>
      <id>siteServer</id>
      <privateKey>/path/to/private/key</privateKey>
      <passphrase>optional; leave empty if not used.</passphrase>
    </server>
    -->
  </servers>

  <!-- mirrors
   | This is a list of mirrors to be used in downloading artifacts from remote repositories.
   |
   | It works like this: a POM may declare a repository to use in resolving certain artifacts.
   | However, this repository may have problems with heavy traffic at times, so people have mirrored
   | it to several places.
   |
   | That repository definition will have a unique id, so we can create a mirror reference for that
   | repository, to be used as an alternate download site. The mirror site will be the preferred
   | server for that repository.
   |-->
  <mirrors>
    <!-- mirror
     | Specifies a repository mirror site to use instead of a given repository. The repository that
     | this mirror serves has an ID that matches the mirrorOf element of this mirror. IDs are used
     | for inheritance and direct lookup purposes, and must be unique across the set of mirrors.
     |
    <mirror>
      <id>mirrorId</id>
      <mirrorOf>repositoryId</mirrorOf>
      <name>Human Readable Name for this Mirror.</name>
      <url>http://my.repository.com/repo/path</url>
    </mirror>
     -->
	 <mirror>
      <id>nexus-public-snapshots</id>
      <mirrorOf>public-snapshots</mirrorOf>
     <url>http://maven.aliyun.com/nexus/content/repositories/snapshots/</url>
    </mirror>
	<mirror>
      <id>nexus</id>
      <name>internal nexus repository</name>
      <url>https://repo.maven.apache.org/maven2</url>
      <mirrorOf>central</mirrorOf>
    </mirror>

	<mirror>
      <id>maven-central</id>
	  <name>central</name>
	  <url>https://repo1.maven.org/maven2/</url>
      <mirrorOf>central</mirrorOf>
    </mirror>

    <mirror>
      <id>uk</id>
      <mirrorOf>central</mirrorOf>
      <name>Human Readable Name for this Mirror.</name>
      <url>http://uk.maven.org/maven2/</url>
    </mirror>

    <mirror>
      <id>CN</id>
      <name>OSChina Central</name>
      <url>http://maven.oschina.net/content/groups/public/</url>
      <mirrorOf>central</mirrorOf>
    </mirror>
  </mirrors>

  <!-- profiles
   | This is a list of profiles which can be activated in a variety of ways, and which can modify
   | the build process. Profiles provided in the settings.xml are intended to provide local machine-
   | specific paths and repository locations which allow the build to work in the local environment.
   |
   | For example, if you have an integration testing plugin - like cactus - that needs to know where
   | your Tomcat instance is installed, you can provide a variable here such that the variable is
   | dereferenced during the build process to configure the cactus plugin.
   |
   | As noted above, profiles can be activated in a variety of ways. One way - the activeProfiles
   | section of this document (settings.xml) - will be discussed later. Another way essentially
   | relies on the detection of a system property, either matching a particular value for the property,
   | or merely testing its existence. Profiles can also be activated by JDK version prefix, where a
   | value of '1.4' might activate a profile when the build is executed on a JDK version of '1.4.2_07'.
   | Finally, the list of active profiles can be specified directly from the command line.
   |
   | NOTE: For profiles defined in the settings.xml, you are restricted to specifying only artifact
   |       repositories, plugin repositories, and free-form properties to be used as configuration
   |       variables for plugins in the POM.
   |
   |-->
  <profiles>
    <!-- profile
     | Specifies a set of introductions to the build process, to be activated using one or more of the
     | mechanisms described above. For inheritance purposes, and to activate profiles via <activatedProfiles/>
     | or the command line, profiles have to have an ID that is unique.
     |
     | An encouraged best practice for profile identification is to use a consistent naming convention
     | for profiles, such as 'env-dev', 'env-test', 'env-production', 'user-jdcasey', 'user-brett', etc.
     | This will make it more intuitive to understand what the set of introduced profiles is attempting
     | to accomplish, particularly when you only have a list of profile id's for debug.
     |
     | This profile example uses the JDK version to trigger activation, and provides a JDK-specific repo.
    <profile>
      <id>jdk-1.4</id>

      <activation>
        <jdk>1.4</jdk>
      </activation>

      <repositories>
        <repository>
          <id>jdk14</id>
          <name>Repository for JDK 1.4 builds</name>
          <url>http://www.myhost.com/maven/jdk14</url>
          <layout>default</layout>
          <snapshotPolicy>always</snapshotPolicy>
        </repository>
      </repositories>
    </profile>
    -->

    <!--
     | Here is another profile, activated by the system property 'target-env' with a value of 'dev',
     | which provides a specific path to the Tomcat instance. To use this, your plugin configuration
     | might hypothetically look like:
     |
     | ...
     | <plugin>
     |   <groupId>org.myco.myplugins</groupId>
     |   <artifactId>myplugin</artifactId>
     |
     |   <configuration>
     |     <tomcatLocation>${tomcatPath}</tomcatLocation>
     |   </configuration>
     | </plugin>
     | ...
     |
     | NOTE: If you just wanted to inject this configuration whenever someone set 'target-env' to
     |       anything, you could just leave off the <value/> inside the activation-property.
     |
    <profile>
      <id>env-dev</id>

      <activation>
        <property>
          <name>target-env</name>
          <value>dev</value>
        </property>
      </activation>

      <properties>
        <tomcatPath>/path/to/tomcat/instance</tomcatPath>
      </properties>
    </profile>
    -->
  </profiles>

  <!-- activeProfiles
   | List of profiles that are active for all builds.
   |
  <activeProfiles>
    <activeProfile>alwaysActiveProfile</activeProfile>
    <activeProfile>anotherAlwaysActiveProfile</activeProfile>
  </activeProfiles>
  -->
</settings>
```
