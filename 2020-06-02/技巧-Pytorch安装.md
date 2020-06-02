# 技巧-Pytorch安装

1. 进入官网 [https://pytorch.org/](https://pytorch.org/)

2. 找到[安装文档](https://pytorch.org/get-started/locally/)
![安装文档](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200602172656.png)

3. 发现没有自己想要的版本（有的话，直接运行下面的命令就可以了），就自己去[下载页面](https://download.pytorch.org/whl/torch_stable.html)找到自己的版本

4. 我的配置是 python3.6.5 + cuda10 + windows10
![pytorch](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200602173334.png)
![torchvision](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200602173225.png)


5. 下载到本地（速度慢的就开vpn）

6. 本地安装
```bash
pip3 install "C:\Users\Administrator\Desktop\torch-1.2.0-cp36-cp36m-win_amd64.whl"
pip3 install "C:\Users\Administrator\Desktop\torchvision-0.4.0-cp36-cp36m-win_amd64.whl"
```
![安装完成](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200602173841.png)
可以看到本地安装速度是非常快的

7. 测试
```python
import torch
torch.cuda.is_available()
# 打印 true 安装完美成功
```
![测试成功](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200602174340.png)
