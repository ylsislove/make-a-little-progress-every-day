# 技巧-Ubuntu开发环境配置

## 环境
* 腾讯云轻量应用服务器 Ubuntu 18.04.1 LTS
* CPU: 1核 内存: 1GB
* 系统盘：25GB
* 峰值带宽 30Mbps，流量包 1024GB/月

## 设置一些常用的命令别名
清屏的命令是 `clear`，我比较喜欢用 `cls`，所以就可以设置别名来简化操作
```bash
# 查看已经设置的别名列表
alias -p
# 设置 cls 为 clear 的别名
alias cls='clear'
```

alias命令只作用于当次登入的操作。如果想每次登入都能使用这些命令的别名，则可以把相应的alias命令存放在 `~/.bashrc` 文件中。

打开 `~/.bashrc` 文件，输入要设置的 alias 命令，保存，然后运行 `source ~/.bashrc`。

如果 `~/.bashrc` 文件有导入 `.bash_aliases` 的命令，我们也可以将自定义别名设置在 `~/.bash_aliases` 文件中，方便管理。
```bash
# 检查 ~ 目录下有没有 .bash_aliases 文件
ls -al ~/
# 没有的话创建 .bash_aliases 文件
cd ~
touch .bash_aliases
# 将 alias cls='clear' 写入刚创建的文件中，<Esc>:wq 保存退出
vim .bash_aliases
# 重新加载配置文件
source ~/.bashrc
```

## 配置 SSH 命令每次登录无需输入密码
参考我之前的博客：[SSH、SCP命令相关知识点](https://ylsislove.github.io/2020/06/09/WG7DRX.html)

## 解决 SSH 超时无输入自动断开连接的问题
修改 `/etc/ssh/sshd_config`
```bash
# server每隔60秒发送一次请求给client，然后client响应，从而保持连接
ClientAliveInterval 60
# server发出请求后，客户端没有响应得次数达到3，就自动断开连接，正常情况下，client不会不响应
ClientAliveCountMax 3 
```

然后重启服务：`sudo systemctl restart sshd`

## 关闭 Linux 终端发出的烦人提示音
`sudo vim /etc/inputrc` 找到 `set bell-style none` 将前面的 ＃ 去掉，之后重启系统即可解决声音问题。

## 配置 Vim
> 我的个人 vim 配置仓库：[https://github.com/ylsislove/my-vim-config/tree/master](https://github.com/ylsislove/my-vim-config/tree/master)

1. 克隆本仓库
```bash
cd ~
git clone https://github.com/ylsislove/my-vim-config.git
```

2. 创建软链接
```bash
ln -s ~/my-vim-config/.vim ~/.vim
ln -s ~/my-vim-config/.vimrc ~/.vimrc
```

3. 下载vundle
```
cd .vim/
mkdir bundle
git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
```

4. 通过vundle安装插件
```
vim
:PluginInstall
```

刚启动 vim 时因为插件还没有安装，所以会报一些警告，这是正常的，完全不用担心，直接回车回车进入 vim 里，用 :PluginInstall 安装完以后就没问题啦，好看的 vim 如下图
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210703132913.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210703132913.png)

我设置的一些常用快捷键如下：
* `空格 + q`：关闭当前窗口，等价于 `:q`
* `空格 + 空格`：保存当前修改，等价于 `:w`
* `空格 + h`：将光标移动到左侧窗口
* `空格 + j`：将光标移动到下侧窗口
* `空格 + k`：将光标移动到上侧窗口
* `空格 + l`：将光标移动到左侧窗口。可以在左侧导航栏窗口输入 `?` 查看更多关于窗口操作的命令
* `F3`：`关闭/打开` 左侧导航栏窗口

更多操作可以查看 `.vimrc` 文件

## 配置 NodeJS
```bash
# 更新
sudo apt-get update
sudo apt-get upgrade

# 安装
sudo apt install nodejs
sudo apt install npm
# 安装n模块
sudo npm install -g n
# 升级 nodejs 到最新 stable 版本
sudo n stable
# 升级最新npm
sudo npm install npm@latest -g

# 查看版本
node --version
npm --version
# 设置淘宝镜像源
npm config set registry https://registry.npm.taobao.org
# 查看
npm config ls -l

# 全局安装 forever
sudo npm i forever -g
```

## 配置 Python
```bash
# 更新 pip
python3 -m pip install --upgrade pip

# 安装常用开发软件包
python3 -m pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple

# 根据警告把 /home/ubuntu/.local/bin 路径添加进环境变量
sudo vim /etc/profile
export PATH=$PATH:/home/ubuntu/.local/bin
# 重新载入
source /etc/profile

# 继续安装常用开发软件包
python3 -m pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
python3 -m pip install opencv-contrib-python -i https://pypi.tuna.tsinghua.edu.cn/simple
python3 -m pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```

如果 `import cv2` 报 `Segmentation fault (core dumped)` 错的话，运行 `sudo apt install python3-opencv` 应该能解决。

## 配置 Nginx
```bash
# 安装
sudo apt update
sudo apt install nginx

# 查看版本
nginx -v
```

常用命令：
* 启动 Nginx 服务：sudo systemctl start nginx
* 停止 Nginx 服务：sudo systemctl stop nginx
* 重启 Nginx 服务：sudo systemctl restart nginx
* 在进行一些配置更改后重新加载 Nginx 服务：sudo systemctl reload nginx
* 开启自启：sudo systemctl enable nginx
* 关闭开启：sudo systemctl disable nginx
* 检查状态：sudo systemctl status nginx

在 `/etc/nginx/sites-available/default` 文件中配置 server，在 `/etc/nginx/nginx.conf` 文件中配置 `user root;`
