# 小熊派-串口读取RS485输出的土壤七合一传感器数据（基于STM32CubeMX）

  - [环境](#%E7%8E%AF%E5%A2%83)
  - [硬件](#%E7%A1%AC%E4%BB%B6)
  - [接线图](#%E6%8E%A5%E7%BA%BF%E5%9B%BE)
  - [创建工程](#%E5%88%9B%E5%BB%BA%E5%B7%A5%E7%A8%8B)
  - [在 Keil5-MDK 中编写代码](#%E5%9C%A8-keil5-mdk-%E4%B8%AD%E7%BC%96%E5%86%99%E4%BB%A3%E7%A0%81)
  - [编译、烧录程序](#%E7%BC%96%E8%AF%91%E7%83%A7%E5%BD%95%E7%A8%8B%E5%BA%8F)

## 环境
* JRE（Java Runtime Environment）
* STM32CubeMX v6.3.0
* HAL 库 L4 v1.7.0
* Keil5-MDK

环境搭建参考：[STM32CubeMX学习记录--安装配置与使用](https://blog.csdn.net/weixin_43599390/article/details/106863929)

如果不想去官网下，也可以从我的百度云分享里下载 STM32CubeMX 和 HAL 库

链接：https://pan.baidu.com/s/10MKGKPNQrIxZnuMZvVKqkg 
提取码：zjor 

## 硬件
* 小熊派开发板

![小熊派开发板](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211014224832.png)

* 土壤七合一传感器（水分、温度、电导率、氮磷钾、PH值）

![土壤七合一传感器（水分、温度、电导率、氮磷钾、PH值）](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211014225338.png)

* RS485 转 TTL 模块

![RS485 转 TTL 模块](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211014225640.png)

## 接线图
* 小熊派的 `5v` 电源接土壤传感器的 `电源正`
* 小熊派的 `GND` 接土壤传感器的 `电源地`
* 小熊派的 `3.3v` 电源接转接模块的 `VCC`
* 小熊派的 `GND` 接转接模块的 `GND`
* 小熊派的 `UART2_TX` 接转接模块的 `TXD`
* 小熊派的 `UART2_RX` 接转接模块的 `RXD`
* 转接模块的 `A+` 接土壤传感器的 `485-A`
* 转接模块的 `B-` 接土壤传感器的 `485-B`

![](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211014225819.png)

## 创建工程
打开 STM32CubeMX，选择新建一个工程，如下图

![新建工程](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010002342.png)

在输入框中输入 `stm32l431rc`，选中，然后双击选择中间 `LQFP64` 的这款，如下图

![选择芯片](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010002605.png)

查看原理图，`KEY1` 按键对应的引脚为 `PB2`，如下图

![按键原理图](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010151956.png)

在 STM32CubeMX 中选择 `PB2` 引脚输出模式为 `GPIO_input`

![设置PB2引脚](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211014232637.png)

设置 `PB2` 输出方式和别名，如下图

![设置PB2引脚](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211014232843.png)

设置 `UART1` 为异步输出，该串口是用来和 PC 端进行通信，波特率就用默认的 115200，如下图

![设置UART1引脚](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211014233020.png)

设置 `UART2` 为异步输出，该串口用来和土壤传感器进行通信，我们上面的硬件接线也是使用的是 `UART2` 串口。土壤传感器的波特率为 9600，所以工程里该串口波特率设置为 9600，如下图

![设置UART2引脚](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211014233628.png)

时钟使用内部默认时钟，设置为最高 80MHz

![设置时钟](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211014233902.png)

![设置时钟](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211014233930.png)

最后配置生成工程设置，如下图

![生成工程设置](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211014234411.png)

![代码生成设置](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211010154022.png)

最后选择右上角的 `GENERATE CODE`，即可完成工程的创建

## 在 Keil5-MDK 中编写代码
进入 `MDK-ARM` 目录，打开工程，在 `usart.c` 中编写如下代码

```c
/* USER CODE BEGIN 1 */
int fputc(int ch, FILE *file)
{
	uint8_t temp[1] = {ch};
	HAL_UART_Transmit(&huart1, temp, 1, 0xff);
	return HAL_OK;
}
/* USER CODE END 1 */
```

并在该文件头部添加头文件

```c
/* USER CODE BEGIN 0 */
#include "stdio.h"
/* USER CODE END 0 */
```

重写 `fputc` 可以将 `printf` 函数的输出重定向到 `uart1` 串口上，就可以通过串口助手显示出来

在 `main.c` 中，首先添加头文件

```c
/* USER CODE BEGIN Includes */
#include "stdio.h"
/* USER CODE END Includes */
```

然后在 main 函数的 while 循环中编写如下代码

```c
/* USER CODE BEGIN 3 */
// 如果检测到 KEY1 按下
if (HAL_GPIO_ReadPin(KEY1_GPIO_Port, KEY1_Pin) == GPIO_PIN_RESET)
{
    // 按键去抖
    HAL_Delay(20);
    while (HAL_GPIO_ReadPin(KEY1_GPIO_Port, KEY1_Pin) == GPIO_PIN_RESET);
    HAL_Delay(20);
    
    // 发送问询帧
    uint8_t askData[] = {0x01, 0x03, 0x00, 0x00, 0x00, 0x04, 0x44, 0x09};
    HAL_UART_Transmit(&huart2, askData, 8, 0xff);
    
    // 接收应答帧
    uint8_t result[13];
    HAL_UART_Receive(&huart2, result, 13, 0xff);
    for (int i = 0; i < 13; i++)
    {
        printf(" %x ", result[i]);
    }
}
```

这里的 `HAL_UART_Transmit` 和 `HAL_UART_Receive` 都是用的 `uart2` 串口，向我们的土壤传感器发送和接收数据。

查阅土壤传感器的用户手册，想要获取数据，要先发送一个问询帧，如下

![土壤传感器的用户手册](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211015143909.png)

因此，我们根据用户手册里的示例，向 `uart2` 串口发送一个如代码所示的问询帧，然后接收返回来的应答帧，最后输出到串口助手上就好啦

## 编译、烧录程序
![勾选 MicroLIB 库](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211015144300.png)

勾选 `MicroLIB` 库很重要，不然会无法向串口助手输出数据

![勾选 reset and run](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211015144515.png)

![勾选 reset and run](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211015144540.png)

勾选 `reset and run` 可以让程序烧录完成后自动运行。

设置完成后点击确定，OK

点击编译，然后烧录，下图所示表示烧录成功

![编译烧录](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211015152547.png)

打开串口助手，这里我用的是 QCOM。打开端口，然后按下小熊派的 `KEY1` 按键，可以看到串口助手打印出了应答帧的信息，如下图

![串口助手](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211015153218.png)

根据土壤传感器的用户手册，可以解析出温度数据为：`0x01 0x03（十六进制） = 259（十进制）`，所以当前温度为 25.9 ℃
