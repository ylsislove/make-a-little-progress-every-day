# OpenCV4（18）-图像直方图均衡化（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
**图像直方图均衡化：**

图像直方图均衡化可以用于图像增强、对输入图像进行直方图均衡化处理，提升后续对象检测的准确率在OpenCV人脸检测的代码演示中已经很常见。此外对医学影像图像与卫星遥感图像也经常通过直方图均衡化来提升图像质量。

**相关API：**
```c++
void equalizeHist( InputArray src, OutputArray dst );
```

## C++代码
```c++
#ifndef DAY18
#define DAY18

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

Mat showHistogram(Mat* image);

void day18() {

	// 以灰度方式读取图像
	Mat src = imread("E:\\_Image\\OpenCVTest\\flower.jpg", IMREAD_GRAYSCALE);
	if (src.empty()) {
		printf("could not load image...\n");
		return;
	}
	imshow("input", src);

	// 显示直方图
	Mat histImage;
	histImage = showHistogram(&src);
	imshow("Histogram Original", histImage);

	// 直方图均衡化
	Mat dst;
	equalizeHist(src, dst);
	imshow("equalize", dst);

	// 显示直方图
	histImage = showHistogram(&dst);
	imshow("Histogram Equalize", histImage);

	waitKey();
}

Mat showHistogram(Mat* image) {

	// 定义参数变量
	const int ninages = 1;
	const int channels[] = { 0 };
	const int dims = 1;
	//const int bins[] = { 32 };
	const int bins[] = { 256 };
	float hranges[] = { 0, 255 };
	const float* ranges[] = { hranges };

	// 计算直方图
	Mat dest;
	calcHist(image, ninages, channels, Mat(), dest, dims, bins, ranges);

	// 画布参数
	int hist_w = 512;
	int hist_h = 400;
	int bin_w = cvRound((double)hist_w / bins[0]);
	Mat histImage(hist_h, hist_w, CV_8UC3, Scalar(255, 255, 255));

	// 归一化直方图数据，范围是[0, hist_h]，
	normalize(dest, dest, 0, hist_h, NORM_MINMAX, -1, Mat());

	// 绘制直方图，注意画布的原点在左上角
	Rect rect;
	for (int i = 1; i < bins[0]; i++) {
		rect.x = bin_w * (i - 1);
		rect.y = hist_h - cvRound(dest.at<float>(i - 1));
		rect.width = bin_w;
		rect.height = cvRound(dest.at<float>(i - 1));
		rectangle(histImage, rect, Scalar(255, 0, 0), -1, LINE_8, 0);
	}

	return histImage;
}

#endif // !DAY18
```

## 结果展示
![input-equalize](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201125000706.png)

![original-equalize](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201125000843.png)
