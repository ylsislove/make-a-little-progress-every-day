---
title: 用Python理解图像和视频的本质
date: 2022-10-28 00:57:08
categories:
 - [人工智能, 基础知识]
tags: 
 - python
 - numpy
---

## 安装jupyterlab
更换国内源之后，在anaconda powershell prompt用下面命令安装
```
conda install jupyterlab
```

安装完成后，在命令行输入`jupyter-lab`启动

## numpy常用命令
| 命令                              | 备注                        |
| --------------------------------- | --------------------------- |
| np.array([1,2,3,4])               | Python列表转换为numpy的数组 |
| np.arange(0,10)                   | 创建一个0~9的一维数组       |
| np.ones(shape=(3,3))              | 创建一个大小为3*3的全1数组  |
| np.zeros(shape=(5,5))             | 创建大小为5*5的全0数组      |
| np.random.randint(0,100,10)       | 随机10个整数                |
| arr.max()                         | 获取最大值                  |
| arr.argmax()                      | 获取最大值的索引            |
| arr.min()                         | 获取最小值                  |
| arr.argmin()                      | 获取最小值索引              |
| arr.mean()                        | 获取平均值                  |
| arr.shape                         | 获取numpy数组的大小         |
| arr.reshape((5,2))                | 转换数组的形状              |
| np.arange(0,100).reshape((10,10)) | 创建一个10*10 的矩阵        |

```python
# 首先导入numpy包，重命名一下
import numpy as np

# 首先创建一个Python 列表
list_c = [1,2,3,4]

# 检查类型
type(list_c)

# 在使用np.array()将Python列表转换为numpy的数组
my_array = np.array(list_c)

# 比如我们使用np.arange()可以快速创建连续数字的数组
# 比如我创建一个0~9 的一维数组
np.arange(0,10)

# jupyterlab中使用shift+tab可以查看函数的帮助文档（查看一下，此刻输入np.arange()，弹出对应函数帮助文档）
# 可以看到这个arange()函数有start、stop和step参数，分别代表了起始值，终止值，以及步长
# 如果我希望创建0~10中连续偶数的数组，只需将步长设为2（此刻输入np.arange(0,10,2)）
np.arange(0,10,2)

# 还可以用np.ones创建全是1的数组，（此时输入np.ones()，弹出帮助说明）
# 比如我要创建一个大小为3*3的全1数组
np.ones(shape=(3,3))

# 或者使用np.zeros()全0数组
# 比如创建大小为5*5的全0数组
np.zeros(shape=(5,5))

# 首先使用np.randint函数一些随机整数
arr = np.random.randint(0,100,10)

# 使用max获取最大值
arr.max()
# 再使用argmax() 获取最大值的索引
arr.argmax()
# 使用min函数获取最小值
arr.min()
# 使用argmin获取最小值索引
arr.argmin()
# 使用mean()方法获取取平均值
arr.mean()

# 如果要获取humpy数组的大小，使用numpy.shape，
arr.shape
# 也可以使用reshape函数转换数组的形状，比如我将arr转换成5*2的数组
arr.reshape((5,2))

# 首先创建一个10*10 的矩阵
matrix = np.arange(0,100).reshape((10,10))
# 查看一下大小
matrix.shape
# 使用中括号中加索引方式，获取矩阵对应元素，比如我获取第3行第5列元素
matrix[2,4]
# 再获取矩阵第9行第7列元素
matrix[8,6]
# 如果要获取某一行所有元素，我们需要使用numpy的切片：
# 比如我要获取第3行所有元素，只需将第二个位置变成冒号:
matrix[2,:]
# 类似的，比如我要获取第6列所有元素，只需将第一个位置变成冒号:
matrix[:,5]
# 查看shape
matrix[:,5].shape
# 用reshape恢复成原来的样子
matrix[:,5].reshape((10,1))
# 比如我要获取第1~3行，第2~4列矩阵，我们可以用数字配合冒号的方式来获取
matrix[0:3,1:4]
# 当然我们可以使用等号赋值语句，比如我将这些位置赋值0
matrix[0:3,1:4] = 0
```

## PIL和matplotlib对图像的基本操作
| 命令                                        | 备注                     |
| ------------------------------------------- | ------------------------ |
| Image.open('./img/cat.jpg')                 | 读取图片                 |
| np.asarray(img)                             | 转化为numpy数组          |
| plt.imshow(img_arr)                         | 显示Numpy数组形式的图片  |
| img_arr.copy()                              | 复制一份原图             |
| plt.imshow(img_arr_copy[:,:,0],cmap='gray') | 将cmap颜色设置为gray灰度 |
| img_arr_copy[:,:,0].shape                   | 单独看一个通道           |

