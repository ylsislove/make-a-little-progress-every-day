---
title: Win11基于WSL2安装CUDA、cuDNN和TensorRT
date: 2023-02-28 21:22:51
categories:
 - [人工智能, 基础知识]
tags: 
 - win11
 - wsl
 - nvidia
 - cuda
 - cudnn
 - tensorrt
---

- [2023-03-06 更新](#2023-03-06-更新)
- [2023-03-05 更新](#2023-03-05-更新)
- [前言](#前言)
- [TensorRT介绍](#tensorrt介绍)
- [环境配置](#环境配置)
  - [CUDA Driver](#cuda-driver)
    - [检查安装](#检查安装)
  - [安装CUDA](#安装cuda)
  - [安装nvcc](#安装nvcc)
  - [安装cuDNN](#安装cudnn)
    - [安装](#安装)
    - [验证](#验证)
  - [安装TensorRT](#安装tensorrt)
    - [安装](#安装-1)
    - [验证](#验证-1)

## 2023-03-06 更新
:::info
如果有小伙伴看了2023-03-05更新，发现设置环境变量后运行cuda代码在链接过程中仍然会有报错问题啥的，那我这里建议，先别管2023-03-05更新的内容了，还是按照我博客里的安装步骤一步一步往下安装，用`sudo apt install nvidia-cuda-toolkit`命令去安装nvcc，也不需要配置环境变量了。因为博客里的安装步骤是我亲自执行过的，在我的WSL2环境里是一点问题都没有。

如果跟着我的博客步骤走，发现在测试`./mnistCUDNN`时有问题，那就再根据我2023-03-05更新的内容尝试一下。不过这里我觉得可以先别卸载`nvidia-cuda-toolkit`，先去配置环境变量，然后跑代码看有没有问题，没有问题的话那就最好啦，如果还有问题，那就卸载`nvidia-cuda-toolkit`，配置好环境变量，再重启下，然后再跑下代码看看~

目前根据小伙伴的反映，就先记录到这里吧，后面有新情况也会继续更新的~
:::

## 2023-03-05 更新
:::info
有小伙伴反映，按照NVIDIA官网命令安装完CUDA后，nvcc实际上也是被成功安装啦，且nvcc的版本和我们选择CUDA的版本是保持一致的。但如果再运行`sudo apt install nvidia-cuda-toolkit`命令，就会导致nvcc的版本被覆盖为低版本。

比如，我们选择CUDA的版本是11.8，那安装完CUDA后，我们是可以在`/usr/local/cuda/bin`目录下找到nvcc可执行文件的，在那个目录下运行`./nvcc -V`就可以看到版本和CUDA保持一致，也是11.8。所以实际上我们`不需要`再运行`sudo apt install nvidia-cuda-toolkit`命令安装nvcc啦，只需要再安装完CUDA后，配置下环境变量即可，如下

```bash
export CPATH=/usr/local/cuda-11.8/include:$CPATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH
export PATH=/usr/local/cuda-11.8/bin:$PATH
export CUDA_ROOT=/usr/local/cuda-11.8
```

当然，如果你运行了`sudo apt install nvidia-cuda-toolkit`命令，从我博客里记录的图片可以看到nvcc的版本被覆盖为10.1啦，在我的WSL2环境里，10.1的nvcc版本并没有什么问题，后面用`./mnistCUDNN`测试也是成功哒~

但小伙伴测试说会报`CUDA driver version is insufficient for CUDA runtime version`版本不匹配的错误，所以后面的小伙伴可以参考下，先不要运行`sudo apt install nvidia-cuda-toolkit`命令，直接根据NVIDIA官网安装完CUDA，然后配置下环境变量即可~

如果已经用`sudo apt install nvidia-cuda-toolkit`命令安装完了，测试也真报错了，就卸载掉nvidia-cuda-toolkit，然后再配置下环境变量，再测试下看看吧~
:::

## 前言
之前我写了一篇博客：[Win11安装WSL2和Nvidia驱动](https://blog.aayu.today/artificial-intelligence/basic/20221217/)，记录了在WSL2里安装CUDA，当时我选择了第二种安装方式，即用WSL2里的MiniConda去安装的PyTorch和CUDA等相关库，最近在使用中发现了这种方式的不足，即使用`cuda`和`nvcc`等命令时都要切换到conda相关环境下才能使用。比如我之前在`py38`环境下安装的，当我进入终端处于`base`环境下，nvcc命令是不能使用哒

最近也在跟着恩培老师学TensorRT，担忧用MiniConda安装的CUDA等库可能导致TensorRT安装失败，所以这次就试试直接在`base`环境下用上一篇博客的第一种方式安装`cuda`、`cudnn`和`tensorrt`吧~

结果也是很顺利的安装成功啦，便在此记录下来哈哈~

## TensorRT介绍
* NVIDIA® TensorRT™是一个用于高性能深度学习的推理框架，能够在NVIDIA GPU上实现低延迟、高吞吐量的部署
* TensorRT包含用于训练好的模型的优化器，以及用于执行推理的runtime
* 它可以与TensorFlow、PyTorch和MXNet等训练框架相辅相成地工作

## 环境配置
### CUDA Driver
使用CUDA前，要求GPU驱动与`cuda` 的版本要匹配，匹配关系如下：

> 参考：https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#cuda-major-component-versions__table-cuda-toolkit-driver-versions
>

![](https://image.aayu.today/uploads/2023/03/01/202303012238954.png){width="800px"}

安装可以参考我之前的WSL2博客吖：[Win11安装WSL2和Nvidia驱动](https://blog.aayu.today/artificial-intelligence/basic/20221217/)

#### 检查安装
输入`nvidia-smi`命令，查看GPU驱动版本

```bash
(base) aayu@AayuComputer-Pro:~$ nvidia-smi
Tue Feb 28 00:58:02 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.65       Driver Version: 527.56       CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  On   | 00000000:01:00.0  On |                  N/A |
| N/A   40C    P8    13W / 139W |   1668MiB /  6144MiB |      6%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A        23      G   /Xwayland                       N/A      |
+-----------------------------------------------------------------------------+
```

可以看到当前安装的驱动版本是`527.56`，后面的`CUDA Version: 12.0`是指当前驱动支持的最高CUDA版本~

### 安装CUDA
在Nvidia官网选择对应版本：https://developer.nvidia.com/cuda-toolkit-archive

![](https://image.aayu.today/uploads/2023/03/01/202303012249965.png){width="800px"}

比如我选择的是`11.8`版本，选择`Linux`，`x86_64`，`WSL-Ubuntu`，`2.0`，`deb(local)`，如下图

![](https://image.aayu.today/uploads/2023/03/01/202303012249980.png){width="800px"}

安装命令已经给出啦，如下，直接在WSL2终端执行就好~

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb
sudo dpkg -i cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb
sudo cp /var/cuda-repo-wsl-ubuntu-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```

成功安装如下图

![](https://image.aayu.today/uploads/2023/03/01/202303012250963.png){width="800px"}

### 安装nvcc
```bash
sudo apt install nvidia-cuda-toolkit
```

安装完后重启电脑，检查安装结果，成功如下图~

![](https://image.aayu.today/uploads/2023/03/01/202303012251060.png)

### 安装cuDNN
下载安装包：访问：https://developer.nvidia.com/zh-cn/cudnn，选择对应的版本，下载对应的安装包（建议使用Debian包安装）

![](https://image.aayu.today/uploads/2023/03/01/202303012252029.png)

比如我下载的是：[Local Installer for Ubuntu20.04 x86_64 (Deb)](https://developer.nvidia.com/downloads/c118-cudnn-local-repo-ubuntu2004-8708410-1amd64deb)，下载后的文件名为`cudnn-local-repo-ubuntu2004-8.7.0.84_1.0-1_amd64.deb`

#### 安装
> 参考链接：https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html
>

```bash
# 注意，运行下面的命令前，将下面的 X.Y和v8.x.x.x 替换成自己具体的CUDA 和 cuDNN版本，如我的CUDA 版本是11.8，cuDNN 版本是 8.7.0.84

# Enable the local repository.
sudo dpkg -i cudnn-local-repo-${OS}-8.x.x.x_1.0-1_amd64.deb
# 我的：sudo dpkg -i cudnn-local-repo-ubuntu2004-8.7.0.84_1.0-1_amd64.deb

# Import the CUDA GPG key.
sudo cp /var/cudnn-local-repo-*/cudnn-local-*-keyring.gpg /usr/share/keyrings/

# Refresh the repository metadata.
sudo apt-get update

# Install the runtime library.
sudo apt-get install libcudnn8=8.x.x.x-1+cudaX.Y
# 我的：sudo apt-get install libcudnn8=8.7.0.84-1+cuda11.8

# Install the developer library.
sudo apt-get install libcudnn8-dev=8.x.x.x-1+cudaX.Y
# 我的：sudo apt-get install libcudnn8-dev=8.7.0.84-1+cuda11.8

# Install the code samples and the cuDNN library documentation.
sudo apt-get install libcudnn8-samples=8.x.x.x-1+cudaX.Y
# 我的：sudo apt-get install libcudnn8-samples=8.7.0.84-1+cuda11.8
```

#### 验证
```bash
# 复制文件
cp -r /usr/src/cudnn_samples_v8/ $HOME
cd  $HOME/cudnn_samples_v8/mnistCUDNN
make clean && make
./mnistCUDNN
```

> 可能报错：test.c:1:10: fatal error: FreeImage.h: No such file or directory
>
> 解决办法：sudo apt-get install libfreeimage3 libfreeimage-dev
>

成功验证如下图

![](https://image.aayu.today/uploads/2023/03/01/202303012253057.png)

### 安装TensorRT
访问：https://developer.nvidia.com/nvidia-tensorrt-8x-download 下载对应版本的TensorRT

![](https://image.aayu.today/uploads/2023/03/01/202303012254209.png)

比如我选择的是 8.5.3版本，下载完文件名为：`nv-tensorrt-local-repo-ubuntu2004-8.5.3-cuda-11.8_1.0-1_amd64.deb`

#### 安装
> 参考地址：https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html#installing-debian
>

```bash
# 替换成自己的OS和版本信息
os="ubuntuxx04"
tag="8.x.x-cuda-x.x"
sudo dpkg -i nv-tensorrt-local-repo-${os}-${tag}_1.0-1_amd64.deb
# 我的：sudo dpkg -i nv-tensorrt-local-repo-ubuntu2004-8.5.3-cuda-11.8_1.0-1_amd64.deb

sudo cp /var/nv-tensorrt-local-repo-${os}-${tag}/*-keyring.gpg /usr/share/keyrings/
# 我的：sudo cp /var/nv-tensorrt-local-repo-ubuntu2004-8.5.3-cuda-11.8/*-keyring.gpg /usr/share/keyrings/

sudo apt-get update
sudo apt-get install tensorrt
```

#### 验证
输入`dpkg -l | grep TensorRT`

```bash
(base) aayu@HPSCIL:~/tensorrt_install$ dpkg -l | grep TensorRT
ii  libnvinfer-bin                                    8.5.3-1+cuda11.8                  amd64        TensorRT binaries
ii  libnvinfer-dev                                    8.5.3-1+cuda11.8                  amd64        TensorRT development libraries and headers
ii  libnvinfer-plugin-dev                             8.5.3-1+cuda11.8                  amd64        TensorRT plugin libraries
ii  libnvinfer-plugin8                                8.5.3-1+cuda11.8                  amd64        TensorRT plugin libraries
ii  libnvinfer-samples                                8.5.3-1+cuda11.8                  all          TensorRT samples
ii  libnvinfer8                                       8.5.3-1+cuda11.8                  amd64        TensorRT runtime libraries
ii  libnvonnxparsers-dev                              8.5.3-1+cuda11.8                  amd64        TensorRT ONNX libraries
ii  libnvonnxparsers8                                 8.5.3-1+cuda11.8                  amd64        TensorRT ONNX libraries
ii  libnvparsers-dev                                  8.5.3-1+cuda11.8                  amd64        TensorRT parsers libraries
ii  libnvparsers8                                     8.5.3-1+cuda11.8                  amd64        TensorRT parsers libraries
ii  tensorrt                                          8.5.3.1-1+cuda11.8                amd64        Meta package for TensorRT
```

> 如果遇到`unmet dependencies`的问题, 一般是cuda cudnn没有安装好。TensorRT的`INCLUDE` 路径是 `/usr/include/x86_64-linux-gnu/`, `LIB`路径是`/usr/lib/x86_64-linux-gnu/`,Sample code在`/usr/src/tensorrt/samples`, `trtexec`在`/usr/src/tensorrt/bin`下。
>

![](https://image.aayu.today/uploads/2023/03/01/202303012254945.png)
