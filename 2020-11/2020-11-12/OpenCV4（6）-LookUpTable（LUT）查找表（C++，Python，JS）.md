# OpenCV4（6）-LookUpTable（LUT）查找表（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
Look Up Table（LUT）查找表
```c
applyColorMap(src, dst, COLORMAP)
```
- src 表示输入图像
- dst表示输出图像
- OpenCV 支持 13 种颜色风格的查找表映射

![查找表](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201112235120.png)

## C++代码
```c++
#ifndef DAY06
#define DAY06

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day06() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");

	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}

	/*
	 * COLORMAP_AUTUMN = 0
	 * COLORMAP_BONE = 1
	 * COLORMAP_COOL = 8
	 * COLORMAP_HOT = 11
	 * COLORMAP_HSV = 9
	 * COLORMAP_JET = 2
	 * COLORMAP_OCEAN = 5
	 * COLORMAP_PARULA = 12
	 * COLORMAP_PINK = 10		好看
	 * COLORMAP_RAINBOW = 4
	 * COLORMAP_SPRING = 7
	 * COLORMAP_SUMMER = 6
	 * COLORMAP_WINTER = 3
	*/

	Mat dst;
	applyColorMap(src, dst, COLORMAP_PINK);
	imshow("colorMap", dst);

	waitKey(0);
}

#endif // !DAY06
```

## 结果展示
![结果展示](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201112235813.png)