```python
# 首先导入numpy
import numpy as np
# 为了在notebook中显示图片，导入matplotlib库
import matplotlib.pyplot as plt

# 加这行在Notebook显示图像
%matplotlib inline

# 再使用一个PIL库，用于读取图像
from PIL import Image

# 我在img文件夹下放了一张图片（演示一下）
# 我们用PIL库读取图片，注意路径要正确
img = Image.open('./img/cat.jpg')

# 查看一下变量的类型
type(img)

# 首先我们需要将它转化为numpy 数组，使用numpy.asarray()函数
img_arr = np.asarray(img)

# 再使用matplot的imshow()方法显示Numpy数组形式的图片
plt.imshow(img_arr)

# 我们继续对这个图片操作，先使用numpy的copy方法复制一份原图
img_arr_copy = img_arr.copy()

# 首先使用numpy切片，将R,G,B三个颜色通道中的R红色通道显示出来
# 大家会发现这个颜色很奇怪，都是翠绿色，为什么会显示成这样呢？
# 我们打开matplot的官网关于颜色表colormap的说明：
# https://matplotlib.org/stable/gallery/color/colormap_reference.html
# 可以看到默认的颜色：是翠绿色（viridis ）。那这个颜色方便色盲观看的
plt.imshow(img_arr_copy[:,:,0])

# 我们也可以将cmap颜色设置成火山岩浆样式：magma
plt.imshow(img_arr_copy[:,:,0],cmap='magma')

# 好，我们知道，计算机是分不清到底哪一个通道是红色的，每一个颜色通道其实都是一个灰度图，我们首先将cmap颜色设置为gray灰度看一下
plt.imshow(img_arr_copy[:,:,0],cmap='gray')

# 可以查看大小shape，会发现大小仍然不变
img_arr_copy.shape

# 而单独看一个通道的时候，大小会变化
img_arr_copy[:,:,0].shape
```

## OpenCV对图像和视频的基本操作
| 命令                                                                                                                                | 备注                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| cv2.imread('./img/cat.jpg')                                                                                                         | 使用opencv的imread方法，打开图片                                             |
| cv2.cvtColor(img,cv2.COLOR_BGR2RGB)                                                                                                 | 将OpenCV BGR转换成RGB                                                        |
| cv2.imread('./img/cat.jpg',cv2.IMREAD_GRAYSCALE)                                                                                    | 再读取图片时也可以以灰度模式读取                                             |
| cv2.resize(img_fixed,(1000,300))                                                                                                    | 使用resize缩放                                                               |
| cv2.flip(img_fixed,-1)                                                                                                              | 翻转图片：0表示垂直翻转、1表示水平翻转，-1表示水平垂直都翻转                 |
| cv2.imwrite('./img_flip.jpg',img_save)                                                                                              | 写入numpy格式的图片                                                          |
| cv2.waitKey(1) & 0xFF == 27                                                                                                         | 等待至少1ms ，而且按了ESC 键，也可以用 ord('q')                              |
| cv2.imshow('display image',img)                                                                                                     | 显示图片窗口                                                                 |
| np.zeros(shape=(800,800,3),dtype=np.int16)                                                                                          | 创建一个纯黑色图，纯黑色就是图片的元素全部为0，这里给一个数据类型为Int16     |
| cv2.rectangle(img=black_img,pt1=(100,100),pt2=(400,300),color=(0,255,0),thickness=10)                                               | 画一个矩形                                                                   |
| cv2.rectangle(img=black_img,pt1=(20,550),pt2=(220,750),color=(255,0,0),thickness=10)                                                | 画一个正方形                                                                 |
| cv2.circle(img=black_img,center=(400,400),radius=100,color=(0,0,255),thickness=10)                                                  | 画一个圆                                                                     |
| cv2.circle(img=black_img,center=(500,600),radius=50,color=(0,0,255),thickness=-1)                                                   | 一个实心圆                                                                   |
| cv2.line(img=black_img,pt1=(0,0),pt2=(800,800),color=(255,0,255),thickness=10)                                                      | 画一条线                                                                     |
| cv2.putText(img=black_img,text="Python",org=(500,150),fontFace=font,fontScale=4,color=(255,0,255),thickness=5,lineType=cv2.LINE_AA) | 添加英文文字                                                                 |
| cv2.polylines(img=black_img,pts=[pts],isClosed=True,color=(255,0,255),thickness=10)                                                 | 画一个多边形                                                                 |
| cv2.VideoCapture(0)                                                                                                                 | 读取默认摄像头，后面的数字表示摄像头的编号，如果有多个摄像头可以换成其他数字 |
| cv2.destroyAllWindows()                                                                                                             | 释放窗口资源                                                                 |
| cv2.VideoWriter('./myDemoVideo.mp4',cv2.VideoWriter_fourcc(*'X264'),fps,(width,height))                                             | 存储摄像头视频流                                                             |
| cv2.VideoCapture('./myDemoVideo.mp4')                                                                                               | 参数可以换成文件名，我们读取前面保存的MP4视频                                |

