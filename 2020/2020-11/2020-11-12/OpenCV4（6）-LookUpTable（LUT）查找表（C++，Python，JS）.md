# OpenCV4（6）-LookUpTable（LUT）查找表（C++，Python，JS）

  - [环境](#%E7%8E%AF%E5%A2%83)
  - [知识点](#%E7%9F%A5%E8%AF%86%E7%82%B9)
  - [C++代码](#c%E4%BB%A3%E7%A0%81)
  - [Python代码](#python%E4%BB%A3%E7%A0%81)
  - [JS代码](#js%E4%BB%A3%E7%A0%81)
  - [结果展示](#%E7%BB%93%E6%9E%9C%E5%B1%95%E7%A4%BA)

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
假设我们想在地图上显示美国不同地区的温度。我们可以用不同的颜色代表不同的意思。用蓝色表示较冷的温度，用红色表示较温暖的温度。温度数据只是一个例子，但还有其他几个数据是单值（灰度）的情况，但将其转换为彩色数据以实现可视化是有意义的。用伪彩色更好地显示数据的其他例子是高度、压力、密度、湿度等等。

Look Up Table（LUT）查找表
```c
applyColorMap(src, dst, COLORMAP)
```

- src 表示输入图像
- dst 表示输出图像
- OpenCV 支持多种颜色风格的查找表映射

![查找表](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201112235120.png)

```c
enum cv::ColormapTypes {
  cv::COLORMAP_AUTUMN = 0,
  cv::COLORMAP_BONE = 1,
  cv::COLORMAP_JET = 2,
  cv::COLORMAP_WINTER = 3,
  cv::COLORMAP_RAINBOW = 4,
  cv::COLORMAP_OCEAN = 5,
  cv::COLORMAP_SUMMER = 6,
  cv::COLORMAP_SPRING = 7,
  cv::COLORMAP_COOL = 8,
  cv::COLORMAP_HSV = 9,
  cv::COLORMAP_PINK = 10,
  cv::COLORMAP_HOT = 11,
  cv::COLORMAP_PARULA = 12,
  cv::COLORMAP_MAGMA = 13,
  cv::COLORMAP_INFERNO = 14,
  cv::COLORMAP_PLASMA = 15,
  cv::COLORMAP_VIRIDIS = 16,
  cv::COLORMAP_CIVIDIS = 17,
  cv::COLORMAP_TWILIGHT = 18,
  cv::COLORMAP_TWILIGHT_SHIFTED = 19,
  cv::COLORMAP_TURBO = 20,
  cv::COLORMAP_DEEPGREEN = 21
}
```

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

	Mat dst;
	applyColorMap(src, dst, COLORMAP_PINK);
	imshow("colorMap", dst);

	waitKey(0);
}

#endif // !DAY06
```

官方文档链接：[https://docs.opencv.org/4.5.0/d3/d50/group__imgproc__colormap.html](https://docs.opencv.org/4.5.0/d3/d50/group__imgproc__colormap.html)


## Python代码
```Python
import cv2 as cv

# 查看版本
print(cv.__version__)

# 读取图像
src = cv.imread("E:/_Image/OpenCVTest/girl.jpg")
cv.imshow("input", src)

# COLORMAP_AUTUMN = 0
# COLORMAP_BONE = 1
# COLORMAP_COOL = 8
# COLORMAP_HOT = 11 还行
# COLORMAP_HSV = 9
# COLORMAP_JET = 2
# COLORMAP_OCEAN = 5
# COLORMAP_PARULA = 12
# COLORMAP_PINK = 10 好看
# COLORMAP_RAINBOW = 4
# COLORMAP_SPRING = 7
# COLORMAP_SUMMER = 6 还行
# COLORMAP_WINTER = 3
dst = cv.applyColorMap(src, cv.COLORMAP_SUMMER)
cv.imshow("output", dst)

# 等待键盘输入 释放内存
cv.waitKey(0)
cv.destroyAllWindows()
```

## JS代码
很遗憾的是，opencv.js 好像没有提供 `applyColorMap` 函数的支持，我在 4.5.0 的版本中并没有找到这个方法。如果有读者朋友找到了这个方法，欢迎给我留言呀~

## 结果展示
![结果展示](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201112235813.png)