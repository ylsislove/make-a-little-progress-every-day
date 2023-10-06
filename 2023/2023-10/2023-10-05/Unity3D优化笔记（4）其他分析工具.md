---
title: Unity3D优化笔记（4）其他分析工具
math: true
date: 2023-10-05 23:49:32
categories:
 - [Unity3D]
tags: 
 - Unity3D
---

## Unity Frame Debugger 窗口（帧调试器窗口）

Frame Debugger 窗口也叫帧调试器窗口，用于查看每一帧的画面是如何渲染出来的，可以详细查看这一帧的绘制过程。

打开 Frame Debugger 面板的方式：

* Window——Analysis——Frame Debugger

按下“Enable”，则会启动帧调试，此时如果运行了游戏，则会自动暂停，然后当前这帧的渲染情况可以在这个窗口中查看。

上方的 X of X 表示绘制过程中有多少步，可以查看下一步或上一步。

如果要禁用帧调试，可以按下“Disable”。

==用 Frame Debugger 窗口查看当前一帧的每一步时，可以配合 Stats 窗口使用，以此来确定哪一个物体造成的性能开销较大==。

绘制的步骤越少，性能越好。

Frame Debugger 窗口也能看到每一帧的 Shader 信息，但是需要有一定 Shader 基础才能看懂。

* 大多数平台都支持帧调试器的使用，可以用手机的数据线成功连接到电脑，在手机上运行 Unity 的游戏，Frame Debugger 窗口中会多出该手机设备供我们选择，我们就可以分析该手机设备上运行的 Unity 项目的性能。
* 也可以让手机和电脑都连接同一个 wifi，这样一来，Frame Debugger 窗口中也会多出该手机设备供我们选择，我们就可以分析该手机设备上运行的 Unity 项目的性能。
* 但是要注意，构建时必须在 Project Settings 窗口中勾选“Development Build”。而且有些平台可能不支持 Frame Debugger 的使用，例如 WebGL 平台。

## Memory Profiler

==Memory Profiler 可以查看游戏当前一帧具体的内存使用情况==，我们可以详细地看到各种东西占用了多少内存。

如果发现某样东西占用了过高的内存，则可以考虑问题是不是出在它身上，从它身上入手来进行优化。也可以分析是不是存在内存泄漏问题，即可以分析是不是某些资源一直占着内存得不到释放，才导致内存占用过高。

旧版 Unity 安装它的方法：
Windows——Package Manager——All packages——Memory Profiler——Install
如果找不到，说明它可能在当前 Unity 版本下是预览版，可以在 Advanced 下拉菜单选择 Show preview packages，再查找它出来安装

安装方法：
Edit——Project Settings——Package Manager——勾选 Enable Pre-release Packages——关闭窗口——Window——Package Manager——点击左上方的 + 号——Add package by name——输入 com.unity.memoryprofiler——点击 Add
注意：下载的时候可能需要科学上网。

安装完后打开方式：
Window——Analysis——Memory Profiler

点击 Capture New Snapshot 会创建当前这一时刻的内存快照，可以看到这一帧的内存情况。==它默认会存储在与 Assets 文件夹同级的目录的一个叫做 MemoryCaptures 的文件夹中。==如果要修改这个路径，也可以点击右上角的三点，点击 Open Preferences，修改 Memory Snapshot Storage Path 的值。

Single Snapshot 表示用来分析单张内存快照，Compare Snapshots 可以通过对比来分析两张内存快照。

选中一张内存快照后，点击 Tree Map 可以看出各种资源和脚本所占用的内存，选中其中一块，可以具体地看出到底它们分别占用多少内存。如果某个名字的资源占用的内存高，那么可以考虑问题是不是出在它身上，这样我们就可以从它身上入手来进行优化。但是要注意，有一些名字的资源可能在项目中不找到，因为它们是 Unity 自带的资源。

==在 Unity 编辑器中运行游戏，Memory Profiler 记录的内存情况可能会不准确==，它会把 Unity 编辑器的一些内存占用情况也记录进去。==我们应该把游戏构建到电脑或者手机，然后在电脑或者手机上运行游戏，再用 Memory Profiler 拍内存快照来分析，此时这些内存快照记录的数据才是准确的。==

