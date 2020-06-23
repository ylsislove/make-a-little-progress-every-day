# 技巧-VSCode浏览器开发环境部署

  - [环境](#%E7%8E%AF%E5%A2%83)
  - [安装 Docker](#%E5%AE%89%E8%A3%85-docker)
  - [安装 code-server](#%E5%AE%89%E8%A3%85-code-server)
  - [构建 code-server 代码运行环境](#%E6%9E%84%E5%BB%BA-code-server-%E4%BB%A3%E7%A0%81%E8%BF%90%E8%A1%8C%E7%8E%AF%E5%A2%83)

自从年初重装系统，弃用笨重的 PyCharm 改用 VSCode 后，对 VSCode 就越来越喜欢了。目前我主要使用的编程语言 JS 和 Python，在 VSCode 中用起来是如鱼得水般自在嘻嘻。除此之外，VSCode 对 Markdown 天然的支持，让我爱上了记录生活的感觉哈哈。还有一点最最兴奋的是，VSCode 广大的开发者们将 Drawio 作为插件集成到了 VSCode，知道这意味着什么吗，如果我在编写 Markdown 时想顺带绘制一些好看的流程图，可以直接创建 xxx.drawio.png 格式的文件，打开！像在网页端编辑 drawio 文件一样绘制流程图，绘制完毕后直接保存。就可以直接作为图片插入 Markdown 中了，真的是很方便很方便。最近还有比较火的彩虹屁，这里就不多介绍了。

深夜白话了这么多，开始进入正题吧，在服务器上配置一个 VSCode 环境，从此就可以通过网页端用 VSCode 进行开发了~

## 环境
* CentOS / 7.3 x86_64 (64bit)


## 安装 Docker 

1. 查看内核版本。docker 官方建议内核版本 3.10 以上
    ```bash
    [root@yaindream ~]# uname -a
    Linux yaindream 3.10.0-514.26.2.el7.x86_64 #1 SMP Tue Jul 4 15:04:05 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
    ```

2. 更新 yum 包
    ```bash
    [root@yaindream ~]# yum update
    ```

3. 安装 yum-util。yum-util 提供 yum-config-manager 功能
    ```bash
    [root@yaindream ~]# yum install yum-utils
    ```

4. 设置 yum 源（阿里仓库）
    ```bash
    [root@yaindream ~]# yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    Loaded plugins: fastestmirror
    adding repo from: http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    grabbing file http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo to /etc/yum.repos.d/docker-ce.repo
    repo saved to /etc/yum.repos.d/docker-ce.repo
    ```

5. 安装 docker 
    ```bash
    [root@yaindream ~]# yum install docker
    ```

6. 启动 docker 并加入开机启动
    ```bash
    [root@yaindream ~]# systemctl start docker
    [root@yaindream ~]# docker version
    [root@yaindream ~]# systemctl enable docker
    Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
    ```

## 安装 code-server

code-server 是一款在线的 vscode 工具，只要将 code-server 部署到自己的服务器之后，就可以通过浏览器使用 vscode，很好的解决了远程编辑服务器中文件的问题，方便好用。code-server 的 GitHub 地址为：https://github.com/cdr/code-server

1. 创建一个目录，用来存放编辑器可以访问的文件
    ```bash
    [root@yaindream ~]# mkdir code
    ```

2. 修改文件夹权限，否则可能无法创建和修改文件
    ```bash
    [root@yaindream ~]# chmod -R 777 code/
    ```

3. docker 安装 code-server
    ```bash
    [root@yaindream code]# docker run --name codeserver -d -u root -p 8080:8080 -v "/root/code:/home/coder/project" -e PASSWORD=xxx codercom/code-server:latest --auth password
    ```

4. 浏览器访问
    ```
    ip_address:8080
    ```

## 构建 code-server 代码运行环境

1. 在 VSCode 插件市场搜索 code runner，直接安装即可~

2. 进入 code-server 容器
    ```bash
    [root@yaindream code]# docker exec -it codeserver /bin/bash
    ```

3. 更新安装列表，升级软件
    ```bash
    root@152fe0071609:/home/coder# apt-get update
    root@152fe0071609:/home/coder# apt-get upgrade
    ```

4. 安装 Nodejs 运行环境
    
    添加源

    ```bash
    root@152fe0071609:/home/coder# curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
    ...
    ## Run `sudo apt-get install -y nodejs` to install Node.js 12.x and npm
    ## You may also need development tools to build native addons:
        sudo apt-get install gcc g++ make
    ## To install the Yarn package manager, run:
        curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
        echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
        sudo apt-get update && sudo apt-get install yarn
    ```

    安装 nodejs

    ```
    root@152fe0071609:/home/coder# sudo apt-get install -y nodejs
    ```

    验证 

    ```
    root@152fe0071609:/home/coder# nodejs -v
    v12.18.1
    ```

5. 愉快的玩耍