### OpenCV读取、缩放、翻转、写入图像
```python
# 导入必要的包
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# 导入opencv
import cv2

# 使用opencv的imread方法，打开图片
img = cv2.imread('./img/cat.jpg')

# 检查类型，会发现自动转成了Numpy 数组的形式
type(img)

# 如果打开一张不存在的图片，不会报错，但是会返回空类型
img_wrong = cv2.imread('./img/wrong.jpg')

# 为什么会显示的这么奇怪？（OpenCV和matplotlib 默认的RBG顺序不一样）
plt.imshow(img)

# matplotlib: R G B
# opencv: B G R
# 需要调整顺序

# 将OpenCV BGR 转换成RGB，cv2.COLOR_可以看到更多转换形式
img_fixed = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# 显示正常了
plt.imshow(img_fixed)

# 另外，我们再读取图片时也可以以灰度模式读取
img_gray = cv2.imread('./img/cat.jpg',cv2.IMREAD_GRAYSCALE)

# 只剩2个维度，没有了颜色通道
img_gray.shape

# 显示这个灰度图
plt.imshow(img_gray,cmap="gray")

# 使用resize缩放（打开函数帮助）
img_resize = cv2.resize(img_fixed,(1000,300))

# 显示缩放后的图片
plt.imshow(img_resize)

# 翻转图片：0表示垂直翻转、1表示水平翻转，-1表示水平垂直都翻转
img_flip = cv2.flip(img_fixed,-1)
plt.imshow(img_flip)

# 先将颜色通道顺序调回OpenCV的形式
img_save = cv2.cvtColor(img_flip,cv2.COLOR_RGB2BGR)

# 写入numpy格式的图片
cv2.imwrite('./img_flip.jpg', img_save)
```

### OpenCV绘制文字和几何图形
```python
# OpenCV 绘制文字和几何图形
# 导入必要的包
import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# 创建一个纯黑色图，纯黑色就是图片的元素全部为0，这里给一个数据类型为Int16
black_img = np.zeros(shape=(800,800,3),dtype=np.int16)

# 显示一下
plt.imshow(black_img)

# 首先使用OpenCV画一个矩形
# 使用cv2.rectangle函数来创建，首先看一下这个函数的帮助文档 
# 可以看到分别是：thickness（线粗）
# 那我们在刚才的黑色图片上创建一个矩形
cv2.rectangle(img=black_img,pt1=(100,100),pt2=(400,300),color=(0,255,0),thickness=10)

# 再画一个正方形在左下角
cv2.rectangle(img=black_img,pt1=(20,550),pt2=(220,750),color=(255,0,0),thickness=10)

# 在使用opencv.circle方法画一个圆
# 看一下帮助文档分别是圆心、半径
cv2.circle(img=black_img,center=(400,400),radius=100,color=(0,0,255),thickness=10)

# 换一个实心圆
cv2.circle(img=black_img,center=(500,600),radius=50,color=(0,0,255),thickness=-1)

# 再使用opencv的line函数画一条线，用法和矩形一样
# 我们沿着画面对角线画一条紫色线条
cv2.line(img=black_img,pt1=(0,0),pt2=(800,800),color=(255,0,255),thickness=10)

# 我们再使用OpenCV添加文字
# 首先是英文
# 定义字体
font = cv2.FONT_HERSHEY_PLAIN
# 然后使用puttext方法
cv2.putText(img=black_img,text="Python",org=(500,150),fontFace=font,fontScale=4,color=(255,0,255),thickness=5,lineType=cv2.LINE_AA)

# 我们再用画一个多边形
# 重新创建一个黑色图
black_img = np.zeros(shape=(800,800,3))
plt.imshow(black_img)

# 定义多边形顶点，这些顶点得以二维数据形式存储
points = np.array( [[400,100],[200,300],[400,700],[600,300] ] ,dtype=np.int32)
# 然后呢，opencv比较麻烦，还需转换成三维数组格式
pts = points.reshape((-1,1,2))
# 然后使用OpenCV的polyline方法创建，注意这里还需要用列表形式把点传过去
cv2.polylines(img=black_img,pts=[pts],isClosed=True,color=(255,0,255),thickness=10)

# 再说一下添加中文字体，这个比较麻烦，这里我已经写好了一个函数大家可以直接调用
# 要注意两点：
# 1、对应的字体要安装好或者放在目录下
# 2、不像cv2.puttext可以直接生效，因为这里用了各种转换，所以需要用一个变量来保存结果

# 导入PIL对应包
from PIL import Image, ImageDraw, ImageFont
# 定义一个函数
def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    print(type(img))
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "./font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

img_cat = cv2AddChineseText(img_cat, '阿宇', (400,800), textColor=(0, 255, 0), textSize=200)
img_cat_fixed = cv2.cvtColor(img_cat,cv2.COLOR_BGR2RGB)
plt.imshow(img_cat_fixed)
```