构建项目到电脑时，应勾选 Build Settings 窗口的 Development Build、Autoconnect Profiler，这样当发布的游戏运行时，就可以在 Unity 引擎的 Memory Profiler 左上角的下拉菜单选择关联刚才发布的程序，拍下快照查看它的内存占用情况。

用手机数据线连接到电脑，在手机上运行游戏，并在电脑分析，也必须勾选 Build Settings 窗口的 Development Build、Autoconnect Profiler，而且手机上应勾选“开启开发者选项”、“USB 调试”、“USB 安装”。当用手机数据线连接到电脑，Memory Profiler 左上的下拉菜单可以选择连接到电脑的手机设备。

## Unity Physics Debugger 窗口（物理调试窗口）

Physics Debugger 窗口也叫物理调试窗口，使用它可以在 Scene 窗口中查看当前场景中游戏对象的碰撞器、触发器、刚体、关节等与物理模拟相关的东西的范围。尤其是在游戏对象较多的场景中，==使用物理调试窗口可以方便我们观看它们的范围==。

打开方法：Window——Analysis——Physics Debugger

官方文档：https://docs.unity3d.com/cn/current/Manual/PhysicsDebugVisualization.html

在 Scene 窗口中勾选 Collision Geometry，则会在 Scene 窗口中显示游戏对象的碰撞几何体，具体的情况可以在 Physics Debugger 窗口中查看到和修改。如果勾选 Mouse Select，则会开启鼠标悬停和鼠标选择功能，方便查看碰撞几何体。

点击右上方的 Reset 可以重置 Physics Debugger 窗口中的设置。

* Selected Object Info 表示当前选中的游戏对象的信息。
* Show Physics Scene 表示要在哪些场景中显示碰撞几何体。
* Show Layers 表示哪些 Layer 层的游戏对象要显示碰撞几何体。
* Show Static Colliders 表示显示静态的碰撞器组件的范围。
* Show Triggers 表示显示勾选了 Is Trigger 属性的碰撞器的范围。
* Show Rigidbodies 表示显示 Rigidbody 组件的范围。
* Show Kinematic Bodies 表示显示勾选了 Is Kinematic 的 Rigidbody 组件的范围。
* Show Articulation Bodies 表示显示 Articulation Body 组件的范围。Articulation Body 组件用于模拟机器人、车辆等物体的关节行为。例如可以实现机器人的动作、车辆的悬挂等物理效果。
* Show Sleeping Bodies 表示显示处于睡眠状态的 Rigidbody 组件的范围。当一个刚体在一段时间内没有受到外力作用，则会自动进入睡眠状态，进入睡眠状态的刚体不会参与物理模拟。当它再次受到外力的作用时，它就会从睡眠状态中唤醒，此时就又会重新参与物理模拟了。

Collider Types

* Show BoxColliders 表示显示盒子碰撞器的范围。
* Show SphereColliders 表示显示球体碰撞器的范围。
* Show CapsuleColliders 表示显示胶囊体碰撞器的范围。
* Show MeshColliders(convex)表示显示网格碰撞器的范围。
* Show MeshColliders(concave)表示显示网格碰撞器的范围。
* Show Terrain Colliders 表示显示地形碰撞器的范围。

Colors

* Static Colliders 表示显示静态的碰撞器的颜色。
* Triggers 表示显示勾选了 Is Trigger 属性的碰撞器的颜色。
* Rigidbodies 表示显示 Rigidbody 组件的颜色。
* Kinematic Bodies 表示显示勾选了 Is Kinematic 的 Rigidbody 组件的颜色。
* Articulation Bodies 表示显示 Articulation Body 组件的颜色。
* Sleeping Bodies 表示显示处于睡眠状态的 Rigidbody 组件的颜色。
* Variation 表示要显示的颜色与随机颜色混合的程度。调节这个变量，会影响所有显示的几何碰撞体的颜色。

Rendering

* Transparency 控制绘制的碰撞几何体的透明度。
* Force Overdraw，勾选后，绘制的碰撞集合体会更加清晰。
* View Distance 控制能在 Scene 窗口中看到碰撞几何体的距离。
* Terrain Tiles Max 控制能在 Scene 窗口中看到 Unity 自带的地形系统 Terrain 的瓦片的最大数量。

## Unity Import Activity 窗口

==Import Activity 可以查看项目中的资源的信息。例如什么时候导入这个资源的、这个资源的文件大小等==。

