---
title: VSCode配置C++和Python编译和调试环境
date: 2022-12-09 23:16:27
categories:
 - [人工智能, 基础知识]
tags: 
 - python
 - c++
---

## VSCode配置
* Visual Studio Code 下载地址：https://code.visualstudio.com/download
* VS Code建议安装插件列表：
  * 中文菜单：
    * MS-CEINTL.vscode-language-pack-zh-hans
  * SSH远程开发：
    * ms-vscode-remote.remote-ssh
    * ms-vscode-remote.remote-ssh-edit
    * ms-vscode.remote-explorer
* C++开发
  * ms-vscode.cpptools
* python开发
  * ms-python.python
* 代码补全
  * GitHub.copilot

## SSH连接远端Linux主机
点击VSCode左下角的><符号，创建一个新的SSH连接，输入连接命令即可打开新的窗口，然后正确输入密码即可连接到远端的Linux主机

## Linux配置
### 安装miniconda
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh
bash Miniconda3-py39_4.12.0-Linux-x86_64.sh
```

默认会安装在用户目录下，保持默认即可

安装完成后用`source .bashrc`刷新配置文件，即可看见命令行前面有个`(base)`前缀，即安装成功

### 安装opencv
如果用`conda install opencv`命令安装成功后，import cv2可能还会报错，缺少一个依赖，运行下列命令安装依赖
```bash
sudo apt update
sudo apt install libgl1-mesa-glx
```

如果用pip安装mediapipe速度慢，可以在用户目录下创建`.pip/pip.conf`文件，然后配置如下内容
```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```

然后重启命令行，再次用`pip install mediapipe`即可满速

### 安装g++
```bash
sudo apt update
sudo apt install build-essential
which g++
gcc --version
```

这个命令将会安装一系列软件包，包括gcc,g++,和make

### 安装gdb
```bash
sudo apt update
sudo apt install gdb
```

## 测试Python
```python
# python 代码测试

# 计算 1+2+3+4+5 的和
sum = 0;
for i in range(5):
    sum += i

# 打印结果
print(sum);
```

debuger配置.vscode下launch.json添加
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true  // false表示可以进入第三方库（如Pytorch）里进行调试
        }
    ]
}
```

## 测试C++
```cpp
#include <iostream>
using namespace std;

int main(){
    
    // 计算 1+2+3+4+5
    int sum {0};
    for (int i {0}; i < 5; i++){
        sum += i;
    }
    // 输出结果
    cout << sum << endl;
    return 0;
    
}
```

* 方法一：用g++  main.cpp -o main生成可执行文件
* 方法二：在.vscode先添加tasks.json
```json
{
	"version": "2.0.0",
	"tasks": [
	  {
		"type": "cppbuild",
		"label": "C/C++: g++ 生成活动文件",
		"command": "/usr/bin/g++", // g++的路径
		"args": [
		  "-fdiagnostics-color=always", // 颜色
		  "-g",  // 调试信息
		  "-Wall", // 开启所有警告
		  "-std=c++14", // c++14标准
		  "${file}", // 文件本身，仅适用于C++基础知识教学，无法同时编译所有文件
		  // "${fileDirname}/*.cpp", // 文件所在的文件夹路径下所有cpp文件
		  "-o", // 输出
		  "${workspaceFolder}/release/${fileBasenameNoExtension}" // 文件所在的文件夹路径/release/当前文件的文件名，不带后缀
		],
		"options": {
		  "cwd": "${fileDirname}" // 文件所在的文件夹路径
		},
		"problemMatcher": [
		  "$gcc"
		],
		"group": {
		  "kind": "build",
		  "isDefault": true
		},
		"detail": "编译器: /usr/bin/g++"
	  }
	]
}
```

需要debuger，launch.json修改为：
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "C++ 调试 (gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/release/${fileBasenameNoExtension}", // 文件所在的文件夹路径/release/当前文件的文件名，不带后缀
            "args": [],
            "stopAtEntry": false,
            "cwd": "${fileDirname}", // 文件所在的文件夹路径
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                },
                {
                    "description": "Set Disassembly Flavor to Intel",
                    "text": "-gdb-set disassembly-flavor intel",
                    "ignoreFailures": true
                }
            ],
            "preLaunchTask": "C/C++: g++ 生成活动文件"  // tasks.json的label
        },
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

## VSCode中变量解释
* `${workspaceFolder}` :表示当前workspace文件夹路径，也即/home/Coding/Test
* `${workspaceRootFolderName}`:表示workspace的文件夹名，也即Test
* `${file}`:文件自身的绝对路径，也即/home/Coding/Test/.vscode/tasks.json
* `${relativeFile}`:文件在workspace中的路径，也即.vscode/tasks.json
* `${fileBasenameNoExtension}`:当前文件的文件名，不带后缀，也即tasks
* `${fileBasename}`:当前文件的文件名，tasks.json
* `${fileDirname}`:文件所在的文件夹路径，也即/home/Coding/Test/.vscode
* `${fileExtname}`:当前文件的后缀，也即.json
* `${lineNumber}`:当前文件光标所在的行号
* `${env:PATH}`:系统中的环境变量

## 参考链接
* [Ubuntu ：20.04 上安装 gcc/g++7.5](https://blog.csdn.net/hhd1988/article/details/123651476)
* [vscode error: Please specify the "MIDebuggerPath" option](https://www.cnblogs.com/dbnn/p/16315316.html)
