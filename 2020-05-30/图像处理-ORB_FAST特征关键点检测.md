# 图像处理-ORB_FAST特征关键点检测

  - [原理介绍](#%E5%8E%9F%E7%90%86%E4%BB%8B%E7%BB%8D)
  - [相关API](#%E7%9B%B8%E5%85%B3api)
  - [代码演示](#%E4%BB%A3%E7%A0%81%E6%BC%94%E7%A4%BA)
  - [结果展示](#%E7%BB%93%E6%9E%9C%E5%B1%95%E7%A4%BA)

## 原理介绍
ORB - (Oriented Fast and Rotated BRIEF) 算法是基于 FAST 特征检测与 BRIEF 特征描述子匹配实现，相比 BRIEF 算法中依靠随机方式获取而值点对，ORB 通过 FAST 方法，FAST 方式寻找候选特征点方式是假设灰度图像像素点 A 周围的像素存在连续大于或者小于 A 的灰度值，选择任意一个像素点 P，假设半径为 3，周围 16 个像素表示如下

![ORB_FAST特征关键点检测](./ORB_FAST特征关键点检测.png)

## 相关API
```c++

static Ptr<ORB> cv::ORB::create (   
        int     nfeatures = 500,
        float   scaleFactor = 1.2f,
        int     nlevels = 8,
        int     edgeThreshold = 31,
        int     firstLevel = 0,
        int     WTA_K = 2,
        int     scoreType = ORB::HARRIS_SCORE,
        int     patchSize = 31,
        int     fastThreshold = 20 
) 
```
| 参数 | 含义 |
| - | - |
| nfeatures | The maximum number of features to retain. 最终输出最大特征点数目 |
| scaleFactor | Pyramid decimation ratio, greater than 1. scaleFactor==2 means the classical pyramid, where each next level has 4x less pixels than the previous, but such a big scale factor will degrade feature matching scores dramatically. On the other hand, too close to 1 scale factor will mean that to cover certain scale range you will need more pyramid levels and so the speed will suffer. 金字塔上采样比率，大于1。scale factor==2 表示经典的金字塔，其中每个下一级的像素比上一级少4倍，但如此大的比例因子将显著降低特征匹配分数。另一方面，太接近1个比例因子将意味着要覆盖一定的比例范围，你将需要更多的金字塔层次，因此速度将受到影响。|
| nlevels | The number of pyramid levels. The smallest level will have linear size equal to input_image_linear_size/pow(scaleFactor, nlevels). 金字塔的层数。最小级别的线性大小将等于输入图像的线性大小/pow（缩放因子，nlevels）。|
| edgeThreshold | This is size of the border where the features are not detected. It should roughly match the patchSize parameter. 未检测到特征的边缘阈值。它应该与patchSize参数大致匹配。|
| firstLevel | It should be 0 in the current implementation. 当前实现中应为0。|
| WTA_K | 跟BRIEF描述子有关。[详情看链接。](https://docs.opencv.org/3.2.0/db/d95/classcv_1_1ORB.html#adc371099dc902a9674bd98936e79739c) |
| scoreType | The default HARRIS_SCORE means that Harris algorithm is used to rank features (the score is written to KeyPoint::score and is used to retain best nfeatures features); FAST_SCORE is alternative value of the parameter that produces slightly less stable keypoints, but it is a little faster to compute. 对所有的特征点进行排名用的方法。默认的 HARRIS_SCORE 表示 HARRIS 算法用于对特征进行排序（该分数写入 KeyPoint::SCORE 并用于保留最佳 nfeatures 特征）；FAST_SCORE 是产生稍微不稳定的 keypoints 的参数的可选值，但计算速度稍快。 |
| patchSize | 	size of the patch used by the oriented BRIEF descriptor. Of course, on smaller pyramid layers the perceived image area covered by a feature will be larger. 定向简短描述符使用的修补程序的大小。当然，在较小的金字塔层上，特征覆盖的感知图像区域将更大。 |
| fastThreshold | [opencv官方文档](https://docs.opencv.org/3.2.0/db/d95/classcv_1_1ORB.html#adc371099dc902a9674bd98936e79739c) |


## 代码演示
```python
import cv2 as cv
import numpy as np
# 导入自己写的一个工具库
import opencv_utils

src = cv.imread(r"F:\opencvTest\girl.jpg")
orb = cv.ORB().create()
kps = orb.detect(src)
# opencv 自带的绘制特征点函数 drawKeypoints
# result = cv.drawKeypoints(src, kps, None, (0, 255, 0), cv.DrawMatchesFlags_DEFAULT)
# 自己实现的绘制特征点
i = 0
result = np.copy(src)
color = np.random.randint(0, 255, (len(kps), 3))
for kp in kps:
    x, y = kp.pt
    cv.circle(result, (np.int32(x), np.int32(y)), 3, color[i].tolist(), 2)
    i += 1
out_img = opencv_utils.merge2Image(src, result)
cv.imshow("result", out_img)
cv.imwrite(r"E:\_Code\GitHub\make-a-little-progress-every-day\2020-05-30\orb_result.png", out_img)
cv.waitKey(0)
cv.destroyAllWindows()
```

## 结果展示
![orb_result](./orb_result.png)
