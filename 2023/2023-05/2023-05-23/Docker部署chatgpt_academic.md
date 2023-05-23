---
title: Docker部署chatgpt_academic
date: 2023-05-23 22:26:38
categories:
 - [不看会后悔的实用技巧分享, 工具篇]
tags: 
 - ChatGPT
---

## 前言
如果你是一个搞学术的人，相信你一定会爱上这款大杀器~

功能 | 描述
--- | ---
一键润色 | 支持一键润色、一键查找论文语法错误
一键中英互译 | 一键中英互译
一键代码解释 | 显示代码、解释代码、生成代码、给代码加注释
[自定义快捷键](https://www.bilibili.com/video/BV14s4y1E7jN) | 支持自定义快捷键
模块化设计 | 支持自定义强大的[函数插件](https://github.com/binary-husky/chatgpt_academic/tree/master/crazy_functions)，插件支持[热更新](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%87%BD%E6%95%B0%E6%8F%92%E4%BB%B6%E6%8C%87%E5%8D%97)
[自我程序剖析](https://www.bilibili.com/video/BV1cj411A7VW) | [函数插件] [一键读懂](https://github.com/binary-husky/chatgpt_academic/wiki/chatgpt-academic%E9%A1%B9%E7%9B%AE%E8%87%AA%E8%AF%91%E8%A7%A3%E6%8A%A5%E5%91%8A)本项目的源代码
[程序剖析](https://www.bilibili.com/video/BV1cj411A7VW) | [函数插件] 一键可以剖析其他Python/C/C++/Java/Lua/...项目树
读论文、[翻译](https://www.bilibili.com/video/BV1KT411x7Wn)论文 | [函数插件] 一键解读latex/pdf论文全文并生成摘要
Latex全文[翻译](https://www.bilibili.com/video/BV1nk4y1Y7Js/)、[润色](https://www.bilibili.com/video/BV1FT411H7c5/) | [函数插件] 一键翻译或润色latex论文
批量注释生成 | [函数插件] 一键批量生成函数注释
Markdown[中英互译](https://www.bilibili.com/video/BV1yo4y157jV/) | [函数插件] 看到上面5种语言的[README](https://github.com/binary-husky/chatgpt_academic/blob/master/docs/README_EN.md)了吗？
chat分析报告生成 | [函数插件] 运行后自动生成总结汇报
[PDF论文全文翻译功能](https://www.bilibili.com/video/BV1KT411x7Wn) | [函数插件] PDF论文提取题目&摘要+翻译全文（多线程）
[Arxiv小助手](https://www.bilibili.com/video/BV1LM4y1279X) | [函数插件] 输入arxiv文章url即可一键翻译摘要+下载PDF
[谷歌学术统合小助手](https://www.bilibili.com/video/BV19L411U7ia) | [函数插件] 给定任意谷歌学术搜索页面URL，让gpt帮你[写relatedworks](https://www.bilibili.com/video/BV1GP411U7Az/)
互联网信息聚合+GPT | [函数插件] 一键[让GPT先从互联网获取信息](https://www.bilibili.com/video/BV1om4y127ck)，再回答问题，让信息永不过时
公式/图片/表格显示 | 可以同时显示公式的[tex形式和渲染形式](https://user-images.githubusercontent.com/96192199/230598842-1d7fcddd-815d-40ee-af60-baf488a199df.png)，支持公式、代码高亮
多线程函数插件支持 | 支持多线调用chatgpt，一键处理[海量文本](https://www.bilibili.com/video/BV1FT411H7c5/)或程序
启动暗色gradio[主题](https://github.com/binary-husky/chatgpt_academic/issues/173) | 在浏览器url后面添加```/?__theme=dark```可以切换dark主题

详细介绍参见官方仓库：[binary-husky/chatgpt_academic](https://github.com/binary-husky/gpt_academic)

## 极空间部署
### 下载镜像
在仓库中搜索我的用户名`ylsislove`，选择`gpt_academic`，下载最新版本即可

![](https://image.aayu.today/uploads/2023/05/23/202305232159957.png)

### 配置
![](https://image.aayu.today/uploads/2023/05/23/202305232200256.png)
![](https://image.aayu.today/uploads/2023/05/23/202305232201849.png)
![](https://image.aayu.today/uploads/2023/05/23/202305232202385.png)
![](https://image.aayu.today/uploads/2023/05/23/202305232203871.png)
![](https://image.aayu.today/uploads/2023/05/23/202305232205799.png)
{.gallery  data-height="240"}

* `API_EKY`：你的OpenAI API Key，可同时填写多个API-KEY，用英文逗号分割，例如sk-openaikey1,sk-openaikey2,fkxxxx-api2dkey1,fkxxxx-api2dkey2
* `DEFAULT_WORKER_NUM`：多线程函数插件中，默认允许多少路线程同时访问OpenAI。Free trial users的限制是每分钟3次，Pay-as-you-go users的限制是每分钟3500次。一言以蔽之：免费用户填3，OpenAI绑了信用卡的用户可以填 16 或者更高。提高限制请查询：https://platform.openai.com/docs/guides/rate-limits/overview
* `LAYOUT`：LEFT-RIGHT（左右布局）TOP-DOWN（上下布局）
* `WEB_PORT`：网页的端口，注意要和端口配置里的容器端口相同
* `AUTHENTICATION`：设置用户名和密码，例如`[("root", "123456")]`，可配置多个
* `API_URL_REDIRECT`：重新URL重新定向，实现更换API_URL的作用。例如：{"https://api.openai.com/v1/chat/completions": "在这里填写重定向的api.openai.com的URL"}

更多参数配置参见：[gpt_academic/config.py](https://github.com/binary-husky/gpt_academic/blob/master/config.py)

例如，如果你有自己的网络代理，那么就可以不用配置`API_URL_REDIRECT`，直接配置`USE_PROXY`为`True`，然后配置`proxies`为你的代理地址即可，如`{ "http": "socks5h://localhost:10880", "https": "socks5h://localhost:10880", }`，参见：[gpt_academic/docker-compose.yml](https://github.com/binary-husky/gpt_academic/blob/master/docker-compose.yml)

完成以上配置后，直接点击运行即可~

### 使用
在浏览器输入`http://极空间IP地址:28890`，出现如下界面，配置成功~

![](https://image.aayu.today/uploads/2023/05/23/202305232217181.png)

输入配置的用户名和密码，即可进入主界面，试用下`[插件demo] 历史上的今天`，完美运行~

![](https://image.aayu.today/uploads/2023/05/23/202305232220615.png)

接下来愉快的玩耍吧~

## 局限性
Docker部署因为没有高性能显卡的支持，所以只能使用`chatgpt`，`newbing`等远程服务，不支持官方仓库里的`ChatGLM`、`LLAMA`、`盘古`、`RWKV`等本地模型。

## 致谢
* [gpt_academic](https://github.com/binary-husky/gpt_academic)
