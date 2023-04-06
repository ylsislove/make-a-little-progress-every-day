---
title: 思源笔记源码解析之kernel篇（九）mobile
date: 2023-04-06 20:02:50
categories:
 - [不看会后悔的实用技巧分享, 源码解析, 思源笔记]
tags: 
 - 思源笔记
---

## [0/1] kernel.go

该文件是 mobile 工程的一部分，主要涉及启动 kernel 和相关的一些操作。具体来说：

* import 了一些库和包，包括了 kernel/cache、kernel/job、kernel/model、kernel/server、kernel/sql 和 golang.org/x/mobile/bind。
* 定义了两个函数 StartKernelFast 和 StartKernel，前者不做任何操作，后者是启动 kernel 的入口。
* 实现了一些辅助函数。
* Language 接受一个整数，返回对应的语言字符串。
* ShowMsg 推送一个消息。
* IsHttpServing 返回是否正在提供 HTTP 服务。
* SetTimezone 设置时间区域。

注释中还提到了该程序基于 GNU Affero General Public License 发布。