打开方法：

* Window——Analysis——Import Activity
* 右击一个资源，点击 View in Import Activity Window。
* 在 Inspector 窗口中右击 Inspector，点击 Open in Import Activity Window。

官方文档：https://docs.unity3d.com/2021.2/Documentation/Manual/ImportActivityWindow.html

点击左上方的 Show Overview 可以看出项目中依赖最多的资源和导入时花费时间最长的资源。

左上方 Options 的选项

* Use relative timestamps：勾选后，资源的最后导入时间会以“几小时前”、“几天前”这样的格式显示。取消勾选，则资源的最后导入时间会以“日-月-年小时:分钟:秒”的格式显示。
* Show previous imports：勾选后，选中一个资源，则会显示这个资源以前导入时的信息，也能在 Library 文件夹中查看一个资源有多少个历史版本。但是要注意，当 Unity 的 AGC（Artifact Garbage Collection）运行时，或者重新启动 Unity 时，以前导入的资源的信息会被清空掉。如果要关闭 AGC 的执行，则可以取消勾选“Edit——Project Settings——Editor——Remove unused Artifacts on Restart”，也可以在脚本中通过 EditorUserSettings.artifactGarbageCollection 来禁用它。
* Include PreviewImporter：勾选后，会包含由预览窗口生成的 Artifacts。

右上方的搜索框可以搜索项目中的资源。

左侧的 Asset 表示资源，Last Import 表示最后一次导入这个资源是在什么时候，Duration(ms)表示最后一次导入这个资源时花费了多少毫秒才将它导入到项目中。

* 选中一个资源后，可以在右侧看到它的信息。
* 点击 Asset，Project 窗口会在项目中定位到该资源存放的位置。
* GUID 表示 Unity 分配给这个资源的全局唯一标识。
* Asset Size 表示这个资源的文件大小。
* Path 表示这个资源在项目中的路径。
* Editor 表示是 Unity 的哪个版本创建这个资源的 Artifact 的。
* Timestamp 表示这个资源的 Artifact 被创建时的时间，它对应 Library 文件夹中指定文件的 Timestamp 的值。
* Duration 表示导入这个资源所花费的时间。
* Reason for import 表示导入原因，即这个资源最近重新导入的描述，以及这个资源相关依赖类型的详细信息。当导入原因有多个是，可以用搜索栏进行查找。
* Produced Files/Artifacts 表示这个资源最后一次导入 Unity 时，在 Library 文件夹中呈现的 Artifact 的路径。通常每个资产只有一个 Artifact，有时也可能有多个。
* Dependencies 表示这个资源依赖的其它资源，如果修改它们，可能会导致这个资源被重新导入到 Unity。如果 Dependencies 的数量过多，可以使用搜索栏查找。

## Unity Code Coverage 窗口

==Code Coverage 用来评估我们编写的代码，在游戏测试运行的时候有多少被执行了==。如果有一部分代码没有被执行，我们就要考虑是不是我们代码的逻辑有问题，从而改进我们的代码。

打开方法：Window——Analysic——Code Coverage

官方文档：https://docs.unity.cn/Packages/com.unity.testtools.codecoverage@1.1/manual/index.html

使用思路：

先勾选 Enable Code Coverage，然后勾选 Auto Generate Report，再点击 Start Recording 按钮，接着点击播放按钮运行游戏。点击 Start Recording 按钮后，它会变成 Stop Recording，测试完毕后点击它，就会停止测试。然后我们就可以在 Result Location 的路径找到生成的报告，从中看出在测试的时候有多少代码被执行了。

* Results Location 表示生成的报告要存放到的路径。
* History Location 表示生成的报告的历史记录要存放到的路径。必须勾选了 Generate History 才会生成。
* Enable Code Coverage 表示启用代码覆盖，测试之前要勾选它。
* Included Assemblies 表示测试的时候要考虑哪些程序集的代码。
* Included Paths 表示测试的时候要考虑哪些文件夹或文件中的代码。
* Excluded Paths 表示测试的时候不考虑哪些文件夹或文件中的代码。
* Generate HTML Report，勾选后，生成报告时，会以 html 的格式来生成报告。如果取消勾选，则会以其它形式来生成报告，但是这样不方便我们观看。建议勾选。
* Generate Summary Badges，勾选后，生成的报告的文件夹中，会额外生成.svg 和.png 后缀的文件，概括这次测试中有百分之几的代码被使用了。
* Generate History，勾选后，生成报告时，会自动在 History Location 的路径生成历史记录。
* Generate Additional Metrics，勾选后，生成报告时，报告中会有额外的衡量指标。
* Auto Generate Report，勾选后，我们点击 Start Recording 开始测试，然后点击 Stop Recording 结束测试后，会自动在 Results Location 的路径生成报告。
* Clear Data 清空上一次测试的数据。
* Clear History，清空 History Location 路径中的所有历史记录。
* Generate from Last，根据上一次测试的数据，在 Results Location 的路径生成报告。
* Start Recording，开始测试。

