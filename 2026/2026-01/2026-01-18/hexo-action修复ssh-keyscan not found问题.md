---
title: hexo-action修复ssh-keyscan not found问题
date: 2026-01-18 17:05:03
categories:
 - [不看会后悔的实用技巧分享, 个人博客]
tags: 
 - Hexo
 - Blog
 - MacBook
---

## 用本地的hexo-action目录替换远程

要不然每次在本地添加一些排查语句，都得上传到 GitHub 上去排查调试，太麻烦了

所以第一步一定要用本地的去调试

请按照以下步骤操作：

在博客项目内创建本地 Action 目录
标准的做法是在你的博客项目内创建一个 .github/actions 目录，用于存放本地 Action。

```bash
mkdir -p /Users/yuwang/Code/blog/.github/actions
```

将你的 hexo-action 复制或 clone 到该目录

```bash
cp -r /Users/yuwang/Code/hexo-action /Users/yuwang/Code/blog/.github/actions/
```

现在，你本地的 Action 路径应该是：/Users/yuwang/Code/blog/.github/actions/hexo-action

修改工作流文件以使用相对路径

将 deployment.yml 中的 uses 修改为指向项目内的这个相对路径。这是 GitHub Actions 支持引用本地 Action 的标准语法。

```yml
- name: Deploy
  id: deploy
  # 使用项目内的相对路径引用本地 Action
  uses: ./.github/actions/hexo-action
```

清理缓存并重新运行

```bash
# 清理旧的缓存
rm -rf /Users/yuwang/.cache/act/ylsislove-hexo-action@v1.0.5
# 运行测试
act -j hexo-deployment --container-architecture linux/amd64 -s DEPLOY_KEY="YOUR_PRIVATE_KEY_HERE"
```

这样就可以尝试在本地修改 hexo-action 并快速验证了

## 直接构建本地 Docker 容器验证
为了快速定位问题，我们直接使用你本地的 Dockerfile 和上下文进行独立构建和测试，这样可以得到更清晰的错误输出。

在你的博客项目目录下，执行以下命令：

```bash
# 切换到你的本地 Action 目录
cd /Users/yuwang/Code/blog/.github/actions/hexo-action

# 使用 Docker 直接构建镜像，不使用 act，这会输出详细的构建过程
docker build --platform linux/amd64 -t test-hexo-action .
```

通过 docker build 命令可以直接看到问题是哪里报错了

## 修复
问题根源明确了：你使用的 node:18-buster-slim 镜像已经过时，其对应的 Debian “buster” 版本官方软件源已停止维护，导致 apt-get update 失败。

打开 /Users/yuwang/Code/blog/.github/actions/hexo-action/Dockerfile，将第一行替换为：

```dockerfile
FROM node:18-bullseye-slim
```

或者，如果你想使用一个更新的版本：

```dockerfile
FROM node:18-bookworm-slim
```

bullseye 是当前较稳定且受长期支持的版本。

问题终于修复，博客可以继续更新了，冲～

