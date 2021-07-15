# Ubuntu-Ubuntu系统中创建新用户

## 前言
本文基于 Linux 的 Ubuntu 系统新建一个普通用户，linux 系统的用户名为 peng, 主机名为 ubuntu
* 1. 新建用户
* 2. 允许该用户以管理员身份执行指令

## 创建步骤
1. 切换为 root 用户为了获取创建用户的权限
```bash
peng@ubuntu:~$ sudo su
```

2. 添加一个新用户（如用户名为 csdn）
```bash
root@ubuntu:/home/peng# adduser csdn
```
然后根据系统提示进行密码和注释性描述的配置，全程不用自己输入其他命令即可配置成功，用户主目录和命令解析程序都是系统自动指定。

3. 查看用户的属性
```bash
root@ubuntu:/home/peng# cat /etc/passwd
```

4. 退出当前用户，以用户 csdn 登陆系统

5. 删除用户通过 deluser 命令

## 允许该用户以管理员身份执行指令
当我们在指令前加入 sudo 执行一些指令时（如切换到 root 用户），会出现错误：
> csdn is not in the sudoers file. This incident will be reported.

1. 再次切换到 root 用户（不要用 sudo su, 而用 su root）

如果这里提示“su: Authentication failure”，是因为没有给root设置登录密码，解决方法：
- 先切换回用户peng: su peng
- 在给root设置登录密码：sudo passwd root

2. 执行 visudo 命令
```bash
csdn@ubuntu:/home/peng$ visudo
```

3. 该命令实际上打开的是/etc/sudoers文件，修改该文件，在“root ALL=(ALL:ALL) ALL”这一行下面加入一行：
```bash
csdn ALL=(ALL:ALL) ALL
```
ctrl+o（然后再按 enter）保存，ctrl+c 取消，ctrl+x 退出

4. 切换回 csdn
```bash
root@ubuntu:/home/peng# su csdn
```

5. 用 sudo su 再次登录 root
```bash
csdn@ubuntu:/home/peng$ sudo su
```
可以看到，用户 csdn 就可以用 sudo 命令以管理员身份执行指令了。
