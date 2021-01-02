# （补）OpenCV4（10）-图像像素值统计（C++，Python，JS）

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
像素值统计
- 最小（min）
- 最大（max）
- 均值（mean）
- 标准方差（standard deviation）

相关 API
- 最大最小值 minMaxLoc
- 计算均值与标准方差 meanStdDev

```c++
meanStdDev(Mat src, MatOfDouble mean, MatOfDouble stddev)
```
- src 表示输入 Mat 图像
- mean 表示计算出各个通道的均值,数组长度与通道数目一致
- stddev 表示计算出各个通道的标准方差，数组长度与通道数目一致

`minMaxLoc()` 函数要求输入图像必须是 `CV_8UC1` 类型的，否则会报错。

## C++代码
```c++
#ifndef DAY10
#define DAY10

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day10() {

	// 读取一张灰度图像
	Mat src_gray = imread("E:\\_Image\\OpenCVTest\\girl.jpg", IMREAD_GRAYSCALE);
	if (src_gray.empty()) {
		cout << "could not load image.." << endl;
		return;
	}
	imshow("src_gray", src_gray);

	if (src_gray.type() == CV_8UC1) {
		double minVal = 0, maxVal = 0;
		Point minLoc, maxLoc;
		minMaxLoc(src_gray, &minVal, &maxVal, &minLoc, &maxLoc, Mat());
		printf("min: %.2f, max: %.2f\n", minVal, maxVal);
		printf("min loc: (%d, %d)\n", minLoc.x, minLoc.y);
		printf("max loc: (%d, %d)\n", maxLoc.x, maxLoc.y);
	}
	else {
		cout << "not gray image.." << endl;
	}
	
	// 读取一张三通道彩色图像，获得它的均值和方差
	Mat src_color = imread("E:\\_Image\\OpenCVTest\\girl.jpg");
	if (src_color.empty()) {
		cout << "could not load image.." << endl;
		return;
	}
	imshow("src_color", src_color);

	Mat mean, stddev;
	meanStdDev(src_color, mean, stddev);
	printf("blue channel -> mean: %.2f, stddev: %2f\n", mean.at<double>(0, 0), stddev.at<double>(0, 0));
	printf("green channel -> mean: %.2f, stddev: %2f\n", mean.at<double>(1, 0), stddev.at<double>(1, 0));
	printf("red channel -> mean: %.2f, stddev: %2f\n", mean.at<double>(2, 0), stddev.at<double>(2, 0));
	
	// 根据图像的均值将彩色图像转换为二值图像
	for (int row = 0; row < src_color.rows; row++) {
		for (int col = 0; col < src_color.cols; col++) {
			Vec3b bgr = src_color.at<Vec3b>(row, col);
			bgr[0] = bgr[0] < mean.at<double>(0, 0) ? 0 : 255;
			bgr[1] = bgr[1] < mean.at<double>(1, 0) ? 0 : 255;
			bgr[2] = bgr[2] < mean.at<double>(2, 0) ? 0 : 255;
			src_color.at<Vec3b>(row, col) = bgr;
		}
	}
	imshow("binary", src_color);

	waitKey(0);
}

#endif // !DAY10
```

## Python代码
```python
import cv2 as cv
import numpy as np

# 查看版本
print(cv.__version__)

# 读取和显示图像
src = cv.imread("E:/_Image/OpenCVTest/girl.jpg", cv.IMREAD_GRAYSCALE)
cv.imshow("src", src)

# 获取灰度图的极值及位置
mmin, mmax, minLoc, maxLoc = cv.minMaxLoc(src)
print("min: %.2f, max: %.2f" % (mmin, mmax))
print("minLoc: ", minLoc)
print("maxLoc: ", maxLoc)

# 获取灰度图的均值和方差
means, stddev = cv.meanStdDev(src)
print("means: %.2f, stddev: %.2f" % (means, stddev))
src[np.where(src < means)] = 0
src[np.where(src > means)] = 255
cv.imshow("binary", src)

## 彩色图像二值化
src = cv.imread("E:/_Image/OpenCVTest/girl.jpg")
cv.imshow("color", src)
h, w, ch = src.shape
means, stddev = cv.meanStdDev(src)
print("blue channel -> means: %.2f, stddev: %.2f" % (means[0], stddev[0]))
print("green channel -> means: %.2f, stddev: %.2f" % (means[1], stddev[1]))
print("red channel -> means: %.2f, stddev: %.2f" % (means[2], stddev[2]))
print("h, w, ch", h, w, ch)
for row in range(h):
    for col in range(w):
        b, g, r = src[row, col]
        b = 0 if b < means[0] else 255
        g = 0 if g < means[1] else 255
        r = 0 if r < means[2] else 255
        src[row, col] = [b, g, r]
cv.imshow("color_binary", src)

# 等待键盘输入，释放内存
cv.waitKey()
cv.destroyAllWindows()
```

