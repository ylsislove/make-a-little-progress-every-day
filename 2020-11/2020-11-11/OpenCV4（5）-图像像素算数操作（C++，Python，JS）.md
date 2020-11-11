# OpenCV4（5）-图像像素算数操作（C++，Python，JS）.md

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
1. 像素算术操作
   - 加 add
   - 减 subtract
   - 乘 multiply
   - 除 divide

2. 参与运算的图像的数据类型、通道数目、大小必须相同

3. 读取图像的 imread() 函数有第二个参数，其默认值是 IMREAD_COLOR，即将加载的图像总是转换为彩色图像。转换后图像的类型是 CV_8UC3。

4. C++ 使用 saturate_cast 防止数据溢出

## C++代码
```c++
#ifndef DAY05
#define DAY05

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day05() {

	Mat src1 = imread("E:\\_Image\\OpenCVTest\\girl.jpg");
	if (src1.empty()) {
		cout << "could not load image1.." << endl;
		return;
	}

	// 第二个参数默认值是 IMREAD_COLOR
	// 即将加载的图像总是转换为彩色图像。转换后图像的类型是 CV_8UC3。
	Mat src2 = imread("E:\\_Image\\OpenCVTest\\girl_gray.jpg");
	if (src2.empty()) {
		cout << "could not load image2.." << endl;
		return;
	}

	if (src1.channels() != src2.channels()) {
		cout << "chennels is not equal!" << endl;
		return;
	}
	
	imshow("input1", src1);
	imshow("input2", src2);

	// 自己实现的 add 算法
	int height = src1.rows;
	int width = src1.cols;

	int b1 = 0, g1 = 0, r1 = 0;
	int b2 = 0, g2 = 0, r2 = 0;
	int b = 0, g = 0, r = 0;
	Mat result = Mat::zeros(src1.size(), src1.type());
	for (int row = 0; row < height; row++) {
		for (int col = 0; col < width; col++) {
			b1 = src1.at<Vec3b>(row, col)[0];
			g1 = src1.at<Vec3b>(row, col)[1];
			r1 = src1.at<Vec3b>(row, col)[2];

			b2 = src2.at<Vec3b>(row, col)[0];
			g2 = src2.at<Vec3b>(row, col)[1];
			r2 = src2.at<Vec3b>(row, col)[2];

			// saturate_cast 防止数据溢出
			result.at<Vec3b>(row, col)[0] = saturate_cast<uchar>(b1 + b2);
			result.at<Vec3b>(row, col)[1] = saturate_cast<uchar>(g1 + g2);
			result.at<Vec3b>(row, col)[2] = saturate_cast<uchar>(r1 + r2);
		}
	}
	imshow("output", result);

	// 直接调用 API
	Mat add_result = Mat::zeros(src1.size(), src1.type());
	add(src1, src2, add_result);
	imshow("add_result", add_result);

	Mat sub_result = Mat::zeros(src1.size(), src1.type());
	subtract(src1, src2, sub_result);
	imshow("sub_result", sub_result);

	Mat mul_result = Mat::zeros(src1.size(), src1.type());
	multiply(src1, src2, mul_result);
	imshow("mul_result", mul_result);

	Mat div_result = Mat::zeros(src1.size(), src1.type());
	divide(src1, src2, div_result);
	imshow("div_result", div_result);

	waitKey(0);
}

#endif // !DAY05
```