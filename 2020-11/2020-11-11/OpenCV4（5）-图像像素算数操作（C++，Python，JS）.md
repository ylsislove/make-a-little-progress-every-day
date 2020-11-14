# OpenCV4（5）-图像像素算数操作（C++，Python，JS）.md

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
1. 像素算术操作
   - 加 add
   - 减 subtract
   - 乘 multiply
   - 除 divide

2. 参与运算的图像的数据类型、通道数目、大小必须相同

3. 读取图像的 imread() 函数有第二个参数，其默认值是 IMREAD_COLOR，即将加载的图像总是转换为彩色图像。转换后图像的类型是 CV_8UC3。

4. C++ 使用 saturate_cast 防止数据溢出

## C++代码
```c++
#ifndef DAY05
#define DAY05

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day05() {

	Mat src1 = imread("E:\\_Image\\OpenCVTest\\girl.jpg");
	if (src1.empty()) {
		cout << "could not load image1.." << endl;
		return;
	}

	// 第二个参数默认值是 IMREAD_COLOR
	// 即将加载的图像总是转换为彩色图像。转换后图像的类型是 CV_8UC3。
	Mat src2 = imread("E:\\_Image\\OpenCVTest\\girl_gray.jpg");
	if (src2.empty()) {
		cout << "could not load image2.." << endl;
		return;
	}

	if (src1.channels() != src2.channels()) {
		cout << "chennels is not equal!" << endl;
		return;
	}
	
	imshow("input1", src1);
	imshow("input2", src2);

	// 自己实现的 add 算法
	int height = src1.rows;
	int width = src1.cols;

	int b1 = 0, g1 = 0, r1 = 0;
	int b2 = 0, g2 = 0, r2 = 0;
	int b = 0, g = 0, r = 0;
	Mat result = Mat::zeros(src1.size(), src1.type());
	for (int row = 0; row < height; row++) {
		for (int col = 0; col < width; col++) {
			b1 = src1.at<Vec3b>(row, col)[0];
			g1 = src1.at<Vec3b>(row, col)[1];
			r1 = src1.at<Vec3b>(row, col)[2];

			b2 = src2.at<Vec3b>(row, col)[0];
			g2 = src2.at<Vec3b>(row, col)[1];
			r2 = src2.at<Vec3b>(row, col)[2];

			// saturate_cast 防止数据溢出
			result.at<Vec3b>(row, col)[0] = saturate_cast<uchar>(b1 + b2);
			result.at<Vec3b>(row, col)[1] = saturate_cast<uchar>(g1 + g2);
			result.at<Vec3b>(row, col)[2] = saturate_cast<uchar>(r1 + r2);
		}
	}
	imshow("output", result);

	// 直接调用 API
	Mat add_result = Mat::zeros(src1.size(), src1.type());
	add(src1, src2, add_result);
	imshow("add_result", add_result);

	Mat sub_result = Mat::zeros(src1.size(), src1.type());
	subtract(src1, src2, sub_result);
	imshow("sub_result", sub_result);

	Mat mul_result = Mat::zeros(src1.size(), src1.type());
	multiply(src1, src2, mul_result);
	imshow("mul_result", mul_result);

	Mat div_result = Mat::zeros(src1.size(), src1.type());
	divide(src1, src2, div_result);
	imshow("div_result", div_result);

	waitKey(0);
}

#endif // !DAY05
```

## Python代码
```python
import cv2 as cv
import numpy as np

# 查看版本
print(cv.__version__)

# 读取图像
src1 = cv.imread("E:/_Image/OpenCVTest/girl.jpg")
src2 = cv.imread("E:/_Image/OpenCVTest/girl_gray.jpg")

# 展示
cv.imshow("input1", src1)
cv.imshow("input2", src2)

# 获取属性
h, w, ch = src1.shape
print("h , w, ch", h, w, ch)

# 调用 API 算数操作
add_result = np.zeros(src1.shape, src1.dtype)
cv.add(src1, src2, add_result)
cv.imshow("add_result", add_result)

sub_result = np.zeros(src1.shape, src1.dtype)
cv.subtract(src1, src2, sub_result)
cv.imshow("sub_result", sub_result)

mul_result = np.zeros(src1.shape, src1.dtype)
cv.multiply(src1, src2, mul_result)
cv.imshow("mul_result", mul_result)

div_result = np.zeros(src1.shape, src1.dtype)
cv.divide(src1, src2, div_result)
cv.imshow("div_result", div_result)

# 等待键盘输入 释放内存
cv.waitKey(0)
cv.destroyAllWindows()
```

## JS代码
```js
<template>
  <div>
    <p>图像像素算数操作</p>
    <p id="status">OpenCV.js is loading...</p>
    <div class="inputoutput">
      <img id="imageSrc1" src="imgs/girl.jpg" />
      <img id="imageSrc2" src="imgs/girl_gray.jpg" />
    </div>
    <div class="inputoutput">
      <canvas id="canvasOutput"></canvas>
      <div class="caption">canvasOutput</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "day05",
  mounted() {
    this.init();
  },
  methods: {
    init() {
      setTimeout(() => {
        if (window.cv) {
          this.onOpenCvReady(window.cv);
        } else {
          this.init();
        }
      }, 500);
    },
    onOpenCvReady(cv) {
      document.getElementById("status").innerHTML = "OpenCV.js is ready.";

      let src1 = cv.imread("imageSrc1");
      let src2 = cv.imread("imageSrc2");
      let dst = new cv.Mat();

      // 官方文档链接
      // https://docs.opencv.org/4.5.0/dd/d4d/tutorial_js_image_arithmetics.html

      // 加法
      //   cv.add(src1, src2, dst);

      // 减法
      // Note that when used with RGBA images, the alpha channel is also subtracted.
      cv.cvtColor(src1, src1, cv.COLOR_RGBA2RGB);
      cv.cvtColor(src2, src2, cv.COLOR_RGBA2RGB);
      cv.subtract(src1, src2, dst);

      // 乘法
      //   cv.multiply(src1, src2, dst);

      // 除法
      //   cv.divide(src1, src2, dst);

      cv.imshow("canvasOutput", dst);

      src1.delete();
      src2.delete();
      dst.delete();
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
```

官方文档链接：[https://docs.opencv.org/4.5.0/dd/d4d/tutorial_js_image_arithmetics.html](https://docs.opencv.org/4.5.0/dd/d4d/tutorial_js_image_arithmetics.html)

## 结果展示
![input1-input2-output](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201114220325.png)

![add-sub](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201114220533.png)

![mul-div](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201114220728.png)