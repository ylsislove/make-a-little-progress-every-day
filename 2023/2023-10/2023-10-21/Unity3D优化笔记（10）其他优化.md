---
title: Unity3D优化笔记（10）其他优化
math: true
date: 2023-10-21 22:52:00
categories:
 - [Unity3D]
tags: 
 - Unity3D
---

## 代码优化

==使用 AssetBundle 作为资源加载方案。==而且经常一起使用的资源可以打在同一个 AssetBundle 包中。尽量避免同一个资源被打包进多个 AB 包中。

压缩方式尽量使用 LZ4，少用或不要用 LZMA 的压缩方式。如果确定后续开发不会升级 Unity 版本，则可以尝试启用打包选项 BuildAssetBundleOption.DisableWriteType，这样 TypeTree 信息不会被打到 AB 包中，可以极大减小包体大小以及运行加载时的内存开销。

使用 AssetBundle 或者 Addressables 加载的资源，如果不使用，要记得卸载它们，否则会造成内存泄漏。

不用的资源要释放掉，不用的引用类型的变量也要赋值为 null，不要让它们一直占着内存中。

==加载资源时尽量使用异步加载。==

==频繁创建和销毁对象，可以使用对象池。==

==切换场景时，旧的场景要释放掉，不用的资源也可以考虑释放掉==，也可以考虑用 System.GC.Collect 来进行一次垃圾回收。

==锁定游戏的帧率==。帧率为 30，游戏会明显卡顿，但是对于手游来说，消耗手机的电量比较少。帧率为 45，游戏有一点点卡，但还凑合，消耗电量中等。帧率为 60，游戏很流畅，但消耗手机的电量会比较多。可以用 Application.targetFrameRate 来锁定帧率，也可以用 UnityEngine.Rendering 命名空间中的 OnDemandRendering.renderFrameInterval 来锁定帧率。

尽量少用 foreach 语句，可以改为 for 语句。因为每次使用 foreach 语句会造成微量的内存垃圾。

要判断 GameObject 型对象.tag 是不是某个标签，使用 GameObject 型对象.CompareTag 方法会更高效。

==尽量少用 GameObject.Find 方法和 Object.FindObjectOfType 方法来查找游戏对象，可以提前把要查找的游戏对象存储在变量、列表、字典等容器中，方便查找。也可以用 GameObject.FindGameObjectWithTag 方法来查找游戏对象。==

==在 UI 显示字符串的时候，如果一些内容是固定的，我们可以把它拆分开来，这样可以减少使用 + 号来拼接的次数，减少内存垃圾的产生==。例如“杀敌数：999”，其中“杀敌数：”是固定的，冒号后面的数字才是会变的，那么我们可以用两个 Text 组件分别记录它们，改变的时候只改变冒号后面的数字。

==频繁对字符串赋新的值，或者频繁拼接字符串的时候，可以使用 StringBuilder 代替 string==

如果要频繁操作某脚本，不要每次都用 GetComponent 方法来获取这些脚本。可以用一个变量存储起获得的这个脚本，之后要访问它，就直接访问这个变量即可。也可以考虑在生命周期方法 Awake 或者 Start 中声明变量来存储，之后访问这个变量即可。

==尽量少用正则表达式。虽然正则表达式的形式看上去比较简便，但是使用它会造成一定的性能消耗，且会产生内存垃圾。==

尽量少用 LINQ 语法，因为每次使用 LINQ 都会产生一定量的内存垃圾。

==尽量少用 Camera.main 来访问主摄像机==，因为每次访问它，实际上 Unity 都是从场景中查找它的。可以声明一个变量存储它，在生命周期方法 Awake 或 Start 中获取主摄像机的应用。

==在 Animator、Shader 中使用 Get 方法和 Set 方法时，不传入字符串作为参数，而是传入哈希值==。例如 Animator 组件可以使用 Animator.StringToHash 方法获得指定字符串的哈希值，再把它作为参数传入 Animator 组件的 Get 方法或 Set 方法中进行使用。例如 Shader，则可以用 Shader.PropertyToID 方法来获取指定属性的 ID

