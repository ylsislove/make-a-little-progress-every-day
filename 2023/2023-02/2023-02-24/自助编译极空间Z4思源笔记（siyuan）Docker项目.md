---
title: 自助编译极空间Z4思源笔记（siyuan）Docker项目
date: 2023-02-24 02:55:49
categories:
 - [我的NAS捣鼓笔记, 极空间]
tags: 
 - NAS
 - 极空间
---

## 前言
最近入了思源笔记的坑，想好好的捣鼓捣鼓。去年在自己的极空间NAS上部署了思源笔记的Docker版，但版本已经跟不上了（D大和V姐的更新太频繁了🤣），借助极空间论坛里大佬的帮助，我们自己也可以编译适配极空间Z4的最新版思源笔记Docker镜像了，于是在此记录下编译的过程~

## 编译环境
* Ubuntu：Ubuntu 20.04.4 LTS x86_64
* Docker
* Git

## 步骤
### 拉取思源笔记最新源码
```bash
git clone https://github.com/siyuan-note/siyuan.git
```

### 拉取大佬的zsource仓库
```bash
git clone https://github.com/zs0urce/zsource.git
```

浏览了下大佬的`Dockerfile.z4`文件，发现大佬主要是将`addgroup --gid 1000 siyuan && adduser --uid 1000 --ingroup siyuan --disabled-password siyuan`这个创建普通用户的命令去掉了，然后将`USER siyuan`这个指定用户的命令也去掉了，这样就可以使用root用户了，从而解决极空间Z4上的权限问题了

### 拷贝
拷贝大佬项目中siyuan目录下的所有文件到思源笔记仓库代码目录中

:::info
国内的网络环境真的是太恶劣了，为了解决环境问题，深夜踩坑了一晚上，在更改了下`Dockerfile.z4`文件后，终于解决了，欣慰啊
文件中需要更改的地方我都已经高亮标出了~
:::

```dockerfile Dockerfile.z4 mark:4,11-13
FROM node:16 as NODE_BUILD
WORKDIR /go/src/github.com/siyuan-note/siyuan/
ADD . /go/src/github.com/siyuan-note/siyuan/
RUN cd app && npm install -g pnpm && ELECTRON_MIRROR=https://cnpmjs.org/mirrors/electron/ pnpm install electron@21.4.1 -D && pnpm install && pnpm run build

FROM golang:1.19-alpine as GO_BUILD
WORKDIR /go/src/github.com/siyuan-note/siyuan/
COPY --from=NODE_BUILD /go/src/github.com/siyuan-note/siyuan/ /go/src/github.com/siyuan-note/siyuan/
ENV GO111MODULE=on
ENV CGO_ENABLED=1
ENV GOPROXY=https://goproxy.cn,direct
RUN apk add --no-cache gcc musl-dev git && \
    git config --global http.https://github.com.proxy socks5://192.168.1.101:10808 && git config --global https.https://github.com.proxy socks5://192.168.1.101:10808 && \
    cd kernel && go build --tags fts5 -v -ldflags "-s -w -X github.com/siyuan-note/siyuan/kernel/util.Mode=prod" && \
    mkdir /opt/siyuan/ && \
    mv /go/src/github.com/siyuan-note/siyuan/app/appearance/ /opt/siyuan/ && \
    mv /go/src/github.com/siyuan-note/siyuan/app/stage/ /opt/siyuan/ && \
    mv /go/src/github.com/siyuan-note/siyuan/app/guide/ /opt/siyuan/ && \
    mv /go/src/github.com/siyuan-note/siyuan/kernel/kernel /opt/siyuan/ && \
    find /opt/siyuan/ -name .git | xargs rm -rf

FROM ghcr.io/linuxserver/baseimage-alpine:3.16
LABEL maintainer="wangyu<wangyu0814@foxmail.com>"

WORKDIR /opt/siyuan/
COPY --from=GO_BUILD /opt/siyuan/ /opt/siyuan/

RUN \
  apk add --no-cache \
    ca-certificates \
    tzdata && \
  echo "**** cleanup ****" && \
  rm -rf \
      /root/.cache \
      /tmp/* 

# copy local files
COPY root/ /

ENV TZ=Asia/Shanghai
ENV WORKSPACE=/siyuan/workspace/
ENV ACCESSAUTHCODE=
ENV PUID=0
ENV PGID=0
VOLUME /siyuan/workspace/
EXPOSE 6806
```

### 编译
```bash
sudo sh ./build_z4.sh
```

成功之后，就可以参考我之前的文章【[极空间上常用Docker应用推荐-可玩性+++](https://blog.aayu.today/nas/zspace/20220902/)】进行部署啦，bingo~

在此放一张编译成功，以及成功部署后的图吧，镇帖 (๑•̀ㅂ•́)و✧

![](https://image.aayu.today/uploads/2023/02/24/202302240658460.png)
![](https://image.aayu.today/uploads/2023/02/24/202302240659155.png)
{.gallery  data-height="240"}
