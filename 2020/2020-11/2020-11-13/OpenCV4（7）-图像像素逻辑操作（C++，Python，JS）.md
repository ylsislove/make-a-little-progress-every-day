# OpenCV4（7）-图像像素逻辑操作（C++，Python，JS）

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
像素操作之逻辑操作
  - bitwise_and
  - bitwise_xor
  - bitwise_or

上面三个类似，都是针对两张图像的位操作

  - bitwise_not

针对输入图像, 图像取反操作，二值图像分析中经常用

![像素操作之逻辑操作](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201114000313.png)

补充说明：图像像素值不是只有 0 和 1，当按位与操作时，结果取两者之间的较小值；按位或操作时，结果取两者间的较大值；异或操作时，结果取两者之间的差值，所以示例代码显示结果的重叠区域的差值为 0，所以是黑色~

有读者可能会疑惑，为什么按位与操作时，结果取两者之间的较小值？可以这样理解，把 0-255 转换成二进制后，再按位与操作，结果就是较小的那个值~

## C++代码
```c++
#ifndef DAY07
#define DAY07

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day07() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\girl.jpg");
	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}
	imshow("input", src);

	// 取反操作
	Mat dst;
	bitwise_not(src, dst);
	imshow("dst", dst);

	// create image1
	Mat src1 = Mat::zeros(Size(400, 400), CV_8UC3);
	Rect rect(100, 100, 100, 100);
	src1(rect) = Scalar(0, 0, 255);
	imshow("input1", src1);

	// create image2
	Mat src2 = Mat::zeros(Size(400, 400), CV_8UC3);
	rect.x = 150;
	rect.y = 150;
	src2(rect) = Scalar(0, 0, 255);
	imshow("input2", src2);

	// 逻辑操作
	Mat dst1, dst2, dst3;
	bitwise_and(src1, src2, dst1);
	bitwise_xor(src1, src2, dst2);
	bitwise_or(src1, src2, dst3);

	// show results
	imshow("dst1", dst1);
	imshow("dst2", dst2);
	imshow("dst3", dst3);

	waitKey(0);
}

#endif // !DAY07
```

## Python代码
```python
import cv2 as cv
import numpy as np

# 查看版本
print(cv.__version__)

# 创建图像 1
src1 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src1[100:200, 100:200, 1] = 255
src1[100:200, 100:200, 2] = 255
cv.imshow("input1", src1)

# 创建图像 2
src2 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src2[150:250, 150:250, 2] = 255
cv.imshow("input2", src2)

# 进行逻辑运算
dst1 = cv.bitwise_and(src1, src2)
dst2 = cv.bitwise_xor(src1, src2)
dst3 = cv.bitwise_or(src1, src2)

# 显示结果
cv.imshow("dst1", dst1)
cv.imshow("dst2", dst2)
cv.imshow("dst3", dst3)

# 图像取反操作
src = cv.imread("E:/_Image/OpenCVTest/girl.jpg")
cv.imshow("input", src)
dst = cv.bitwise_not(src)
cv.imshow("dst", dst)

# 等待键盘输入 释放内存
cv.waitKey(0)
cv.destroyAllWindows()
```

## JS代码
```js
<template>
  <div>
    <p>图像像素逻辑操作</p>
    <p id="status">OpenCV.js is loading...</p>
    <div class="inputoutput">
      <img id="imageSrc" src="imgs/girl.jpg" />
    </div>
    <div class="inputoutput">
      <canvas id="canvasOutput"></canvas>
      <div class="caption">canvasOutput</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "day07",
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

      let src = cv.imread("imageSrc");
      let dst = new cv.Mat();

      // 官方文档链接：https://docs.opencv.org/4.5.0/dd/d4d/tutorial_js_image_arithmetics.html

      // 图像取反
      //   cv.cvtColor(src, src, cv.COLOR_RGBA2RGB);
      //   cv.bitwise_not(src, dst);

      // 创建图像 1
      let src1 = new cv.Mat(512, 512, cv.CV_8UC3);
      for (let i = 100; i < 200; i++) {
        for (let j = 100; j < 200; j++) {
          src1.ucharPtr(i, j)[0] = 255;
          src1.ucharPtr(i, j)[1] = 255;
        }
      }

      // 创建图像 2
      let src2 = new cv.Mat(512, 512, cv.CV_8UC3);
      for (let i = 150; i < 250; i++) {
        for (let j = 150; j < 250; j++) {
          src2.ucharPtr(i, j)[0] = 255;
        }
      }

      // 像素逻辑操作
      //   cv.bitwise_and(src1, src2, dst)
      //   cv.bitwise_or(src1, src2, dst)
      cv.bitwise_xor(src1, src2, dst);

      cv.imshow("canvasOutput", dst);

      src.delete();
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
![src-dst](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201113235457.png)

![input1-input2](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201113235551.png)

![dst1-dst2-dst3](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201113235638.png)
