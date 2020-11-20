# OpenCV4（14）-图像插值（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
四种最常见的图像插值算法

- INTER_NEAREST = 0
- INTER_LINEAR = 1
- INTER_CUBIC = 2
- INTER_LANCZOS4 = 4

相关API

```c++
void resize(InputArray src, OutputArray dst, Size dsize, double fx = 0, double fy = 0, int interpolation = INTER_LINEAR);
```

如果 `Size` 被设置的话，则根据 `Size` 做缩放插值；否则根据 `fx` 和 `fy` 做缩放插值。

应用场景

常被用于图像的几何变换、透视变换及插值计算新像素等。在计算量方面，临近点插值计算量最小，双立方插值计算量最大；在精度方面，临近点插值精度最低，具有明显的齿距效果，双立方插值的精度最高；

关于这四种插值算法的详细代码及理论解释可参考以下博客

- [图像放缩之临近点插值](https://blog.csdn.net/jia20003/article/details/6907152)
- [图像放缩之双线性内插值](https://blog.csdn.net/jia20003/article/details/6915185)
- [图像放缩之双立方插值](https://blog.csdn.net/jia20003/article/details/6919845)
- [图像处理之三种常见双立方插值算法](https://blog.csdn.net/jia20003/article/details/40020775)
- [图像处理之Lanczos采样放缩算法](https://blog.csdn.net/jia20003/article/details/17856859)

## C++代码
```c++
#ifndef DAY14
#define DAY14

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day14() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\small.png");
	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}
	imshow("src", src);

	int h = src.rows;
	int w = src.cols;
	float fx = 0.0, fy = 0.0;
	Mat dst = Mat::zeros(src.size(), src.type());
	resize(src, dst, Size(w * 2, h * 2), fx = 0, fy = 0, INTER_NEAREST);
	imshow("INTER_NEAREST", dst);
	
	resize(src, dst, Size(w * 2, h * 2), fx = 0, fy = 0, INTER_LINEAR);
	imshow("INTER_LINEAR", dst);
	
	resize(src, dst, Size(w * 2, h * 2), fx = 0, fy = 0, INTER_CUBIC);
	imshow("INTER_CUBIC", dst);
	
	resize(src, dst, Size(w * 2, h * 2), fx = 0, fy = 0, INTER_LANCZOS4);
	imshow("INTER_LANCZOS4", dst);

	waitKey();
}

#endif // !DAY14
```

## 结果展示
![结果展示](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201121001538.png)

可以看出，临近点插值的锯齿效果还是挺明显的~