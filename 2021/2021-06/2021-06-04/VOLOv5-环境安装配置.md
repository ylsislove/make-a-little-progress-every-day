# VOLOv5-环境安装配置

## 下载安装 OpenVINO
官网地址：[OpenVINO](https://docs.openvinotoolkit.org/latest/index.html)

选择 windows 版本下载和安装，默认路径尽量不要更改

需要 Cmake 和 Python 的支持

安装完成后，在 `C:\Program Files (x86)\Intel\openvino_2021.2.185\bin` 目录下打开 cmd，运行 .bat 文件，可以设置临时环境变量

然后跳转到 `C:\Program Files (x86)\Intel\openvino_2021.2.185\deployment_tools\demo` 目录下，用设置了临时环境变量的 cmd 运行 `demo_security_barrier_camera.bat` Demo 示例，如果能正常运行，表明安装成功。正常运行图如下图所示

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210604200902.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210604200902.png)

配置环境变量，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210604210014.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210604210014.png)

## OpenVINO VS2019 配置
创建一个 C++ 控制台的空项目，编译配置改为 `Release x64`

打开 `Release x64` 的属性管理器，貌似 VS2019 没有默认的用户属性表了，所有直接右击创建一个就好，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210604202621.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210604202621.png)

配置包含目录和库目录

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210604203216.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210604203216.png)

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210604203155.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210604203155.png)

配置附加依赖项，把刚才那两个库目录路径下的 .lib 文件名配置进去即可。直接用 Python 遍历，脚本如下

```python
import os

files = os.listdir(r"C:\Program Files (x86)\Intel\openvino_2021.2.185\deployment_tools\inference_engine\lib\intel64\Release")

for f in files:
    print(f)
```

```python
import os

files = os.listdir(r"C:\Program Files (x86)\Intel\openvino_2021.2.185\opencv\lib")

for f in files:
    if f.endswith("451.lib"):
        print(f)
```

点击确定保存

创建一个 main.cpp，编写一个测试代码

```c++
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main() {
	Mat src = imread("E:\\_image\\OpenCVTest\\lena.jpg");
	imshow("input", src);
	waitKey(0);
	destroyAllWindows();
	return 0;
}
```

成功显示出图片表示 VS2019 配置成功
