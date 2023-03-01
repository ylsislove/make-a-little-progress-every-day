---
title: WSL2通过OpenCV调用并展示本机摄像头的RTSP视频流
date: 2023-02-27 21:22:51
categories:
 - [人工智能, 基础知识]
tags: 
 - win11
 - wsl
 - nvidia
---

## 前言
![](https://image.aayu.today/uploads/2023/03/01/202303012127332.png)

本篇博客的由来如上图哈哈，WSL2 相关安装教程可以参考我之前的博客：[Win11安装WSL2和Nvidia驱动](https://blog.aayu.today/artificial-intelligence/basic/20221217/)

## 安装 CMake
ubuntu上请执行

```bash
sudo apt install cmake -y
```

或者编译安装

```bash
# 以v3.25.1版本为例
git clone -b v3.25.1 https://github.com/Kitware/CMake.git 
cd CMake
# 你使用`--prefix`来指定安装路径，或者去掉`--prefix`,安装在默认路径。
./bootstrap --prefix=<安装路径> && make && sudo make install

# 验证
cmake --version
```

如果报错`Could NOT find OpenSSL`，安装如下依赖即可解决

```bash
sudo apt update
sudo apt upgrade
sudo apt install libssl-dev
```

## 安装 OpenCV 和 FFmpeg
```bash
sudo apt install libopencv-dev
sudo apt install ffmpeg
```

## 启动 Windows 本机的 RTSP 视频流
### 查看本机摄像头设备
Windows 本机安装 ffmpeg 这里不再赘述啦，网上教程很多~

查看本机摄像头设备命令如下

```bash
ffmpeg -list_devices true -f dshow -i dummy
```

![](https://image.aayu.today/uploads/2023/03/01/202303012138041.png){width="800px"}

### 开始推流
```bash
ffmpeg -f dshow -i video="USB2.0 Camera" -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -rtsp_transport tcp -f rtsp rtsp://172.27.148.34/test
```

参数解释
* `-f dshow -i video="摄像头名称"` 指定从本地摄像头中读取视频流。将“摄像头名称”替换为您的摄像头名称，例如“USB2.0 Camera”。
* `-vcodec libx264` 指定使用 x264 编码器进行视频编码。
* `-preset ultrafast` 设置编码速度。这里使用的是最快的编码速度，但可能会导致视频质量下降。
* `-tune zerolatency` 设置编码器以实现零延迟。
* `-f rtsp` 指定输出流的格式为 RTSP。
* `rtsp://<IP地址>/<路径>` 指定 RTSP 流的目标地址。请将 `<IP地址>` 替换为 Windows 本机 IP 地址，将 `<路径>` 替换为您想要为流指定的路径。

成功推流如下，注意保持控制台的运行

![](https://image.aayu.today/uploads/2023/03/01/202303012139056.png){width="800px"}

## 开放本机防火墙
因为我们要在 WSL2 里访问本机的 RTSP 视频流，所以需要打开本机的防火墙，如下图

![](https://image.aayu.today/uploads/2023/03/01/202303012140033.png){width="800px"}

关闭专用网络和公用网络即可

## 用 OpenCV 接收视频流
代码如下

```cpp
#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>

int main(int argc, char **argv)
{
    // Ubuntu安装ffmpeg：sudo apt-get install ffmpeg
    // rtsp地址，模拟四路视频流进行展示
    std::string rtsp1 = "rtsp://172.27.148.34/test";
    std::string rtsp2 = rtsp1;
    std::string rtsp3 = rtsp1;
    std::string rtsp4 = rtsp1;

    // CAP_FFMPEG：使用ffmpeg解码
    cv::VideoCapture stream1 = cv::VideoCapture(rtsp1, cv::CAP_FFMPEG);
    cv::VideoCapture stream2 = cv::VideoCapture(rtsp2, cv::CAP_FFMPEG);
    cv::VideoCapture stream3 = cv::VideoCapture(rtsp3, cv::CAP_FFMPEG);
    cv::VideoCapture stream4 = cv::VideoCapture(rtsp4, cv::CAP_FFMPEG);

    if (!stream1.isOpened() || !stream2.isOpened() || !stream3.isOpened() || !stream4.isOpened())
    {
        std::cout << "有视频流未打开" << std::endl;
        return -1;
    }

    cv::Mat frame1;
    cv::Mat frame2;
    cv::Mat frame3;
    cv::Mat frame4;

    cv::Mat H1, H2, V, blur;

    // 使用namedWindow创建窗口，WINDOW_AUTOSIZE：自动调整窗口大小
    cv::namedWindow("rtsp_demo", cv::WINDOW_AUTOSIZE);

    while (true)
    {
        if (!stream1.read(frame1) || !stream2.read(frame2) || !stream3.read(frame3) || !stream4.read(frame4))
        {
            std::cout << "有视频流未读取" << std::endl;
            continue;
        }
        // 缩放等处理
        cv::resize(frame1, frame1, cv::Size(500, 300));

        cv::resize(frame2, frame2, cv::Size(500, 300));
        cv::flip(frame2, frame2, 1);

        cv::resize(frame3, frame3, cv::Size(500, 300));
        cv::cvtColor(frame1, frame1, cv::COLOR_BGR2GRAY);
        cv::cvtColor(frame1, frame1, cv::COLOR_GRAY2BGR);

        cv::resize(frame4, frame4, cv::Size(500, 300));
        cv::putText(frame4, "RTSP demo", cv::Point(100, 100), cv::FONT_ITALIC, 1, cv::Scalar(0, 0, 255), 2);
        // 拼接
        cv::hconcat(frame1, frame2, H1);
        cv::hconcat(frame3, frame4, H2);
        cv::vconcat(H1, H2, V);

        // 高斯模糊一下
        cv::GaussianBlur(V, blur, cv::Size(25, 25), 0);

        cv::imshow("rtsp_demo", blur);

        if (cv::waitKey(1) == 27)
        {
            break;
        }
    }

    return 0;
}
```

CMakeLists.txt 内容如下

```cmake
# 最低版本要求
cmake_minimum_required(VERSION 3.10)

# 项目信息
project(rtsp_demo)

# 添加opencv库
find_package(OpenCV REQUIRED)

# 添加头文件
include_directories(${OpenCV_INCLUDE_DIRS})
# 添加库文件
link_libraries(${OpenCV_LIBS})

# 添加可执行程序
add_executable(rtsp_demo src/main.cpp)
```

启动 cmake 配置并构建

```bash
cmake -S . -B build 
cmake --build build 
```

运行可执行程序

```bash
./build/rtsp_demo
```

## 结果展示
成功用 WSL2 展示出四路 RTSP 视频流~

![](https://image.aayu.today/uploads/2023/03/01/202303012141053.png){width="800px"}
