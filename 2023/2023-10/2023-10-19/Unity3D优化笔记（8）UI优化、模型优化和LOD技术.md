---
title: Unity3D优化笔记（8）UI优化、模型优化和LOD技术
math: true
date: 2023-10-19 23:56:10
categories:
 - [Unity3D]
tags: 
 - Unity3D
---

## UI 优化

* 尽量避免使用 IMGUI 来做游戏时的 UI，因为 IMGUI 的开销比较大。
* ==如果一个 UGUI 的控件不需要进行射线检测，则可以取消勾选 Raycast Target。==
* 尽量==避免使用完全透明的图片和 UI 控件==。因为即使完全透明，我们看不见它，但它仍然会产生一定的性能开销。如果 UI 中一定要用到很多张完全透明的图片，则建议把这些完全透明的图片由单独的摄像机进行渲染，且这些 UI 不要叠加到场景摄像机的渲染范围内。
* ==尽量避免 UI 控件的重叠==。如果多个 UI 有重叠的部分，则会稍微增加一些额外的计算和渲染的开销。虽然这部分开销通常是非常小的，但我们最好也尽量避免这种情况。
* ==UI 的文字使用 TextMeshPro 比使用 Text 的性能更好。但是 TextMeshPro 对中文的支持不太好。==

## 模型优化

模型导入 Unity 后，可以选中这个模型，在 Inspector 窗口设置它的属性。

* 在 Model 选项卡

  * ==启用 Mesh Compression 可以压缩模型，压缩程度越高，模型精度越低，但是模型也会节省一些空间。==
  * 如果该模型不需要用代码来读写，则可以取消勾选 Read/Write Enabled。
  * 设置 Optimize Game Objects 可以优化模型，通常默认选择 Everything。
  * 如果该模型不需要使用法线，则可以把 Normals 设置为 None。
  * 如果该模型不需要用混合变形法线，则可以把 Blend Shape Normals 设置为 None。
  * 如果该模型不需要使用切线，则可以把 Tangents 设置为 None。
  * 如果该模型不需要用光照 UV 贴图，则可以取消勾选 Swap UVs 和 Generate Lightmap UVs。
* 对于 Rig 选项卡

  * Animation Type 如果选择 Generic Rig 会比 Humanoid Rig 性能更好，但无法使用动画重定向。一般使用 Humanoid Rig 是为了对人型的角色进行动画重定向，所以要根据自己的情况来选择。
  * ==如果模型不需要使用动画，例如一些完全不会动的石头等物体，则可以将 Animation Type 选择为 None。==
  * Skin Weights 默认是 4，对于一些不重要的动画对象，本变量可以设置为 1，这样可以节省计算量。
  * 建议勾选 Optimize Bones，这样会自动剔除没有蒙皮顶点的骨骼。
  * 勾选 Optimize Game Object 可以提高角色动画的性能，但是在某些情况下可能会导致角色动画出现问题，是否勾选要看动画效果而定。
* 对于 Animation 选项卡

  * 如果模型不需要使用动画，则可以取消勾选 Import Animation。
  * ==设置 Anim.Compression 可以调整动画的压缩方式==

    * Off 表示不压缩动画，这样动画文件可能会占用较大的空间，但是在运行时不会有任何信息损失，
    * Keyframe Reduction 表示使用关键帧算法来压缩动画，这样会显著减小动画文件的大小，同时保持相对较高的动画质量，
    * Optimal 表示会尽可能高地压缩网格，但是这样也会导致压缩时间增加。
* 对于 Materials 选项卡

  * 如果使用 Untiy 的默认材质，则可以把 Material Creation Mode 设置为 None。

Edit——Project Settings——Player——勾选 Optimize Mesh Data，这样一来，Unity 会在构建的时候中对网格数据进行优化处理，以达到提高游戏性能的效果。但是这样往往会修改网格，我们勾选之后应该要进行测试，确保没有问题，再确定启用它。

把多个模型的网格合并为一个网格。可以使用自己写代码，使用 Unity 自带的 CombineMeshes 方法，也可以使用资源商店的插件，在资源商店搜 Mesh Combine 可以搜索到相关的插件，例如 Easy Mesh Combine Tool 等插件。

减少模型的顶点、面、材质、骨骼、蒙皮网格。这一般由美术人员来完成。

## LOD（Level of Detail）

LOD 是 Level of Detail 的简称，意思是细节层次，它是一种优化技术。

LOD 的原理，就是我们可以为一个游戏对象设定多个模型，这些模型消耗的游戏性能由高到低排列。会根据摄像机距离模型的远近自动显示对应的模型。近的时候显示最精细的模型，距离中等的时候显示没那么精细的模型，远的时候显示粗糙的模型，最远的时候可以隐藏该模型。

==使用 LOD 技术能起到优化渲染性能的效果。但是使用 LOD 技术也会增加内存占用。==

在 Unity 中可以使用 LODGroup 组件来实现 LOD 技术。
