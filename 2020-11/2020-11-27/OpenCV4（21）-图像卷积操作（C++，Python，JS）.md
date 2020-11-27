# OpenCV4（21）-图像卷积操作（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
**图像卷积操作：**

图像卷积可以看成是一个窗口区域在另外一个大的图像上移动，对每个窗口覆盖的区域都进行点乘得到的值作为中心像素点的输出值。窗口的移动是从左到右，从上到下。窗口可以理解成一个指定大小的二维矩阵，里面有预先指定的值。

![[图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128020127.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128020127.png)

**相关API：**
```c++
void blur( InputArray src, OutputArray dst,
           Size ksize, Point anchor = Point(-1,-1),
           int borderType = BORDER_DEFAULT );
```

- src：输入图像，Mat 类型，图像深度为 CV_8U、CV_16U、CV_16S、CV_32F、CV_64F；
- dst：输出图像，与输入图像有相同的类型和尺寸；
- ksize：卷积核的大小；
- anchor：-1表示卷积之后的数据放在卷积核中心对应的位置；
- borderType：图像边界处理方式，通常默认即可。有如下类型：

```c++
enum BorderTypes {
    BORDER_CONSTANT    = 0, //!< `iiiiii|abcdefgh|iiiiiii`  with some specified `i`
    BORDER_REPLICATE   = 1, //!< `aaaaaa|abcdefgh|hhhhhhh`
    BORDER_REFLECT     = 2, //!< `fedcba|abcdefgh|hgfedcb`
    BORDER_WRAP        = 3, //!< `cdefgh|abcdefgh|abcdefg`
    BORDER_REFLECT_101 = 4, //!< `gfedcb|abcdefgh|gfedcba`
    BORDER_TRANSPARENT = 5, //!< `uvwxyz|abcdefgh|ijklmno`
 
    BORDER_REFLECT101  = BORDER_REFLECT_101, //!< same as BORDER_REFLECT_101
    BORDER_DEFAULT     = BORDER_REFLECT_101, //!< same as BORDER_REFLECT_101
    BORDER_ISOLATED    = 16 //!< do not look outside of ROI
};
```

## C++代码
```c++
#ifndef DAY21
#define DAY21

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day21() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");
	if (src.empty()) {
		printf("could not load image...\n");
		return;
	}
	namedWindow("input", WINDOW_AUTOSIZE);
	imshow("input", src);

	int h = src.rows;
	int w = src.cols;

	// 3x3 均值模糊，自定义版本实现
	Mat dst = src.clone();
	for (int row = 1; row < h - 1; row++) {
		for (int col = 1; col < w - 1; col++) {
			Vec3b p1 = src.at<Vec3b>(row - 1, col - 1);
			Vec3b p2 = src.at<Vec3b>(row - 1, col);
			Vec3b p3 = src.at<Vec3b>(row - 1, col + 1);
			Vec3b p4 = src.at<Vec3b>(row, col - 1);
			Vec3b p5 = src.at<Vec3b>(row, col);
			Vec3b p6 = src.at<Vec3b>(row, col + 1);
			Vec3b p7 = src.at<Vec3b>(row + 1, col - 1);
			Vec3b p8 = src.at<Vec3b>(row + 1, col);
			Vec3b p9 = src.at<Vec3b>(row + 1, col + 1);

			int b = p1[0] + p2[0] + p3[0] + p4[0] + p5[0] + p6[0] + p7[0] + p8[0] + p9[0];
			int g = p1[1] + p2[1] + p3[1] + p4[1] + p5[1] + p6[1] + p7[1] + p8[1] + p9[1];
			int r = p1[2] + p2[2] + p3[2] + p4[2] + p5[2] + p6[2] + p7[2] + p8[2] + p9[2];

			dst.at<Vec3b>(row, col)[0] = saturate_cast<uchar>(b / 9);
			dst.at<Vec3b>(row, col)[1] = saturate_cast<uchar>(g / 9);
			dst.at<Vec3b>(row, col)[2] = saturate_cast<uchar>(r / 9);
		}
	}
	imshow("blur", dst);

	// OpenCV API 均值模糊
	Mat result;
	blur(src, result, Size(15, 15), Point(-1, -1), 4);
	imshow("result", result);

	waitKey();
}

#endif // !DAY21
```

## 结果展示
![[图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128021243.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201128021243.png)
