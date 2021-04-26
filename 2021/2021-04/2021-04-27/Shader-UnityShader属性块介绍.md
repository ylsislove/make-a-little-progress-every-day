# Shader-UnityShader属性块介绍

## 基本属性
```c
Properties
{
    _Int("Int", Int) = 2
    _Float("Float", float) = 1.5
    _Range("Range", range(0.0, 2.0)) = 1.0
    _Color("Color", Color) = (1, 1, 1, 1)
    _Vector("Vector", Vector) = (1, 4, 3, 8)
    _MainTex ("Texture", 2D) = "white" {}
    _Cube("Cube", Cube) = "white" {}
    _3D("3D", 3D) = "black" {}
}
```

## 编辑器显示结果
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427041334.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210427041334.png)
