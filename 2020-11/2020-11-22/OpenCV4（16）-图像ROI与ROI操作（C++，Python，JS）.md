# OpenCV4（16）-图像ROI与ROI操作（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
图像的 ROI(region of interest) 是指图像中感兴趣区域、在 OpenCV 中图像设置图像 ROI 区域，实现只对 ROI 区域的操作。

提取不规则 ROI 区域的一般步骤：
1. 通过 inRange 函数生成 mask
2. 通过按位与操作提取 ROI

## C++代码
```c++
#ifndef DAY16
#define DAY16

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day16() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\scene.jpg");
	namedWindow("input", WINDOW_AUTOSIZE);
	imshow("input", src);
	int h = src.rows;
	int w = src.cols;

	// 获取ROI
	int cy = h / 2;
	int cx = w / 2;
	Rect rect(cx - 100, cy - 100, 200, 200);
	Mat roi = src(rect);
	imshow("roi", roi);

	Mat image = roi.clone();
	// 直接更改ROI，因为是直接赋值的，指向同一块内存区域，所以原图也会被修改
	roi.setTo(Scalar(255, 0, 0));
	imshow("result", src);

	// 更改拷贝的ROI，指向不同的内存区域，所以原图不受影响
	image.setTo(Scalar(0, 0, 255));
	imshow("result2", src);
	imshow("copy roi", image);

	// 获取不规则形状的ROI，通过inRange函数
	Mat src2 = imread("E:\\_Image\\OpenCVTest\\tinygreen.jpg");
	imshow("src2", src2);
	Mat hsv, mask;
	cvtColor(src2, hsv, COLOR_BGR2HSV);
	inRange(hsv, Scalar(35, 43, 46), Scalar(77, 255, 255), mask);
	imshow("mask", mask);

	// 通过mask提取人物部分，即我们的ROI。mask的白色区域才会执行与操作，黑色区域不执行
	Mat person;
	bitwise_not(mask, mask);
	bitwise_and(src2, src2, person, mask);
	imshow("person", person);

	// 生成一张蓝色背景
	Mat result = Mat::zeros(src2.size(), src2.type());
	result.setTo(Scalar(255, 0, 0));

	// 将蓝色背景与ROI融合
	Mat dst;
	bitwise_not(mask, mask);
	bitwise_or(result, result, dst, mask);
	add(dst, person, dst);

	imshow("dst", dst);

	waitKey();
}

#endif // !DAY16
```
