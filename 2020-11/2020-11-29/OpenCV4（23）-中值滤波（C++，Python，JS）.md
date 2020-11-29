# OpenCV4（23）-中值滤波（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
**中值模糊：**

中值滤波本质上是统计排序滤波器（包括最小值滤波器和最大值滤波器）的一种，中值滤波对图像特定噪声类型（椒盐噪声）会取得比较好的去噪效果，也是常见的图像去噪声与增强的方法之一。中值滤波也是窗口在图像上移动，其覆盖的对应ROI区域下，所有像素值排序，取中值作为中心像素点的输出值。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201129214654.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201129214654.png)

**相关API：**
```c++
void medianBlur( InputArray src, OutputArray dst, int ksize );
```

- src：输入图像，Mat类型，图像深度为 CV_8U、CV_16U、CV_16S、CV_32F、CV_64F；
- dst：输出图像，与输入图像有相同的类型和尺寸；
- ksize：卷积核的大小，必须是奇数，而且必须大于 1。ksize 越大，去噪效果越好，但滤波后的图像越模糊，所以需要根据实际情况选取合适的 ksize。

## C++代码
```c++
#ifndef DAY23
#define DAY23

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day23() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl2_salt_noise.jpg");
	if (src.empty()) {
		printf("could not load image...\n");
		return;
	}
	namedWindow("input", WINDOW_AUTOSIZE);
	imshow("input", src);

	Mat dst;
	//medianBlur(src, dst, 5);
	medianBlur(src, dst, 3);
	imshow("medianblur ksize=3", dst);

	waitKey();
}

#endif // !DAY23
```

## 结果展示
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201129215100.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201129215100.png)
