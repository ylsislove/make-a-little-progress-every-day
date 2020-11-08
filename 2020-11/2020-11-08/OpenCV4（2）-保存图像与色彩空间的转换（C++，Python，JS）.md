# OpenCV4（2）-保存图像与色彩空间的转换（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
1. 图像保存 — imwrite
* 第一个参数是图像保存路径
* 第二个参数是图像内存对象

2. 色彩空间转换函数 — cvtColor
* COLOR_BGR2GRAY = 6 彩色到灰度
* COLOR_GRAY2BGR = 8 灰度到彩色
* COLOR_BGR2HSV = 40 BGR到HSV
* COLOR_HSV2BGR = 54 HSV到BGR

## C++代码
```c++
#ifndef DAY02
#define DAY02

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day02() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");

	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}

	namedWindow("show", WINDOW_AUTOSIZE);
	imshow("show", src);

	Mat gray;
	cvtColor(src, gray, COLOR_BGR2GRAY);
	namedWindow("gray", WINDOW_AUTOSIZE);
	imshow("gray", gray);

	imwrite("E:\\_Image\\OpenCVTest\\girl_gray.jpg", gray);

	if (gray.type() == CV_8UC1) {
		//input image is grayscale
		cout << "gray" << endl;
	}
	else {
		//input image is colour
		cout << "color" << endl;
	}

	waitKey(0);
}

#endif // !DAY02
```

注意事项：
1. COLOR_GRAY2BGR 要求图像的类型是 CV_8UC1。该函数的原理是将图像的通道变多，但是每个像素点三通道的像素值还是一样！所以即使转换成功，图像依旧是灰色的。

2. 读取图像的 imread() 函数有第二个参数，其默认值是 IMREAD_COLOR ，即将加载的图像总是转换为彩色图像。转换后图像的类型是 CV_8UC3。
