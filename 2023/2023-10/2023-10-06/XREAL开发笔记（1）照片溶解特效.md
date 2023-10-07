---
title: XREAL开发笔记（1）照片溶解特效
math: true
date: 2023-10-06 23:12:33
categories:
 - [Unity3D, XREAL]
tags: 
 - Unity3D
 - XREAL
---

## 前言
最近学了一个照片溶解特效，感觉很炫酷，也可以作为后续项目花里胡哨的基础，便在此将学习过程记录一下吧~

话不多说，先看看最终效果~

![](https://image.aayu.today/uploads/2023/10/07/202310071342614.gif)

## 创建和配置项目
选择 3D（URP）项目，然后点击 Create Project 即可创建项目。

![](https://image.aayu.today/uploads/2023/10/06/202310062329303.png)

打开 Unity，File-->Build Settings, 选择 Android，点击 Switch Platform

![](https://image.aayu.today/uploads/2023/10/07/202310071110378.png)

在 Build Settings 窗口中，选择 Player Settings, 然后按照下面对应的设置进行配置

![](https://image.aayu.today/uploads/2023/10/07/202310071112820.png)

![](https://image.aayu.today/uploads/2023/10/07/202310071115921.png)

![](https://image.aayu.today/uploads/2023/10/07/202310071115680.png)

![](https://image.aayu.today/uploads/2023/10/07/202310071118937.png)

![](https://image.aayu.today/uploads/2023/10/07/202310071118023.png)

## 导入 NRSDK
将 NRSDKForUnity_Release_1.10.2 拖入到 Assets 文件夹中，点击 Import 即可导入

在 Scenes 文件夹下创建个新场景，删除默认的相机，将 NRCameraRig 和 NRInput 拖拽到场景中

## 创建 Shader
在 Assets 下创建 Materials 文件夹，在 Materials 文件夹上右键，点击 Create -> Shader Graph -> URP -> Lit Shader Graph，命名为 Dissolve，双击打开

![](https://image.aayu.today/uploads/2023/10/07/202310071135598.png)

小 Tip：双击选项卡可以最大化选项卡，再次双击可以恢复

首先创建 4 个可以暴露的属性，注意创建属性的类型

![](https://image.aayu.today/uploads/2023/10/07/202310071138114.png)

然后将 MainTex 拖拽到画板里，从节点拉出一根线然后在空白书松开，选择 Sample Texture 2D，双击创建新节点，然后把 RGBA 连接到 Base Color

![](https://image.aayu.today/uploads/2023/10/07/202310071141655.png)

勾选 Graph Inspector 窗口里的 Alpha Clip，可以看到片元着色器就会多出两个属性，透明度和透明度裁剪阈值，我们的溶解特效就是根据这两个属性实现的。具体来讲就是随机一个高斯噪声，根据噪声透明度和阈值裁剪照片，将透明度小于该值的像素点裁剪掉，通过将阈值从小变到大，从而实现溶解特效。

![](https://image.aayu.today/uploads/2023/10/07/202310071145121.png)

在画板空白处右键，选择 Simple Noise 节点创建，将 X 值调为 30 左右，然后将 Out 连接到 Alpha 变量上

为了溶解特效更加炫酷，可以将溶解边缘增加发光效果，具体节点和连接如下

![](https://image.aayu.today/uploads/2023/10/07/202310071202381.png)

小 Tip：可以框选住一些节点，然后右键选择 Group Selection，可以将这些节点合并成一个节点，方便一起拖拽

可以在右侧 Graph Inspector 窗口的 Node Settings 里将 AlphaThreshold 模式变为滑动条模式，并给一个默认值 0.5，就可以看到 Step 节点下面的预览图像为二值化后的图像了

RimColor 将模式变为 HDR，然后默认颜色可以设为红色，这样就可以将溶解边缘设为红色的发光了

然后再将最后的 Out 连接到片元着色器的 Emission 上，这样溶解边缘发光的 Shader 就配置好啦

边缘发光的宽度可以通过 RimWidth 属性控制，可以将 RimWidth 也设为滑动条模式，然后范围设为 0 到 5，默认值为 2

![](https://image.aayu.today/uploads/2023/10/07/202310071204576.png)

至此，溶解特效的 Shader 就配置好啦，点击左上角的 Save Asset 保存，然后双击选项卡退出最大化

## 创建材质
在 Assets 里的 Dissolve Shader 上右键，点击 Create -> Material，命名为 Mat_Dissolve

然后在场景中创建一个 Quad，双击可以聚焦到这个物体，然后将 Mat_Dissolve 拖拽到这个物体上，就可以看到这个物体的材质变成了 Mat_Dissolve

![](https://image.aayu.today/uploads/2023/10/07/202310071211267.png)

现在溶解特效就已经可以看出来了

可以将 Quad 的 Z 值设为 3，即物体在镜头外 3 米的地方，这样就可以在 Game 窗口里看到物体了

将 NRSDK 里自带的 Image 拖拽到我们在 Shader 里设置的 MainTex 属性上

![](https://image.aayu.today/uploads/2023/10/07/202310071215794.png)

然后拖拽 AlphaThreshold 就可以看到效果了

想要看到炫光还需要一点配置

首先在场景处右键，选择 Volume -> Global Volume，然后配置文件选择默认已有的 SampleSceneProfile 即可

![](https://image.aayu.today/uploads/2023/10/07/202310071221375.png)

然后将 LeftCamera，CenterCamera，RightCamera 的 Post Processing 都打上勾，即启用后处理配置

![](https://image.aayu.today/uploads/2023/10/07/202310071224514.png)

然后再回到 Quad，可以在 RimColor 里调整炫光强度

![](https://image.aayu.today/uploads/2023/10/07/202310071225331.png)

至此，照片溶解特效就配置好啦

## 编写脚本
在 Assets 下创建 Scripts 文件夹，然后在 Scripts 文件夹上右键，点击 Create -> C# Script，命名为 Dissolve，双击打开代码编辑器，代码内容如下

```csharp
using System.Collections;
using UnityEngine;

public class Dissolve : MonoBehaviour
{
    private static readonly int mAlphaThreshold = Shader.PropertyToID("_AlphaThreshold");

    public void StartDissolve()
    {
        StartCoroutine(DissolveEffect());
    }

    private IEnumerator DissolveEffect()
    {
        // 获取当前物体的MeshRenderer组件
        MeshRenderer meshRenderer = gameObject.GetComponent<MeshRenderer>();
        // 获取当前物体的材质
        Material material = meshRenderer.material;
        // 将材质的溶解值缓慢从0变为1，持续2s
        for (float i = 0; i < 2; i += Time.deltaTime)
        {
            material.SetFloat(mAlphaThreshold, i);
            yield return null;
        }
        // 重新设置溶解值为0
        material.SetFloat(mAlphaThreshold, 0);
    }
}
```

在 Quad 上添加一个 Button 组件，并将 Dissolve 脚本先拖拽到 Quad 物体上，然后把 Quad 拖拽到 On Click 事件里，然后选择 Dissolve -> StartDissolve

![](https://image.aayu.today/uploads/2023/10/07/202310071252207.png)

这样，当控制器的射线点击到 Quad 上时，就会触发溶解特效了

![](https://image.aayu.today/uploads/2023/10/07/202310071256539.gif)

最后就是构建成手机 App，然后将 Air2 眼镜切换为 3D 模式，运行应用就可以看到效果啦

完结撒花~
