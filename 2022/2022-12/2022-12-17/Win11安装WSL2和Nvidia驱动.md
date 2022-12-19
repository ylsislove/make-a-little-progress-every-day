---
title: Win11安装WSL2和Nvidia驱动
date: 2022-12-17 21:09:51
categories:
 - [人工智能, 基础知识]
tags: 
 - win11
 - wsl
 - nvidia
---
## 前言
以前捣鼓过wsl，即Windows下的Linux子系统，但兼容性依然比不过原生的Linux系统，使用cmake等命令会出现奇怪的问题。

最近听说wsl2出来了，而且也可以在wsl上安装nvidia显卡驱动了，有网友实测跑深度学习模型速度能比Windows的快一倍左右，哈哈这就必须得捣鼓捣鼓了，如果兼容性真的没问题的话，那可比虚拟机或双系统要爽多了~

目前还发现，微软官网对wsl的使用教程也写的非常友好，推荐大家多看看官方教程，毕竟时效性可以保证~~

微软wsl官方教程：https://learn.microsoft.com/zh-cn/windows/wsl/install

:::info
wsl安装过程中可能需要科学上网，推荐大家去「 [一元机场](https://xn--4gq62f52gdss.com/#/register?code=DydJBuvW) 」平台订阅，每月500G流量月均0.9元，性价比拉满~
:::

## 系统环境
* CPU：i5-12450
* 内存：32G
* 显卡：3060
* Windows版本：Windows11 22H2 22621.963

:::warning
本篇教程后面涉及到WSL2上的GPU加速，经网上帖子的建议，用最新的win11系统可以保证最大的成功率。如果是win10系统，需将win10升级为预览体验版本，建议谨慎折腾！

没特殊需求的，都建议将系统升级为win11再进行尝试。
:::

## WSL 1和WSL 2功能对比
![](https://image.aayu.today/uploads/2022/12/17/202212172118749.png){width="800px"}

从对比图中可以看到，除非对跨OS的文件系统性能有要求，WSL 2是全面优于WSL 1的。官方文档也建议使用VSCode对WSL中的文件进行访问和操作，所以WSL 2搭配VSCode应该是非常棒的组合~

![](https://image.aayu.today/uploads/2022/12/17/202212172122761.png){width="800px"}

## 安装WSL2
:::info
管理员模式下打开 PowerShell 或 Windows 命令提示符
:::
查看可用发行版本列表
```bash
wsl --list --online
```
可以看到有`Ubuntu-20.04`这个发行版本，正是我们需要的~

安装`Ubuntu-20.04`发行版
```bash
wsl --install -d Ubuntu-20.04
```

这里默认安装的就是wsl2，如果对wsl1有需求，可以查阅官方文档哦，有很详尽的介绍~

安装大概花费5\~10分钟左右，视电脑配置和网络状况，耐心等待即可~

提示安装成功后，重启电脑即可完成安装。重启后会默认弹出Linux powershell，设置完用户名和密码，安装正式完成，如下图~

![](https://image.aayu.today/uploads/2022/12/17/202212172134452.png){width="800px"}

## 更新和升级包
```bash
sudo apt update && sudo apt upgrade
```

## 配置VSCode
在VSCode中安装「 Remote Development 」扩展。除了远程 - SSH 和开发容器扩展，此扩展包还包括 WSL 扩展，使你能够在容器、远程计算机上或 WSL 中打开任何文件夹。

可以通过在WSL2命令行中输入`code .`就可以直接用VSCode打开Linux中的文件夹进行开发了~

## 配置GPU加速
### 安装Nvidia驱动
下载并安装 NVIDIA GPU 的最新驱动程序：https://www.nvidia.com/Download/index.aspx

我的笔记本是3060，所以可以按如下配置搜索

搜索出来后点击下载即可，可以看到驱动版本目前最新是527.56

![](https://image.aayu.today/uploads/2022/12/18/202212180051600.png)
![](https://image.aayu.today/uploads/2022/12/18/202212180059301.png)
{.gallery  data-height="240"}

:::warning
这是您需要安装的唯一驱动程序。不要在 WSL 中安装任何 Linux 显卡驱动程序。
详情参阅Nvidia官方说明：[WSL 2 上的 CUDA 入门](https://docs.nvidia.cn/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl-2)

再次强调，不要在WSL中安装任何Linux版的Nvidia驱动！
:::

下载完驱动后就可以安装了，我直接选择默认的`NVIDIA 显卡驱动和 GeForce Experience`选项，安装选项为`精简`，安装完成后重启下电脑即可~

打开powershell，输入`nvidia-smi`，可以看到Windows下已经正常输出显卡驱动信息了

输入`wsl`，可以进入Linux命令行，再次输入`nvidia-smi`，可以看到Linux环境下，也输出了显卡驱动信息，大功告成~

![](https://image.aayu.today/uploads/2022/12/18/202212181857151.png)
![](https://image.aayu.today/uploads/2022/12/18/202212181857604.png)
{.gallery  data-height="280"}

:::info
如果在wsl2命令行中输入`nvidia-smi`发现没有正常输出，而是报错，首先要检查的就是你的Windows版本是不是太低了，还是建议升级到最新的win11系统再进行折腾

因为有[网友已经实践](https://blog.csdn.net/iwanvan/article/details/122119595)，升级到win11后啥都不用做，直接就把wsl2链接到GPU了

所以看到报错先检查Windows版本，千万不要在WSL中安装任何Linux版的Nvidia驱动！不需要的！
:::

### 安装Cuda Toolkit
接下来就有两种方式了：

一个是按Nvidia官方说明：[WSL 2 上的 CUDA 入门](https://docs.nvidia.cn/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl-2)上的，在[CUDA Toolkit](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_network)下载界面选择适合WSL的CUDA Toolkit进行安装，如下图所示

![](https://image.aayu.today/uploads/2022/12/18/202212182152370.png){width="800px"}

另一种是根据网友的评论，可以依赖于conda和pytorch直接安装gpu版本的pytorch，安装成功后cuda也是可以直接用了。pytorch官方给出的安装命令如下图，可以看到其中也包含了cuda 11.7

![](https://image.aayu.today/uploads/2022/12/19/202212191544772.png)
![](https://image.aayu.today/uploads/2022/12/18/202212182203319.png)
{.gallery  data-height="280"}

:::warning
这两种的区别，据有网友说第二种方式安装的CUDA Toolkit貌似只适用于Pytorch，所以如果想将CUDA Toolkit和C\++搭配使用的话，还是得要用第一种方式安装一次CUDA Toolkit

但经博主亲自实践，用conda安装的cuda，也是可以直接和C++搭配使用的！
:::

所以接下来的内容就是，用第二种方式安装pytorch的gpu版本，即可将cuda安装好。然后编写一个c++脚本测试一下，都没问题的话，即WSL2的GPU加速配置大功告成~

:::info
本节教程和[微软wsl官方教程](https://learn.microsoft.com/zh-cn/windows/wsl/install)中的GPU加速配置有区别，好像是官方教程里好像设置了Docker什么的，我目前好像还用不到这么深，所以就没参考微软wsl的官方教程
:::

#### 通过PyTorch安装CUDA Toolkit
界面截图如上图所示，PyTorch直接给出了安装命令，如下
```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
```

因此，我们直接在Linux的命令行中，切换到我们自己创建的python虚拟环境，运行以上命令进行安装，以下是conda给出安装前的输出信息，可以看到里面就包含了CUDA Toolkit
```bash
## Package Plan ##

  environment location: /home/aayu/miniconda3/envs/py38

  added / updated specs:
    - pytorch
    - pytorch-cuda=11.7
    - torchaudio
    - torchvision


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    cuda-11.7.1                |                0           1 KB  nvidia
    cuda-cccl-11.7.91          |                0         1.2 MB  nvidia
    cuda-command-line-tools-11.7.1|                0           1 KB  nvidia
    cuda-compiler-11.7.1       |                0           1 KB  nvidia
    cuda-cudart-11.7.99        |                0         194 KB  nvidia
    cuda-cudart-dev-11.7.99    |                0         1.1 MB  nvidia
    cuda-cuobjdump-11.7.91     |                0         158 KB  nvidia
    cuda-cupti-11.7.101        |                0        22.9 MB  nvidia
    cuda-cuxxfilt-11.7.91      |                0         293 KB  nvidia
    cuda-demo-suite-12.0.76    |                0         5.0 MB  nvidia
    cuda-documentation-12.0.76 |                0          89 KB  nvidia
    cuda-driver-dev-11.7.99    |                0          16 KB  nvidia
    cuda-gdb-12.0.90           |                0         5.3 MB  nvidia
    cuda-libraries-11.7.1      |                0           1 KB  nvidia
    cuda-libraries-dev-11.7.1  |                0           2 KB  nvidia
    cuda-memcheck-11.8.86      |                0         168 KB  nvidia
    cuda-nsight-12.0.78        |                0       113.6 MB  nvidia
    cuda-nsight-compute-12.0.0 |                0           1 KB  nvidia
    cuda-nvcc-11.7.99          |                0        42.7 MB  nvidia
    cuda-nvdisasm-12.0.76      |                0        47.9 MB  nvidia
    cuda-nvml-dev-11.7.91      |                0          80 KB  nvidia
    cuda-nvprof-12.0.90        |                0         4.3 MB  nvidia
    cuda-nvprune-11.7.91       |                0          64 KB  nvidia
    cuda-nvrtc-11.7.99         |                0        17.3 MB  nvidia
    cuda-nvrtc-dev-11.7.99     |                0        16.9 MB  nvidia
    cuda-nvtx-11.7.91          |                0          57 KB  nvidia
    cuda-nvvp-12.0.90          |                0       114.3 MB  nvidia
    cuda-runtime-11.7.1        |                0           1 KB  nvidia
    cuda-sanitizer-api-12.0.90 |                0        16.6 MB  nvidia
    cuda-toolkit-11.7.1        |                0           1 KB  nvidia
    cuda-tools-11.7.1          |                0           1 KB  nvidia
    cuda-visual-tools-11.7.1   |                0           1 KB  nvidia
    cudatoolkit-10.1.243       |       h036e899_8       427.4 MB  nvidia
    gds-tools-1.5.0.59         |                0        40.9 MB  nvidia
    intel-openmp-2022.1.0      |    h9e868ea_3769         4.5 MB
    lcms2-2.12                 |       h3be6417_0         312 KB
    libcublas-11.10.3.66       |                0       286.1 MB  nvidia
    libcublas-dev-11.10.3.66   |                0       296.4 MB  nvidia
    libcufft-10.7.2.124        |       h4fbf590_0        93.6 MB  nvidia
    libcufft-dev-10.7.2.124    |       h98a8f43_0       197.3 MB  nvidia
    libcufile-1.5.0.59         |                0         754 KB  nvidia
    libcufile-dev-1.5.0.59     |                0          13 KB  nvidia
    libcurand-10.3.1.50        |                0        51.7 MB  nvidia
    libcurand-dev-10.3.1.50    |                0         449 KB  nvidia
    libcusolver-11.4.0.1       |                0        78.7 MB  nvidia
    libcusolver-dev-11.4.0.1   |                0        55.9 MB  nvidia
    libcusparse-11.7.4.91      |                0       151.1 MB  nvidia
    libcusparse-dev-11.7.4.91  |                0       309.5 MB  nvidia
    libnpp-11.7.4.75           |                0       129.3 MB  nvidia
    libnpp-dev-11.7.4.75       |                0       126.6 MB  nvidia
    libnvjpeg-11.8.0.2         |                0         2.2 MB  nvidia
    libnvjpeg-dev-11.8.0.2     |                0         1.9 MB  nvidia
    mkl-2022.1.0               |     hc2b9512_224       129.7 MB
    ninja-1.10.2               |       h06a4308_5           8 KB
    ninja-base-1.10.2          |       hd09550d_5         109 KB
    nsight-compute-2022.4.0.15 |                0       764.0 MB  nvidia
    pillow-9.2.0               |   py38hace64e9_1         666 KB
    pytorch-1.4.0              |py3.8_cuda10.1.243_cudnn7.6.3_0       433.1 MB  pytorch
    pytorch-cuda-11.7          |       h67b0de4_1           3 KB  pytorch
    torchaudio-0.4.0           |             py38         6.1 MB  pytorch
    torchvision-0.5.0          |       py38_cu101         9.1 MB  pytorch
    ------------------------------------------------------------
                                           Total:        3.91 GB

The following NEW packages will be INSTALLED:

  cuda               nvidia/linux-64::cuda-11.7.1-0
  cuda-cccl          nvidia/linux-64::cuda-cccl-11.7.91-0
  cuda-command-line~ nvidia/linux-64::cuda-command-line-tools-11.7.1-0
  cuda-compiler      nvidia/linux-64::cuda-compiler-11.7.1-0
  cuda-cudart        nvidia/linux-64::cuda-cudart-11.7.99-0
  cuda-cudart-dev    nvidia/linux-64::cuda-cudart-dev-11.7.99-0
  cuda-cuobjdump     nvidia/linux-64::cuda-cuobjdump-11.7.91-0
  cuda-cupti         nvidia/linux-64::cuda-cupti-11.7.101-0
  cuda-cuxxfilt      nvidia/linux-64::cuda-cuxxfilt-11.7.91-0
  cuda-demo-suite    nvidia/linux-64::cuda-demo-suite-12.0.76-0
  cuda-documentation nvidia/linux-64::cuda-documentation-12.0.76-0
  cuda-driver-dev    nvidia/linux-64::cuda-driver-dev-11.7.99-0
  cuda-gdb           nvidia/linux-64::cuda-gdb-12.0.90-0
  cuda-libraries     nvidia/linux-64::cuda-libraries-11.7.1-0
  cuda-libraries-dev nvidia/linux-64::cuda-libraries-dev-11.7.1-0
  cuda-memcheck      nvidia/linux-64::cuda-memcheck-11.8.86-0
  cuda-nsight        nvidia/linux-64::cuda-nsight-12.0.78-0
  cuda-nsight-compu~ nvidia/linux-64::cuda-nsight-compute-12.0.0-0
  cuda-nvcc          nvidia/linux-64::cuda-nvcc-11.7.99-0
  cuda-nvdisasm      nvidia/linux-64::cuda-nvdisasm-12.0.76-0
  cuda-nvml-dev      nvidia/linux-64::cuda-nvml-dev-11.7.91-0
  cuda-nvprof        nvidia/linux-64::cuda-nvprof-12.0.90-0
  cuda-nvprune       nvidia/linux-64::cuda-nvprune-11.7.91-0
  cuda-nvrtc         nvidia/linux-64::cuda-nvrtc-11.7.99-0
  cuda-nvrtc-dev     nvidia/linux-64::cuda-nvrtc-dev-11.7.99-0
  cuda-nvtx          nvidia/linux-64::cuda-nvtx-11.7.91-0
  cuda-nvvp          nvidia/linux-64::cuda-nvvp-12.0.90-0
  cuda-runtime       nvidia/linux-64::cuda-runtime-11.7.1-0
  cuda-sanitizer-api nvidia/linux-64::cuda-sanitizer-api-12.0.90-0
  cuda-toolkit       nvidia/linux-64::cuda-toolkit-11.7.1-0
  cuda-tools         nvidia/linux-64::cuda-tools-11.7.1-0
  cuda-visual-tools  nvidia/linux-64::cuda-visual-tools-11.7.1-0
  cudatoolkit        nvidia/linux-64::cudatoolkit-10.1.243-h036e899_8
  gds-tools          nvidia/linux-64::gds-tools-1.5.0.59-0
  intel-openmp       pkgs/main/linux-64::intel-openmp-2022.1.0-h9e868ea_3769
  lcms2              pkgs/main/linux-64::lcms2-2.12-h3be6417_0
  libcublas          nvidia/linux-64::libcublas-11.10.3.66-0
  libcublas-dev      nvidia/linux-64::libcublas-dev-11.10.3.66-0
  libcufft           nvidia/linux-64::libcufft-10.7.2.124-h4fbf590_0
  libcufft-dev       nvidia/linux-64::libcufft-dev-10.7.2.124-h98a8f43_0
  libcufile          nvidia/linux-64::libcufile-1.5.0.59-0
  libcufile-dev      nvidia/linux-64::libcufile-dev-1.5.0.59-0
  libcurand          nvidia/linux-64::libcurand-10.3.1.50-0
  libcurand-dev      nvidia/linux-64::libcurand-dev-10.3.1.50-0
  libcusolver        nvidia/linux-64::libcusolver-11.4.0.1-0
  libcusolver-dev    nvidia/linux-64::libcusolver-dev-11.4.0.1-0
  libcusparse        nvidia/linux-64::libcusparse-11.7.4.91-0
  libcusparse-dev    nvidia/linux-64::libcusparse-dev-11.7.4.91-0
  libnpp             nvidia/linux-64::libnpp-11.7.4.75-0
  libnpp-dev         nvidia/linux-64::libnpp-dev-11.7.4.75-0
  libnvjpeg          nvidia/linux-64::libnvjpeg-11.8.0.2-0
  libnvjpeg-dev      nvidia/linux-64::libnvjpeg-dev-11.8.0.2-0
  mkl                pkgs/main/linux-64::mkl-2022.1.0-hc2b9512_224
  ninja              pkgs/main/linux-64::ninja-1.10.2-h06a4308_5
  ninja-base         pkgs/main/linux-64::ninja-base-1.10.2-hd09550d_5
  nsight-compute     nvidia/linux-64::nsight-compute-2022.4.0.15-0
  pillow             pkgs/main/linux-64::pillow-9.2.0-py38hace64e9_1
  pytorch            pytorch/linux-64::pytorch-1.4.0-py3.8_cuda10.1.243_cudnn7.6.3_0
  pytorch-cuda       pytorch/noarch::pytorch-cuda-11.7-h67b0de4_1
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_1
  torchaudio         pytorch/linux-64::torchaudio-0.4.0-py38
  torchvision        pytorch/linux-64::torchvision-0.5.0-py38_cu101
```

贴一张安装过程中的截图哈哈

安装成功！用`nvcc -V`命令测试一下是否能正常输出，成功输出，如下图

![](https://image.aayu.today/uploads/2022/12/18/202212182247894.png)
![](https://image.aayu.today/uploads/2022/12/18/202212182327537.png)
{.gallery  data-height="280"}

导入Pytorch测试一下，正确链接到GPU，并识别出显卡

![](https://image.aayu.today/uploads/2022/12/19/202212190031485.png){width="800px"}

### 测试Nvcc
编写一个cuda脚本
```cpp cuda_test_1.cu
#include "cuda_runtime.h"
#include <stdlib.h>
#include <assert.h>
#include <iostream>

// Device code
__global__ void VecAdd(float* A, float* B, float* C)
{
    int i = threadIdx.x;
    C[i] = A[i] + B[i];
}

// Host code
int main()
{
    int N = 1024;
    size_t size = N * sizeof(float);

    // Allocate input vectors h_A and h_B in host memory
    float* h_A = (float*)malloc(size);
    float* h_B = (float*)malloc(size);
    float* h_C = (float*)malloc(size);

    // Initialize input vectors
    for (size_t i = 0; i < N; i++)
    {
        h_A[i] = 1.;
        h_B[i] = 2.;
    }

    // Allocate vectors in device memory
    float* d_A;
    cudaMalloc(&d_A, size);
    float* d_B;
    cudaMalloc(&d_B, size);
    float* d_C;
    cudaMalloc(&d_C, size);

    // Copy vectors from host memory to device memory
    cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);

    // Kernel invocation with N threads
    VecAdd<<<1, N>>>(d_A, d_B, d_C);

    // Copy result from device memory to host memory
    // h_C contains the result in host memory
    cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
    for (size_t i = 0; i < N; i++){
        assert(h_C[i] == 3.);
    }
    std::cout << "\t\t\t\tDONE!" << std::endl;

    // Free device memory
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    // Free host memory
    free(h_A);
    free(h_B);
    free(h_C);

    return 0;
}
```

然后在刚刚安装了cuda的python环境下用以下命令编译
```bash
nvcc cuda_test_1.cu -o cuda_test_1
```

编译成功后用`./cuda_test_1`运行，成功运行如下图

![](https://image.aayu.today/uploads/2022/12/19/202212191538223.png){width="800px"}

大功告成！

## 参考链接
* [Windows10/11 WSL2 安装nvidia-cuda驱动](https://www.bilibili.com/read/cv14608547)
* [Windows 11/10 WSL2 Ubuntu 20.04 下配置Cuda及Pytorch](https://blog.csdn.net/iwanvan/article/details/122119595)
* [【PyTorch】B站首个，终于有人把 GPU/ CUDA/ cuDNN 讲清楚了](https://www.bilibili.com/video/BV15Q4y1i7Bp/?p=2)
* [【资源记录】各个历史版本 cuda toolkit 下载链接](https://blog.csdn.net/gtf215998315/article/details/105359743)
