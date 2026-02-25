---
title: 在Mac系统中实现STLink烧录固件（不用虚拟机！）
date: 2026/01/18 20:01
categories:
 - [不看会后悔的实用技巧分享, MacBook]
tags: 
 - MacBook
 - STLink
---

## 参考链接
* [Mac系统中实现STLink驱动下载（STM32）的完整方案](https://blog.csdn.net/weixin_42513928/article/details/156441019)
* [Keil5生成BIN文件及烧录方法详解](https://chat.deepseek.com/share/tibnluyn0kakt4z0ot)

## 使用Homebrew安装openocd
```bash
brew install libusb openocd
```

工具说明：

| 工具 | 作用 |
| --- | --- | 
| libusb | 提供用户态直接访问 USB 设备的能力，绕过系统驱动限制 |
| openocd | 实现 ARM Cortex-M 调试协议栈，充当“调试服务器” |

安装完成后，你可以通过以下命令检查版本：

```bash
openocd --version
# 输出类似：Open On-Chip Debugger 0.12.0
```

## 文件格式区别

### AXF文件 (ARM eXecutable Format)

包含内容：完整的可执行代码 + 调试信息 + 符号表 + 段信息

文件大小：通常比HEX/BIN大很多

主要用途：用于调试（可以用Keil/IDE单步调试）

不能直接烧录到MCU，因为包含太多非代码信息

### HEX文件 (Intel HEX格式)

包含内容：纯可执行代码 + 地址信息（文本格式）

文件格式：ASCII文本格式，每行包含地址、数据、校验和

可以烧录到MCU，烧录工具会自动解析地址

### BIN文件 (Binary格式)

包含内容：纯二进制代码（无地址信息）

文件格式：原始二进制，最紧凑

烧录时需要指定起始地址（如你命令中的0x08000000）

## 烧录命令

```bash
# 方案A：使用BIN
openocd -f interface/stlink.cfg -f target/stm32f1x.cfg \
  -c "program firmware.bin 0x08000000 verify reset exit"

# 方案B：使用HEX（更简单）
openocd -f interface/stlink.cfg -f target/stm32f1x.cfg \
  -c "program firmware.hex verify reset exit"
```
