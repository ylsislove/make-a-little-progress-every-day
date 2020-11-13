# OpenCV4（7）-图像像素逻辑操作（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
像素操作之逻辑操作
  - bitwise_and
  - bitwise_xor
  - bitwise_or

上面三个类似，都是针对两张图像的位操作

  - bitwise_not

针对输入图像, 图像取反操作，二值图像分析中经常用

## C++代码
```c++
#ifndef DAY07
#define DAY07

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day07() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");
	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}
	imshow("input", src);

	// 取反操作
	Mat dst;
	bitwise_not(src, dst);
	imshow("dst", dst);

	// create image1
	Mat src1 = Mat::zeros(Size(400, 400), CV_8UC3);
	Rect rect(100, 100, 100, 100);
	src1(rect) = Scalar(0, 0, 255);
	imshow("input1", src1);

	// create image2
	Mat src2 = Mat::zeros(Size(400, 400), CV_8UC3);
	rect.x = 150;
	rect.y = 150;
	src2(rect) = Scalar(0, 0, 255);
	imshow("input2", src2);

	// 逻辑操作
	Mat dst1, dst2, dst3;
	bitwise_and(src1, src2, dst1);
	bitwise_xor(src1, src2, dst2);
	bitwise_or(src1, src2, dst3);

	// show results
	imshow("dst1", dst1);
	imshow("dst2", dst2);
	imshow("dst3", dst3);

	waitKey(0);
}

#endif // !DAY07
```

## 结果展示
![src-dst](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201113235457.png)

![input1-input2](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201113235551.png)

![dst1-dst2-dst3](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201113235638.png)
