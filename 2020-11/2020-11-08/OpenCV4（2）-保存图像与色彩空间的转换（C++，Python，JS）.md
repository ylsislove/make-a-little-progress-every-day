# OpenCV4（2）-保存图像与色彩空间的转换（C++，Python，JS）

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
1. 图像保存 — imwrite
   * 第一个参数是图像保存路径
   * 第二个参数是图像内存对象

2. 色彩空间转换函数 — cvtColor
   * COLOR_BGR2GRAY = 6 彩色到灰度
   * COLOR_GRAY2BGR = 8 灰度到彩色
   * COLOR_BGR2HSV = 40 BGR到HSV
   * COLOR_HSV2BGR = 54 HSV到BGR

## C++代码
```c++
#ifndef DAY02
#define DAY02

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day02() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");

	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}

	namedWindow("show", WINDOW_AUTOSIZE);
	imshow("show", src);

	Mat gray;
	cvtColor(src, gray, COLOR_BGR2GRAY);
	namedWindow("gray", WINDOW_AUTOSIZE);
	imshow("gray", gray);

	imwrite("E:\\_Image\\OpenCVTest\\girl_gray.jpg", gray);

	if (gray.type() == CV_8UC1) {
		//input image is grayscale
		cout << "gray" << endl;
	}
	else {
		//input image is colour
		cout << "color" << endl;
	}

	waitKey(0);
}

#endif // !DAY02
```

注意事项：
1. COLOR_GRAY2BGR 要求图像的类型是 CV_8UC1。该函数的原理是将图像的通道变多，但是每个像素点三通道的像素值还是一样！所以即使转换成功，图像依旧是灰色的。

2. 读取图像的 imread() 函数有第二个参数，其默认值是 IMREAD_COLOR ，即将加载的图像总是转换为彩色图像。转换后图像的类型是 CV_8UC3。

## Python代码
```python
import cv2 as cv

# 查看版本
print(cv.__version__)

# 读取图像
src = cv.imread("E:/_Image/OpenCVTest/girl.jpg")

# 显示图像
cv.imshow("input", src)

# 彩色转灰度
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# 显示图像
cv.imshow("gray", gray)

# 保存图像
cv.imwrite("E:/_Image/OpenCVTest/girl_gray.jpg", gray)

# 等待键盘输入
cv.waitKey()

# 释放内存
cv.destroyAllWindows()
```

## JS代码
```js
<template>
  <div>
    <p>保存图像与色彩空间的转换</p>
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
  name: "day02",
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
        // mat with channels stored in RGBA order.
        let src = cv.imread(imgElement);
        let gray = new cv.Mat();
        // 官方文档链接：https://docs.opencv.org/4.5.0/db/d64/tutorial_js_colorspaces.html
        cv.cvtColor(src, gray, cv.COLOR_RGBA2GRAY, 0);
        cv.imshow("canvasOutput", gray);
        // opencv.js不支持imwrite方法
        src.delete();
        gray.delete();
      };
    }
  }
};
</script>

<style lang="scss" scoped>
</style>
```

注意事项：
1. opencv.js 不支持 imwrite 方法。仔细想想也可以理解，毕竟是 web 端程序，不可以随意往服务器端保存东西呀

2. 但是，如果看官用的是 opencv4nodejs，它是提供 imwrite 方法的，亲测。这是专门用于服务器端的 opencv，注意我说的是服务器端，而不是 web 端。意思是 opencv4nodejs 可以用于 nodejs 写的服务器端，但是直接在浏览器是无法运行的。具体如何安装 opencv4nodejs 可以看我写的这篇文章：[OpenCV-npm安装opencv4nodejs（Windows）](../2020-11-01/OpenCV-npm安装opencv4nodejs（Windows）.md)

3. 官方文档链接：[https://docs.opencv.org/4.5.0/db/d64/tutorial_js_colorspaces.html](https://docs.opencv.org/4.5.0/db/d64/tutorial_js_colorspaces.html)

## 结果展示
![结果展示](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201109001923.png)
