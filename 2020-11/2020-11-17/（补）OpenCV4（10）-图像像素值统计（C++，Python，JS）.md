# （补）OpenCV4（10）-图像像素值统计（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
像素值统计
- 最小（min）
- 最大（max）
- 均值（mean）
- 标准方差（standard deviation）

相关 API
- 最大最小值 minMaxLoc
- 计算均值与标准方差 meanStdDev

`minMaxLoc()` 函数要求输入图像必须是 `CV_8UC1` 类型的，否则会报错。

## C++代码
```c++
#ifndef DAY10
#define DAY10

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day10() {

	// 读取一张灰度图像
	Mat src_gray = imread("E:\\_Image\\OpenCVTest\\girl.jpg", IMREAD_GRAYSCALE);
	if (src_gray.empty()) {
		cout << "could not load image.." << endl;
		return;
	}
	imshow("src_gray", src_gray);

	if (src_gray.type() == CV_8UC1) {
		double minVal = 0, maxVal = 0;
		Point minLoc, maxLoc;
		minMaxLoc(src_gray, &minVal, &maxVal, &minLoc, &maxLoc, Mat());
		printf("min: %.2f, max: %.2f\n", minVal, maxVal);
		printf("min loc: (%d, %d)\n", minLoc.x, minLoc.y);
		printf("max loc: (%d, %d)\n", maxLoc.x, maxLoc.y);
	}
	else {
		cout << "not gray image.." << endl;
	}
	
	// 读取一张三通道彩色图像，获得它的均值和方差
	Mat src_color = imread("E:\\_Image\\OpenCVTest\\girl.jpg");
	if (src_color.empty()) {
		cout << "could not load image.." << endl;
		return;
	}
	imshow("src_color", src_color);

	Mat mean, stddev;
	meanStdDev(src_color, mean, stddev);
	printf("blue channel -> mean: %.2f, stddev: %2f\n", mean.at<double>(0, 0), stddev.at<double>(0, 0));
	printf("green channel -> mean: %.2f, stddev: %2f\n", mean.at<double>(1, 0), stddev.at<double>(1, 0));
	printf("red channel -> mean: %.2f, stddev: %2f\n", mean.at<double>(2, 0), stddev.at<double>(2, 0));
	
	// 根据图像的均值将彩色图像转换为二值图像
	for (int row = 0; row < src_color.rows; row++) {
		for (int col = 0; col < src_color.cols; col++) {
			Vec3b bgr = src_color.at<Vec3b>(row, col);
			bgr[0] = bgr[0] < mean.at<double>(0, 0) ? 0 : 255;
			bgr[1] = bgr[1] < mean.at<double>(1, 0) ? 0 : 255;
			bgr[2] = bgr[2] < mean.at<double>(2, 0) ? 0 : 255;
			src_color.at<Vec3b>(row, col) = bgr;
		}
	}
	imshow("binary", src_color);

	waitKey(0);
}

#endif // !DAY10
```

## 结果展示
![结果展示1](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201117234247.png)

![结果展示2](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201117234329.png)