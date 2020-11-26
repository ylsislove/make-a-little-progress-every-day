# OpenCV4（20）-图像直方图反向投影（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
**图像直方图反向投影：**

图像直方图反向投影是通过构建指定模板图像的二维直方图空间与目标的二维直方图空间，进行直方图数据归一化之后， 进行比率操作，对所有得到非零数值，生成查找表对原图像进行像素映射之后，再进行图像模糊输出的结果。

**直方图反向投影流程：**
- 计算直方图
- 计算比率 R
- LUT 查找表
- 卷积模糊
- 归一化输出

**相关API：**
```c++
void calcBackProject( const Mat* images, int nimages,
                      const int* channels, InputArray hist,
                      OutputArray backProject, const float** ranges,
                      double scale = 1, bool uniform = true );
```

- images：目标图像数组；
- nimages：目标图像的个数；
- channels：需要进行统计的通道数组，第一个数组通道从 `0` 到 `image[0].channels()-1`，第二个数组从 `image[0].channels()` 到 `images[0].channels()+images[1].channels()-1`，以后的数组以此类推；
- hist：模板图像；
- backProject：目标图像反向投影后的输出图像；
- ranges：每一个特征维度中 bin 的取值范围；
- scale：是否需要对图像进行放缩，默认 1.0 即可；
- uniform：直方图是否均匀的标识符，默认为 true。

**注意：**

事实上，在 OpenCV 中，为了加快速度，进行直方图的反向投影并不会进行计算比率 R 的这一步操作，在得到模板图形的直方图数据，且进行归一化操作之后，OpenCV 直接进行模板图像和目标图像的 LUT 查找表映射，最终得到反射投影后的结果。

上文所说的直方图反射投影的流程，具体实现代码可以参考贾志刚老师的 [CV4J 开源代码](https://github.com/imageprocessor/cv4j)，纯 Java 语言的轻量级图像处理库。

## C++代码
```c++
#ifndef DAY20
#define DAY20

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void backProjection_demo(Mat &image, Mat &model);

void day20() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\target.png");
	Mat model = imread("E:\\_Image\\OpenCVTest\\sample.png");
	if (src.empty() || model.empty()) {
		printf("could not load image...\n");
		return;
	}
	imshow("target", src);
	imshow("model", model);

	backProjection_demo(src, model);

	waitKey();
}

void backProjection_demo(Mat &image, Mat &model) {
	// 转化为HSV色彩空间
	Mat model_hsv, image_hsv;
	cvtColor(model, model_hsv, COLOR_BGR2HSV);
	cvtColor(image, image_hsv, COLOR_BGR2HSV);

	// 定义直方图参数与属性
	int h_bins = 32; int s_bins = 32;
	int histSize[] = { h_bins, s_bins };
	// h通道取值范围0到180，s通道取值范围0到256
	float h_ranges[] = { 0, 180 };
	float s_ranges[] = { 0, 256 };
	const float* ranges[] = { h_ranges, s_ranges };
	int channels[] = { 0, 1 };

	// 计算model的直方图
	Mat roiHist;
	calcHist(&model_hsv, 1, channels, Mat(), roiHist, 2, histSize, ranges);

	// 直方图归一化
	normalize(roiHist, roiHist, 0, 255, NORM_MINMAX, -1, Mat());

	// 直方图二维化显示
	Mat roiHist_Show;
	roiHist.convertTo(roiHist_Show, CV_8UC3);
	resize(roiHist_Show, roiHist_Show, Size(400, 400));
	imshow("roiHist_Show_400x400", roiHist_Show);

	// 将image和model进行反向投影，得到反向投影后的结果backproj
	MatND backproj;
	calcBackProject(&image_hsv, 1, channels, roiHist, backproj, ranges, 1.0);

	// 显示backproj
	imshow("BackProj", backproj);
}

#endif // !DAY20
```

## 结果展示
![[图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201127003114.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201127003114.png)

![[图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201127003156.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201127003156.png)
