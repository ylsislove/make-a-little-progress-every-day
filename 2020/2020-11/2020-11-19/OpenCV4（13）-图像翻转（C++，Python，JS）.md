# OpenCV4（13）-图像翻转（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
图像翻转的本质是像素映射，OpenCV支持三种图像翻转方式

- X 轴翻转 flipcode = 0
- Y 轴翻转 flipcode = 1
- XY 轴翻转 flipcode = -1

相关 API

```c++
void flip(InputArray src, OutputArray dst, int flipCode);
```

## C++代码
```c++
#ifndef DAY13
#define DAY13

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day13() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");
	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}
	imshow("src", src);

	Mat dst;
	flip(src, dst, 0);
	imshow("x-flip", dst);

	flip(src, dst, 1);
	imshow("y-flip", dst);

	flip(src, dst, -1);
	imshow("xy-flip", dst);

	waitKey();
}

#endif // !DAY13
```

## 结果展示
![src-xflip](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201120002645.png)

![yflip-xyflip](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201120002850.png)