## OpenCV读取摄像头视频流，并显示
```python
"""
OpenCV读取摄像头视频流，并显示
类似demo1.py中的显示图片
"""

# 导入OpenCV
import cv2

# 使用VideoCapture，读取默认摄像头，后面的数字表示摄像头的编号，如果有多个摄像头可以换成其他数字
cap = cv2.VideoCapture(0)

# 再使用cap.read()读取视频流，类似照片，他会以一帧帧的图片返回，所以我们需要用一个循环语句来一直获取
while True:
    # 返回的是元组
    ret,frame = cap.read()

    # 这里可以把frame 就当成图片来处理
    # 镜像
    frame = cv2.flip(frame,1)
    # 颜色变为灰度
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # 显示图像
    cv2.imshow('demo',gray)

    # 退出条件: ESC
    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
```

## OpenCV读取摄像头视频流，并存储为MP4文件
```python
"""
OpenCV读取摄像头视频流，并存储为MP4文件
"""

# 导入OpenCV
import cv2

# 读取默认摄像头
cap = cv2.VideoCapture(0)

 
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# 

fps = 20
width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int( cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

# 这里使用OpenCV的VideoWriter方法来，我们看一下官网他是如何使用的
# 可以看到第一个参数是文件名，然后是fourcc编码，然后是FPS帧率，再是画面大小
# 这里需要注意的是Fourcc编码，我们再看一下文档，可以看到
# Windows系统建议用DIVX编码
# macOS系统建议永MJPG、DIVX、X264
# 推荐用 X264、DIVX，一般macOS和Windows都试用
# 写法需要注意*'X264'
#

# FPS 帧率一般根据摄像头的帧率来填写，比如我的是20
# 高度、宽度可以自定义，不过我们也可以直接和原画面一样，使用cap.get方法获取

writer = cv2.VideoWriter('./myDemoVideo.mp4',cv2.VideoWriter_fourcc(*'X264'),fps,(width,height))

while True:
    # 读取视频
    ret,frame = cap.read()
    
    
    # 这里可以把frame 就当成图片来处理
    # 镜像
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # 写入画面
    writer.write(frame)

    # 显示图像
    cv2.imshow('demo',gray)

    # 退出条件: ESC
    if cv2.waitKey(10) & 0xFF == 27:
        break
    
# 释放句柄    
writer.release()
cap.release()
cv2.destroyAllWindows()
```

## OpenCV读取mp4视频文件
```python
"""
OpenCV读取mp4视频文件
"""

# 导入OpenCV
import cv2
import time

# 还是使用cv2.VideoCapture，只不过参数可以换成文件名，我们读取前面保存的MP4视频
cap = cv2.VideoCapture('./myDemoVideo.mp4')

# 首先加一个判断，如果文件不存在或编码错误提示
if not cap.isOpened():
    print('文件不存在或编码错误')

while cap.isOpened():
    # 读取帧
    
    ret,frame = cap.read()

    if ret:
        # 显示
        cv2.imshow('demo',frame)

        # 降低显示速度（不加这行会显示得特别快）
        time.sleep(1/20)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
```

## OpenCV读取摄像头视频视频流，并在画面上绘制文字和图形
;;;id1 main.py
```python
"""
OpenCV 读取摄像头视频视频流，并在画面上绘制文字和图形
"""

# 导入OpenCV
import cv2
import time

import drawUtils

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


left_x = width // 2
left_y = height // 2

rect_w = width // 4
rect_h = height // 4

start_time = time.time()

while True:
    
    # 读取每一帧
    ret,frame = cap.read()

    # 绘制矩形
    cv2.rectangle(frame,(left_x,left_y),(left_x+rect_w,left_y+rect_h),(0,255,0),10)
    
    # 计算FPS
    now = time.time()
    fps_text  = int(1 / ( now - start_time))
    start_time = now

    # 添加中文（首先导入模块）
    frame = drawUtils.cv2AddChineseText(frame, '帧率：'+str(fps_text), (20,50), textColor=(0, 255, 0), textSize=30)

    # 显示画面
    cv2.imshow('demo',frame)

    # 退出条件
    if cv2.waitKey(10) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
```
;;;

;;;id1 drawUtils.py
```python
"""
绘制工具
"""

# 导入PIL对应包
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 绘制中文
def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "./font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
```
;;;
