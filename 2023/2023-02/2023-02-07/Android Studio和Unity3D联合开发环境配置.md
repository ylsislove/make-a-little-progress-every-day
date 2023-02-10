---
title: Android Studio和Unity3D联合开发环境配置
date: 2023-02-07 01:27:40
categories:
 - [Android]
tags: 
 - Android Studio
 - Unity3D
---

## Android Studio安装
这里我使用的版本是2021.2.1.15。放个百度网盘链接，需要的自取

链接：https://pan.baidu.com/s/1LFpHWQtQ3RBYsYxzLgQEww 
提取码：wfjq

## Android SDK配置
:::info
如果发现自己Android SDK无法刷新出新的东西，表明自己的网络可能不太行。推荐大家去「 [一元机场](https://xn--4gq62f52gdss.com/#/register?code=DydJBuvW) 」平台订阅，每月500G流量月均0.9元，性价比拉满~
:::
代理配置的过程，可以根据平台教程配置好「 Clash for Windows 」，配置好主程序默认端口，如下图，然后在Android Studio上配置好代理，如下图，即可~

![](https://image.aayu.today/uploads/2023/02/07/202302070143758.png)
![](https://image.aayu.today/uploads/2023/02/07/202302070146621.png)
{.gallery  data-height="240"}

可以点击Check connection测试下`https://dl.google.com/android/repository/repository2-3.xml`能否访问成功，可以的话就表示代理没问题~

确认自己手机的Android版本，例如，手机的Android版本是10，就勾选这几项
![](https://image.aayu.today/uploads/2023/02/07/202302070130739.png){width="800px"}

:::warning
注意，默认安装的Android SDK（例如Android SDK Platform 33）不能删除，否则可能会有未知Bug
:::

然后在SDK Tools，安装如下几项，可保后面与Unity3D联调不出奇奇怪怪的Bug~

![](https://image.aayu.today/uploads/2023/02/07/202302070137372.png)
![](https://image.aayu.today/uploads/2023/02/07/202302070139356.png)
![](https://image.aayu.today/uploads/2023/02/07/202302070413902.png)
![](https://image.aayu.today/uploads/2023/02/07/202302070140863.png)
{.gallery  data-height="240"}

创建一个空项目，当下方进度条的Gradle显示Successful，表明Android Studio的配置可以初告一个段落了~

哦补充一个，在下图这里记得设置JDK为8

![](https://image.aayu.today/uploads/2023/02/07/202302070336910.png){width="800px"}

## Unity3D配置
以安装2021最新稳定版为例，在Unity Hub上安装如下

![](https://image.aayu.today/uploads/2023/02/07/202302070203190.png){width="800px"}

创建一个新项目，首先在「 File -> Build Settings -> Player Settings 」里设置下公司名和项目名，如下，unity会自动组合成包名

![](https://image.aayu.today/uploads/2023/02/07/202302070217872.png)
![](https://image.aayu.today/uploads/2023/02/07/202302070218601.png)
{.gallery  data-height="300"}

然后在「 Editor -> Preference 」里正确设置JDK，Android SDK和NDK，然后打开下Gradle的路径，记住Unity的Gradle的版本是多少，后面Android Studio联调时，需要和Unity保持一致

![](https://image.aayu.today/uploads/2023/02/07/202302070221586.png){width="800px"}

## 创建Android密钥文件
```bash
keytool -genkey -alias 密钥库名称 -keyalg RSA -validity 有效时间 -keystore 密钥库文件名
```

![](https://image.aayu.today/uploads/2023/02/07/202302070238825.png)

密钥文件将生成在运行命令的所在目录下~
