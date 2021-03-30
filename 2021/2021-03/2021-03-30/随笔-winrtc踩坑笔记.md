# 随笔-winrtc踩坑笔记

## 前言
事情的起因是 [MixedReality-WebRTC](https://github.com/microsoft/MixedReality-WebRTC/tree/master) 项目目前（2021-03-30）还不支持 ARM64 构建，导致我不能在 Hololens2 上一边使用研究模式 API，一边使用 webrtc 进行实时视频流传输，呜呜。在看了很多 Issue 后，发现了 [winrtc](https://github.com/microsoft/winrtc) 项目，这个项目旨在代替已过时的 [webrtc-uwp-sdk](https://github.com/webrtc-uwp/webrtc-uwp-sdk) 项目，且提供了 ARM64 构建的支持。国内目前关于 winrtc 的开发资料貌似挺少的，所以想在后面记录下自己的踩坑经历，共勉！

## 前置博文
* [Hololens2-MixedReality-WebRTC的使用问题](./../2021-03-10/Hololens2-MixedReality-WebRTC的使用问题.md)
