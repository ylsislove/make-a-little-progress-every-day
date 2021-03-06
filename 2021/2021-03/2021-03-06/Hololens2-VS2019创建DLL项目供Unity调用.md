# Hololens2-VS2019创建DLL项目供Unity调用

  - [前言](#%E5%89%8D%E8%A8%80)
  - [环境](#%E7%8E%AF%E5%A2%83)
  - [VS2019创建DLL项目](#vs2019%E5%88%9B%E5%BB%BAdll%E9%A1%B9%E7%9B%AE)
  - [编写DLL代码](#%E7%BC%96%E5%86%99dll%E4%BB%A3%E7%A0%81)
  - [生成DLL文件](#%E7%94%9F%E6%88%90dll%E6%96%87%E4%BB%B6)
  - [Unity调用DLL](#unity%E8%B0%83%E7%94%A8dll)
  - [部署到Hololens上](#%E9%83%A8%E7%BD%B2%E5%88%B0hololens%E4%B8%8A)
  - [参考](#参考)

## 前言
[上一篇](./../2021-03-05/Hololens2-Unity项目整合Hololens2研究模式.md)尝试将 Hololens2 的研究模式与 Unity 项目进行了整合。归根结底，就是将研究模式的相关 API（C++）构建成 DLL 文件，才能实现在 Unity（C#）中进行调用。这篇就介绍一下如何自己创建一个最简单的 DLL 文件，实现在 Unity 中的调用。

## 环境
* Windows 10 教育版 18363.1379
* Unity 2019.4.20f1c1
* VS2019 16.8.6
* WIN SDK 10.0.18362.0
* Hololens2 内部预览版本 10.0.20301.1000

## VS2019创建DLL项目
选择创建新项目，搜索 DLL 模板，选择 `DLL（通用Windows）` 模板，点击下一步

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210306190323.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210306190323.png)

设置项目名称和位置，点击创建

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210306191013.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210306191013.png)

选择目标版本最低版本，一般默认即可。实际上，项目创建完成后，在项目属性设置中也可更改这个设置，如何更改可以看：[Hololens2-运行研究模式官方案例（SensorVisualization）](./../2021-03-04/Hololens2-运行研究模式官方案例（SensorVisualization）.md)

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210306190610.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210306190610.png)

## 编写DLL代码
主要更改的就是 `HL2RmUnityPlugin.h` 和 `HL2RmUnityPlugin.cpp` 这两个文件。编写代码如下

HL2RmUnityPlugin.h
```c++
#pragma once

#define FUNCTIONS_EXPORTS_API extern "C" __declspec(dllexport)

extern "C" {
	typedef struct IMUInputForUnity {
		double x;
		double y;
		double z;
	}INPUT;

	typedef struct IMUOutputForUnity {
		double x;
		double y;
		double z;
	}OUTPUT;
}

namespace HL2Stream {

	FUNCTIONS_EXPORTS_API int __stdcall GetIMUStreaming(INPUT* input, OUTPUT* output);

}
```

HL2RmUnityPlugin.cpp
```c++
#include "pch.h"
#include "HL2RmUnityPlugin.h"

int __stdcall HL2Stream::GetIMUStreaming(INPUT* input, OUTPUT* output)
{
	output->x = input->x * input->x;
	output->y = input->y * input->y;
	output->z = input->z * input->z;
	return 200;
}
```

`GetIMUStreaming` 函数接收两个结构体作为参数，返回 int 类型表示执行结果。

## 生成DLL文件
因为最终 Unity 项目要部署到 Hololens2 上，所以这里构建方式选择 `Release ARM64`。点击菜单栏生成 -> 生成解决方案。成功后即可在项目目录下找到 `ARM64\Release\HL2RmUnityPlugin\HL2RmUnityPlugin.dll` 文件了。

## Unity调用DLL
把 dll 文件拷贝到 Unity 项目的 `Assets\Plugins\HL2RmStream` 目录下，目录不存在就创建。然后在 `Assets\Scripts` 目录下创建一个 C# 脚本，编写如下：

```csharp
using System;
using System.Runtime.InteropServices;
using TMPro;
using UnityEngine;

public class GetTime : MonoBehaviour
{
    [StructLayout(LayoutKind.Sequential)]
    struct INPUT
    {
        public double x;
        public double y;
        public double z;
    };

    [StructLayout(LayoutKind.Sequential)]
    struct OUTPUT
    {
        public double x;
        public double y;
        public double z;
    }

#if ENABLE_WINMD_SUPPORT
    [DllImport("HL2RmUnityPlugin", EntryPoint = "GetIMUStreaming", CallingConvention = CallingConvention.StdCall)]
    public static extern int GetIMUStreaming(IntPtr pv1, IntPtr pv2);
#endif

    public TextMeshPro textMeshPro;

    private void Start()
    {
#if ENABLE_WINMD_SUPPORT
        INPUT pIn = new INPUT();
        pIn.x = 1.0;
        pIn.y = 2.0;
        pIn.z = 3.0;

        int sizeIn = Marshal.SizeOf(typeof(INPUT));
        IntPtr pBuffIn = Marshal.AllocHGlobal(sizeIn);
        Marshal.StructureToPtr(pIn, pBuffIn, true);

        int sizeOut = Marshal.SizeOf(typeof(OUTPUT));
        IntPtr pBuffOut = Marshal.AllocHGlobal(sizeOut);

        int result = GetIMUStreaming(pBuffIn, pBuffOut);

        OUTPUT pOut = (OUTPUT)Marshal.PtrToStructure(pBuffOut, typeof(OUTPUT));

        textMeshPro.text = $"{pOut.x} {pOut.y} {pOut.z}";
#endif
    }
}
```

C# 需要将结构体转为指针进行调用。为了能看到运行结果，创建一个 `TextMeshPro` 对象挂载到这个脚本时来显示运行结果。

## 部署到Hololens上
因为 Windows 机器不能运行 ARM64 的程序，所以只能把 Unity 项目构建部署到 Hololens 上运行即可~

部署相关操作看之前的文章吧，这里不在赘述了。接下来来好好的捣鼓捣鼓 Hololens 的研究模式吧~

## 参考
[Unity3D中调用C++动态链接库(dll)-两种方式(Managed Plugins 和 Native Plugins)](https://blog.csdn.net/kuaxianpan2004/article/details/86160840)