## JS代码
```js
<template>
  <div>
    <p>图像像素值统计</p>
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
  name: "day10",
  mounted() {
    this.init();
  },
  destoryed() {},
  data() {
    return {
      mats: [],
    };
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

      // 官方文档链接：

      // 读取图像
      let src = this.createMat(cv, 1, { name: "imageSrc" });

      // 转化到 gray 色彩空间
      let gray = this.createMat(cv, 2);
      cv.cvtColor(src, gray, cv.COLOR_RGBA2GRAY);

      // 计算灰度图的极值和位置
      // 和 C++，Python 程序运行的结果不一致，感到很奇怪
      if (gray.type() === cv.CV_8UC1) {
        let ret = cv.minMaxLoc(gray);
        console.log(ret);
      }

      // 计算彩色图的均值和方差
      let bgr = this.createMat(cv, 2);
      cv.cvtColor(src, bgr, cv.COLOR_RGBA2BGR);
      let means = this.createMat(cv, 2);
      let stddev = this.createMat(cv, 2);
      cv.meanStdDev(bgr, means, stddev);
      //   this.showImgInfo(means)
      //   this.showImgInfo(stddev)
      // 和 C++，Python 程序运行的结果不一致，感到很奇怪
      console.log(`blue channel -> mean: ${means.ucharAt(0, 0)}, stddev: ${stddev.ucharAt(0, 0)}`);
      console.log(`green channel -> mean: ${means.ucharAt(1, 0)}, stddev: ${stddev.ucharAt(1, 0)}`);
      console.log(`red channel -> mean: ${means.ucharAt(2, 0)}, stddev: ${stddev.ucharAt(2, 0)}`);

      // 显示图像
      cv.imshow("canvasOutput", gray);

      // 销毁所有 mat
      this.destoryAllMats();
    },
    createMat(cv, type, ops) {
      switch (type) {
        case 1:
          if (ops && ops.name) {
            let mat = cv.imread(ops.name);
            this.mats.push(mat);
            return mat;
          }
          break;
        case 2: {
          let mat = new cv.Mat();
          this.mats.push(mat);
          return mat;
        }
        case 3:
          if (ops && ops.rows && ops.cols && ops.type && ops.initValue) {
            let mat = new cv.Mat(ops.rows, ops.cols, ops.type, ops.initValue);
            this.mats.push(mat);
            return mat;
          }
          break;
        default:
          break;
      }
    },
    showImgInfo(src) {
      console.log("img size :", src.size());
      console.log("img type :", src.type());
      console.log("img cols :", src.cols);
      console.log("img rows :", src.rows);
      console.log("img depth:", src.depth());
      console.log("img channels:", src.channels());
    },
    destoryAllMats() {
      let i = 0;
      this.mats.forEach((item) => {
        item.delete();
        i++;
      });
      console.log("销毁图象数：", i);
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
```

补充说明：我并没有在官方文档中找到这次的 js 版本的 API 说明。更显奇怪的是，js 的统计结果和 c++ 还有 Python 的统计结果是不一致的，但 c++ 和 python 的结果是一致的，如果有小伙伴知道原因，欢迎私信我或给我留言。

## 结果展示
![结果展示1](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201117234247.png)

![结果展示2](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201117234329.png)

![结果展示3](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201121183446.png)