# HoloLens 2 Research Mode as a Tool for Computer Vision Research

HoloLens2 研究模式作为计算机视觉研究的工具

## 摘要
混合现实头盔，如微软 HoloLens2，是具有集成计算能力的强大传感设备，这使它成为计算机视觉研究的理想平台。在本技术报告中，我们介绍了HoloLens2 研究模式，一个 API 和一组工具，使能访问原始传感器流。我们将对 API 进行概述，并解释如何使用它来构建基于处理传感器数据的混合现实应用程序。我们还展示了如何将研究模式传感器数据与 HoloLens2 提供的内置眼和手跟踪功能相结合。通过发布研究模式 API 和一组开源工具，我们的目标是促进计算机视觉和机器人领域的进一步研究，并鼓励研究社区的贡献。

## 1. 介绍
混合现实技术具有巨大的潜力，可以从根本上改变我们与环境、他人和物理世界的互动方式。像微软 HoloLens1 & 2 这样的混合现实头盔已经在许多领域得到广泛应用，特别是在一线工作场景中，从辅助手术到远程协作，从任务指导到将数字孪生设备叠加到真实世界。尽管在这些领域已经被采用，但混合现实的总体空间仍处于起步阶段。通常，新的混合现实应用的发展需要基础研究和不同传感器的新组合。通过使用工具，我们可以有效地收集原始传感器数据，并开发新的运行在设备上的计算机视觉算法，这大大降低了该领域计算机视觉研究的门槛。

2018 年发布的第一代 HoloLens 研究模式，通过提供所有原始图像传感器流（包括深度和红外），使设备上的计算机视觉研究成为可能。与一个收集辅助工具和示例应用程序[4]的公共存储库一起发布的研究模式，促进了 HoloLens 作为计算机视觉和机器人[1]研究的强大工具的使用。

2019 年发布的 HoloLens2（图1）带来了与第一代设备相比的许多改进，如专用 DNN 核心、关节式手跟踪和眼球注视跟踪[2]。然而，HoloLens2 是建立在新硬件上的新平台，与之前版本的研究模式不兼容。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307205418.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307205418.png)

图 1 所示微软 Hololens2

在这份技术报告中，我们介绍了 2020 年推出的第二代全息透镜研究模式。Research Mode 提供了一组 c++ api 和工具来访问 HoloLens2 传感器流。我们讨论了与前一个版本有关的主要新奇之处，并提出了一组构建在其之上的应用程序。要了解更多的资料和 API 文档，请读者参考 GitHub 存储库[3]。

研究模式是为在计算机视觉和机器人领域探索新思路的学术和工业研究人员设计的。它并不用于部署到最终用户的应用程序。此外，微软并没有保证在未来的硬件或操作系统更新中支持研究模式。

本技术报告的其余部分组织如下：

第 2 节介绍了 HoloLens2 设备，详细介绍了它的输入流。第 3 节概述了 Research Mode API，第 4 节展示了几个示例应用程序。最后，第五节总结了我们的贡献。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307205636.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307205636.png)

图2：HPU 和 SoC: HPU（顶部）位于设备的前部，靠近传感器。背面的 SoC（底部）是高通骁龙 850。

## 2. HoloLens2
与第一代设备相比，HoloLens2 混合现实耳机带来了一系列改进——包括更大的视场、定制 DNN 核心、全铰接手跟踪和眼睛凝视跟踪。

该设备具有第二代定制全息处理单元（HPU 2.0），能够实现低功耗、实时计算机视觉。HPU 在设备上运行所有的计算机视觉算法（头部跟踪、手部跟踪、眼睛注视跟踪、空间映射等），并承载 DNN 核心。它位于设备的前部，靠近传感器（图2，顶部）。SoC 上的 CPU（高通SnapDragon 850）仍然完全可用。SoC 位于背面（图2，底部）。

该设备配有深度和 RGB 摄像头、四个灰度摄像头和一个惯性测量单元（IMU），如图 3 所示。音频捕获与麦克风阵列（5通道）。

HoloLens2 的研究模式允许访问以下输入流:
- 4 个可见光跟踪摄像机（VLC）：系统用于实时视觉惯性 SLAM 的灰度摄像机（30 帧/秒）。
- 深度相机，有两种模式：
    - AHAT（关节式手部跟踪），用于手部跟踪的高帧率（45 帧/秒）近深度传感。由于手的支撑距离设备 1 米，HoloLens2 仅通过计算基于相位的飞行时间相机的“混叠深度”来节省电力。这意味着当用米来表示时，信号只包含到设备的距离的小数部分（见图4）。
    - 用于在设备上计算空间映射的远距离、低帧率（1-5 fps）深度传感。
