# 图像处理-BRIEF特征描述子匹配

  - [原理介绍](#%E5%8E%9F%E7%90%86%E4%BB%8B%E7%BB%8D)
  - [代码演示](#%E4%BB%A3%E7%A0%81%E6%BC%94%E7%A4%BA)
  - [结果展示](#%E7%BB%93%E6%9E%9C%E5%B1%95%E7%A4%BA)

## 原理介绍
BRIEF 特征描述子匹配得到特征点数据之后，根据 BRIEF 算法就可以建立描述子。选择候选特征点周围 S x S 大小的像素块、随机选择 n 对像素点。其中 P(x) 是图像模糊处理之后的像素值，原因在于高斯模糊可以抑制噪声影响、提供特征点稳定性，在实际代码实现中通常用均值滤波替代高斯滤波以便利用积分图方式加速计算获得更好的性能表现。常见滤波时候使用 3x3 ~ 9x9 之间的卷积核。滤波之后，根据上述描述子的生成条件，得到描述子。

作者论文提到 n 的取值通常为 128、256 或者 512。得到二进制方式的字符串描述子之后，匹配就可以通过 XOR 方式矩形，计算汉明距离。ORB 特征提取跟纯 BRIEF 特征提取相比较，BRIEF 方式采用随机点方式得最终描述子、而 ORB 通过 FAST 得到特征点然后得到描述子。

## 代码演示
```python
import cv2 as cv

box = cv.imread(r"F:\opencvTest\box.png");
box_in_sence = cv.imread(r"F:\opencvTest\box_in_scene.png");

# 创建 ORB 特征检测器
orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(box,None)
kp2, des2 = orb.detectAndCompute(box_in_sence,None)

# 暴力匹配
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)

# 绘制匹配
result = cv.drawMatches(box, kp1, box_in_sence, kp2, matches, None)
cv.imshow("orb-match", result)
cv.imwrite(r"E:\_Code\GitHub\make-a-little-progress-every-day\2020-05-30\orb_match.png", result)
cv.waitKey(0)
cv.destroyAllWindows()
```

## 结果展示
![orb_match](./orb_match.png)