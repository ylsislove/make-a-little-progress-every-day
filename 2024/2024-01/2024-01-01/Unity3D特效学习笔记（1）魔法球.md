---
title: Unity3D特效学习笔记（1）魔法球
math: true
date: 2024-01-01 22:00:52
categories:
 - [Unity3D]
tags: 
 - Unity3D
---

## 创建项目
![](https://image.aayu.today/uploads/2024/01/01/202401012208061.png)

## 安装包
确保 Visual Effect Graph 和 Shader Graph 已经安装，如果没有安装，可以在 Unity 的 Package Manager 中安装。

![](https://image.aayu.today/uploads/2024/01/01/202401012211254.png)

## 创建 Visual Effect Graph
在 Project 视图中，右键点击鼠标，选择 Create -> Visual Effects -> Visual Effect Graph，创建一个 Visual Effect Graph。

![](https://image.aayu.today/uploads/2024/01/01/202401012228110.png)

把 Visual Effect Graph 拖拽到 Hierarchy 场景中

## 创建 Trail 粒子特效

在画布中按空格，可以创建一个节点，输入 Trail，选择创建

![](https://image.aayu.today/uploads/2024/01/01/202401012229141.png)

添加三个变量，分别用来控制路径生成速率，颜色和范围大小

![](https://image.aayu.today/uploads/2024/01/01/202401012242140.png)

再添加一个变量，用来控制路径的随机生命周期

![](https://image.aayu.today/uploads/2024/01/01/202401012248250.png)

在更新粒子节点中，添加 conform to sphere，用来控制粒子的位置

![](https://image.aayu.today/uploads/2024/01/01/202401012309557.png)

在 GPU 事件中，更改粒子初始化生命周期为继承父级

![](https://image.aayu.today/uploads/2024/01/01/202401012310209.png)

在输出节点中，先取消激活粒子大小随生命变化，添加一个我们可以控制大小的节点，并设置随机范围为 0.001 到 0.02

![](https://image.aayu.today/uploads/2024/01/01/202401012316317.png)

再次激活粒子大小随生命变化，在选中节点时，修改 Inspector 中的组合模式为 Add，使得场景中既可以有我们设置的随机大小，又可以有粒子大小随生命变化的效果

![](https://image.aayu.today/uploads/2024/01/01/202401012320514.png)

框选全部，右键，Group Selection，把所有节点组合起来，命名为 Trail，我们的第一个特效就弄好了

![](https://image.aayu.today/uploads/2024/01/01/202401012322986.png)

## 创建 Beam 粒子特效

在旁边我们开始创建第一个特效，按空格，输入 empty，选择创建一个空粒子系统

系统节点里选择创建一个周期性爆炸粒子，并设置属性如下图

![](https://image.aayu.today/uploads/2024/01/01/202401012330490.png)

设置大小和颜色，为了避免周期性爆炸粒子在周期切换的时候闪烁，我们需要添加一个 add color over life，设置颜色随生命变化，透明度设置从 0 到 100 再到 0，这样就可以避免闪烁了

![](https://image.aayu.today/uploads/2024/01/01/202401012336171.png)

上面的 Blender Mode 设置为 Additive，效果会比 Alpha 模式好一点，可以自己根据情况改变

将我们设置好的第二种特效框选起来，命名为 Beam

![](https://image.aayu.today/uploads/2024/01/01/202401012343896.png)

## 创建 Shell 粒子特效
在画布旁边按空格，输入 simply，选择创建一个简单粒子特效

将纹理贴图设置为默认粒子，混合模式改为 Additive

![](https://image.aayu.today/uploads/2024/01/01/202401012347467.png)

创建一个变量用来控制粒子生成速率，并设置粒子的生成位置和速率属性，如下图

![](https://image.aayu.today/uploads/2024/01/01/202401012352110.png)

在粒子输出节点，控制粒子的大小和颜色

![](https://image.aayu.today/uploads/2024/01/02/202401020003836.png)

在粒子更新节点，为了让粒子的运动更加炫酷，就需要给粒子的位置叠加一个噪声，节点如下图

![](https://image.aayu.today/uploads/2024/01/02/202401020015044.png)

将我们设置好的第三种特效框选起来，命名为 Shell

可以随意更改颜色，大小，速率等变量，至此，就可以得到一个很炫酷的魔法球特效了

![](https://image.aayu.today/uploads/2024/01/02/202401020029423.png)
