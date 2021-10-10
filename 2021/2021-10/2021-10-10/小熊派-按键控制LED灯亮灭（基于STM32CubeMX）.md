# 小熊派-按键控制LED灯亮灭（基于STM32CubeMX）

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

外设引脚对应表
| MCU 引脚 | 引脚标注名 |
| :----: | :----: |
| PC13 | LED |
| PB2 | KEY1 |
| PB3 | KEY2 |

按键原理图

![按键原理图](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010151825.png)

![按键原理图](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010151956.png)

配置时钟树。STM32L4 的最高主频可达到 80M，使 `HCLK = 80Mhz`，如下图

![配置时钟树](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010152206.png)

![配置时钟树](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010152443.png)

配置 LED GPIO 引脚，并修改用户标签名（相当于取另一个新名字），如下图
![配置PC13引脚](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010004322.png)

![修改用户标签名](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010152918.png)

配置 PB2 和 PB3 设置成上拉输入，如下图

![配置 PB2 和 PB3 设置成上拉输入](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010153257.png)

![配置 PB2 和 PB3 设置成上拉输入](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010153430.png)

最后配置生成工程设置，如下图

![生成工程设置](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010153559.png)

![代码生成设置](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/b

最后选择右上角的 `GENERATE CODE`，即可完成工程的创建

## 在 Keil5-MDK 中编写代码
进入 `MDK-ARM` 目录，打开工程，在 `main.c` 中编写如下代码

```c
	while (1)
	{
		/* USER CODE END WHILE */
			
		if (HAL_GPIO_ReadPin(KEY1_GPIO_Port, KEY1_Pin) == 0) {
			HAL_Delay(20);
			while (HAL_GPIO_ReadPin(KEY1_GPIO_Port, KEY1_Pin) == 0);
			HAL_Delay(20);
			
			// filp LED status
			HAL_GPIO_TogglePin(LED_GPIO_Port, LED_Pin);
			
			// the above code is equivalent to the following
//			if (HAL_GPIO_ReadPin(LED_GPIO_Port, LED_Pin) == 0) {
//				HAL_GPIO_WritePin(LED_GPIO_Port, LED_Pin, 1);
//			}
//			else {
//				HAL_GPIO_WritePin(LED_GPIO_Port, LED_Pin, 0);
//			}
		}
```

点击编译和烧录，烧录配置参考：[小熊派开发笔记-点亮LED灯（基于STM32CubeMX）](https://blog.csdn.net/Apple_Coco/article/details/120681966)

烧录成功如下图

![烧录成功](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010155405.png)

## 实验结果
![实验结果](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010155936.gif)
