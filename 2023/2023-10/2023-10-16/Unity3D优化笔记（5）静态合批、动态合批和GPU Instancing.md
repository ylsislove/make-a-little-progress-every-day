---
title: Unity3D优化笔记（5）静态合批、动态合批和GPU Instancing
math: true
date: 2023-10-16 13:38:40
categories:
 - [Unity3D]
tags: 
 - Unity3D
---

## 静态合批

静态合批也叫静态批处理，是 Unity 的一种优化技术。

==对于始终静止不动的物体使用静态合批后，CPU 会把它们合并为一个批次发送给 GPU 处理，这样可以减少 Draw Call 带来的性能消耗，从而提升游戏性能。==

官方文档：https://docs.unity3d.com/cn/current/Manual/static-batching.html

要使用静态合批，必须确保 Edit——Project Settings——Player——Other Settings——Static Batching 是勾选的。

把一个物体设置为静态的方法：

* 选中该物体，点击在 Inspector 窗口右上角的 Static 右方的下拉菜单，选择 Batching Static。

==使用静态合批虽然可以提升游戏性能，但是设置为静态的物体在整个游戏中就不能再运动了，强行使它们运动会出问题。==

而且即使按照以上步骤进行了静态合批，也不一定保证会成功，必须满足以下全部条件，静态合批才会成功：

1. 游戏对象处于激活状态。
2. 游戏对象有一个 Mesh Filter 组件，并且该组件已启用。
3. Mesh Filter 组件具有对网格的引用。
4. 网格已启用 Read/Write 功能。
5. 网格的顶点计数大于 0。
6. 该网格尚未与另一个网格组合。
7. 游戏对象有一个 Mesh Renderer 组件，并且该组件已启用。
8. 网格渲染器组件不将任何材质与 DisableBatching 标记设置为 true 的着色器一起使用。
9. 要批处理在一起的网格使用相同的顶点属性。例如，Unity 可以将使用顶点位置、顶点法线和一个 UV 的网格与另一个 UV 进行批处理，但不能将使用顶点定位、顶点法线、UV0、UV1 和顶点切线的网格进行批处理。

即使静态合批成功，==合出来的每个批次可以包含的网格顶点数是有限的，最多是 64000 个顶点。如果超过这个数，则会创建到另一个批次中。==

如果要在游戏运行时进行静态合批，则可以使用 StaticBatchingUtility 类的 Combine 方法。

StaticBatchingUtility.Combine(GameObject 根物体)

* 对指定的根物体的所有子孙物体进行静态合批。
* 只有当它们符合静态合批的所有条件，静态合批才会成功。
* 成功之后，这些物体就不能再运动了，强行运动会出问题。但是该根物体仍然允许运动。

StaticBatchingUtility.Combine(GameObject[] 要进行静态合批的游戏对象, GameObject 根物体)

* 对指定的游戏对象进行静态合批，并指定它们静态合批的根物体。
* 只有当它们符合静态合批的所有条件，静态合批才会成功。
* 成功之后，这些物体就不能再运动了，强行运动会出问题。但是该根物体仍然允许运动。

## 动态合批

动态合批也叫动态批处理，是 Unity 的一种优化技术。

==对移动的物体使用动态合批后，则 Unity 不会一个个绘制它们，而是把它们合并为一个批次（Batch）==，再由 CPU 把它们一次性提交给 GPU 进行处理，这样可以减少 Draw Call 带来的性能消耗，从而提高性能。

官方文档：https://docs.unity3d.com/cn/current/Manual/dynamic-batching.html

==动态合批默认是由 Unity 自动完成==。可以在 Edit——Project Settings——Player——Other Settings——Dynamic Batching 查看。==默认 Dynamic Batching 是勾选的==，当条件满足时，==Unity 会自动对使用了相同材质（Material）的物体进行动态合批==。如果取消勾选，则不会进行动态合批。

