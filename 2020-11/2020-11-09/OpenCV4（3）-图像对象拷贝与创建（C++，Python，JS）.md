# OpenCV4（3）-图像对象拷贝与创建（C++，Python，JS）

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
1. 图像对象的拷贝

    学过C++的应该都很清楚，拷贝分为深拷贝和浅拷贝。OpenCV 的 `clone()` 和 `copyTo` 是深拷贝，赋值运算符 `=` 是浅拷贝。

    ![图像对象的拷贝](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201109232731.png)

    头部保存了该图像的宽度和高度还有通道数等信息，数据部分保存了该图像的像素信息

2. 图像对象的创建

    常用方法有 `Mat::zeros()` 和 `Mat::ones()`

## C++代码
```c++
#ifndef DAY03
#define DAY03

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day03() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");

	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}

	// 创建方法-克隆
	Mat m1 = src.clone();

	// 复制
	Mat m2;
	src.copyTo(m2);

	// 赋值法
	Mat m3 = src;

	// 创建空白图像
	Mat m4 = Mat::zeros(src.size(), src.type());
	Mat m5 = Mat::zeros(Size(512, 512), CV_8UC3);
	Mat m6 = Mat::ones(Size(512, 512), CV_8UC3);

	waitKey(0);
}

#endif // !DAY03
```

## Python代码
```python
import cv2 as cv
import numpy as np

# 查看版本
print(cv.__version__)

# 读取图像
src = cv.imread("E:/_Image/OpenCVTest/girl.jpg")

# 深拷贝 克隆图像
m1 = np.copy(src)

# 浅拷贝 赋值
m2 = src

# 修改 src，m2 也会跟着变
src[100:200, 200:300, :] = 255

# 显示
cv.imshow("src", src)
cv.imshow("m1", m1)
cv.imshow("m2", m2)

# 创建图像对象
m3 = np.zeros(src.shape, src.dtype)
cv.imshow("m3", m3)

m4 = np.zeros([512, 512], np.uint8)
m4[:, :] = 127
cv.imshow("m4", m4)

m5 = np.ones(shape=[512, 512, 3], dtype=np.uint8)
m5[:, :, 0] = 255
cv.imshow("m5", m5)

# 等待键盘输入
cv.waitKey()

# 释放内存
cv.destroyAllWindows()
```

## JS代码
```js
<template>
  <div>
    <p>图像对象拷贝与创建</p>
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
  name: "day03",
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

        // 获取图像数据
        // 图像数据有图像的属性、类型、行数、列数、大小、深度、通道
        console.log("img size :", src.size());
        console.log("img type :", src.type());
        console.log("img cols :", src.cols);
        console.log("img rows :", src.rows);
        console.log("img depth:", src.depth());
        console.log("img channels:", src.channels());
        // img size : {width: 512, height: 562}
        // img type : 24
        // img cols : 512
        // img rows : 562
        // img depth: 0
        // img channels: 4

        // 图像对象的克隆 clone
        let dst = src.clone();

        // 图像对象的克隆 clone
        let dst2 = new cv.Mat();
        src.copyTo(dst2);

        //使用4个构造函数构造矩阵
        let rows = 512;
        let cols = 512;
        let type = cv.CV_8UC4;
        //创建默认矩阵
        let mat1 = new cv.Mat();
        //创建有行、列、类型的矩阵
        let mat2 = new cv.Mat(rows, cols, type);
        //创建有行、列、类型、初始化值得矩阵（R G B A）
        let mat3 = new cv.Mat(rows, cols, type, [255, 0, 0, 127]);

        //创建全零矩阵
        let mat4 = cv.Mat.zeros(rows, cols, type);
        //创建全 1 矩阵
        let mat5 = cv.Mat.ones(rows, cols, type);
        //创建单位矩阵
        let mat6 = cv.Mat.eye(rows, cols, type);

        // 显示
        cv.imshow("canvasOutput", mat3);

        src.delete();
        dst.delete();
        dst2.delete();
        mat1.delete();
        mat2.delete();
        mat3.delete();
        mat4.delete();
        mat5.delete();
        mat6.delete();
      };
    }
  }
};
</script>

<style lang="scss" scoped>
</style>
```

官方文档链接：[https://docs.opencv.org/4.5.0/de/d06/tutorial_js_basic_ops.html](https://docs.opencv.org/4.5.0/de/d06/tutorial_js_basic_ops.html)