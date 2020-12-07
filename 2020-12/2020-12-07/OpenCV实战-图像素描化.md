# OpenCV实战-图像素描化

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

欢迎访问博主搭建的 [在线运行平台 (o゜▽゜)o☆](http://systemcall.gitee.io/keep-thinking)

## 运行结果
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201207203252.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201207203252.png)

## JS代码
```js
onOpenCvReady() {
  const cv = window.cv

  // 读取图像
  const src = this.createMat(cv, 'source', { name: 'imageSrcRaw' })

  // 转换为灰度
  const gray = this.createMat(cv, 'empty')
  cv.cvtColor(src, gray, cv.COLOR_RGBA2GRAY)

  // 图像取反
  const inv = this.createMat(cv, 'empty')
  cv.bitwise_not(gray, inv)

  // 高斯模糊 取反
  const blur = this.createMat(cv, 'empty')
  cv.GaussianBlur(inv, blur, new cv.Size(15, 15), 50, 50)
  cv.bitwise_not(blur, blur)

  // 像素算数操作 
  const dst = this.createMat(cv, 'empty')
  cv.divide(gray, blur, dst, 255)

  // 显示图像
  this.imshow('canvasOutput', dst)

  // 销毁所有 mat 释放内存
  this.destoryAllMats()
  this.running = false
},
imshow(element, mat) {
  window.cv.imshow(element, mat)
  const canvas = document.getElementById('canvasOutput')
  this.outputUrl = canvas.toDataURL('image/png')
},
createMat(cv, type, ops) {
  switch (type) {
    case 'source':
      if (ops && ops.name) {
        const mat = cv.imread(ops.name)
        this.mats.push(mat)
        return mat
      }
      break
    case 'empty': {
      const mat = new cv.Mat()
      this.mats.push(mat)
      return mat
    }
    case 'options':
      if (ops && ops.rows && ops.cols && ops.type && ops.initValue) {
        const mat = new cv.Mat(ops.rows, ops.cols, ops.type, ops.initValue)
        this.mats.push(mat)
        return mat
      }
      break
    default:
      break
  }
},
destoryAllMats() {
  let i = 0
  this.mats.forEach(item => {
    item.delete()
    i++
  })
  this.mats = []
  console.log('销毁图象数：', i)
},
```
