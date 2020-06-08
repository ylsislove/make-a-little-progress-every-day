# 技巧-shell脚本解决ssh、scp命令需要输入密码的问题

  - [前言](#%E5%89%8D%E8%A8%80)
  - [客户端生成公钥和私钥](#%E5%AE%A2%E6%88%B7%E7%AB%AF%E7%94%9F%E6%88%90%E5%85%AC%E9%92%A5%E5%92%8C%E7%A7%81%E9%92%A5)
  - [公钥保存至服务器](#%E5%85%AC%E9%92%A5%E4%BF%9D%E5%AD%98%E8%87%B3%E6%9C%8D%E5%8A%A1%E5%99%A8)
  - [ssh 命令](#ssh-%E5%91%BD%E4%BB%A4)
  - [scp 命令](#scp-%E5%91%BD%E4%BB%A4)

## 前言
如果你想在本地的电脑上通过 ssh 命令连接云服务器，每次又懒得输入命令和服务器密码，希望能直接执行一个 shell 命令即可，那么本文可能会对你有些帮助

## 客户端生成公钥和私钥
在客户端运行命令
```bash
ssh-keygen -t rsa
```
rsa 是一种常用的加密算法，还有一种加密算法是 dsa。
当在客户端执行这条命令时，会在 home 目录下的 .ssh 目录生成两把密钥，分别是**私钥**（id_rsa）和**公钥**（id_rsa.pub）。
私钥存在客户端，公钥存放在任何想要连接的服务器上。
在执行这条命令时，另一个需要设置的就是私钥的密码。如果想为了更加安全，这里需要设置一个妥当的密码，通过该密码来解开私钥连接服务器（目的就是防止黑客直接窃走私钥连接服务器）。但如果想图方便，这里可以直接回车默认，不设置私钥密码，出事了别找我呀嘿嘿

## 公钥保存至服务器
可以在客户端执行scp命令将公钥上传到服务器上
```bash
scp ~/.ssh/id_rsa.pub username@<ssh_server_ip>:~
```

然后通过 ssh 登录服务器
```bash
ssh username@<ssh_server_ip>
```

在服务器上执行以下操作
```bash
cat id_rsa.pub >> ～/.ssh/authorized_keys
```
完成配置。至此，在客户端执行 ssh 和 scp 命令时就无需输入服务器密码了（未设置私钥密码的情况下）。如果前面设置了私钥密码，在连接时还必须要输入私钥密码才能连接成功。

## ssh 命令
```bash
ssh -i ~/.ssh/id_rsa username@<ssh_server_ip>
```

## scp 命令
```bash
scp -i ~/.ssh/id_rsa filename username@<ssh_server_ip>:~
```

如果将私钥放在 home 目录下的 .ssh 目录（默认就是），以上命令就可以省略 `-i ~/.ssh/id_rsa` 