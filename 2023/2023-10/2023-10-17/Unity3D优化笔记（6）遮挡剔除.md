---
title: Unity3D优化笔记（6）遮挡剔除
math: true
date: 2023-10-17 13:43:03
categories:
 - [Unity3D]
tags: 
 - Unity3D
---

正常情况下，如果一个障碍物 A 挡住了后面的物体 B，虽然我们看不见物体 B，但是 Unity 仍然会消耗性能来渲染这个物体 B。这样 CPU 和 GPU 就会有一部分性能白白浪费在渲染物体 B 身上。

==如果想在一个障碍物挡住了后面的物体后，不渲染被挡住的物体，则可以使用遮挡剔除。==

官方文档：https://docs.unity3d.com/cn/current/Manual/OcclusionCulling.html

以一堵墙挡住几个小球为例，选中这堵墙，在 Inspector 窗口右上角的 Static 右侧的下拉菜单处选择 Occluder Static，则这堵墙就是遮挡物。分别选中这些小球，在 Inspector 窗口右上角的 Static 右侧的下拉菜单处选择 Occludee Static，则这些小球就是被遮挡物。

==注意，无论是勾选了 Occluder Static 还是 Occludee Static，勾选后物体就无法运动了。==

对于一个物体，两个标签都可以勾选，这样它既可以遮挡剔除别的物体，也可以被别的物体遮挡剔除。

==有时候被遮挡物只勾 Occludee Static，烘焙之后可能看不出遮挡剔除的效果，建议把 Occluder Static 也勾上，再重新烘焙，或许就能看出效果了。==

==选中摄像机，要确保它启用了 Occlusion Culling 属性。==

设置完之后，要创建一个遮挡区域，当摄像机处于这个遮挡区域中，遮挡剔除才会生效。

创建遮挡区域的方法：

* 方法 1、打开 Occlusion Culling 窗口。打开方法：Window——Rendering——Occlusion Culling——Bake。打开之后，选择 Object 选项卡，点击 Occlusion Areas，点击 Create New 右侧的 Occlusion Area。
* 方法 2、创建一个空物体，在它身上添加 Occlusion Area 组件。

Occlusion Area 组件的 Size 决定了遮挡剔除区域的范围，它越大，烘焙之后生成的遮挡剔除区域就越大。Center 控制遮挡区域中心点的世界坐标。==Is View Volume 表示是否定义视图体积，只有启用了这个选项，Occlusion Area 组件才可能生效。==

之后，要让遮挡剔除生效，还要在 Occlusion Culling 窗口的 Bake 选项卡中点击右下方的 Bake 按钮，进行烘焙，遮挡剔除才可能生效。==而且以后每次调整完场景的遮挡物、被遮挡物、Occlusion Area 组件的范围，都要这样烘焙一次==。如果点击旁边的 Clear 按钮，则会清除之前烘焙的数据。

烘焙完之后，当摄像机在 Occlusion Area 组件的范围内，则被遮挡的物体不会被渲染。遮挡物实际上遮挡了摄像机视锥体的范围，只要物体完全没有出现在摄像机视锥体的范围内，则都不会被渲染。==但是一旦物体的任意一小部分暴露在了摄像机视锥体的范围内，则这个物体整个会被渲染出来==

当摄像机移出了 Occlusion Area 组件的范围，则遮挡剔除会失效。

Occlusion Culling 窗口：

Object 选项卡。通过点击 All、Renderers、Occlusion Areas 按钮可以筛选 Hierarchy 窗口的内容。之后，在 Hierarchy 窗口或 Scene 窗口中选择一个筛选出来的游戏对象，就可以 Occlusion Culling 窗口中查看它的遮挡剔除设置。

Bake 选项卡。用于烘焙。==遮挡剔除必须烘焙之后才可能生效==。Set default parameters 用于将参数重置为默认值。

* Smallest Occluder 表示用于遮挡其它游戏对象的最小游戏对象的大小，以米为单位，数值越小遮挡的效果越精确，但是性能开销也越大。Smallest Hole 表示摄像机可以看到的最小间隙的直径，以米为单位，需要注意的是，设置过小的
* Smallest Hole 值可能会导致一些细微的间隙被错误地认为是可见的，从而导致部分遮挡物不被正确地剔除。
* Backface Threshold 的数值越小，烘焙所产生的文件所占空间就越小，但也可能造成视觉上的失真。Bake 按钮用于烘焙。Clear 按钮用于清除上一次烘焙的数据。

Visualization 选项卡。选择后，可以在 Scene 窗口看到遮挡剔除的效果。此时在 Scene 窗口可以看到三个选项。

* Camera Volumes。启用后，可以在 Scene 窗口看到黄色区域，当摄像机在这个黄色区域内，遮挡剔除才可能会生效，摄像机离开这个区域，则遮挡剔除就会失效。我们还可以看到灰线，这些灰线指示摄像机当前位置所对应的遮挡剔除数据中的单元格以及当前单元格中的细分。Bake 选项卡 Smallest Hole 参数设置定义了单元格内细分的最小大小，它的值越小，每个单元格产生的细分越多且越小，从而使精度提高并且文件增大。
* Visibility Lines。启用后，我们会看到绿色的区域，它表示摄像机可以看到的范围。
* Portals。启用后，我们可以看到一些线，它们代表遮挡数据中单元格之间的连接。

进行遮挡剔除的烘焙时，不会烘焙动态的游戏对象的信息到遮挡剔除的数据中。动态的游戏对象只能作为被遮挡物，而不能充当遮挡物。要让动态的游戏对象成为遮挡剔除中的被遮挡物，可以选中它，启用它身上 Mesh Renderer 组件身上的 Dynamic Occlusion 属性。

## 在代码中控制遮挡剔除

使用 Occlusion Portal 组件也可以实现遮挡剔除。

==例如可以在一堵墙上添加 Occlusion Portal 组件。而且这堵墙不勾选 Inspector 窗口右上角下拉菜单的 Occluder Static 和 Occludee Static，但是被它遮挡的物体仍然要勾选 Occluder Static 和 Occludee Static。==

设置好之后，打开 Occlusion Culling 窗口，在 Bake 选项卡进行烘焙。

这样一来，Occlusion Portal 组件就会生效。当取消勾选它的 Open 属性后，被这堵墙就会使用遮挡剔除。当勾选它的 Open 属性后，被这堵墙就不会使用遮挡剔除。我们可以使用代码来控制 Open 属性，控制这堵墙在什么时候使用遮挡剔除，什么时候不使用遮挡剔除。

Occlusion Portal 组件的 Center 属性控制了中心的位置，Size 属性控制了遮挡的范围。点击 Edit Bounds 左侧的按钮后，可以在 Scene 窗口手动调节 Occlusion Portal 组件的遮挡范围。每次调整完，或者修改过场景，都要重新烘焙。
