# OpenCV4（22）-图像均值与高斯模糊（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
**图像均值与高斯模糊：**

均值模糊，是卷积核的系数完全一致。上一节我们便实现了自定义版本的均值模糊与API版本的均值模糊；

高斯模糊，考虑了中心像素距离的影响，对距离中心像素使用高斯分布公式生成不同的权重系数给卷积核，然后用此卷积核完成图像卷积得到输出结果就是图像高斯模糊之后的输出。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128223329.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128223329.png)

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128223355.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128223355.png)

**相关API：**
```c++
void GaussianBlur( InputArray src, OutputArray dst, Size ksize,
                   double sigmaX, double sigmaY = 0,
                   int borderType = BORDER_DEFAULT );
```

- src：输入图像，Mat 类型，图像深度为 CV_8U、CV_16U、CV_16S、CV_32F、CV_64F；
- dst：输出图像，与输入图像有相同的类型和尺寸；
- ksize：卷积核的大小，ksize.width 和 ksize.height 可以不相同但是这两个值必须为正奇数，如果这两个值为 0，他们的值将由 sigma 计算；
- sigmaX：高斯核函数在 X 方向上的标准偏差；
- sigmaY：高斯核函数在 Y 方向上的标准偏差，如果 sigmaY 是 0，则函数会自动将 sigmaY 的值设置为与 sigmaX 相同的值，如果 sigmaX 和 sigmaY 都是 0，这两个值将由 ksize.width 和 ksize.height 计算。通常将 ksize、sigmaX 和 sigmaY 都指定出来；
- borderType：图像边界处理方式，通常默认即可。

**注意：**

ksize越大，图像模糊程度越厉害；sigma越大，图像模糊程度越厉害。高斯模糊的源码分析，可以参考这篇博客：[OpenCV源码分析（三）：高斯模糊](https://www.jianshu.com/p/1fb59e951c72)

## C++代码
```c++
#ifndef DAY22
#define DAY22

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day22() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");
	if (src.empty()) {
		printf("could not load image...\n");
		return;
	}
	namedWindow("input", WINDOW_AUTOSIZE);
	imshow("input", src);

	Mat dst1, dst2, dst3;
	blur(src, dst1, Size(5, 5), Point(-1, -1), 4);
	GaussianBlur(src, dst2, Size(5, 5), 15, 0, 4);
	GaussianBlur(src, dst3, Size(0, 0), 15, 0, 4);
	//GaussianBlur(src, dst2, Size(0, 0), 30, 0, 4);

	imshow("blur", dst1);
	imshow("gaussian blur ksize = 5", dst2);
	imshow("gaussian blur sigmaX = 15", dst3);

	waitKey();
}

#endif // !DAY22
```

## 结果展示
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128224412.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128224412.png)

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128224654.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128224654.png)
