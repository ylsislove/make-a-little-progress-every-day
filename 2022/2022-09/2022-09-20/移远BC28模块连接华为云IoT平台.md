---
title: 移远BC28模块连接华为云IoT平台
date: 2022-09-20 23:38:07
categories:
 - [硬件修炼手册, 物联网]
tags: 
 - IoT
 - BC28
---

## 基础命令
| 命令 | 说明 |
| :--: | :--: | 
| AT+CFUN=1 | 开启射频（全功能模式）。如果关闭了自动连接默认+CFUN:0，需要手动开启 |
| AT+NCCID | 读取 SIM 卡 ID，如果能返回+NCCID:开头的一串 ID，证明 SIM 与 NB-IoT 设备的物理连接没问题（不能排除卡欠费等问题） |
| AT+CGATT=1 | 让 NB-IoT 设备去附着网络 |
| AT+CSQ | 查询卡信号，如果是+CSQ:99,99，表示当前没信号 |
| AT+CGSN=1 | 返回 IMEI（国际移动设备识别码） |
| AT+CIMI | 获得IMSI。用来读取或者识别SIM卡的IMSI（国际移动签署者标识），识别移动设备附带的SIM卡标识。 |
| AT+CEREG? | 查询 NB 网络注册状态，+CEREG:0,1 表示已注册到归属网络 |

## 连接教程
待更，先放一个大概步骤吧，后续有空再整理

1. AT
2. AT+CFUN? 是否开启了频射
3. AT+CFUN=1 开启频射
4. AT+CGATT? 是否附着网络
5. AT+CGATT=1 附着网络
6. AT+CSQ 查询信号强度
7. AT+NCCID 物联网卡是否正常接入
8. AT+CGSN=1 查询设备标识码
:::info
查看配置项
AT+QMTCFG=?
AT+QMTCFG="version",0
:::
9. AT+QMTCFG="version",0,4 设置 MQTT 版本为3.1.1
10. AT+QMTOPEN=0,"3f9e85b40a.iot-mqtts.cn-north-4.myhuaweicloud.com",1883
11. AT+QMTCONN=0,"<ClientId>","<Username>","<Password>"
12. AT+QMTSUB=0,1,"$oc/devices/<device_id>/user/messages/up",0 订阅消息
:::warning
华为云物联网平台不能直接订阅预设的Topic：AT+QMTSUB=0,1,"$oc/devices/<device_id>/sys/messages/up",0
:::
13. AT+QMTPUB=0,0,0,0,"$oc/devices/<device_id>/user/messages/up" 发布消息
:::info
此处被坑惨了
:::

## 被坑笔记
哇，真的是被坑惨了，我用的是 BC28 模块，整个 MQTT 连接流程走下来，就一直卡在用 `AT+QMTPUB=` 命令发布消息这里，我这里参考了 `Quectel_BC26BC20_MQTT_应用指导_V1.0` BC26 的 MQTT 应用指导手册，其中对 `AT+QMTPUB=` 命令的介绍如下图

![](https://image.aayu.today/uploads/2022/09/21/202209210236879.png)

我死活无法用 `AT+QMTPUB=<TCP_connectID>,<msgID>,<qos>,<retain>,"<topic>","<msg>"` 这个命令来直接发布消息，QCOM 客户端直接给我返回 `ERROR`，看到这个 ERROR 我都要欲哭无泪了，为啥啊，为啥我不能一次性发布消息，如果用上图所示的 `进入数据模式` 发布消息，我又咋在代码里面按 `Ctrl+Z` 结束发送呢，哭死

:::info
在找资料过程中的一个意外收获，在出现 > 这个符号后，发送完自己想发送的数据后，直接用（HEX String）模式（针对 QCOM 客户端），也是就 16 进制模式发送 1A 字符串，就可以结束发送啦，这样用代码也就可以实现了 `进入数据模式` 的发布消息命令了，真的是最后一根稻草了
:::

我就找啊找，找啊找，根本就在网上找不到相关的帖子说 BC28 模块的 `AT+QMTPUB=` 命令报错，呜呜呜，但天无绝人之路，就在我以为是我的 BC28 模块的固件版本太老，想升级固件，用 `BC28JAR01A08` 为关键字在 Bing 上搜索，终于让我找到一个相关的帖子：[BC26 MQTT OK BC28 Fail](https://forums.quectel.com/t/bc26-mqtt-ok-bc28-fail/4148) 说这事了，真的流泪了

移远的技术支持也好心的回复了这个帖子

> BC28 Special characters are not supported.
> You can use the following modes to publish messages.
> AT+QMTPUB=,,,,"" After “>” is responded, input the data to be sent. Tap “CTRL+Z” to send, and tap “ESC” to cancel the operation.

原来真的是 BC28 不支持直接发布消息的命令啊，知道真相的我眼泪掉下来。总之，这个坑也真的是让我花了一晚上的时间去查找资料，还是很有必要在这记录下来的，生活不易，猫猫叹气

## 参考链接
* [BC35/BC28无法入网的原因及排错方法](https://bbs.huaweicloud.com/blogs/191706)
* [BC26 MQTT OK BC28 Fail](https://forums.quectel.com/t/bc26-mqtt-ok-bc28-fail/4148)
* [BC28使用MQTT协议 连接OneNET平台的流程解析](https://blog.csdn.net/tiantangmoke/article/details/92789801)
* [为什么NB-IOT模组在华为云平台一直显示未激活？](https://bbs.huaweicloud.com/forum/thread-195600-1-1.html)
* [BC28_MQTT调试笔记](https://cxymm.net/article/qq_41298245/106803298)
* [移远BC20连接MQTT服务器小记](https://blog.csdn.net/helpinfo/article/details/119341951)
* [物联网-移远M26模块MQTT开发（AT命令）](https://blog.csdn.net/u014754841/article/details/84573178)
* [【BC28】【注册网络】AT+NMSTATUS查询出现的状态分别代表什么意思](https://bbs.huaweicloud.com/forum/thread-190154-1-1.html)

## 低功耗模式相关问题链接
* [BC35-G模块的初始化流程，基于COAP协议，怎么优化更好？](https://bbs.huaweicloud.com/forum/thread-16693-1-1.html)
* [BC28 PSM进入问题](https://bbs.huaweicloud.com/forum/thread-18562-1-1.html)
* [你们的移动NB卡，PSM模式下54分钟会自动唤醒一次吗？](https://bbs.huaweicloud.com/forum/thread-34313-1-1.html)
* [移远BC28 模块进入PSM模式后功耗较大，且还能进行AT指令的回复](https://bbs.huaweicloud.com/forum/thread-123330-1-1.html)
