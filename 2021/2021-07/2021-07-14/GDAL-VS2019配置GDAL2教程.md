# GDAL-VS2019配置GDAL2教程

  - [环境](#%E7%8E%AF%E5%A2%83)
  - [配置教程](#%E9%85%8D%E7%BD%AE%E6%95%99%E7%A8%8B)
    - [1. 下载 GDAL 2.3.2](#1-%E4%B8%8B%E8%BD%BD-gdal-232)
    - [2. 修改源代码](#2-%E4%BF%AE%E6%94%B9%E6%BA%90%E4%BB%A3%E7%A0%81)
    - [3. 编译源代码](#3-%E7%BC%96%E8%AF%91%E6%BA%90%E4%BB%A3%E7%A0%81)
    - [4. 在 VS2019 项目中配置 GDAL](#4-%E5%9C%A8-vs2019-%E9%A1%B9%E7%9B%AE%E4%B8%AD%E9%85%8D%E7%BD%AE-gdal)
    - [5. 设置环境变量](#5-%E8%AE%BE%E7%BD%AE%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)
    - [6. 拷贝 gdal203.dll 到 C:\Windows\System32](#6-%E6%8B%B7%E8%B4%9D-gdal203dll-%E5%88%B0-c%5Cwindows%5Csystem32)
    - [7. 编写代码测试](#7-%E7%BC%96%E5%86%99%E4%BB%A3%E7%A0%81%E6%B5%8B%E8%AF%95)
  - [参考链接](#%E5%8F%82%E8%80%83%E9%93%BE%E6%8E%A5)

## 环境
* VS 2019
* GDAL 2.3.2

## 配置教程
### 1. 下载 GDAL 2.3.2
下载地址：[http://download.osgeo.org/gdal/](http://download.osgeo.org/gdal/) 或 [https://github.com/OSGeo/gdal/releases](https://github.com/OSGeo/gdal/releases)

找到 `gdal232.zip` 文件下载到本地，解压并修改文件夹名，如：`E:\ThirdSDK\gdal232`

### 2. 修改源代码
用文本编辑器（如notepad++）打开 `nmake.opt` 文件，在本教程中该路径位于 `E:\ThirdSDK\gdal232\nmake.opt`，共需修改以下三处位置：
- 第 41 行的代码修改为：MSVC_VER=1921（注：vs2019对应1921，vs2017对应1910）
- 第 57 行的代码修改为：GDAL_HOME="E:\ThirdSDK\gdal2_x64_2019"
- 第 184 行的代码，去除 `WIN64=YES` 前面的 `#` 符号

### 3. 编译源代码
以管理员身份运行适用于 VS 2017 的 x64 本机工具命令提示该程序（英文版本为 x64 Native Tools Command Prompt for VS 2017），如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714195727.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714195727.png)

注意，需要右键选择以管理员身份运行

在命令行中依次输入，并回车
```bash
C:\Windows\System32>E:
C:\Windows\System32>cd ThirdSDK\gdal232
C:\Windows\System32>nmake /f makefile.vc
```

稍微等十分钟，编译结束若无错误提示，再进行后续安装操作：
```bash
C:\Windows\System32>nmake /f makefile.vc install
C:\Windows\System32>nmake /f makefile.vc devinstall
```

若无错误提示，安装即已完成。打开安装目录下的文件夹（代码修改的路径），会看到有 `bin,data,html,lib,include` 等几个文件夹，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714201116.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714201116.png)

### 4. 在 VS2019 项目中配置 GDAL
打开 vs2019，创建一个 c++ 空项目，创建完成后将其改成 `x64`。因为当前安装的 GDAL 为 win64 位版本，所以应选择 x64 进行编译执行，否则会出现模块计算机类型“x64”与目标计算机类型“x86”冲突这一问题

在 `视图->其他窗口->属性管理器`，打开属性管理器。

在 `Debug | x64` 上右击，选择添加新项目属性表，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714201723.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714201723.png)

然后双击新添加的项目属性表，在 `包含目录` 和 `库目录` 中添加编译好的 `gdal` 路径，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714202154.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714202154.png)

点击应用。然后在 `链接器->输入->附加依赖项` 中点击编辑，手动输入 `gdal_i.lib`，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714202309.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714202309.png)

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714202454.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714202454.png)

这个 `gdal_i.lib` 实际上就是 gdal 安装路径下 lib 文件夹里的那个 .lib 文件名

点击应用，确定，配置完成

### 5. 设置环境变量
依次点击 `计算机->属性->高级系统设置->环境变量->系统变量` 内的 `path`，添加如下

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714202903.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714202903.png)

依次点击确定按钮，确保环境变量生效

### 6. 拷贝 gdal203.dll 到 C:\Windows\System32
将 `E:\ThirdSDK\gdal2_x64_2019\bin` 路径下的 `gdal203.dll` 文件拷贝到 `C:\Windows\System32` 路径下

### 7. 编写代码测试
在刚刚创建的工程中创建 `main.cpp`，编写如下代码，注意把图片路径换成自己本地的图片路径
```c++
#include <iostream>  
#include "gdal_priv.h"

using namespace std;

int main()
{
	const char* pszFile;
	GDALAllRegister();
	pszFile = "E:\\_image\\OpenCVTest\\lena.jpg";
	GDALDataset* poDataset = (GDALDataset*)GDALOpen(pszFile, GA_ReadOnly);
	GDALRasterBand* poBand = poDataset->GetRasterBand(1);
	int xsize = poBand->GetXSize();
	int ysize = poBand->GetYSize();
	cout << xsize << endl;
	cout << ysize << endl;
	system("pause");

	return 0;
}
```

注意，程序需要在 x64 下运行哦，最后成功输出图片尺寸，大功告成~

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714203804.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210714203804.png)

## 参考链接
- [win10 x64 配置 VS2017 + GDAL](https://www.jianshu.com/p/79863f5d4eeb)
- [VS2017编译配置GDAL——超详细，适合初学者！！！](https://blog.csdn.net/qq_32153213/article/details/81363588) 
