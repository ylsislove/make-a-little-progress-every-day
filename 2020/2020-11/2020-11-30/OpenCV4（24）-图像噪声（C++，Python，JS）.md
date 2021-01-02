# OpenCV4（24）-图像噪声（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
**图像噪声：**

图像噪声产生的原因很复杂，有的可能是数字信号在传输过程中发生了丢失或者受到干扰，有的是成像设备或者环境本身导致成像质量不稳定，反应到图像上就是图像的亮度与颜色呈现某种程度的不一致性。从噪声的类型上，常见的图像噪声可以分为如下几种：

|||
|-|-|
| 椒盐噪声 | 是一种随机在图像中出现的稀疏分布的黑白像素点，对椒盐噪声一种有效的去噪手段就是图像中值滤波 |
| 高斯噪声/符合高斯分布 | 一般会在数码相机的图像采集(acquisition)阶段发生,这个时候它的物理/电/光等各种信号都可能导致产生高斯分布噪声 |
| 均匀分布噪声 | 均匀/规则噪声一般都是因为某些规律性的错误导致的 |

## C++代码
```c++
#ifndef DAY24
#define DAY24

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void add_salt_pepper_noise(Mat &image);
void gaussian_noise(Mat &image);

void day24() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl2.jpg");
	if (src.empty()) {
		printf("could not load image...\n");
		return;
	}
	namedWindow("input", WINDOW_AUTOSIZE);
	imshow("input", src);

	add_salt_pepper_noise(src);
	gaussian_noise(src);

	waitKey();
}

void add_salt_pepper_noise(Mat &image) {
	RNG rng(12345);
	int h = image.rows;
	int w = image.cols;
	int nums = 5000;

	Mat dst = image.clone();
	for (int i = 0; i < nums; i++) {
		int x = rng.uniform(0, w);
		int y = rng.uniform(0, h);
		if (i % 2 == 1) {
			dst.at<Vec3b>(y, x) = Vec3b(255, 255, 255);
		}
		else {
			dst.at<Vec3b>(y, x) = Vec3b(0, 0, 0);
		}
	}
	imshow("salt pepper", dst);
}

void gaussian_noise(Mat &image) {
	Mat noise = Mat::zeros(image.size(), image.type());

	// 通过randn产生高斯随机噪声来填充矩阵，15是高斯均值，30是高斯方差
	randn(noise, 15, 30);

	Mat dst;
	add(image, noise, dst);
	imshow("gaussian noise", dst);
}

#endif // !DAY24
```

## 结果展示
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201201022435.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201201022435.png)
