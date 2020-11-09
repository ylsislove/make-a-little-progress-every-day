# OpenCV4（3）-图像对象拷贝与创建（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
1. 图像对象的拷贝

    学过C++的应该都很清楚，拷贝分为深拷贝和浅拷贝。OpenCV 的 clone() 和 copyTo 是深拷贝，赋值运算符 `=` 是浅拷贝。

    ![图像对象的拷贝](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201109232731.png)

    头部保存了该图像的宽度和高度还有通道数等信息，数据部分保存了该图像的像素信息

2. 图像对象的创建

    常用方法有 `Mat::zeros()` 和 `Mat::ones()`

## C++代码
```c++
#ifndef DAY03
#define DAY03

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day03() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");

	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}

	// 创建方法-克隆
	Mat m1 = src.clone();

	// 复制
	Mat m2;
	src.copyTo(m2);

	// 赋值法
	Mat m3 = src;

	// 创建空白图像
	Mat m4 = Mat::zeros(src.size(), src.type());
	Mat m5 = Mat::zeros(Size(512, 512), CV_8UC3);
	Mat m6 = Mat::ones(Size(512, 512), CV_8UC3);

	waitKey(0);
}

#endif // !DAY03
```
