# Linux-解决ssh超时无输入自动断开连接的问题

## 方法一：修改 server 端的 `etc/ssh/sshd_config`
```powershell
# server每隔60秒发送一次请求给client，然后client响应，从而保持连接
ClientAliveInterval 60
# server发出请求后，客户端没有响应得次数达到3，就自动断开连接，正常情况下，client不会不响应
ClientAliveCountMax 3 
```

重启服务：`systemctl restart sshd`

## 方法二：在命令参数里 `ssh -o ServerAliveInterval=60`
这样子只会在需要的连接中保持持久连接， 毕竟不是所有连接都要保持持久的

