---
title: Unity3D优化笔记（9）合并网格、动画、音频、物理优化
math: true
date: 2023-10-20 21:34:24
categories:
 - [Unity3D]
tags: 
 - Unity3D
---

## 合并网格（Mesh Combine）

对使用相同材质的模型可以使用第三方插件（例如：Easy Mesh Combine Tool）合并网格

合并后，所有被合并的模型被整合成一个新的模型，DrawCall 和 Shader Caster 会下降，但顶点个数和三角面个数可能会增多，所以需要根据实际情况来使用

## 动画优化

恰当地设置 Animator 组件的 Culling Mode。

* Always Animate 表示如果该动画不可见，也会播放它。
* ==Cull Update Transformations 表示如果该动画不可见，则不会渲染该动画，但是依然会根据该动画的播放来改变游戏对象的位置、旋转、缩放==，这样是常用的选项。
* Cull Completely 表示完全不会播放该动画，不但不会渲染该动画，而且也不会改变游戏对象的位置、旋转、缩放。

禁用 SkinMesh Renderer 组件的 Update When Offscreen 可以让角色在不可见的时候动画不更新，这样可以减少计算量，提升性能。

==对于 Animator 组件，可以使用 Animator.StringToHash 方法获得指定字符串的哈希值==，再把它作为参数传入 Animator 型对象.GetXXX 方法和 Animator 型对象.SetXXX 方法中进行使用。

==不用的 Animation 组件和 Animator 组件可以考虑删掉，因为只要它们存在，就会消耗性能来检测当前的状态和过渡条件。==

==一些简单的动画可以使用 DoTween、iTween 等插件实现==，而不需要每个动画都用 Animator 来实现。

## 音频优化

Unity 支持后缀为.wav、.ogg、.mp3 的音频文件，但==建议使用 .wav，因为 Unity 对它的支持特别好==。注意：Unity 在构建项目时总是会自动重新压缩音频文件，因此无需刻意提前压缩一个音频文件再导入 Unity，因为这样只会降低该音频文件最终的质量。

把音频文件导入 Unity 后，选中它，可以在 Inspector 窗口设置它的属性。

* 建议勾选 Force To Mono，这样就会把这个音频文件设置为单声道。可以节省该资源所占据的空间。因为很少有移动设备实际配备立体声扬声器。在移动平台项目中，将导入的音频剪辑强制设置为单声道会使其内存消耗减半。此设置也适用于没有立体声效果的任何音频，例如大多数 UI 声音效果。

对于 Load Type 选项

* 小文件（小于 200kb）选择 Decompress on Load
* 中等大小的文件（大于等于 200kb）选择 Compressed In Memory
* 比较大的文件（如背景音乐）选择 Streaming

对于 Compression Format 的选项

* PCM 表示不压缩
* Vorbis 表示压缩，但也会尽量保证音频的质量
* ADPCM 表示压缩，且压缩的程度比 Vobis 更高

==由于 PCM 不会压缩音频，所以占用的空间大，应尽量少用，长时间的音频文件可以使用 Vorbis，短时间的音频文件可以使用 ADPCM==。

Sample Rate Setting 用于控制音频文件的采样率，对于移动平台，采样率不需要太高，建议选择 Override Sample Rate，然后在下方的 Sample Rate 选择 22050Hz，一般这样就够用了。

## 物理优化

==使用简单的碰撞器进行碰撞检测==，如球体碰撞器、盒子碰撞器、胶囊体碰撞器，==少用网格碰撞器等复杂的碰撞器==。即使用多个简单的碰撞器组合在一起，也往往比使用网格碰撞器的性能要好。

如果要把多个碰撞器组合成一个碰撞器，可以用复合碰撞器。

==如果同一个功能既可以用碰撞器来做，也可以用触发器来做，则往往使用触发器来做，性能更好。==

==尽量减少刚体组件，因为刚体组件的物理计算较多。==

如果勾选刚体组件的 Is Kinematic，则性能会有所提高。但这样一来，这个刚体只会给别的刚体施加力，自己不会受到别的刚体施加的力的作用。

Edit——Project Settings——Player——勾选 Optimization 下方的 Prebake Collision Meshes，可以提高碰撞的效率，但是构建游戏的时间会增长。

Edit——Project Settings——Physics 或者 Physics 2D——设置 Layer Collision Matrix。它规定了哪些 Layer 层的游戏对象可以彼此碰撞，哪些 Layer 层的游戏对象会忽略碰撞。如果有些 Layer 层的游戏对象之前不需要进行碰撞，则可以在这里设置，取消勾选则表示不会碰撞。

Edit——Project Settings——Time——稍微调大 Fixed Timestep，这样可以稍微提升游戏性能，但是物体的运动可能会出现问题。
