# OpenCV4（4）-图像像素读写操作（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
C++中的像素遍历与访问
- 数组遍历
- 指针遍历

Python中的像素遍历与访问
- 数组遍历

## C++代码
```c++
#ifndef DAY04
#define DAY04

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day04() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");

	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}

	// 直接读取图像像素
	int height = src.rows;
	int width = src.cols;
	int ch = src.channels();
	for (int row = 0; row < height; row++) {
		// 像素取反
		for (int col = 0; col < width; col++) {
			if (ch == 3) {
				Vec3b bgr = src.at<Vec3b>(row, col);
				bgr[0] = 255 - bgr[0];
				bgr[1] = 255 - bgr[1];
				bgr[2] = 255 - bgr[2];
				src.at<Vec3b>(row, col) = bgr;
			}
			else if (ch == 1) {
				int gray = src.at<uchar>(row, col);
				src.at<uchar>(row, col) = 255 - gray;
			}
		}
	}
	imshow("output", src);

	// 指针读取
	Mat result = Mat::zeros(src.size(), src.type());
	int blue = 0, green = 0, red = 0;
	int gray;
	for (int row = 0; row < height; row++) {
		uchar* curr_row = src.ptr<uchar>(row);
		uchar* result_row = result.ptr<uchar>(row);
		for (int col = 0; col < width; col++) {
			if (ch == 3) {
				blue = *curr_row++;
				green = *curr_row++;
				red = *curr_row++;

				*result_row++ = blue;
				*result_row++ = green;
				*result_row++ = red;
			}
			else if (ch == 1) {
				gray = *curr_row++;
				*result_row++ = gray;
			}
		}
	}
	imshow("result", result);

	waitKey(0);
}

#endif // !DAY04
```