- 两个深度模式的红外流（有效亮度，简称 AB），计算从相同的调制红外信号深度计算。这些图像由红外线照射，不受周围可见光的影响（见图4，右）。
- 惯性测量单元（IMU）：
    - 加速度计，系统使用它来确定沿 x, y, z 轴的线性加速度以及重力。
    - 陀螺仪，系统中用来确定旋转的仪器。
    - 磁强计，系统用于绝对方位估计。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307214229.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307214229.png)

图3 HoloLens2 输入传感器

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307214406.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307214406.png)

图4 AHAT 模式下的深度相机：深度（左）和有效亮度（右）图像。

对于每个流，研究模式提供了检索帧和相关信息（例如，分辨率和时间戳）的接口，并将传感器与设备和世界映射到一起。表 1 总结了每个（摄像机）输入流的主要特征。在下一节中，我们将提供 API 的概述。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307213659.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307213659.png)

## 3. 研究模式 API
在本节中，我们将描述研究模式暴露的主要对象以及如何使用它们访问传感器输入流。我们向读者推荐[3]以获取详细的 API 文档。

研究模式的主传感器循环（第 3.1 节）首先创建一个 ResearchModeDevice 对象，该对象用于获取可用传感器的列表。传感器对象公开方法来检索和处理帧（第 3.2 节），并根据设备和世界（第 3.3 节）定位传感器。

### 3.1 主传感器循环
主要的传感器处理循环包括实例化 ResearchModeDevice、获取传感器描述符、打开传感器流和获取帧:

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307214816.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307214816.png)

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307214846.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307214846.png)

注意，OpenStream 和 GetNextBuffer 需要从同一个线程调用。由于 GetNextBuffer 调用是阻塞的，每个传感器帧循环应该在它们自己的线程上运行。这允许传感器以它们自己的帧速率处理。

### 3.2 传感器和传感器框架
前一节介绍的 IResearchModeSensor 接口对研究模式传感器进行了抽象。它提供了所有传感器通用的方法和属性：OpenStream, CloseStream, GetFriendlyName, GetSensorType, GetNextBuffer。传感器可以有以下几种类型：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307215010.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307215010.png)

其中前六种为摄像机传感器，其余三种为 IMU 传感器。相机和 IMU 传感器曝光的方法不同：例如，相机传感器曝光的方法是将相机空间中的 3D 点投射到图像空间中的 2D 点（见第 3.3 节），而 IMU 传感器不这样做。传感器专门化是通过调用 QueryInterface 获得的:

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307215158.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307215158.png)

IResearchModeSensorFrame 接口在每个指定的传感器之间也存在类似的区别。一旦传感器处于流模式，传感器帧将被 IResearchModeSensor::GetNextBuffer 检索。所有的传感器帧都有一个共同的 IResearchModeSensorFrame 接口，它返回所有类型帧的共同的帧信息：时间戳和以字节为单位的样本大小。如上所述，相机和 IMU 帧专门化是通过调用 QueryInterface 获得的：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307215452.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307215452.png)

通过相机和 IMU 帧可以访问以下信息：

相机帧提供了分辨率，曝光，增益。此外，
- VLC 帧返回灰度缓冲区;
- 长抛深度帧返回一个深度缓冲区，一个 sigma 缓冲区和一个有效亮度缓冲区;
- 深度帧返回一个深度缓冲区和一个有效亮度缓冲区。

有效亮度缓冲区返回所谓的 IR 读数。在干净的红外读数中的像素值与从场景返回的光量成比例。该图像看起来与常规的红外图像相似。

长抛的 sigma 缓冲区用于基于深度算法计算的无效掩码来无效不可靠的深度。为了提高效率，无效代码被嵌入到深度通道本身中。

下面的代码演示了如何访问长抛出深度：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307215758.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307215758.png)

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307215828.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307215828.png)

IMU 帧存储传感器批量样品。加速度计帧存储加速度计测量值和温度；陀螺仪帧存储陀螺仪测量值和温度；磁强计帧存储磁强计测量值。

### 3.3 传感器坐标帧
所有传感器都被定位在一个设备定义的坐标帧中，该帧被定义为 rigNode。每个传感器返回其变换到 rigNode（设备原点），表示为 extrinsics 刚体变换（旋转和平移）。在HoloLens2 上，设备原点对应于左前方可见光相机；因此，该传感器返回的变换对应于恒等变换。图 5 显示了相对于 rigNode 的摄像机坐标帧。
