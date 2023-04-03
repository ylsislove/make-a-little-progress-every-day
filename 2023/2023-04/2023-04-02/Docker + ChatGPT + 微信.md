---
title: Docker + ChatGPT + 微信
date: 2023-04-03 02:43:28
categories:
 - [不看会后悔的实用技巧分享, 工具篇]
tags: 
 - ChatGPT
---

## 前言
终于捣鼓成功啦，项目地址：[ylsislove/wechatbot](https://github.com/ylsislove/wechatbot)，欢迎 star ~

:::warning
最新消息：https://mp.weixin.qq.com/s/1M8JFbq9Ea29EzE9QqocPQ
如果账号是从第三方手上购买过来的，不要尝试了，OpenAI最近在封这类账号。以及自己的代理域名也不要分享给他人使用了，像评论里有人评论的，保护好自己的账号最重要~
如果是自己亲手注册的，也绑定了信用卡（向OpenAI表明自己不是白嫖党/滑稽），同时也有一个自己搭建的稳定的代理域名，那么就可以捣鼓一下啦~
实在担心的话，就先收藏一下本帖子，等最近风头过去了在尝试吧
:::

## 极空间部署
### 下载镜像
在仓库中搜索我的用户名`ylsislove`，选择`wechatbot`，下载最新版本即可

![](https://image.aayu.today/uploads/2023/04/03/202304030227517.png)
![](https://image.aayu.today/uploads/2023/04/03/202304030228047.png)
{.gallery  data-height="240"}

### 创建配置文件
找一个位置，新建`config.txt`，内容如下，根据个人信息进行修改

![](https://image.aayu.today/uploads/2023/04/03/202304030230032.png)
![](https://image.aayu.today/uploads/2023/04/03/202304030231212.png)
{.gallery  data-height="240"}

```json
{
  "api_key": "your api key",
  "auto_pass": true,
  "session_timeout": 60,
  "max_tokens": 1024,
  "model": "gpt-3.5-turbo",
  "temperature": 1,
  "reply_prefix": "来自机器人回复：",
  "session_clear_token": "清空会话",
  "base_url": "https://api.openai.com/v1/",
  "request_timeout": 60
}
```

参数含义参见：[配置文件说明](https://github.com/ylsislove/wechatbot#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E8%AF%B4%E6%98%8E)

:::info
国内用户注意设置好base_url，base_url设置稳定再访问，API账户就不会出问题，我用了很长时间了都还在稳定使用~
base_url可以参考https://github.com/Ice-Hazymoon/openai-scf-proxy这个教程，设置一个稳定的代理域名即可。挂到腾讯云香港地区的轻量应用服务器上都行，我用的就是这个
:::

### 创建容器
双击刚才下载的镜像，配置极其简单，像网络、端口、别名、环境都不用管，只需配置好`文件夹路径`和`启动命令`即可，如下

![](https://image.aayu.today/uploads/2023/04/03/202304030234539.png)
![](https://image.aayu.today/uploads/2023/04/03/202304030234624.png)
![](https://image.aayu.today/uploads/2023/04/03/202304030236817.png)
{.gallery  data-height="240"}

点击应用，bingo~，容器创建成功

### 扫码登录
我们可以在容器的日志中看到我们要扫描的二维码，但控制台不好扫描，我们就把日志下载下来即可~

下载后，用本地的记事本打开，看到二维码清晰的展现在我们面前了，爽~

![](https://image.aayu.today/uploads/2023/04/03/202304030240193.png)
![](https://image.aayu.today/uploads/2023/04/03/202304030238171.png)
![](https://image.aayu.today/uploads/2023/04/03/202304030249151.png)
![](https://image.aayu.today/uploads/2023/04/03/202304030241329.png)
{.gallery  data-height="240"}

扫描成功后刷新日志，成功登录，接下来开始愉快的学习吧~

## 效果展示
![](https://image.aayu.today/uploads/2023/04/03/202304030216436.jpg)
![](https://image.aayu.today/uploads/2023/04/03/202304030216410.jpg)
![](https://image.aayu.today/uploads/2023/04/03/202304030216301.jpg)
{.gallery  data-height="600"}
