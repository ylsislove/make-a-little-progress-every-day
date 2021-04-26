# Shader-几何阶段和光栅化阶段

  - [几何阶段](#%E5%87%A0%E4%BD%95%E9%98%B6%E6%AE%B5)
    - [顶点着色器](#%E9%A1%B6%E7%82%B9%E7%9D%80%E8%89%B2%E5%99%A8)
    - [裁剪](#%E8%A3%81%E5%89%AA)
    - [屏幕映射](#%E5%B1%8F%E5%B9%95%E6%98%A0%E5%B0%84)
  - [光栅化阶段](#%E5%85%89%E6%A0%85%E5%8C%96%E9%98%B6%E6%AE%B5)
    - [三角形设置和三角形遍历](#%E4%B8%89%E8%A7%92%E5%BD%A2%E8%AE%BE%E7%BD%AE%E5%92%8C%E4%B8%89%E8%A7%92%E5%BD%A2%E9%81%8D%E5%8E%86)
    - [片元着色器](#%E7%89%87%E5%85%83%E7%9D%80%E8%89%B2%E5%99%A8)
    - [逐片元操作](#%E9%80%90%E7%89%87%E5%85%83%E6%93%8D%E4%BD%9C)
      - [模板测试](#%E6%A8%A1%E6%9D%BF%E6%B5%8B%E8%AF%95)
      - [深度测试](#%E6%B7%B1%E5%BA%A6%E6%B5%8B%E8%AF%95)
      - [合并混合](#%E5%90%88%E5%B9%B6%E6%B7%B7%E5%90%88)
      - [各种测试总结](#%E5%90%84%E7%A7%8D%E6%B5%8B%E8%AF%95%E6%80%BB%E7%BB%93)
  - [附加知识](#%E9%99%84%E5%8A%A0%E7%9F%A5%E8%AF%86)
    - [CPU和GPU如何并行工作](#cpu%E5%92%8Cgpu%E5%A6%82%E4%BD%95%E5%B9%B6%E8%A1%8C%E5%B7%A5%E4%BD%9C)
    - [什么是固定管线渲染](#%E4%BB%80%E4%B9%88%E6%98%AF%E5%9B%BA%E5%AE%9A%E7%AE%A1%E7%BA%BF%E6%B8%B2%E6%9F%93)
    - [什么是Shader](#%E4%BB%80%E4%B9%88%E6%98%AFshader)

## 几何阶段
### 顶点着色器
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427025237.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427025237.png)

### 裁剪
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427025505.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427025505.png)

### 屏幕映射
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427025645.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427025645.png)

## 光栅化阶段
### 三角形设置和三角形遍历
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427030030.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427030030.png)

### 片元着色器
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427030735.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427030735.png)

### 逐片元操作
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427031131.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427031131.png)

#### 模板测试
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427031835.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427031835.png)

#### 深度测试
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427031924.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427031924.png)

#### 合并混合
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427032515.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427032515.png)

#### 各种测试总结
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427033118.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427033118.png)

## 附加知识
### CPU和GPU如何并行工作
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427034243.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427034243.png)

### 什么是固定管线渲染
固定函数的流水线（Fixed-Function Pipeline），简称固定管线，通常是指在较旧的 Gpu 上实现的渲染流水线。这种流水线只给开发者提供一些配置操作，但开发者没有对流水线阶段的完全控制权。在 Unity 中目前的固定管线 shader 都会自动编译顶点片元 shader。

### 什么是Shader
Gpu 流水线上一些可高度编程的阶段，而由着色器编译出来的最终代码是会在Gpu上运行的；有一些特定类型的着色器，如顶点着色器，片元着色器等。依靠着色器我们可以控制流水线中的渲染细节，例如用顶点着色器来进行顶点变换及传递数据，用片元着色器来进行逐像素渲染。
