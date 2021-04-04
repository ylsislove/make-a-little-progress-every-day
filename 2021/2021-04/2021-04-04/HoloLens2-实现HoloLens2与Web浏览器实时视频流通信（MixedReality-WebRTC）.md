# HoloLens2-实现HoloLens2与Web浏览器实时视频流通信（MixedReality-WebRTC）

## 前言
在查阅了很多 Issues 和学习了 WebRTC SDP 相关的诸多知识后，终于实现了这一需求，开心~

## 开发环境
* Windows 10 教育版 18363.1379
* Unity 2019.4.20f1c1
* VS2019 16.9.3
* WIN SDK 10.0.18362.0
* Hololens2 内部预览版本 10.0.20301.1000

## 信令服务器
使用[官方教程](https://microsoft.github.io/MixedReality-WebRTC/manual/unity/helloworld-unity-signaler.html)里的 [node-dss](https://github.com/bengreenier/node-dss)

## Web客户端脚本
可以参考我的 GitHub 仓库：[peerconnection_hololens](https://github.com/ylsislove/webrtc-learning/tree/master/peerconnection_hololens)

其中，信令服务器部署在一台云服务器上，Web客户端部署在另一台云服务器上，云服务器需要有备案域名，可以申请SSL证书从而提供Https服务，不然无法请求 Web 浏览器的摄像头。

## 通信流程
1. Web 客户端连接信令服务器
2. HoloLens 2 客户端连接信令服务器，并发送 Offer
3. Web 客户端收到 Offer，设置 SDP，生成 Answer。通过信令服务器发送给 HoloLens 2 客户端
4. HoloLens 2 客户端收到 Answer，设置 SDP
5. 双方客户端互相发送 ICE 候选者，建立连接

## 遇到的问题
HoloLens 客户端可以看到浏览器的摄像头视频流，但无法在浏览器端看到 HoloLens 2 端的视频流。

## 分析问题
从浏览器控制台查看了 HoloLens 端发送的 Offer 和浏览器端回应的 Answer，发现 Offer 有一些不同，如下：

这是 HoloLens 发送 Offer 的一部分：
```
a=group:BUNDLE 0 1
a=msid-semantic: WMS
m=video 9 UDP/TLS/RTP/SAVPF 96 97 98 99 100 101 127 125 104
a=mid:0
a=sendrecv
a=msid:- f583a0a9-2f80-4d85-b6af-ef7ba83ed13d
a=ssrc-group:FID 2667659048 3959474471
a=ssrc:2667659048 cname:CWYsPV9tCmupNHSl
a=ssrc:2667659048 msid: f583a0a9-2f80-4d85-b6af-ef7ba83ed13d
a=ssrc:2667659048 mslabel:
a=ssrc:2667659048 label:f583a0a9-2f80-4d85-b6af-ef7ba83ed13d
m=audio 9 UDP/TLS/RTP/SAVPF 111 103 9 102 0 8 105 13 110 113 126
a=mid:1
a=sendrecv
a=msid:- a69056ce-f68f-49d0-a376-d2012b6ad755
a=ssrc:1498154044 cname:CWYsPV9tCmupNHSl
a=ssrc:1498154044 msid: a69056ce-f68f-49d0-a376-d2012b6ad755
a=ssrc:1498154044 mslabel:
a=ssrc:1498154044 label:a69056ce-f68f-49d0-a376-d2012b6ad755
```

这是浏览器回应的 Answer 的一部分：
```
a=group:BUNDLE 0 1
a=msid-semantic: WMS egMOeAUXRITlOTOaE3PRZZoftadyBOOhMNxy
m=video 9 UDP/TLS/RTP/SAVPF 96 97 98 99 100 101 127 125 104
a=mid:0
a=sendrecv
a=msid:egMOeAUXRITlOTOaE3PRZZoftadyBOOhMNxy dceec5bc-426f-4869-9727-f4df48c98818
a=ssrc-group:FID 300348358 243777033
a=ssrc:300348358 cname:Sqg5iBI1faqe3I0w
a=ssrc:243777033 cname:Sqg5iBI1faqe3I0w
m=audio 9 UDP/TLS/RTP/SAVPF 111 103 9 0 8 105 13 110 113 126
a=mid:1
a=sendrecv
a=msid:egMOeAUXRITlOTOaE3PRZZoftadyBOOhMNxy c30fc5ed-e915-43d5-b189-4326ef006e91
a=ssrc:144003280 cname:Sqg5iBI1faqe3I0w
```

可以发现，Offer 的 `a=msid-semantic` 属性有一些不对劲，缺少一个流 ID，导致音频轨和视频轨没有绑定到流上，所以浏览器端无法获取到 HoloLens 端的视频流。

看了 MixedReality-WebRTC 的 [Issue](https://github.com/microsoft/MixedReality-WebRTC/issues/695)，问题确实就是出在这，如下：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210404205420.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210404205420.png)

最重要的是仓库成员给出了解决办法：设置 `Transceiver.StreamIDs` 即可

## 解决问题
浏览一下 MixedReality-WebRTC 的 `PeerConnection.cs` 脚本，发现在 `StartConnection` 函数中可以创建 `TransceiverInitSettings` 类。所以只需在创建 `TransceiverInitSettings` 时设置一下 `StreamIDs` 属性（UUID字符串）即可，如下：

```csharp
var settings = new TransceiverInitSettings
{
    Name = $"mrsw#{index}",
    InitialDesiredDirection = wantsDir,
    StreamIDs = new List<string>() { "86181edf-1c7a-4f5d-ba0d-80021fcf7036" }
};
tr = _nativePeer.AddTransceiver(mediaLine.MediaKind, settings);
```

重新运行，在浏览器端控制台检查 Offer，更改成功，Web 端成功接收到 HoloLens 端视频流，bingo！

## 结果展示
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210404214616.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210404214616.png)
