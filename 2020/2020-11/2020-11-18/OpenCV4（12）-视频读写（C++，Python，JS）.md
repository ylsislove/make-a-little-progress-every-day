# OpenCV4（12）-视频读写（C++，Python，JS）

## 环境
* Python：3.6.5 OpenCV 4.1.2
* C++：OpenCV 4.1.2
* JS：OpenCV 4.5.0

环境搭建可参考：[B站视频](http://space.bilibili.com/365916694/#/)

## 知识点
VideoCapture 视频文件读取、摄像头读取、视频流读取

获取视频的相关属性

- CAP_PROP_FRAME_HEIGHT 高
- CAP_PROP_FRAME_WIDTH  宽
- CAP_PROP_FRAME_COUNT  总帧数
- CAP_PROP_FPS  帧率

VideoWriter 视频写出、文件保存

## C++代码
```c++
#ifndef DAY12
#define DAY12
 
#include <opencv2/opencv.hpp>
#include <iostream>
 
using namespace std;
using namespace cv;
 
void day12() {
 
	VideoCapture capture;
	// 打开本地的视频文件
	//capture.open("G:\\opencvTest\\video.mp4");
	// 打开摄像头，0是电脑自带的摄像头，序号依次递增为外接摄像头
	capture.open(1);
 
	if (!capture.isOpened()) {
		cout << "could not open this capture.." << endl;
	}
 
	int width = static_cast<int>(capture.get(CAP_PROP_FRAME_WIDTH));
	int height = static_cast<int>(capture.get(CAP_PROP_FRAME_HEIGHT));
	int count = static_cast<int>(capture.get(CAP_PROP_FRAME_COUNT));
	int fps = static_cast<int>(capture.get(CAP_PROP_FPS));
	cout << "分辨率：(" << width << "x" << height << ") " << endl;
	cout << "总帧数：" << count << endl;
	cout << "帧率：" << fps << endl;
 
	int type = static_cast<int>(capture.get(CAP_PROP_FOURCC));
	VideoWriter writer("G:\\opencvTest\\video.mp4", type, fps, Size(width, height), true);
 
	Mat frame;
	while (capture.read(frame)) {
		imshow("capture_video", frame);
		writer.write(frame);
		// 监听键盘事件，按Esc退出
		char c = waitKey(50);
		if (c == 27) {
			break;
		}
	}
 
	// 释放资源
	writer.release();
	capture.release();
}
 
#endif // !DAY12
```
