# OpenCV4（4）-图像像素读写操作（C++，Python，JS）

  - [环境](#%E7%8E%AF%E5%A2%83)
  - [知识点](#%E7%9F%A5%E8%AF%86%E7%82%B9)
  - [C++代码](#c%E4%BB%A3%E7%A0%81)
  - [Python代码](#python%E4%BB%A3%E7%A0%81)
  - [JS代码](#js%E4%BB%A3%E7%A0%81)

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
C++ 中的像素遍历与访问
- 数组遍历
- 指针遍历

Python 中的像素遍历与访问
- 数组遍历

## C++代码
```c++
#ifndef DAY04
#define DAY04

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day04() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");

	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}

	// 直接读取图像像素
	int height = src.rows;
	int width = src.cols;
	int ch = src.channels();
	for (int row = 0; row < height; row++) {
		// 像素取反
		for (int col = 0; col < width; col++) {
			if (ch == 3) {
				Vec3b bgr = src.at<Vec3b>(row, col);
				bgr[0] = 255 - bgr[0];
				bgr[1] = 255 - bgr[1];
				bgr[2] = 255 - bgr[2];
				src.at<Vec3b>(row, col) = bgr;
			}
			else if (ch == 1) {
				int gray = src.at<uchar>(row, col);
				src.at<uchar>(row, col) = 255 - gray;
			}
		}
	}
	imshow("output", src);

	// 指针读取
	Mat result = Mat::zeros(src.size(), src.type());
	int blue = 0, green = 0, red = 0;
	int gray;
	for (int row = 0; row < height; row++) {
		uchar* curr_row = src.ptr<uchar>(row);
		uchar* result_row = result.ptr<uchar>(row);
		for (int col = 0; col < width; col++) {
			if (ch == 3) {
				blue = *curr_row++;
				green = *curr_row++;
				red = *curr_row++;

				*result_row++ = blue;
				*result_row++ = green;
				*result_row++ = red;
			}
			else if (ch == 1) {
				gray = *curr_row++;
				*result_row++ = gray;
			}
		}
	}
	imshow("result", result);

	waitKey(0);
}

#endif // !DAY04
```

## Python代码
```python
import cv2 as cv
import numpy as np

# 查看版本
print(cv.__version__)

# 读取图像
src = cv.imread("E:/_Image/OpenCVTest/girl.jpg")

# 查看属性
h, w, ch = src.shape
print("h, w, ch", h, w, ch)

# 像素取反
for row in range(h):
    for col in range(w):
        b, g, r = src[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        src[row, col] = [b, g, r]
cv.imshow("output", src)

# 等待键盘输入
cv.waitKey()

# 释放内存
cv.destroyAllWindows()
```

## JS代码
```js
<template>
  <div>
    <p>图像像素读写</p>
    <p id="status">OpenCV.js is loading...</p>
    <div class="inputoutput">
      <img id="imageSrc" alt="No Image" />
      <div class="caption">imageSrc <input type="file" id="fileInput" name="file" /></div>
    </div>
    <div class="inputoutput">
      <canvas id="canvasOutput"></canvas>
      <div class="caption">canvasOutput</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "day04",
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
      let imgElement = document.getElementById("imageSrc");
      let inputElement = document.getElementById("fileInput");
      inputElement.addEventListener(
        "change",
        e => {
          imgElement.src = URL.createObjectURL(e.target.files[0]);
        },
        false
      );
      imgElement.onload = function() {
        let src = cv.imread(imgElement);

        // 1. data 取值，获取适用于连续Mat，需用 isContinous()检测是否连续
        // 取（3，4）这个位置的像素
        let row = 3;
        let col = 4;
        let R, G, B, A;
        if (src.isContinuous()) {
          R = src.data[row * src.cols * src.channels() + col * src.channels()];
          G =
            src.data[
              row * src.cols * src.channels() + col * src.channels() + 1
            ];
          B =
            src.data[
              row * src.cols * src.channels() + col * src.channels() + 2
            ];
          A =
            src.data[
              row * src.cols * src.channels() + col * src.channels() + 3
            ];
          console.log(R, G, B, A);
        }

        // 2. at 限制：不能修改
        R = src.ucharAt(row, col * src.channels());
        G = src.ucharAt(row, col * src.channels() + 1);
        B = src.ucharAt(row, col * src.channels() + 2);
        A = src.ucharAt(row, col * src.channels() + 3);
        console.log(R, G, B, A);

        // 3. ptr 一般使用这个，简单方便
        let pixel = src.ucharPtr(row, col);
        R = pixel[0];
        G = pixel[1];
        B = pixel[2];
        A = pixel[3];
        console.log(R, G, B, A);
        // 修改
        pixel[0] = 0;
        pixel[1] = 0;
        pixel[2] = 0;
        pixel[3] = 255;
        console.log(src.ucharPtr(row, col));
        cv.imshow("canvasOutput", src);

        src.delete();
      };
    }
  }
};
</script>

<style lang="scss" scoped>
</style>
```

官方文档链接：[https://docs.opencv.org/4.5.0/de/d06/tutorial_js_basic_ops.html](https://docs.opencv.org/4.5.0/de/d06/tutorial_js_basic_ops.html)