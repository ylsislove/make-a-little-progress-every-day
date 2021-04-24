# Shader概述

  - [GPU概述](#gpu%E6%A6%82%E8%BF%B0)
    - [GPU的前世](#gpu%E7%9A%84%E5%89%8D%E4%B8%96)
    - [GPU的今生](#gpu%E7%9A%84%E4%BB%8A%E7%94%9F)
    - [GPU的优越性](#gpu%E7%9A%84%E4%BC%98%E8%B6%8A%E6%80%A7)
    - [GPU的缺陷](#gpu%E7%9A%84%E7%BC%BA%E9%99%B7)
  - [Shader概述](#shader%E6%A6%82%E8%BF%B0-1)
    - [OpenGL简介](#opengl%E7%AE%80%E4%BB%8B)
    - [DirectX简介](#directx%E7%AE%80%E4%BB%8B)
    - [Cg简介](#cg%E7%AE%80%E4%BB%8B)
  - [渲染处理流程](#%E6%B8%B2%E6%9F%93%E5%A4%84%E7%90%86%E6%B5%81%E7%A8%8B)
    - [Cpu应用阶段](#cpu%E5%BA%94%E7%94%A8%E9%98%B6%E6%AE%B5)
    - [几何阶段和光栅化阶段](#%E5%87%A0%E4%BD%95%E9%98%B6%E6%AE%B5%E5%92%8C%E5%85%89%E6%A0%85%E5%8C%96%E9%98%B6%E6%AE%B5)

## GPU概述
### GPU的前世
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172040.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172040.png)

### GPU的今生
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172118.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172118.png)

### GPU的优越性
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172226.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172226.png)

### GPU的缺陷
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172318.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172318.png)

## Shader概述
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172516.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172516.png)

### OpenGL简介
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172751.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424172751.png)

### DirectX简介
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424173032.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424173032.png)

### Cg简介
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424173418.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424173418.png)

## 渲染处理流程
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424174202.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424174202.png)

### Cpu应用阶段
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424174329.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424174329.png)

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424174506.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424174506.png)

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424174529.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424174529.png)

Draw Call 会受到带宽的限制，所以不要大量使用 Draw Call 命令，否则可能会渲染卡顿

### 几何阶段和光栅化阶段
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424175056.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424175056.png)

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424180207.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210424180207.png)
