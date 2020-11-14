# OpenCV4（8）-通道分离与合并（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
OpenCV 中的 imread() 函数原型为：Mat imread(const string& filename, int flags=1 )，flags 有如下几种类型

| 枚举标识              | 备注                                                              |
| --------------------- | ----------------------------------------------------------------- |
| IMREAD_UNCHANGED = -1 | 8 位原通道，新版本已经废置                                        |
| IMREAD_GRAYSCALE = 0  | 8 位 1 通道，图像总是转换成灰度                                   |
| IMREAD_COLOR = 1      | 8 位 3 通道，图像总是转换到彩色                                   |
| IMREAD_ANYDEPTH = 2   | 1 通道，若载入 16 位或 32 位图像返回对应深度图像，否则转换为 8 位 |
| IMREAD_ANYCOLOR = 4   | 8 位 3 通道                                                       |

其默认值是 IMREAD_COLOR，即加载三通道彩色图像。如果想展现最真实的图像，可以使用：

```c++
imread("xx.jpg", IMREAD_ANYDEPTH | IMREAD_ANYCOLOR )；
```

IMREAD_COLOR 色彩空间是 RGB 色彩空间、通道顺序是 BGR（蓝色、绿色、红色）、对于三通道的图像 OpenCV 中提供了两个 API 函数用以实现通道分离与合并
- split 通道分离
- merge 通道合并

## C++代码
```c++
#ifndef DAY08
#define DAY08

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day08() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");
	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}
	imshow("input", src);

	vector<Mat> mv;
	Mat dst1, dst2, dst3;
	// 蓝色通道为零
	split(src, mv);
	mv[0] = Scalar(0);
	merge(mv, dst1);
	imshow("output1", dst1);

	// 绿色通道为零
	split(src, mv);
	mv[1] = Scalar(0);
	merge(mv, dst2);
	imshow("output2", dst2);

	// 红色通道为零
	split(src, mv);
	mv[2] = Scalar(0);
	merge(mv, dst3);
	imshow("output3", dst3);

	waitKey(0);
}

#endif // !DAY08
```

## 结果展示
![input-output](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201114235150.png)

![output2-output3](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201114235237.png)