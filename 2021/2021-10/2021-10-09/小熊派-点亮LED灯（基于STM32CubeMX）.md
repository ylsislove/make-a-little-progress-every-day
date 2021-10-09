# 小熊派-点亮LED灯（基于STM32CubeMX）

## 环境
* JRE（Java Runtime Environment）
* STM32CubeMX v6.3.0
* HAL 库 L4 v1.7.0
* Keil5-MDK

环境搭建参考：[STM32CubeMX学习记录--安装配置与使用](https://blog.csdn.net/weixin_43599390/article/details/106863929)

如果不想去官网下，也可以从我的百度云分享里下载 STM32CubeMX 和 HAL 库

链接：https://pan.baidu.com/s/10MKGKPNQrIxZnuMZvVKqkg 
提取码：zjor 

## 创建工程
打开 STM32CubeMX，选择新建一个工程，如下图

![新建工程](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010002342.png)

在输入框中输入 `stm32l431rc`，选中，然后双击选择中间 `LQFP64` 的这款，如下图

![选择芯片](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010002605.png)

配置时钟源，这里选择外部高速时钟，如下图

![配置时钟源](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010002948.png)

配置 GPIO 引脚，在原理图上查看 LED 灯的连接情况如下

![LED](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010004051.png)

所以在 STM32CubeMX 中选择配置 PC13 引脚，如下图

![配置PC13引脚](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010004322.png)

配置时钟树，选择 HSE，如下图

![配置时钟树](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010004502.png)

配置工程，如下图

![配置工程](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010004701.png)

最后选择右上角的 `GENERATE CODE`，即可完成工程的创建

## 在 Keil5-MDK 中编写代码
STM32CubeMX 生成的代码目录如下

![代码目录](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010004901.png)

进入 `MDK-ARM` 目录，打开工程，如下图

![打开工程](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010005050.png)

在 main.c 中编写如下代码

```c
  while (1)
  {
    /* USER CODE END WHILE */
	  
	HAL_Delay(500);
	HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);

    /* USER CODE BEGIN 3 */
  }
```

然后编译整个工程

![编译整个工程](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010005401.png)

最后进行下载设置。点击菜单栏的 `Options for Target`，如下图

![Options for Target](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010005542.png)

选择 Debug，进行 ST-Link 配置，如下图

![进行 ST-Link 配置](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010005617.png)

选择 `reset and fun`，如下图

![reset and fun](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010005732.png)

点击确定，OK

最后点击下载，如下图

![下载](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010005952.png)

## 实验结果
![实验结果](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010010631.gif)
