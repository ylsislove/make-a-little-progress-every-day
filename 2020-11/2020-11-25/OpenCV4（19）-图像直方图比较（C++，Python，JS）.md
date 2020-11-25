# OpenCV4（19）-图像直方图比较（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
**图像直方图比较：**

图像直方图比较，就是计算两幅图像的直方图数据，比较两组数据的相似性，从而得到两幅图像之间的相似程度，直方图比较在早期的 CBIR 中是应用很常见的技术手段，通常会结合边缘处理、词袋等技术一起使用。

**相关API：**
```c++
double compareHist( InputArray H1, InputArray H2, int method );
```

**比较常见的方法有：**
- 相关性比较（Correlation）：最常用的方法之一，值的绝对值越接近1，表示相关性越强；越趋近与0，表示相关性越弱；
- 卡方比较（Chi-Square）：和相关性比较正好相反，越趋近于0，相关性越强；越趋近于1，相关性越弱；
- 交叉比较（Intersection）：最简单，效果差，并不常用。对比H1,H2并求出最小值，最后求和；
- 巴氏距离（Bhattacharyya distance）：最常用的方法之一，效果最好，但计算量也最大。0强1弱。

![比较常见的方法](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201126000355.png)

想要更加详细的了解这四种相关性比较算法的原理，参考这篇博客：[compareHist函数详解](https://blog.csdn.net/shuiyixin/article/details/80257822)

## C++代码
```c++
#ifndef DAY19
#define DAY19

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day19() {

	Mat src1 = imread("E:\\_Image\\OpenCVTest\\m1.png");
	Mat src2 = imread("E:\\_Image\\OpenCVTest\\m2.png");
	Mat src3 = imread("E:\\_Image\\OpenCVTest\\flower.jpg");
	Mat src4 = imread("E:\\_Image\\OpenCVTest\\girl.jpg");

	imshow("input1", src1);
	imshow("input2", src2);
	imshow("input3", src3);
	imshow("input4", src4);

	Mat hsv1, hsv2, hsv3, hsv4;
	cvtColor(src1, hsv1, COLOR_BGR2HSV);
	cvtColor(src2, hsv2, COLOR_BGR2HSV);
	cvtColor(src3, hsv3, COLOR_BGR2HSV);
	cvtColor(src4, hsv4, COLOR_BGR2HSV);

	// 定义参数变量
	int h_bins = 60; int s_bins = 64;
	int histSize[] = { h_bins, s_bins };
	float h_ranges[] = { 0, 180 };
	float s_ranges[] = { 0, 256 };
	const float* ranges[] = { h_ranges, s_ranges };
	int channels[] = { 0, 1 };

	// 计算图像直方图
	Mat hist1, hist2, hist3, hist4;
	calcHist(&hsv1, 1, channels, Mat(), hist1, 2, histSize, ranges, true, false);
	calcHist(&hsv2, 1, channels, Mat(), hist2, 2, histSize, ranges, true, false);
	calcHist(&hsv3, 1, channels, Mat(), hist3, 2, histSize, ranges, true, false);
	calcHist(&hsv4, 1, channels, Mat(), hist4, 2, histSize, ranges, true, false);

	normalize(hist1, hist1, 0, 1, NORM_MINMAX, -1, Mat());
	normalize(hist2, hist2, 0, 1, NORM_MINMAX, -1, Mat());
	normalize(hist3, hist3, 0, 1, NORM_MINMAX, -1, Mat());
	normalize(hist4, hist4, 0, 1, NORM_MINMAX, -1, Mat());

	for (int i = 0; i < 4; i++)
	{
		// HISTCMP_CORREL = 0,	相关性
		// HISTCMP_CHISQR = 1,	卡方（Chi-Square）
		// HISTCMP_INTERSECT = 2,	交叉（Intersection）
		// HISTCMP_BHATTACHARYYA = 3,	巴氏距离（Bhattacharyya Distance）
		int compare_method = i;
		double src1_src2 = compareHist(hist1, hist2, compare_method);
		double src3_src4 = compareHist(hist3, hist4, compare_method);
		printf(" Method [%d]  : src1_src2 : %.2f, src3_src4: %.2f,  \n", i, src1_src2, src3_src4);
	}

	waitKey();
}

#endif // !DAY19
```

## 结果展示

![src1-src2](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201126000720.png)

![src3-src4](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201126000812.png)

![res](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201126000904.png)