即使勾选了 Dynamic Batching，也必须同时满足以下条件，动态合批才会成功：

1. Unity 不能对包含超过 900 个顶点属性和 225 个顶点的网格应用动态批处理。这是因为网格的动态批处理对每个顶点都有开销。例如，如果你的着色器使用顶点位置、顶点法线和单个 UV，那么 Unity 最多可以批处理 225 个顶点。然而，如果你的着色器使用顶点位置、顶点法线、UV0、UV1 和顶点切线，那么 Unity 只能批处理 180 个顶点。
2. 如果 GameObjects 使用不同的材质实例，Unity 就不能将它们批处理在一起，即使它们本质上是相同的。唯一的例外是阴影施法者的渲染。
3. 带有光贴图的游戏对象有额外的渲染参数。这意味着，如果你想批处理光照贴图的游戏对象，它们必须指向相同的光照贴图位置。
4. Unity 不能完全将动态批处理应用于使用多通道着色器的 GameObjects。

几乎所有的 Unity 着色器都支持正向渲染中的多个光源。为了实现这一点，他们为每个光处理一个额外的渲染通道。Unity 只批处理第一个渲染通道。它不能批处理额外的逐像素灯光的绘制调用。

遗留延迟渲染路径不支持动态批处理，因为它在两个渲染通道中绘制 GameObjects。第一个通道是灯光预通道，第二个通道渲染 GameObjects。

==其中我们要注意的是，物体必须使用相同的材质，才有可能成功进行动态合批。==

==使用动态合批往往能减少 CPU 和 GPU 的开销，提升游戏性能，但同时也会占用一定的内存。==

是否要开启动态合批，要根据自己的项目来定。可以尝试启用，在性能分析器中看看效果如果，如果效果好，再确定启用它。

## GPU Instancing

GPU Instancing 是 Unity 的一种优化技术。

==使用 GPU Instancing 可以在一个 Draw Call 中同时渲染多个相同或类似的物体==，从而减少 CPU 和 GPU 的开销。

官方文档：https://docs.unity3d.com/Manual/GPUInstancing.html

要启用 GPU Instancing，我们可以选中一个材质，然后在 Inspector 窗口勾选 Enable GPU Instancing，这样就可以了。

但是即使勾选了 Enable GPU Instancing，也不一定会成功。

要成功使用 GPU Instancing 进行优化，游戏对象必须同时满足以下条件：

1. ==使用相同的材质和网格。==
2. 材质的着色器必须支持 GPU Instancing。例如标准着色器和表面着色器就支持 GPU Instancing。
3. 网格的顶点布局和着色器必须相同。如果网格的顶点布局或着色器不同，那么它们就无法被合并成一个实例。
4. 每个实例需要有不同的变换信息（例如位置、旋转、缩放）。虽然多个实例可以使用相同的材质和网格，但是它们必须拥有不同的变换信息才能被正确地实例化并渲染出来。

另外需要注意的是，GPU Instancing 与 SRP Batcher 不兼容。如果项目使用了 SRP Batcher，并且配置为优先使用 SRP Batcher 而不是 GPU 实例化，启用 GPU 实例化可能不会生效。SRP Batcher 是 Unity 提供的一种渲染优化技术，它可以将多个网格合并成单个批次进行渲染，从而提高性能。在这种情况下，GPU 实例化将被忽略。

==使用 GPU Instancing 往往能减少 CPU 和 GPU 的开销，提升游戏性能，但同时也会占用一定的内存。==

是否要启用 GPU Instancing，要根据自己的项目来定。可以尝试启用，在性能分析器中看看效果如果，如果效果好，再确定启用它。

一般来说，当场景中有大量重复的网格实例时，可以尝试启用 GPU Instancing。例如场景中有大量树木、草地、石块等，这些实例具有相同的网格和材质，只是位置、颜色等属性稍有差异，那么启用 GPU Instancing 或许能够显著提高性能。
