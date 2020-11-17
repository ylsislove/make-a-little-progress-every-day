# OpenCV4（11）-图像像素归一化（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
OpenCV中提供了四种归一化的方法：
- NORM_MINMAX
- NORM_INF
- NORM_L1
- NORM_L2

最常用的就是 NORM_MINMAX 归一化方法。

相关 API

```c++
void normalize(InputArray src, InputOutputArray dst, double alpha = 1, double beta = 0, int norm_type = NORM_L2, int dtype = -1, InputArray mask = noArray());
```

- InputArray src    // 输入图像
- InputOutputArray dst    // 输出图像
- double alpha = 1    // NORM_MINMAX时候低值
- double beta = 0     // NORM_MINMAX时候高值，通常保持 alpha 和 beta 一大一小即可
- int norm_type = NORM_L2    // NORM_L2、NORM_L1、NORM_INF 只需要 alpha，NORM_MINMAX 需要 alpha 和 beta 两个参数
- int dtype = -1    // 输出数组的type与输入数组的type相同，否则，输出数组与输入数组只是通道数相同，而tpye =  CV_MAT_DEPTH(dtype)
- InputArray mask = noArray()    // mask默认值为空

## C++代码
```c++
#ifndef DAY11
#define DAY11

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day11() {

	// 读取一张灰度图像
	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg", IMREAD_GRAYSCALE);
	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}
	imshow("src", src);

	Mat gray_f;

	// 转换为浮点数类型数组
	src.convertTo(gray_f, CV_32F);


	// NORM_MINMAX 归一化，根据delta = max - min = 8.0
	// 2.0		0.0		((2.0 - 2.0)/8.0)
	// 8.0		0.75	((8.0 - 2.0)/8.0)
	// 10.0		1.0		((10.0 - 2.0)/8.0)
	Mat dst = Mat::zeros(gray_f.size(), CV_32FC1);
	normalize(gray_f, dst, 1.0, 0, NORM_MINMAX);
	Mat result = dst * 255;
	result.convertTo(dst, CV_8UC1);
	imshow("NORM_MINMAX", dst);


	// NORM_INF 归一化，根据最大值
	// 2.0		0.2		(2.0/10.0)
	// 8.0		0.8		(8.0/10.0)
	// 10.0		1.0		(10.0/10.0)
	normalize(gray_f, dst, 1.0, 0, NORM_INF);
	result = dst * 255;
	result.convertTo(dst, CV_8UC1);
	imshow("NORM_INF", dst);


	// NORM_L1 归一化，依据和为1
	// sum(numbers) = 20.0
	// 2.0		0.1		(2.0/20.0)
	// 8.0		0.4		(8.0/20.0)
	// 10.0		0.5		(10.0/20.0)
	normalize(gray_f, dst, 1.0, 0, NORM_L1);
	result = dst * 10000000;
	result.convertTo(dst, CV_8UC1);
	imshow("NORM_L1", dst);


	// NORM_L2 归一化，根据单位向量为1
	// ||positiveData|| = sqrt(2.0*2.0 + 8.0*8.0 + 10.0*10.0) = 12.96
	// 2.0		0.15	(2.0/12.96)
	// 8.0		0.62	(8.0/12.96)
	// 10.0		0.77	(10.0/12.96)
	normalize(gray_f, dst, 1.0, 0, NORM_L2);
	result = dst * 10000;
	result.convertTo(dst, CV_8UC1);
	imshow("NORM_L2", dst);

	waitKey(0);
}

#endif // !DAY11
```