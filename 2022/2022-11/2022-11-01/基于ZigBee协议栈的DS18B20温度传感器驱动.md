---
title: 基于ZigBee协议栈的DS18B20温度传感器驱动
date: 2022-11-01 17:04:48
categories:
 - [硬件修炼手册, ZigBee]
tags: 
 - IoT
 - ZigBee
---

## 前言
最近再搞农业物联网的项目，用到了ZigBee协议栈，需求之一是要监测土壤温度的数据，便采购了「 善学坊 」家的「 YTWD-A1 」传感器，其本质是DS18B20芯片，但网上关于这个芯片的数据读取方式多是51单片机或STM32相关的代码，经过自己的一番踩坑和实验，终于在ZigBee协议栈下写好了这个芯片的驱动，便在此记录下来，希望能帮助到有需要的小伙伴~

![](https://image.aayu.today/uploads/2022/11/01/202211011901441.png){width="400px"}

## 相关代码
```c ds18b20.h
#ifndef HAL_DS18B20_H
#define HAL_DS18B20_H

#ifdef __cplusplus
extern "C" {
#endif

/** @brief   YTWD GPIO. */
#define HAL_DS18B20_PORT  1 //!< Port1.
#define HAL_DS18B20_PIN   2 //!< Pin2.
   
/** @brief   DHT11 Data. */
typedef struct  {
    unsigned char ok;   //!< Is ok?
    unsigned char fg;
    unsigned char xs; //!< xiaoshu.
    unsigned char zs; //!< zhengshu.
} halDS18B20Data_t;

/**
 * @fn      halDS18B20Init
 * 
 * @brief	Init. DS18B20.
 */
unsigned char halDS18B20Init(void);   
   
/**
 * @fn      halDHT11GetData
 * 
 * @brief	Get data from DS18B20.
 *
 * @return  xs&zs value if ok is 1.
 */
halDS18B20Data_t  halDS18B20GetData(void);

#ifdef __cplusplus
}
#endif

#endif /* #ifndef HAL_DS18B20_H */
```

```c ds18b20.c
#include "hal_ds18b20.h"
#include "hal_delay.h"
#include "cc2530_ioctl.h"
#include "hal_lcd.h"
#include <stdio.h>

/* Boolean value. */
#define HAL_DS18B20_FALSE         0
#define HAL_DS18B20_TRUE          1

/* Delay Functions. */   
#define HAL_DS18B20_DELAY_US(x)   delayUsIn32Mhz((x))
#define HAL_DS18B20_DELAY_MS(x)   delayMs(SYSCLK_32MHZ ,(x))

/* Set DS18B20 GPIO mode. */
#define HAL_DS18B20_IO_OUTPUT()         CC2530_IOCTL(HAL_DS18B20_PORT, HAL_DS18B20_PIN, CC2530_OUTPUT)
#define HAL_DS18B20_IO_PULLDOWN()       CC2530_IOCTL(HAL_DS18B20_PORT, HAL_DS18B20_PIN, CC2530_INPUT_PULLDOWN)
#define HAL_DS18B20_IO_PULLUP()         CC2530_IOCTL(HAL_DS18B20_PORT, HAL_DS18B20_PIN, CC2530_INPUT_PULLUP)

/* Set DS18B20 GPIO Level. */ 
#define HAL_DS18B20_IO_SET(port, pin, level) do { \
  if(level) CC2530_GPIO_SET(port, pin);         \
  else CC2530_GPIO_CLEAR(port, pin);            \
} while(0)

#define HAL_DS18B20_IO_SET_LO()  HAL_DS18B20_IO_SET(HAL_DS18B20_PORT, HAL_DS18B20_PIN, 0)
#define HAL_DS18B20_IO_SET_HI()  HAL_DS18B20_IO_SET(HAL_DS18B20_PORT, HAL_DS18B20_PIN, 1)

/*  Get DS18B20 GPIO Status. */
#define HAL_DS18B20_IO_GET(port, pin) CC2530_GPIO_GET(port, pin)
#define HAL_DS18B20_IO()              HAL_DS18B20_IO_GET(HAL_DS18B20_PORT, HAL_DS18B20_PIN)

static uint8_t ReadOneChar(void);
static void WriteOneChar(uint8_t dat);

unsigned char halDS18B20Init(void) 
{ 
    unsigned char x = 0;
    HAL_DS18B20_IO_OUTPUT();
    
    //DQ先置高
    HAL_DS18B20_IO_SET_HI();
    HAL_DS18B20_DELAY_US(74);           //稍延时

    //发送复位脉冲 
    HAL_DS18B20_IO_SET_LO();
    HAL_DS18B20_DELAY_US(750);          //延时（>480us)
 
    //拉高数据线
    HAL_DS18B20_IO_SET_HI();
    HAL_DS18B20_DELAY_US(50);           //等待（15~60us)

    HAL_DS18B20_IO_PULLUP();
    
    x = HAL_DS18B20_IO(); // 用X的值来判断初始化有没有成功，18B20存在的话X=0，否则X=1
//    if (x == 0) HalLcdWriteString("finddddd", 3);
//    else HalLcdWriteString("nooooo", 3);
    HAL_DS18B20_DELAY_US(100);
    
    return x;
}


halDS18B20Data_t halDS18B20GetData(void) 
{
    uint8_t tempL, tempH, xiaoshu1, xiaoshu2;
    halDS18B20Data_t ds18b20Dat = { .ok = HAL_DS18B20_FALSE, .fg = 1 };
    
    halDS18B20Init();
    HAL_DS18B20_DELAY_US(15);
    WriteOneChar(0xcc);                 //跳过读序列号的操作 
    WriteOneChar(0x44);                 //启动温度转换 
    HAL_DS18B20_DELAY_US(1000);         //转换需要一点时间，延时 

    halDS18B20Init();                   //初始化
    HAL_DS18B20_DELAY_US(15);
    WriteOneChar(0xcc);                 //跳过读序列号的操作 
    WriteOneChar(0xbe);                 //读温度寄存器（头两个值分别为温度的低位和高位）
 
    tempL = ReadOneChar();              //读出温度的低位LSB 
    tempH = ReadOneChar();              //读出温度的高位MSB

    if(tempH & 0xf8) //最高5位为1时温度是负 
    { 
        tempL = ~tempL; //补码转换，取反加一 
        tempH = ~tempH+1; 
        ds18b20Dat.fg = 0; //读取温度为负时fg=0
    }
    
    // 温度为负时貌似有问题，后面再改
    ds18b20Dat.zs = tempL/16+tempH*16;          //整数部分 
    xiaoshu1 = (tempL&0x0f)*10/16;              //小数第一位 
    xiaoshu2 = (tempL&0x0f)*100/16%10;          //小数第二位 
    ds18b20Dat.xs = xiaoshu1*10+xiaoshu2;       //小数两位

    // 进行数据校验
    if ((!ds18b20Dat.fg && ds18b20Dat.zs <= 55) || (ds18b20Dat.fg && ds18b20Dat.zs <= 125))
    {
        ds18b20Dat.ok = HAL_DS18B20_TRUE;
    }

    halDS18B20Init();
    return ds18b20Dat;
}

// 主机数据线先从高拉至低电平1us以上，再使数据线升为高电平，从而产生读信号 
static uint8_t ReadOneChar(void) 
{
    uint8_t i = 0; //每个读周期最短的持续时间为60us，各个读周期之间必须有1us以上的高电平恢复期 
    uint8_t dat = 0;
    
    for(i = 8; i>0; i--) //一个字节有8位 
    { 
        HAL_DS18B20_IO_OUTPUT();
      
        dat>>=1;
        HAL_DS18B20_IO_SET_LO();
        HAL_DS18B20_DELAY_US(2);
        HAL_DS18B20_IO_SET_HI();
        
        HAL_DS18B20_IO_PULLUP();
        HAL_DS18B20_DELAY_US(12);
        if(HAL_DS18B20_IO())
            dat |= 0x80;
        
        HAL_DS18B20_DELAY_US(50);
    }
    return dat;
}

// 数据线从高电平拉至低电平，产生写起始信号。15us之内将所需写的位送到数据线上
static void WriteOneChar(uint8_t dat) 
{
    HAL_DS18B20_IO_OUTPUT();
    
    uint8_t i = 0; 
    for(i = 8; i > 0; i--) //在15~60us之间对数据线进行采样，如果是高电平就写1，低写0发生。 
    { 
        HAL_DS18B20_IO_SET_LO(); //在开始另一个写周期前必须有1us以上的高电平恢复期
        HAL_DS18B20_DELAY_US(1);
        
        if (dat&0x01) HAL_DS18B20_IO_SET_HI();
        else HAL_DS18B20_IO_SET_LO();
            
        HAL_DS18B20_DELAY_US(68);
        
        HAL_DS18B20_IO_SET_HI();
        dat >>= 1;
    }
    HAL_DS18B20_DELAY_US(40);
} 
```

## 参考链接
* [液体温度传感器 YTWD-A1](https://zhuanlan.zhihu.com/p/483606656)
* [DS18B20数字温度传感器干货](https://zhuanlan.zhihu.com/p/396356659)
* [温度传感器DS18B20原理，附STM32例程代码](https://zhuanlan.zhihu.com/p/386084633)
* [51单片机DS18B20温度传感器详解](https://blog.csdn.net/u013151320/article/details/50253199)
