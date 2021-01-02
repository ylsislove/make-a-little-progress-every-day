# OpenCV4（9）-色彩空间的转换及应用（C++，Python，JS）

  - [环境](#%E7%8E%AF%E5%A2%83)
  - [知识点](#%E7%9F%A5%E8%AF%86%E7%82%B9)
    - [色彩空间](#%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4)
    - [相关API](#%E7%9B%B8%E5%85%B3api)
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
### 色彩空间
- RGB 色彩空间

    是我们最常用的色彩空间，且与设备无关。

- HSV 色彩空间

    对于一些直方图相关的图像处理和算法，将其转到 HSV 色彩空间，通常会取得较好的效果。

- YUV 色彩空间

    一种跟设备有关的色彩空间。

- YCrCb 色彩空间

    常用作皮肤检测，根据一些颜色的统计模型，通常会取得较好的效果。

### 相关API
- 色彩空间转换 cvtColor
- 提取指定色彩范围区域 inRange

![HSV色彩空间](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201115191804.png)

注：[关于 HSV 各通道在 OpenCV 中取值范围的确定](https://blog.csdn.net/kakiebu/article/details/79476305)

上图清晰的列出来不同的颜色在 HSV 色彩空间的最小值和最大值。利用这个取值范围，我们便可以实现一些好玩的应用。

例如，绿色在 HSV 色彩空间的取值范围是（35， 43， 46）—（77， 255， 255）。通过 inRange 函数，可以很方便的将人物和绿幕背景分离出来。再通过像素的逻辑操作与或非，便可以实现更换背景的效果~~

## C++代码
```c++
#ifndef DAY09
#define DAY09

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

void day09() {

	Mat src = imread("E:\\_Image\\OpenCVTest\\tinygreen.jpg");
	if (src.empty()) {
		cout << "could not load image.." << endl;
		return;
	}
	imshow("src", src);

	Mat hsv, mask, mask_not, people;
	cvtColor(src, hsv, COLOR_BGR2HSV);

	// 获取背景蒙版，即绿幕部分为白，前景人物部分为黑
	inRange(hsv, Scalar(35, 43, 46), Scalar(77, 255, 255), mask);
	imshow("mask", mask);
	// 蒙版取非，即前景人物部分为白色
	bitwise_not(mask, mask_not);
	imshow("mask_not", mask_not);

	// 利用蒙版，将人物部分抠出
	bitwise_and(src, src, people, mask_not);
	imshow("people", people);

	// 取一张背景图，并截取与mask相同尺寸的部分
	Mat scene = imread("E:\\_Image\\OpenCVTest\\scene.jpg");
	Mat dstScene(scene, Rect(0, 0, people.cols, people.rows));
	imshow("dstScene", dstScene);

	// 利用蒙版，在背景图中扣掉待填充的人物蒙版部分
	Mat sceneBackground, finalImage;
	bitwise_and(dstScene, dstScene, sceneBackground, mask);
	imshow("sceneBackground", sceneBackground);

	// 或操作，将人物融入背景图中
	bitwise_or(sceneBackground, people, finalImage);
	imshow("final", finalImage);

	waitKey(0);
}

#endif // !DAY09
```

## Python代码
```python
import cv2 as cv

# 查看版本
print(cv.__version__)

# 读取显示图像
src = cv.imread("E:/_Image/OpenCVTest/tinygreen.jpg")
cv.imshow("bgr", src)

# RGB to HSV
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# RGB to YUV
yuv = cv.cvtColor(src, cv.COLOR_BGR2YUV)
cv.imshow("yuv", yuv)

# RGB to YUV
ycrcb = cv.cvtColor(src, cv.COLOR_BGR2YCrCb)
cv.imshow("ycrcb", ycrcb)

# 获取背景蒙版，即绿幕部分为白，前景人物部分为黑
mask = cv.inRange(hsv, (35, 43, 46), (77, 255, 255))
cv.imshow("mask", mask)

# 蒙版取非，即前景人物部分为白色
mask_not = cv.bitwise_not(mask)
cv.imshow("mask_not", mask_not)

# 利用蒙版，将人物部分抠出
people = cv.bitwise_and(src, src, mask=mask_not)
cv.imshow("people", people)

# 取一张背景图，并截取与mask相同尺寸的部分
scene = cv.imread("E:/_Image/OpenCVTest/scene.jpg")
dstScene = scene[:people.shape[0], :people.shape[1], :]
cv.imshow("dstScene", dstScene)

# 利用蒙版，在背景图中扣掉待填充的人物蒙版部分
sceneBackground = cv.bitwise_and(dstScene, dstScene, mask=mask)
cv.imshow("sceneBackground", sceneBackground)

# 或操作，将人物融入背景图中
finalImage = cv.bitwise_or(sceneBackground, people)
cv.imshow("finalImage", finalImage)

# 等待键盘输入 释放内存
cv.waitKey(0)
cv.destroyAllWindows()
```

## JS代码
```js
<template>
  <div>
    <p>色彩空间的转换及应用</p>
    <p id="status">OpenCV.js is loading...</p>
    <div class="inputoutput">
      <img id="imageSrc" src="imgs/tinygreen.jpg" />
      <img id="imageSrc2" src="imgs/scene.jpg" />
    </div>
    <div class="inputoutput">
      <canvas id="canvasOutput"></canvas>
      <div class="caption">canvasOutput</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "day09",
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

      // 官方文档链接：https://docs.opencv.org/4.5.0/db/d64/tutorial_js_colorspaces.html

      let src = this.createMat(cv, 1, { name: "imageSrc" });

      // 转化到 HSV 色彩空间
      let hsv = this.createMat(cv, 2);
      cv.cvtColor(src, hsv, cv.COLOR_RGB2HSV);

      // 获取背景蒙版，即绿幕部分为白，前景人物部分为黑
      let mask = this.createMat(cv, 2);
      let low = this.createMat(cv, 3, {
        rows: src.rows,
        cols: src.cols,
        type: cv.CV_8UC3,
        initValue: [35, 43, 46, 255],
      });
      let high = this.createMat(cv, 3, {
        rows: src.rows,
        cols: src.cols,
        type: cv.CV_8UC3,
        initValue: [77, 255, 255, 255],
      });
      cv.inRange(hsv, low, high, mask);

      // 蒙版取非，即前景人物部分为白色
      let mask_not = this.createMat(cv, 2);
      cv.bitwise_not(mask, mask_not);

      // 利用蒙版，将人物部分抠出
      let people = this.createMat(cv, 2);
      cv.bitwise_and(src, src, people, mask_not);

      // 取一张背景图，并截取与mask相同尺寸的部分
      let scene = this.createMat(cv, 1, { name: "imageSrc2" });
      let rect = new cv.Rect(0, 0, people.cols, people.rows);
      let dstScene = this.createMat(cv, 2);
      dstScene = scene.roi(rect);

      // 利用蒙版，在背景图中扣掉待填充的人物蒙版部分
      let sceneBackground = this.createMat(cv, 2);
      cv.bitwise_and(dstScene, dstScene, sceneBackground, mask);

      // 或操作，将人物融入背景图中
      let finalImage = this.createMat(cv, 2);
      cv.bitwise_or(sceneBackground, people, finalImage);

      // 显示图像
      cv.imshow("canvasOutput", finalImage);

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
    destoryAllMats() {
      this.mats.forEach((item) => {
        item.delete();
      });
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
```

官方文档链接：[https://docs.opencv.org/4.5.0/db/d64/tutorial_js_colorspaces.html](https://docs.opencv.org/4.5.0/db/d64/tutorial_js_colorspaces.html)

## 结果展示
![结果展示](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201115192055.png)