## Unity Profile Analyzer 窗口

Profile Analyzer 配合 Profiler 使用。当我们使用 Profiler 收集了数据之后，不要关闭 Profiler，并且打开 Profile Analyzer，把 Profiler 收集的数据导入到 Profile Analyzer，==使用 Profile Analyzer 可以帮助我们选出一段数据中最具有代表性的一帧，方便我们进行性能分析。也能看出收集的数据整体的一些情况，例如中位数、平均值、最大值、最小值等==。

Profile Analyzer 也可以比较两段数据的性能开销。

打开方法：Window——Analysis——Profile Analyzer

官方文档：https://docs.unity3d.com/Packages/com.unity.performance.profile-analyzer@1.2/manual/index.html

Profile Analyzer 要配合 Profiler 使用，点击 Open Profiler Window 可以打开 Profiler，此时 Open Profiler Window 会变成 Close Profiler Window，点击 Close Profiler Window 会关闭打开的 Profiler

==左上方的 Mode 有两种模式，选择 Single 会分析一段数据，选择 Compare 会分析两段数据，可以对这两段数据作对比。==

左上方的 Export 可以把分析的结果导出到本地，以便我们查看。

在 Profiler 收集了一段数据之后，可以点击 Profile Analyzer 中的 Pull Data，这样就会导入那段数据到 Profile Analyzer，方便我们分析。点击 Save，则会把数据保存到本地，点击 Load，则可以从本地载入数据。

在上方的图表中，我们可以拖选其中的一段数据，然后在下方的 Top 10 markers on median frame 下看到最具有代表性的一帧，==点击它，则 profiler 窗口中也会自动选中那一帧==。

Top 10 markers on median frame 下方右侧是 10 个最具有代表性的 Marker。

==Marker 表示代码的标记==。Unity 执行的一些关键的方法或者一段关键的代码会被标记，方便我们查看这些方法和代码的性能。

此时在下方的 Marker Details for current selected range 下方可以看到选中的这段数据的信息。

* Filters 的选项用于对数据进行筛选。
* Name Filter 表示筛选含有指定字符串的结果。
* Exclude Names 表示筛选不含有指定字符串的结果。
* Thread 表示筛选指定线程的结果
* Depth Slice 表示筛选指定调用栈的深度。
* 点击 Analyze，则会根据 Filters 的选项的设置重新进行分析，可以在下方的 Marker Details for currently selected range 的下方看到结果。

## Unity IMGUI Debugger 窗口

==IMGUI Debugger 窗口用于查看 Unity 编辑器中的 IMGUI 控件的信息==。例如 Scene 窗口、Game 窗口实际上也是用 IMGUI 写的，我们可以查看其中 IMGUI 控件的信息。

==如果我们在 OnGUI 方法中写了代码来显示 IMGUI 控件，也可以在 IMGUI Debugger 窗口查看这个 IMGUI 控件的信息。==

打开方法：

* Window——Analysis——IMGUI Debugger
* Alt+5

在 <Please Select> 和它右边的下拉菜单中，可以选择要查看哪些 IMGUI 控件。

Show Overlay。启用 Show Overlay，则选择 IMGUI 控件时，能在 Unity 的编辑器中看到选择了哪个控件。

Force Inspect Optimized GUI Blocks。有时候 Unity 可能会对 IMGUI 进行优化，把多个 IMGUI 控件合并为一个。此时如果我们要查看每一个 IMGUI 控件的信息，则可以启用 Force Inspect Optimized GUI Blocks

Pick Style。按住 Pick Style，然后在 Unity 的编辑器中选择一个 IMGUI 控件，可以看到它的信息。