使用非分配物理 API。例如使用 Physics.RaycastNonAlloc 方法代替 Physics.RaycastAll 方法，使用 Physics.SphereCastNonAlloc 方法代替 Physics.SphereCastAll 方法，以此类推。Physics2D 类也有类似的方法。

一般情况下，整数的数学运算比浮点数的数学运算效率高，浮点数的数学运算比矢量的数学运算效率高。可以灵活运用数学的加法交换律、加法结合律、乘法交换律、乘法结合律，在保证结果不变的前提下，调整运算顺序，减少浮点数的数学运算和矢量的数学运算。

使用高效的算法进行计算

==每次执行 Debug.Log 来打印信息会消耗极少量的性能，如果要在游戏正式发布之后不执行某些 Debug.Log 的语句，但又不想把这些代码删掉，则可以使用宏来禁止在游戏正式发布之后执行 Deubg.Log 的语句==。例如使用#if 语句或者 Conditional 特性。

尽量减少在生命周期方法 Update、FixedUpdate、LateUpdate 中的逻辑。其中有些不需要频繁执行的逻辑，可以使用协程或者 Invoke 方法，每隔指定的秒数执行一次或每隔指定的帧数执行一次。

尽量避免频繁的装箱拆箱操作。也可以使用泛型，这样就能避免装箱拆箱。但是要注意，Lua 热更新对泛型的支持不太好。

==如果物体身上添加了刚体组件，则尽量用刚体组件的方法来移动它，而不是用 Transform 类的方法来移动它。==

如果物体身上添加了 CharacterController 组件，则尽量用 CharacterController 组件的方法来移动它，而不是用 Transform 类的方法来移动它。同理，如果物体身上添加了刚体组件，则应尽量用刚体组件的方法来移动它，而不是用 Transform 类的方法来移动它。

==应尽量避免 DontDestroyOnLoad 中加载的资源过多==，因为它在切换场景的时候不会被释放，声明的变量以及加载的资源会一直占用着内存。我们可以考虑把一些资源不用的资源释放掉，需要的时候再加载它。

不使用组件可以删掉，这样可以节省一些内存。常见的有 AudioSource 组件、Animator 组件、Animation 组件等，如果它们不需要使用，则可以删掉。

写一个类继承 AssetPostProcessor，然后定义里面特定的方法，以此来自动设置资源导入 Unity 之后的属性。

尽量避免闭包。因为闭包会产生额外的内存开销。

## 场景优化

对始终静止不动的游戏对象使用静态合批技术。

尽量使用同一个材质，以便使用动态合批技术。

使用 GPU Instancing 技术。

使用遮挡剔除。

进入游戏后的第一个场景要尽量简单，这样可以减少游戏的启动时间。可以先进一个简单的场景，再进行异步加载，之后再进入游戏的主要的场景。

尽量避免 Hierarchy 窗口的层级结构过深。例如一个物体有很多个子物体，这些子物体又有其它子物体，这些子物体又有其它子物体，继续这样下去就会导致层级结构过深，我们应尽量减少这种情况。

Edit——Project Settings——Quality，可以对不同平台中游戏的品质进行设置。

如果使用了后期处理技术，例如 Post Processing 等插件，调整屏幕效果的属性，不要使用太绚丽的特效，可以优化性能。

要优化 Terrain 地形，可以使用 Unity 资源商店的插件，例如 Terrain To Mesh 插件可以把地形烘焙成网格。

场景要尽可能简单，尽量多使用预制体，用代码动态创建它们出来，并管理它们。

## Shader 优化

修改 Shader 的代码，或者自定义一个 Shader

修改渲染管线的源码，改成符合自己项目的渲染管线，或者自定义渲染管线。

## 结尾

可以使用 Unity UPR 对整个项目进行性能分析，找出问题后，再手动优化它们。

Unity UPR 网址：https://upr.unity.cn/instructions/desktop

其中 Unity UPR 中的 Asset Checker 能对本地的整个 Unity 项目进行性能分析，帮助我们找出问题。
