# HoloLens2开发笔记-解决VS2019无法与HoloLens2配对，部署失败的问题

## 前言
有一段时间没开发 HoloLens2 了，最近新配了一台台式机，打算用台式机继续学习 HoloLens2 开发，但问题就出来了，用台式机构建的 HoloLens2 项目始终无法部署在我的 HoloLens2 设备上，报错如下：

`HoloLens COMException - Command failed: 0x80070490 [0x80004005]`

![报错信息](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210909215801.png)

因为台式机是第一次部署 HoloLens2，所以需要通过 Pin 码与 HoloLens2 进行配对，我尝试了好多好多次，能确保我每次输入的 Pin 码都是正确的，但就是无法通过 HoloLens2 的认证，忙活了一天一夜，尝试了重装我的 VS2019，更新我的 HoloLens2 系统，问题依然存在，呜呜。最后，在我快绝望的时候，尝试了最后一个终极办法，重置我的 HoloLens2 系统，乌拉，它它它终于成功了，终于能把应用部署到 HoloLens2 上了，于是在此记录下来，希望能对同样遇到这个坑的小伙伴们有些帮助~

## 解决办法
在 HoloLens2 系统设置中重置系统，解决！

最后放一张部署成功的截图叭

![部署成功](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210909220725.png)