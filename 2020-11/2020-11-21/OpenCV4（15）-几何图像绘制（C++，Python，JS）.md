# OpenCV4（15）-几何图像绘制（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
1. 绘制直线

    ```c++
    void line(InputOutputArray img, Point pt1, Point pt2, const Scalar& color, int thickness = 1, int lineType = LINE_8, int shift = 0);
    ```

    thickness = 1    // 表示线宽为1。thickness = -1 表示进行填充

    lineType = LINE_8    // 表示线条类型，有如下几种可供选择

    ```c++
    enum LineTypes {
        FILLED  = -1,
        LINE_4  = 4, //!< 4-connected line
        LINE_8  = 8, //!< 8-connected line
        LINE_AA = 16 //!< antialiased line
    };
    ```

    shift = 0    // 偏移量，默认为0

2. 绘制矩形

    ```c++
    void rectangle(InputOutputArray img, Rect rec, const Scalar& color, int thickness = 1, int lineType = LINE_8, int shift = 0);
    ```

    Rect    // 设置绘制矩形的起点坐标和宽高

3. 绘制圆

    ```c++
    void circle(InputOutputArray img, Point center, int radius, const Scalar& color, int thickness = 1, int lineType = LINE_8, int shift = 0);
    ```

4. 绘制椭圆

    ```c++
    void ellipse(InputOutputArray img, Point center, Size axes, double angle, double startAngle, double endAngle, const Scalar& color, int thickness = 1, int lineType = LINE_8, int shift = 0);
    ```

    Size    // 设置椭圆x轴方向的长度和y轴方向的长度

5. 随机数API

    RNG 表示 OpenCV C++ 版本中的随机数对象，rng.uniform(a, b) 生成 [a, b) 之间的随机数，包含 a，但是不包含 b。

**注意：** OpenCV 没有专门的填充方法，只是把绘制几何形状时候的线宽 - thickness 参数值设置为负数即表示填充该几何形状或者使用参数 FILLED。

```c++
rectangle(image, rect, Scalar(255, 0, 0), -1, FILLED, 0);
```

这种写法会报错，-1 和 FILLED 不能同时出现。


## C++代码
```c++
#ifndef DAY15
#define DAY15

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day15() {

	Mat image = Mat::zeros(Size(512, 512), CV_8UC3);
	// 设置矩形的起点坐标，以及它的宽和高
	Rect rect(100, 100, 200, 200);
	rectangle(image, rect, Scalar(255, 0, 0), 2, LINE_8, 0);
	circle(image, Point(256, 256), 50, Scalar(0, 0, 255), 2, LINE_8, 0);
	ellipse(image, Point(256, 256), Size(150, 50), 360, 0, 360, Scalar(0, 255, 0), 2, LINE_8, 0);
	imshow("image", image);
	waitKey(0);

	// 声明一个随机数对象，并设置初始化种子
	RNG rng(0xFFFFFF);
	// 清空图像
	image.setTo(Scalar(0, 0, 0));

	for (int i = 0; i < 100000; i++) {
		//image.setTo(Scalar(0, 0, 0));
		int x1 = rng.uniform(0, 512);
		int y1 = rng.uniform(0, 512);
		int x2 = rng.uniform(0, 512);
		int y2 = rng.uniform(0, 512);

		int b = rng.uniform(0, 256);
		int g = rng.uniform(0, 256);
		int r = rng.uniform(0, 256);
		// line(image, Point(x1, y1), Point(x2, y2), Scalar(b, g, r), 1, LINE_AA, 0);
		rect.x = x1;
		rect.y = y1;
		rect.width = x2 - x1;
		rect.height = y2 - y1;
		rectangle(image, rect, Scalar(b, g, r), -1, LINE_AA, 0);
		imshow("image", image);

		char c = waitKey(20);
		if (c == 27)
			break;
	}

	waitKey();
}

#endif // !DAY15
```

## 结果展示
![结果展示1](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201122002726.png)

![结果展示2](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201122002837.gif)

![结果展示3](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201122002920.gif)
