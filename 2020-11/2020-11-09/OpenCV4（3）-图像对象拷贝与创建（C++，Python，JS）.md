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
data() {
  return {
    num2type: {
      1: 'CV_8SC1',
      9: 'CV_8SC2',
      17: 'CV_8SC3',
      25: 'CV_8SC4',
      0: 'CV_8UC1',
      8: 'CV_8UC2',
      16: 'CV_8UC3',
      24: 'CV_8UC4',
      3: 'CV_16SC1',
      11: 'CV_16SC2',
      19: 'CV_16SC3',
      27: 'CV_16SC4',
      2: 'CV_16UC1',
      10: 'CV_16UC2',
      18: 'CV_16UC3',
      26: 'CV_16UC4',
      5: 'CV_32FC1',
      13: 'CV_32FC2',
      21: 'CV_32FC3',
      29: 'CV_32FC4',
      4: 'CV_32SC1',
      12: 'CV_32SC2',
      20: 'CV_32SC3',
      28: 'CV_32SC4',
      6: 'CV_64FC1',
      14: 'CV_64FC2',
      22: 'CV_64FC3',
      30: 'CV_64FC4'
    }
  }
},
methods: {
  onOpenCvReady() {
    if (!this.value) {
      this.$message.error('请选择一种创建类型')
      return
    }
 
    // 官方文档链接：https://docs.opencv.org/4.5.0/de/d06/tutorial_js_basic_ops.html
    const cv = window.cv
 
    // 读取图像
    const src = cv.imread('imageSrcRaw')
 
    // 拷贝 克隆 创建图像
    let dst = null
    switch (this.value) {
      case 1:
        dst = src.clone()
        break
      case 2:
        dst = new cv.Mat()
        src.copyTo(dst)
        break
      case 3:
        dst = new cv.Mat()
        break
      case 4:
        dst = new cv.Mat(512, 512, cv.CV_8UC4)
        break
      case 5:
        dst = new cv.Mat(512, 512, cv.CV_8UC4, [255, 0, 0, 127])
        break
      case 6:
        dst = cv.Mat.zeros(512, 512, cv.CV_8UC4)
        break
      case 7:
        dst = cv.Mat.ones(512, 512, cv.CV_8UC4)
        break
      case 8:
        dst = cv.Mat.eye(512, 512, cv.CV_8UC4)
        break
    }
 
    // 显示图像
    if (dst) cv.imshow('canvasOutput', dst)
 
    // 销毁所有 mat 释放内存
    src.delete()
    if (dst) dst.delete()
  },
  showImgInfo() {
    const img = window.cv.imread('imageSrcRaw')
    let content = ''
    content += 'img type: ' + this.num2type[img.type()] + ' '
    content += 'img cols: ' + img.cols + ' '
    content += 'img rows: ' + img.rows + ' '
    content += 'img depth: ' + img.depth() + ' '
    content += 'img channels: ' + img.channels() + ' '
    this.$alert(content, '图像属性', {
      confirmButtonText: '确定'
    })
  }
}
```

官方文档链接：[https://docs.opencv.org/4.5.0/de/d06/tutorial_js_basic_ops.html](https://docs.opencv.org/4.5.0/de/d06/tutorial_js_basic_ops.html)
