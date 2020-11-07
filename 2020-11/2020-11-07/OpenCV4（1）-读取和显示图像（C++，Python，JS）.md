# OpenCV4（1）-读取和显示图像（C++，Python，JS）

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
* 读取图像：imread
* 显示图像：imshow

## C++代码
```c++
#ifndef DAY01
#define DAY01

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day01() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");

	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}

	namedWindow("show", WINDOW_AUTOSIZE);
	imshow("show", src);

	waitKey(0);
}

#endif // !DAY01
```
注意事项：
在 VS2017 中创建项目的时候选择创建空项目，预编译标头取消勾选。选择 x64 进行编译。

## Python代码
```python
import cv2 as cv

# 查看版本
print(cv.__version__)

# 读取图像
src = cv.imread("E:/_Image/OpenCVTest/girl.jpg")

# 显示图像
cv.imshow("input", src)

# 等待键盘输入
cv.waitKey()

# 释放内存
cv.destroyAllWindows()
```

## JS代码
```js
<template>
  <div>
    <h2>Hello OpenCV.js</h2>
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
  name: "day01",
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
        let mat = cv.imread(imgElement);
        cv.imshow("canvasOutput", mat);
        mat.delete();
      };
    }
  }
};
</script>

<style lang="scss" scoped>
</style>
```