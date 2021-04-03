# 技巧-CentOS开发环境配置

## 环境
* CentOS 8.0 64位
* 2核 4GB

## git
```bash
# 更新
yum update
# 安装
yum install git
# 查看
git version
```

## python配置
```bash
# 更新
yum install
# 安装必要的共享库，参考链接：https://blog.csdn.net/agonysome/article/details/108985079
yum install mesa-libGL.x86_64

# 更新 pip
python3 -m pip install --upgrade pip

# 安装常用开发软件包
python3 -m pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
python3 -m pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
python3 -m pip install opencv-contrib-python -i https://pypi.tuna.tsinghua.edu.cn/simple
python3 -m pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```
