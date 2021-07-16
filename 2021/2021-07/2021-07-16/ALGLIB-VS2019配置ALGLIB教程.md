# ALGLIB-VS2019配置ALGLIB教程

## ALGLIB 简介
ALGLIB是一个跨平台的数值分析和数据处理库。它支持多种编程语言（C ++，C＃，Delphi）和多种操作系统（Windows和POSIX，包括Linux）。
ALGLIB功能非常强大，其主要功能包括：
- 数据分析（分类/回归，统计）
- 优化和非线性求解器
- 插值和线性/非线性最小二乘拟合
- 线性代数（直接算法，EVD / SVD），直接和迭代线性求解器
- 快速傅立叶变换和许多其他算法

## ALGLIB 库下载
本教程所使用的环境为 Visual Studio 2019 开发环境。首先进入 [ALGLIB 官网](http://www.alglib.net/) 进行下载，对于初学者建议选择 ALGLIB 免费版本进行下载。本教程选择的当前最新版本 ALGLIB 3.17.0 for C++，将 alglib-3.17.0.cpp.gpl.zip 下载至本地，并进行解压得到 cpp 文件夹。

cpp文件夹中主要包括：
- src：资源文件夹（里面包括了我们后面配置所需的.cpp文件与.h文件）
- tests：测试代码Demo文件夹，用于测试ALGLIB第三方库是否添加成功
- gpl2, gpl3：这是开源协议，不用管
- manual.cpp：官方帮助文档，非常详细！！

## ALGLIB 库配置及测试
- 首先用 VS2019 创建一个 C++ 空项目工程
- 然后将我们所需功能对应的 h.，cpp. 文件加入到我们项目源文件中（注意：需要处理好各个包之间的依赖关系，都要拷贝进源文件夹添加到项目中，特别是 stdafx.h，可别丢了），并且在 VS 的解决方案资源管理器中添加现有项。
- 最后在主函数中，添加以下代码进行编译测试，若程序正常执行则已经完成了算法库的配置。
```cpp
#include "linalg.h"

int main()
{
    alglib::real_2d_array a("[[1]]");
    alglib::spdmatrixcholesky(a, 1, true);
    return 0;
}
```

## 参考链接
* [ALGLIB库 ( C++, VS2017 ) 配置教程](https://www.jianshu.com/p/d681f8bf3408)
