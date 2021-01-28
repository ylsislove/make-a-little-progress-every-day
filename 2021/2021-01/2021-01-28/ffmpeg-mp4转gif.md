# ffmpeg-mp4转gif

```powershell
ffmpeg -i test.mp4 -ss 8 -t 15 -s 600*400 -r 15 test.gif
```

参数解释（`*`为必需项）：
- `*`i：输入视频文件
- ss：从第几秒开始截取
- -t：往后截取多少秒
- -s：输出视频文件分辨率
- -r：设置帧率
