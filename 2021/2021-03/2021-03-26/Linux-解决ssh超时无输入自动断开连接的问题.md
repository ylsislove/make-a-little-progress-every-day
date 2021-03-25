# Linux-解决ssh超时无输入自动断开连接的问题

方法有以下三种：
1. 修改 server 端的 `etc/ssh/sshd_config`
     - ClientAliveInterval 60 ＃server每隔60秒发送一次请求给client，然后client响应，从而保持连接
     - ClientAliveCountMax 3 ＃server发出请求后，客户端没有响应得次数达到3，就自动断开连接，正常情况下，client不会不响应
2. 修改 client 端的 `etc/ssh/ssh_config` 添加以下：（在没有权限改 server 配置的情形下）
     - ServerAliveInterval 60 ＃client每隔60秒发送一次请求给server，然后server响应，从而保持连接
     - ServerAliveCountMax 3 ＃client发出请求后，服务器端没有响应得次数达到3，就自动断开连接，正常情况下，server不会不响应
3. 在命令参数里 `ssh -o ServerAliveInterval=60` 这样子只会在需要的连接中保持持久连接， 毕竟不是所有连接都要保持持久的

## 原文链接
* [怎么设置ssh超时自动断开连接](https://zhidao.baidu.com/question/2205617112860910148.html)
