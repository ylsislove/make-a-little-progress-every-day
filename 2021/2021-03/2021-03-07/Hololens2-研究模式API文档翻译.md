<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Hololens2-研究模式API文档翻译](#hololens2-%E7%A0%94%E7%A9%B6%E6%A8%A1%E5%BC%8Fapi%E6%96%87%E6%A1%A3%E7%BF%BB%E8%AF%91)
  - [综述](#%E7%BB%BC%E8%BF%B0)
  - [大纲](#%E5%A4%A7%E7%BA%B2)
  - [主传感器读取循环](#%E4%B8%BB%E4%BC%A0%E6%84%9F%E5%99%A8%E8%AF%BB%E5%8F%96%E5%BE%AA%E7%8E%AF)
  - [传感器类型](#%E4%BC%A0%E6%84%9F%E5%99%A8%E7%B1%BB%E5%9E%8B)
    - [相机传感器](#%E7%9B%B8%E6%9C%BA%E4%BC%A0%E6%84%9F%E5%99%A8)
    - [惯性传感器](#%E6%83%AF%E6%80%A7%E4%BC%A0%E6%84%9F%E5%99%A8)
  - [传感器坐标帧](#%E4%BC%A0%E6%84%9F%E5%99%A8%E5%9D%90%E6%A0%87%E5%B8%A7)
  - [传感器](#%E4%BC%A0%E6%84%9F%E5%99%A8)
    - [传感器帧](#%E4%BC%A0%E6%84%9F%E5%99%A8%E5%B8%A7)
    - [VLC帧载荷](#vlc%E5%B8%A7%E8%BD%BD%E8%8D%B7)
    - [AHAT和长抛摄像机帧载荷](#ahat%E5%92%8C%E9%95%BF%E6%8A%9B%E6%91%84%E5%83%8F%E6%9C%BA%E5%B8%A7%E8%BD%BD%E8%8D%B7)
    - [长抛失效](#%E9%95%BF%E6%8A%9B%E5%A4%B1%E6%95%88)
    - [AHAT无效](#ahat%E6%97%A0%E6%95%88)
    - [IMU帧载荷](#imu%E5%B8%A7%E8%BD%BD%E8%8D%B7)
  - [同意提示](#%E5%90%8C%E6%84%8F%E6%8F%90%E7%A4%BA)
  - [设置](#%E8%AE%BE%E7%BD%AE)
    - [要求清单条目](#%E8%A6%81%E6%B1%82%E6%B8%85%E5%8D%95%E6%9D%A1%E7%9B%AE)
  - [API参考](#api%E5%8F%82%E8%80%83)
    - [设备接口](#%E8%AE%BE%E5%A4%87%E6%8E%A5%E5%8F%A3)
    - [传感器接口](#%E4%BC%A0%E6%84%9F%E5%99%A8%E6%8E%A5%E5%8F%A3)
    - [传感器帧](#%E4%BC%A0%E6%84%9F%E5%99%A8%E5%B8%A7-1)
    - [同意接口](#%E5%90%8C%E6%84%8F%E6%8E%A5%E5%8F%A3)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Hololens2-研究模式API文档翻译

## 综述
第一代 HoloLens 引入了研究模式，研究不用于部署访问设备上的关键传感器的应用程序。HoloLens2 的研究模式保留了 HoloLens1 的功能，增加了对额外流的访问。同样，对于第一个版本，可以从以下输入中收集数据:
- 可见光环境跟踪摄像机-系统用于头部跟踪和地图创建。它们返回每像素 8 位的灰度图像。
- 两种模式操纵下的深度摄像机
- 关节式手跟踪方式(AHAT)，用于手跟踪的高频(45帧/秒)近深度传感。支持距离设备 1 米之内的手势追踪，HoloLens2 仅通过计算基于相位的飞行时间相机的“混叠深度”来节省电力。这意味着，当距离超过 1 米时，信号只包含到设备的距离的小数部分。
    - 空间映射中使用的长抛、低频(1-5 FPS)的深度传感。
- 两个版本的红外反射率流- HoloLens 用来计算深度。这些图像由红外线照射，不受周围可见光的影响。

此外，HoloLens2 还支持访问以下内容:
- 加速度计-系统用来确定沿 X, Y, Z 轴的线性加速度以及重力。
- 陀螺仪-系统中用来确定旋转的仪器。
- 磁强计-系统用于绝对方位估计。

## 大纲
研究模式 API 是基于一种名为 Nano-COM 的轻量级派生。Nano-COM 指的是一种 API 设计模式，它使用 IUnknown 作为对象标识和生存期，但不需要 COM 运行时基础设施，用工厂函数替换 CoCreateInstance 的使用，这些工厂函数返回用参数初始化的对象到这些函数。接口只支持 QueryInterface、AddRef 和 Release。api 返回 HRESULT 错误码。DirectX11 和 12 也是一个 Nano-COM api。

API的结构如下:
- 首先创建的对象是研究模式设备。这是API工厂对象。它用于:
    - 按类型枚举可用的传感器
    - 创建传感器对象
    - 请求访问权限
    - 每个传感器类型只能创建一个传感器
- 传感器提供以下功能:
    - 返回传感器的名称和类型
    - 启动和停止流
    - 在流状态下等待和检索帧
    - 返回 extrinsics 矩阵，给出传感器相对于设备连接原点(Rig origin)的相对位置
    - 返回设备坐标帧 GUID，可以用来映射设备坐标帧到其他感知坐标帧
    - 传感器可以是摄像机或 imu，两者都返回帧传感器特定的有效载荷格式
- 传感器帧提供:
    - 帧时间戳
    - 帧大小
    - 专门针对每个传感器的属性和有效负载格式。

对于所有传感器，初始化调用应该只进行一次，而且传感器不是线程安全的。帧应该从传感器打开的线程读取。传感器可以共享一个线程，或者每个都有一个线程。

## 主传感器读取循环
主传感器处理循环概述为:
- 创建研究模式设备
- 获取所有传感器所在的设备坐标框架。我们称之为 rigNode，它由 GUID 标识，GUID 可与 HoloLens 感知 api 一起用于映射其他HoloLens 感知坐标框架中的传感器特定坐标。下面的 https://docs.microsoft.com/en-us/windows/mixed-reality/coordinate-systems 解释了感知坐标框架。
- 枚举传感器
- 获取传感器信息
    - 对于摄像机，该对象在摄像机坐标框架中投影 / 取消投影图像点到 3D 点
    - Extrinsics 用于相对于设备 rigNode 定位传感器。

下面的代码显示了打开研究模式设备，获取传感器描述符和从传感器获取帧。api 返回应该检查错误的结果 HRSULTS。下面的代码省略了错误检查，以便更容易地执行 API 调用。与坐标框架相关的 api 将在后面的章节中描述。

```C++
    HRESULT hr = S_OK; 
    IResearchModeSensorDevice *pSensorDevice; 
    IResearchModeSensorDevicePerception *pSensorDevicePerception; 
    std::vector<ResearchModeSensorDescriptor> sensorDescriptors; 
    size_t sensorCount = 0; 
 
    hr = CreateResearchModeSensorDevice(&pSensorDevice); 
 
    // This call makes cameras run at full frame rate. Normaly they are optimized 
    // for headtracker use. For some applications that may be sufficient 
    pSensorDevice->DisableEyeSelection(); 
 
    hr = pSensorDevice->GetSensorCount(&sensorCount);
    sensorDescriptors.resize(sensorCount); 
 
    hr = pSensorDevice->GetSensorDescriptors(sensorDescriptors.data(), 
sensorDescriptors.size(), &sensorCount); 
 
    for (const auto& sensorDescriptor : sensorDescriptors) 
    { 
        // Sensor frame read thread 
 
        IResearchModeSensor *pSensor = nullptr; 
        size_t sampleBufferSize; 
        IResearchModeSensorFrame* pSensorFrame = nullptr; 
 
        hr = pSensorDevice->GetSensor(sensorDescriptor.sensorType, &pSensor); 
 
        swprintf_s(msgBuffer, L"Sensor %ls\n", pSensor->GetFriendlyName()); 
        OutputDebugStringW(msgBuffer); 
 
        hr = pSensor->GetSampleBufferSize(&sampleBufferSize); 
 
        hr = pSensor->OpenStream(); 
 
        for (UINT i = 0; i < 4; i++) 
        { 
            hr = pSensor->GetNextBuffer(&pSensorFrame); 
 
            if (pSensor->GetSensorType() >= IMU_ACCEL) 
            { 
                ProcessFrameImu(pSensor, pSensorFrame, i); 
            } 
            else 
            { 
                ProcessFrameCamera(pSensor, pSensorFrame, i); 
            } 
 
            if (pSensorFrame) 
            { 
                pSensorFrame->Release(); 
            } 
        } 
 
        hr = pSensor->CloseStream(); 
 
        if (pSensor) 
        { 
            pSensor->Release(); 
        } 
    } 
 
    pSensorDevice->EnableEyeSelection(); 
 
    pSensorDevice->Release(); 
 
    return hr; 
```

上面的代码显示了在同一个线程上读取的所有传感器。由于 GetNextBuffer 调用会引起阻塞，每个传感器帧循环应该在自己的线程上运行。这允许以自己的帧速率处理每个传感器。

OpenStream 和 GetNextBuffer 需要从同一个线程调用。GetNextBuffer 调用会引起阻塞。每个传感器的传感器帧循环应该在它们自己的线程上运行。这允许传感器按照它们自己的帧速率进行处理。推荐使用以下线程模式:
- 主线程管理研究模式设备和传感器
- 每个传感器都有一个线程，它打开传感器流，读取缓冲区并处理缓冲区
- 主线程渲染缓冲区和结果

```c++
SensorLoop(IResearchModeSensor *pSensor) 
{ 
    hr = pSensor->OpenStream(); 
 
    while (fRunning) 
    { 
        hr = pSensor->GetNextBuffer(&pSensorFrame); 
 
        ProcessFrame(pSensor, pSensorFrame, i); 
 
        if (pSensorFrame) 
        { 
            pSensorFrame->Release(); 
        } 
    } 
 
    hr = pSensor->CloseStream(); 
}
```

## 传感器类型
### 相机传感器
- Intrinsics (投影 / 不投影)
- 在相机坐标空间的一些功能
- Extrinsics返回设备空间的 R, T 变换
- 帧被指定为相机帧

### 惯性传感器
- Extrinsics返回设备空间的 R, T 变换
- 帧被指定为惯性传感器帧

## 传感器坐标帧
每个传感器返回它的变换到 rigNode (Rig origin) 表示为一个外部刚体变换。图 1 显示了相机坐标帧相对于设备坐标帧。注意，在 HoloLens2 上，设备原点对应于左前方可见光相机。因此，该传感器返回的变换对应于恒等变换。

extrinsics变换可检索如下:

```c++
IResearchModeCameraSensor *pCameraSensor; 
DirectX::XMFLOAT4X4 cameraPose; 
// … 
// Get matrix of extrinsics wrt the rigNode 
pCameraSensor->GetCameraExtrinsicsMatrix(&cameraPose); 
```

要将 rigNode（以及设备）映射到其他 HoloLens 感知坐标帧中，可以使用感知api。

```c++
using namespace winrt::Windows::Perception::Spatial; 
using namespace winrt::Windows::Perception::Spatial::Preview; 
 
SpatialLocator locator; 
IResearchModeSensorDevicePerception* pSensorDevicePerception; 
GUID guid; 
HRESULT hr = m_pSensorDevice->QueryInterface(IID_PPV_ARGS(&pSensorDevicePerception)); 
if (SUCCEEDED(hr)) 
{ 
    hr = pSensorDevicePerception->GetRigNodeId(&guid); 
    locator = SpatialGraphInteropPreview::CreateLocatorForNode(guid); 
} 
// … 
auto location = locator.TryLocateAtTimestamp(timestamp, anotherCoordSystem); 
```

相机传感器暴露映射 / 不映射方法，以在相机投影 3D 点。图 3 显示了摄像机参考帧的 3D 坐标与二维图像坐标的关系。

Map / unmap 方法可以使用如下:

```c++
IResearchModeCameraSensor *pCameraSensor; 
//… 
float xy[2] = {0}; 
float uv[2] = {0}; 
float uv_mapped[2] = {0}; 
 
for (int i = 0; i <= 10; i++) 
{ 
for (int j = 0; j <= 10; j++) 
       { 
           // VLC images are 640x480 
           uv[0] = i * 64.0f; 
           uv[1] = j * 48.0f; 
  
           pCameraSensor->MapImagePointToCameraUnitPlane(uv, xy); 
           // … 
           pCameraSensor->MapCameraSpaceToImagePoint(xy, uv_mapped); 
           // … 
     } 
}
```

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307162301.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307162301.png)

图 1 相对于 rig node 坐标帧的深度和正面可见光相机坐标帧。Long throw和AHAT是同一相机的不同模式，所以外观是一样的。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307162642.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307162642.png)

图2 Hololens相机。黄色是 VLC 相机，红色是深度相机

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307162738.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307162738.png)

图 3 Map Unmap 方法将摄像机参考帧中的3d (X,Y,Z)坐标转换为摄像机(X,Y)图像坐标，(X,Y)图像坐标转换为摄像机坐标帧中的(X,Y,Z)方向向量。

## 传感器
iresearchmodessensor 抽象了研究模式传感器。它提供了所有传感器通用的方法和属性:

```c++
DECLARE_INTERFACE_IID_(IResearchModeSensor, IUnknown, "4D4D1D4B-9FDD-4001-BA1E-
F8FAB1DA14D0") 
{ 
    STDMETHOD(OpenStream()) = 0; 
    STDMETHOD(CloseStream()) = 0; 
    STDMETHOD_(LPCWSTR, GetFriendlyName)() = 0; 
    STDMETHOD_(ResearchModeSensorType, GetSensorType)() = 0; 
 
    STDMETHOD(GetSampleBufferSize( 
        _Out_ size_t *pSampleBufferSize)) = 0; 
    STDMETHOD(GetNextBuffer( 
        _Outptr_result_nullonfailure_ IResearchModeSensorFrame **ppSensorFrame)) = 0; 
};
```
- OpenStream 将传感器置于产生帧的状态。这必须在检索缓冲区之前调用
- CloseStream 停止帧捕捉
- GetFriendlyName 返回一个包含传感器名称的字符串
- GetSensorType 返回传感器类型
- GetNextBuffer 返回下一个可用的缓冲区。这是一个阻塞调用

传感器可以有以下几种类型:

```c++
enum ResearchModeSensorType 
{
    LEFT_FRONT, 
    LEFT_LEFT, 
    RIGHT_FRONT, 
    RIGHT_RIGHT, 
    DEPTH_AHAT, 
    DEPTH_LONG_THROW, 
    IMU_ACCEL, 
    IMU_GYRO, 
    IMU_MAG 
};
```

每个传感器对象都定义了可以通过 QIed 实现的传感器特定接口。这些将检索传感器特定的信息。

### 传感器帧
一旦传感器处于流模式，传感器帧将通过 IResearchModeSensor::GetNextBuffer 从传感器中获取。所有的传感器帧都有一个共同的接口，它返回所有类型帧的共同的帧信息。缓冲区中包含帧数据的内存归帧对象所有。当释放帧接口时，内存也随之释放。帧接口提供了可以用来访问帧中包含的数据的方法。

```c++
DECLARE_INTERFACE_IID_(IResearchModeSensorFrame, IUnknown, "73479614-89C9-4FFD-9C16-
615BC32C6A09") 
{ 
    STDMETHOD(GetResolution( 
        _Out_ ResearchModeSensorResolution *pResolution)) = 0; 
    // For frames with batched samples this returns the time stamp for the first sample 
in the frame. 
    STDMETHOD(GetTimeStamp( 
        _Out_ ResearchModeSensorTimestamp *pTimeStamp)) = 0; 
};
```

所有传感器帧接口请参见《附录传感器帧》。

每个传感器都有自己的帧专用接口

- 所有的帧类型：
    - 帧时间戳。这些是 HostTicks  和 SensorTicks。HostTicks 是以 filetime 为单位的 CPU 时间，SensorTicks 是以纳秒为单位的传感器滴答数。
    - 以字节为单位的样本大小
- 相机帧
    - 所有的相机帧都提供分辨率，曝光，增益
    - VLC相机帧返回灰度缓冲
    - 深度长投相机帧包含有效的亮度缓冲，距离缓冲和 sigma 缓冲
    - 深度 AHAT 相机帧包含一个有效的亮度缓冲和距离缓冲
- IMU 帧包含大量传感器样本。每个传感器样本都是一个结构体，它包含一个传感器值和相应的 SocTicks (HostTicks)、VinylHupTicks (SensorTicks)和温度
    - 加速度计的值是 3 个 m/s^2 加速度
    - 陀螺计的值是三个角速度，单位是 deg/s
    - 磁强计帧包含磁强计值

### VLC帧载荷
VLC帧实现以下接口

```c++
DECLARE_INTERFACE_IID_(IResearchModeSensorVLCFrame, IUnknown, "5C693123-3851-4FDC-A2D9-
51C68AF53976") 
{ 
    STDMETHOD(GetBuffer( 
        _Outptr_ const BYTE **ppBytes, 
        _Out_ size_t *pBufferOutLength)) = 0; 
    STDMETHOD(GetGain( 
        _Out_ UINT32 *pGain)) = 0; 
    STDMETHOD(GetExposure( 
        _Out_ UINT64 *pExposure)) = 0; 
}; 
```

GetBuffer 返回一个指向内存的指针，该指针包含灰度像素帧。这些是行主字节像素，值从 0 到 255。缓冲区的大小从帧的 IResearchModeSensorFrame::GetResolution 接口获取。

增益的值从 0 到 255，曝光的单位是纳秒。

下面的代码展示了如何从 VLC 帧中提取分辨率、曝光、增益、时间戳和图像数据。

```c++
void ProcessFrame(IResearchModeSensor *pSensor, IResearchModeSensorFrame* pSensorFrame, 
int bufferCount) 
{ 
    ResearchModeSensorResolution resolution; 
    ResearchModeSensorTimestamp timestamp; 
    wchar_t filename[260]; 
    const BYTE *pImage = nullptr; 
    IResearchModeSensorVLCFrame *pVLCFrame = nullptr; 
    HRESULT hr = S_OK; 
    size_t outBufferCount; 
 
    pSensorFrame->GetResolution(&resolution); 
    pSensorFrame->GetTimeStamp(&timestamp); 
 
    hr = pSensorFrame->QueryInterface(IID_PPV_ARGS(&pVLCFrame)); 
 
    if (SUCCEEDED(hr)) 
    { 
        UINT32 gain; 
        UINT64 exposure; 
 
        pVLCFrame->GetBuffer(&pImage, &outBufferCount); 
 
        // Add code to process frame pixels here. 
 
        swprintf_s(filename, L"%s_%d_ts%d.bmp", pSensor->GetFriendlyName(), bufferCount, 
            timestamp.HostTicks); 
        // The pixel data is at pImage memory address. Pixels are BYTES from 0-255 and frame is for major. 
        swprintf_s(filename, L"  %S_%d_ts%d.bmp\n", pSensor->GetFriendlyName(), 
bufferCount, timestamp.HostTicks); 
        OutputDebugStringW(filename); 
 
        hr = pVLCFrame->GetGain(&gain); 
 
        if (SUCCEEDED(hr)) 
        { 
            swprintf_s(filename, L"  Gain %d\n", gain); 
            OutputDebugStringW(filename); 
        } 
 
        hr = pVLCFrame->GetExposure(&exposure); 
 
        if (SUCCEEDED(hr)) 
        { 
            swprintf_s(filename, L"  Exposure %d\n", exposure); 
            OutputDebugStringW(filename); 
        } 
} 
```

### AHAT和长抛摄像机帧载荷
深度帧实现以下接口:

```c++
DECLARE_INTERFACE_IID_(IResearchModeSensorDepthFrame, IUnknown, "35167E38-E020-43D9-898E-
6CB917AD86D3") 
{ 
    STDMETHOD(GetBuffer( 
        _Outptr_ const UINT16 **ppBytes, 
        _Out_ size_t *pBufferOutLength)) = 0; 
    STDMETHOD(GetAbDepthBuffer( 
        _Outptr_ const UINT16 **ppBytes, 
        _Out_ size_t *pBufferOutLength)) = 0; 
    STDMETHOD(GetSigmaBuffer( 
        _Outptr_ const BYTE **ppBytes, 
        _Out_ size_t *pBufferOutLength)) = 0; 
}; 
```

在长抛模式下的深度相机帧有一个深度缓冲和一个 sigma 缓冲用于无效的深度像素，和一个有效的亮度(Ab)缓冲。在 AHAT 模式下，它只有深度缓冲和有效的亮度缓冲。

有效亮度缓冲区返回所谓的 IR 读数。在干净的红外读数中的像素值与从场景返回的光量成比例。该图像看起来与常规的红外图像相似。

长抛的 sigma 缓冲区用于基于深度算法计算的无效掩码使不可靠的深度失效。为了提高效率，AHAT 将无效代码嵌入深度通道本身。

### 长抛失效
它将失效码和置信度嵌入到每个像素的 8 位数据缓冲器中。如果最高有效位(MSB)设置为 1，则其他 7 位表示失效原因。无效掩码是:
- Invalid = 0x80,             // MSB 最高有效位
- OutOfBounds = 0xC0,         // 主动红外照明罩外
- SignalSaturated = 0xA0,     // 饱和的红外信号
- FilterOutlier = 0x90,       // 过滤异常值
- EmptySignal = 0x88,         // 低红外信号
- MultiPathDetected = 0x84,   // 多路径干扰检测（从场景中多个对象接收信号）
- OutOfRangeFar = 0x82,       // 超过最大支持范围(设置为7500mm)
- OutOfRangeNear = 0x81       // 超过最小支持范围(设置为200mm)

### AHAT无效
对于 AHAT，在深度信道中嵌入了失效码。大于 4090 的像素是无效的。无效的代码是:
- 4095：在主动红外照明罩外面
- 4093：低红外信号

读取 AHAT 和长抛深度帧:

分辨率、曝光、增益和时间戳可以按照上面的方法读取。下面的代码展示了如何从 Long Throw 和 AHAT 帧中提取和处理缓冲区。

```c++
void ProcessFrame(IResearchModeSensor *pSensor, IResearchModeSensorFrame* pSensorFrame, 
int bufferCount) 
{ 
    ResearchModeSensorResolution resolution; 
    ResearchModeSensorTimestamp timestamp; 
    wchar_t filename[260]; 
    IResearchModeSensorDepthFrame *pDepthFrame = nullptr; 
    const UINT16 *pAbImage = nullptr; 
    const UINT16 *pDepth = nullptr; 
 
    // sigma buffer needed only for Long Throw 
    const BYTE *pSigma = nullptr; 
 
    // invalidation mask for Long Throw 
    USHORT mask = 0x80; 
 
    // invalidation value for AHAT 
    USHORT maxValue = 4090;  
 
    HRESULT hr = S_OK; 
    size_t outBufferCount; 
 
    pSensorFrame->GetResolution(&resolution); 
    pSensorFrame->GetTimeStamp(&timestamp); 
 
    hr = pSensorFrame->QueryInterface(IID_PPV_ARGS(&pDepthFrame)); 
    bool isLongThrow = (pSensor->GetSensorType() == DEPTH_LONG_THROW); 
 
    if (SUCCEEDED(hr) && isLongThrow) 
    { 
       // extract sigma buffer for Long Throw 
      hr = pDepthFrame->GetSigmaBuffer(&pSigma, &outBufferCount); 
       // Add code to process buffer here. 
    } 
  
    if (SUCCEEDED(hr)) 
    { 
        // extract depth buffer 
        hr = pDepthFrame->GetBuffer(&pDepth, &outBufferCount); 
        // validate depth 
        for (size_t i = 0; i < outBufferCount; ++i) 
        { 
             // use a different invalidation condition for Long Throw and AHAT 
             const bool isInvalid = isLongThrow ? ((pSigma[i] & mask) > 0) : 
                                                   (pDepth[i] >= maxValue)); 
            if (isInvalid) 
            {     
                    pDepth[i] = 0; 
            } 
        }
        // Add code to process buffer here. 
    } 
 
    if (SUCCEEDED(hr)) 
    { 
        // extract active brightness buffer 
        hr = pDepthFrame->GetAbDepthBuffer(&pAbImage, &outBufferCount);         
        // Add code to process buffer here. 
    } 
 
    if (pDepthFrame) 
    { 
        pDepthFrame->Release(); 
    } 
}
```

### IMU帧载荷
IMU帧实现以下接口:

```c++
DECLARE_INTERFACE_IID_(IResearchModeAccelFrame, IUnknown, "42AA75F8-E3FE-4C25-88C6-
F2ECE1E8A2C5") 
{ 
    STDMETHOD(GetCalibratedAccelaration( 
        _Out_ DirectX::XMFLOAT3 *pAccel)) = 0; 
    STDMETHOD(GetCalibratedAccelarationSamples( 
        _Outptr_ const AccelDataStruct **ppAccelBuffer, 
        _Out_ size_t *pBufferOutLength)) = 0; 
}; 
 
DECLARE_INTERFACE_IID_(IResearchModeGyroFrame, IUnknown, "4C0C5EE7-CBB8-4A15-A81F-
943785F524A6") 
{ 
    STDMETHOD(GetCalibratedGyro( 
      Out_ DirectX::XMFLOAT3 *pGyro)) = 0; 
    STDMETHOD(GetCalibratedGyroSamples( 
        _Outptr_ const GyroDataStruct **ppAccelBuffer, 
        _Out_ size_t *pBufferOutLength)) = 0; 
}; 
 
DECLARE_INTERFACE_IID_(IResearchModeMagFrame, IUnknown, "2376C9D2-7F3D-456E-A39E-
3B7730DDA9E5") 
{ 
    STDMETHOD(GetMagnetometer( 
        _Out_ DirectX::XMFLOAT3 *pMag)) = 0; 
    STDMETHOD(GetMagnetometerSamples( 
        _Outptr_ const MagDataStruct **ppMagBuffer, 
        _Out_ size_t *pBufferOutLength)) = 0; 
}; 
```
- 加速度计帧-包含沿X、Y、Z轴的线性加速度以及重力。
- 陀螺仪框架-包含旋转。
- 磁强计-包含绝对方位估计。

IMU帧包含IMU批量样品。每个样本是下列之一：

```c++
struct AccelDataStruct 
{ 
    uint64_t VinylHupTicks; // Sensor ticks in micro seconds 
    uint64_t SocTicks; 
    float AccelValues[3]; // In m/(s*s) 
    float temperature; 
}; 
 
struct GyroDataStruct 
{ 
    uint64_t VinylHupTicks; // Sensor ticks in micro seconds 
    uint64_t SocTicks; 
    float GyroValues[3]; 
    float temperature; 
}; 
 
struct MagDataStruct 
{ 
    uint64_t VinylHupTicks; // Sensor ticks in micro seconds 
    uint64_t SocTicks; 
    float MagValues[3]; 
}; 
```

读取 IMU 帧的一个样本:

下面的代码显示了如何从 IMU 帧的单个样本中提取 IMU 数据

```c++
void PrintSensorValue(IResearchModeSensorFrame *pSensorFrame) 
{ 
    DirectX::XMFLOAT3 sample; 
    IResearchModeGyroFrame *pSensorGyroFrame = nullptr; 
    IResearchModeAccelFrame *pSensorAccelFrame = nullptr; 
    IResearchModeMagFrame *pSensorMagFrame = nullptr; 
    char printString[1000]; 
    HRESULT hr = S_OK; 
    ResearchModeSensorTimestamp timeStamp; 
    UINT64 lastSocTickDelta = 0;  
 
    pSensorFrame->GetTimeStamp(&timeStamp); 
 
    if (glastSocTick != 0) 
    { 
        lastSocTickDelta = timeStamp.HostTicks - glastSocTick; 
    } 
    glastSocTick = timeStamp.HostTicks; 
 
    hr = pSensorFrame->QueryInterface(IID_PPV_ARGS(&pSensorAccelFrame)); 
    if (SUCCEEDED(hr)) 
    {        
        hr = pSensorAccelFrame->GetCalibratedAccelaration(&sample); 
        if (FAILED(hr)) 
        { 
            return; 
        } 
        sprintf(printString, "####Accel: % 3.4f % 3.4f % 3.4f %f %d\n", 
                sample.x, 
                sample.y, 
                sample.z, 
                sqrt(sample.x * sample.x + sample.y * sample.y + sample.z * sample.z), 
                (lastSocTickDelta * 1000) / timeStamp.HostTicksPerSecond 
                ); 
        OutputDebugStringA(printString); 
        pSensorAccelFrame->Release(); 
        return; 
    } 
 
    hr = pSensorFrame->QueryInterface(IID_PPV_ARGS(&pSensorGyroFrame)); 
    if (SUCCEEDED(hr)) 
    {      
        hr = pSensorGyroFrame->GetCalibratedGyro(&sample); 
        if (FAILED(hr)) 
        { 
            return; 
        } 
        sprintf(printString, "####Gyro: % 3.4f % 3.4f % 3.4f %f %d\n", 
                sample.x, 
                sample.y, 
                sample.z, 
                sqrt(sample.x * sample.x + sample.y * sample.y + sample.z * sample.z), 
                (lastSocTickDelta * 1000) / timeStamp.HostTicksPerSecond 
                ); 
        OutputDebugStringA(printString); 
        pSensorGyroFrame->Release(); 
        return; 
    } 
 
    hr = pSensorFrame->QueryInterface(IID_PPV_ARGS(&pSensorMagFrame)); 
    if (SUCCEEDED(hr)) 
    {  
        hr = pSensorMagFrame->GetMagnetometer(&sample); 
        if (FAILED(hr)) 
        { 
            return;
        } 
        sprintf(printString, "####Mag: % 3.4f % 3.4f % 3.4f %d\n", 
                sample.x, 
                sample.y, 
                sample.z, 
                (lastSocTickDelta * 1000) / timeStamp.HostTicksPerSecond 
                ); 
        OutputDebugStringA(printString); 
        pSensorMagFrame->Release(); 
        return; 
    } 
}
```

读取 IMU 帧的所有 IMU 样本：

下面的代码显示了如何从 IMU 帧的所有样本中提取 IMU 数据

```c++
void PrintSensorValue(IResearchModeSensorFrame *pSensorFrame) 
{ 
    DirectX::XMFLOAT3 sample; 
    IResearchModeGyroFrame *pSensorGyroFrame = nullptr; 
    IResearchModeAccelFrame *pSensorAccelFrame = nullptr; 
    IResearchModeMagFrame *pSensorMagFrame = nullptr; 
    char printString[1000]; 
    HRESULT hr = S_OK; 
    ResearchModeSensorTimestamp timeStamp; 
    UINT64 lastSocTickDelta = 0;  
 
    pSensorFrame->GetTimeStamp(&timeStamp); 
 
    hr = pSensorFrame->QueryInterface(IID_PPV_ARGS(&pSensorAccelFrame)); 
    if (SUCCEEDED(hr)) 
    { 
        const AccelDataStruct *pAccelBuffer; 
        size_t BufferOutLength; 
        hr = pSensorAccelFrame->GetCalibratedAccelarationSamples( 
            &pAccelBuffer, 
            &BufferOutLength); 
        if (FAILED(hr)) 
        { 
            return; 
        } 
        for (UINT i = 0; i < BufferOutLength; i++) 
        { 
            sample.x = pAccelBuffer[i].AccelValues[0]; 
            sample.y = pAccelBuffer[i].AccelValues[1]; 
            sample.z = pAccelBuffer[i].AccelValues[2]; 
            if (glastHupTick != 0) 
            { 
                lastSocTickDelta =  pAccelBuffer[i].VinylHupTicks - glastHupTick; 
                sprintf(printString, "####Accel-%3d-%3d-%3d: % 3.4f % 3.4f % 3.4f %f %d\n", 
                        gBatchCount, 
                        i, 
                        BufferOutLength, 
                        sample.x, 
                        sample.y, 
                        sample.z, 
                        sqrt(sample.x * sample.x + sample.y * sample.y + sample.z * sample.z), 
                        lastSocTickDelta / 1000 // micro seconds 
                        ); 
            } 
            glastHupTick = pAccelBuffer[i].VinylHupTicks; 
            OutputDebugStringA(printString); 
        } 
        gBatchCount++; 
        pSensorAccelFrame->Release(); 
        return; 
    } 
 
    hr = pSensorFrame->QueryInterface(IID_PPV_ARGS(&pSensorGyroFrame)); 
    if (SUCCEEDED(hr)) 
    { 
        const GyroDataStruct *pGyroBuffer; 
        size_t BufferOutLength; 
        hr = pSensorGyroFrame->GetCalibratedGyroSamples( 
            &pGyroBuffer, 
            &BufferOutLength); 
        if (FAILED(hr)) 
        { 
            return; 
        } 
        for (UINT i = 0; i < BufferOutLength; i++) 
        { 
            sample.x = pGyroBuffer[i].GyroValues[0]; 
            sample.y = pGyroBuffer[i].GyroValues[1]; 
            sample.z = pGyroBuffer[i].GyroValues[2]; 
            if (glastHupTick != 0) 
            { 
                lastSocTickDelta =  pGyroBuffer[i].VinylHupTicks - glastHupTick; 
                sprintf(printString, "####Gyro-%3d-%3d-%3d: % 3.4f % 3.4f % 3.4f %f %d\n", 
                        gBatchCount, 
                        i, 
                        BufferOutLength, 
                        sample.x, 
                        sample.y, 
                        sample.z, 
                        sqrt(sample.x * sample.x + sample.y * sample.y + sample.z * sample.z), 
                        lastSocTickDelta / 1000 // micro seconds 
                        ); 
            } 
            glastHupTick = pGyroBuffer[i].VinylHupTicks; 
            OutputDebugStringA(printString); 
        } 
        gBatchCount++; 
        pSensorGyroFrame->Release(); 
        return; 
    } 
 
    hr = pSensorFrame->QueryInterface(IID_PPV_ARGS(&pSensorMagFrame)); 
    if (SUCCEEDED(hr)) 
    { 
        const MagDataStruct *pMagBuffer; 
        size_t BufferOutLength; 
        hr = pSensorMagFrame->GetMagnetometerSamples( 
            &pMagBuffer, 
            &BufferOutLength); 
        if (FAILED(hr)) 
        { 
            return; 
        } 
        for (UINT i = 0; i < BufferOutLength; i++) 
        { 
            sample.x = pMagBuffer[i].MagValues[0]; 
            sample.y = pMagBuffer[i].MagValues[1]; 
            sample.z = pMagBuffer[i].MagValues[2]; 
            if (glastHupTick != 0) 
            { 
                lastSocTickDelta =  pMagBuffer[i].VinylHupTicks - glastHupTick; 
                sprintf(printString, "####Mag-%3d-%3d: % 3.4f % 3.4f % 3.4f %d\n", 
                        gBatchCount, 
                        i, 
                        sample.x, 
                        sample.y, 
                        sample.z, 
                        lastSocTickDelta / 1000 // micro seconds 
                        ); 
            } 
            glastHupTick = pMagBuffer[i].VinylHupTicks; 
            OutputDebugStringA(printString); 
        } 
        gBatchCount++; 
        pSensorMagFrame->Release(); 
        return; 
    } 
} 
```

## 同意提示
任何使用研究模式 API 访问摄像机或 imu 的 UWP 应用程序在打开流之前必须征得用户同意。根据用户的输入，应用程序应该进一步进行。
以下步骤概述了在 UWP 应用程序中添加同意提示所需的代码:
- 为了让用户同意摄像头和 IMU 的访问，请确保在应用程序清单中声明以下功能：
    ```xml
    <DeviceCapability Name="webcam" /> 
    <DeviceCapability Name="backgroundSpatialPerception"/> 
    ```
- 查询 Research Mode API 中实现同意检测的 SensorDeviceConsent 接口：
    ```c++
    hr = m_pSensorDevice->QueryInterface(IID_PPV_ARGS(&m_pSensorDeviceConsent)); 
    ```
- 在流可以被打开(OpenStream)之前，必须获得同意。通过回调返回同意结果。将同意响应与 API 调用者同步的一种方法是在同意回调上设置事件。
    ```c++
    ResearchModeSensorConsent camAccessCheck; 
    HANDLE camConsentGiven; 
    
    camConsenGiven = CreateEvent(nullptr, true, false, nullptr); 
    ```
- 在应用程序的主 UI 线程中注册相机和/或 IMU 同意回调。
    ```c++
    hr = m_pSensorDeviceConsent->RequestCamAccessAsync(CamAccessOnComplete); 
    ```
- 定义捕获用户同意的回调函数，并设置为此操作创建的事件。
    ```c++
    void CamAccessOnComplete(ResearchModeConsent consent) 
    { 
    camAccessCheck = consent; 
    SetEvent(camConsentGiven); 
    }
    ```
- 如果使用了工作线程，则等待回调，并寻找用户提供的同意，然后继续。
```c++
void CameraUpdateThread(SlateCameraRenderer* pSlateCameraRenderer, HANDLE camConsentGiven, Res
earchModeSensorConsent *camAccessConsent) 
{ 
    HRESULT hr = S_OK; 
    DWORD waitResult = WaitForSingleObject(camConsentGiven, INFINITE);   
 
   // wait for the event to be set and check for the consent provided by the user. 
 
    if (waitResult == WAIT_OBJECT_0) 
    { 
        switch (*camAccessConsent) 
        { 
        case ResearchModeSensorConsent::Allowed: 
            OutputDebugString(L"Access is granted"); 
            break; 
        case ResearchModeSensorConsent::DeniedBySystem: 
            OutputDebugString(L"Access is denied by the system"); 
            hr = E_ACCESSDENIED; 
            break; 
        case ResearchModeSensorConsent::DeniedByUser: 
            OutputDebugString(L"Access is denied by the user"); 
            hr = E_ACCESSDENIED; 
            break; 
        case ResearchModeSensorConsent::NotDeclaredByApp: 
            OutputDebugString(L"Capability is not declared in the app manifest"); 
                        hr = E_ACCESSDENIED; 
            break; 
        case ResearchModeSensorConsent::UserPromptRequired: 
            OutputDebugString(L"Capability user prompt required"); 
            hr = E_ACCESSDENIED; 
            break; 
        default: 
            OutputDebugString(L"Access is denied by the system"); 
            hr = E_ACCESSDENIED; 
            break; 
        } 
    } 
    else 
    { 
        hr = E_UNEXPECTED; 
    } 
 
    if (SUCCEEDED(hr)) 
    {  
         hr = pSlateCameraRenderer->m_pRMCameraSensor->OpenStream(); 
    }
}
```

为了测试你的应用程序是否正确地执行了这些检查，请确保在应用程序输出之前，检查 camera 和/或 IMUs 的提示是否出现。而且，对于每个用户来说，提示只在第一次使用应用程序时出现。要撤销访问权限，在“设置”中修改以下内容：
- 进入设置->隐私->相机→应用程序，并关闭相机的访问
- 进入设置->隐私→用户移动→应用程序，关闭imu的访问。

## 设置
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307183734.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307183734.png)

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307183811.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210307183811.png)

### 要求清单条目
例子请看：https://github.com/microsoft/HoloLens2ForCV/blob/main/Samples/SensorVisualization/SensorVisualization/Package.appxmanifest

```xml
<Capabilities> 
    <Capability Name="internetClient" /> 
    <uap:Capability Name="documentsLibrary" /> 
    <rescap:Capability Name="perceptionSensorsExperimental" /> 
    <DeviceCapability Name="webcam" /> 
    <DeviceCapability Name="wifiControl" /> 
    <DeviceCapability Name="backgroundSpatialPerception" /> 
</Capabilities> 
```

## API参考
### 设备接口
```c++
DECLARE_INTERFACE_IID_(IResearchModeSensorDevice, IUnknown, "65E8CC3C-3A03-4006-AE0D-
34E1150058CC") 
{ 
    STDMETHOD(DisableEyeSelection()) = 0; 
    STDMETHOD(EnableEyeSelection()) = 0; 
 
    STDMETHOD(GetSensorCount( 
        _Out_ size_t *pOutCount)) = 0; 
    STDMETHOD(GetSensorDescriptors( 
        _Out_writes_(sensorCount) ResearchModeSensorDescriptor *pSensorDescriptorData, 
        size_t sensorCount, 
        _Out_ size_t *pOutCount)) = 0; 
    STDMETHOD(GetSensor( 
        ResearchModeSensorType sensorType, 
        _Outptr_result_nullonfailure_ IResearchModeSensor **ppSensor)) = 0; 
}; 
 
DECLARE_INTERFACE_IID_(IResearchModeSensorDevicePerception, IUnknown, "C1678F4B-ECB4-
47A8-B6FA-97DBF4417DB2") 
{ 
    STDMETHOD(GetRigNodeId( 
        _Outptr_ GUID *pRigNodeId)) = 0; 
}; 
 
DECLARE_INTERFACE_IID_(IResearchModeSensorDeviceConsent, IUnknown, "EAB9D672-9A88-4E43-
8A69-9BA8f23A4C76") 
{ 
    STDMETHOD_(HRESULT, RequestCamAccessAsync)(void  
        (*camCallback)(ResearchModeSensorConsent))= 0; 
    STDMETHOD_(HRESULT, RequestIMUAccessAsync)(void  
        (*imuCallback)(ResearchModeSensorConsent)) = 0; 
};
```

### 传感器接口
```c++
DECLARE_INTERFACE_IID_(IResearchModeSensor, IUnknown, "4D4D1D4B-9FDD-4001-BA1E-
F8FAB1DA14D0") 
{ 
    STDMETHOD(OpenStream()) = 0; 
    STDMETHOD(CloseStream()) = 0; 
    STDMETHOD_(LPCWSTR, GetFriendlyName)() = 0; 
    STDMETHOD_(ResearchModeSensorType, GetSensorType)() = 0; 
 
    STDMETHOD(GetSampleBufferSize( 
        _Out_ size_t *pSampleBufferSize)) = 0; 
    STDMETHOD(GetNextBuffer( 
        _Outptr_result_nullonfailure_ IResearchModeSensorFrame **ppSensorFrame)) = 0; 
}; 
 
DECLARE_INTERFACE_IID_(IResearchModeCameraSensor, IUnknown, "3BDB4977-960B-4F5D-8CA3-
D21E68F26E76") 
{ 
    STDMETHOD(MapImagePointToCameraUnitPlane( 
        float (&uv) [2], 
        float (&xy) [2])) = 0; 
    STDMETHOD(MapCameraSpaceToImagePoint( 
        float(&xy)[2], 
        float(&uv)[2])) = 0; 
    STDMETHOD(GetCameraExtrinsicsMatrix(DirectX::XMFLOAT4X4 *pCameraViewMatrix)) = 0; 
}; 
 
DECLARE_INTERFACE_IID_(IResearchModeAccelSensor, IUnknown, "627A7FAA-55EA-4951-B370-
26186395AAB5") 
{ 
    STDMETHOD(GetExtrinsicsMatrix(DirectX::XMFLOAT4X4 *pAccel)) = 0; 
}; 
 
DECLARE_INTERFACE_IID_(IResearchModeGyroSensor, IUnknown, "E6E8B36F-E6E7-494C-B4A8-
7CFA2561BEE7") 
{ 
    STDMETHOD(GetExtrinsicsMatrix(DirectX::XMFLOAT4X4 *pGyro)) = 0; 
}; 
```

### 传感器帧
```c++
DECLARE_INTERFACE_IID_(IResearchModeSensorVLCFrame, IUnknown, "5C693123-3851-4FDC-A2D9-
51C68AF53976") 
{ 
    STDMETHOD(GetBuffer( 
        _Outptr_ const BYTE **ppBytes, 
        _Out_ size_t *pBufferOutLength)) = 0; 
    STDMETHOD(GetGain( 
        _Out_ UINT32 *pGain)) = 0; 
    STDMETHOD(GetExposure( 
        _Out_ UINT64 *pExposure)) = 0; 
}; 
 
DECLARE_INTERFACE_IID_(IResearchModeSensorDepthFrame, IUnknown, "35167E38-E020-43D9-898E-
6CB917AD86D3") 
{ 
    STDMETHOD(GetBuffer( 
        _Outptr_ const UINT16 **ppBytes, 
        _Out_ size_t *pBufferOutLength)) = 0; 
    STDMETHOD(GetAbDepthBuffer( 
        _Outptr_ const UINT16 **ppBytes, 
        _Out_ size_t *pBufferOutLength)) = 0; 
    STDMETHOD(GetSigmaBuffer( 
        _Outptr_ const BYTE **ppBytes, 
        _Out_ size_t *pBufferOutLength)) = 0; 
}; 
 
DECLARE_INTERFACE_IID_(IResearchModeAccelFrame, IUnknown, "42AA75F8-E3FE-4C25-88C6-
F2ECE1E8A2C5") 
{ 
    STDMETHOD(GetCalibratedAccelaration( 
        _Out_ DirectX::XMFLOAT3 *pAccel)) = 0; 
    STDMETHOD(GetCalibratedAccelarationSamples( 
        _Outptr_ const AccelDataStruct **ppAccelBuffer, 
        _Out_ size_t *pBufferOutLength)) = 0; 
}; 
 
DECLARE_INTERFACE_IID_(IResearchModeGyroFrame, IUnknown, "4C0C5EE7-CBB8-4A15-A81F-
943785F524A6") 
{ 
    STDMETHOD(GetCalibratedGyro( 
        _Out_ DirectX::XMFLOAT3 *pGyro)) = 0; 
    STDMETHOD(GetCalibratedGyroSamples( 
        _Outptr_ const GyroDataStruct **ppAccelBuffer, 
        _Out_ size_t *pBufferOutLength)) = 0; 
}; 
 
DECLARE_INTERFACE_IID_(IResearchModeMagFrame, IUnknown, "2376C9D2-7F3D-456E-A39E-
3B7730DDA9E5") 
{ 
    STDMETHOD(GetMagnetometer( 
        _Out_ DirectX::XMFLOAT3 *pMag)) = 0; 
    STDMETHOD(GetMagnetometerSamples( 
        _Outptr_ const MagDataStruct **ppMagBuffer, 
        _Out_ size_t *pBufferOutLength)) = 0; 
}; 
```

### 同意接口
```c++
DECLARE_INTERFACE_IID_(IResearchModeSensorDeviceConsent, IUnknown, "EAB9D672-9A88-4E43-
8A69-9BA8f23A4C76") 
{ 
    STDMETHOD_(HRESULT, RequestCamAccessAsync)(void 
        (*camCallback)(ResearchModeSensorConsent))= 0; 
    STDMETHOD_(HRESULT, RequestIMUAccessAsync)(void  
        (*imuCallback)(ResearchModeSensorConsent)) = 0; 
}; 
```
