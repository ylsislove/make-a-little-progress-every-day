# Ubuntu-使用sslocal连接Shadowsocks

## 前言
前置文章：[技巧-用Docker科学上网](../../../2020/2020-07/2020-07-24/技巧-用Docker科学上网.md)

## Ubuntu 配置
1. `sudo apt-get install python3-pip`

2. `pip install shadowsocks`

3. 跳转到 `~/.local/bin` 目录下，运行

    `./sslocal -s 部署了shadowsocks的云服务器的ip地址 -p 54285 -k shadowsocks的密码 -l 54285 -t 600 -m aes-256-cfb`

    即可将 Ubuntu 连接到云服务器的 shadowsocks 上。

    或新建一个 sslocal 配置文件，如 ssconfig.json，编辑如下

    ```json
    {
        "server": "部署了shadowsocks的云服务器的ip地址",
        "server_port": 54285,
        "local_port": 54285,
        "password": "shadowsocks的密码",
        "timeout": 600,
        "method": "aes-256-cfb"
    }
    ```

    运行 `./sslocal -c ssconfig.json`，即可

4. 添加 `~/.local/bin` 进环境变量，即可在任意位置访问 sslocal 命令

## 可能遇到的问题
1. AttributeError: /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1: undefined symbol: EVP_CIPHER_CTX_cleanup

    解决方案：

    修改 `~/.local/lib/python3.8/site-packages/shadowsocks/crypto` 目录下的 `openssl.py`

    将 `openssl.py` 文件中的 `libcrypto.EVP_CIPHER_CTX_cleanup.argtypes = (c_void_p,)` 修改为 `libcrypto.EVP_CIPHER_CTX_reset.argtypes = (c_void_p,)`

    可以用 vim 搜索 `cleanup` 快速定位到要修改处

    再次搜索，将 `libcrypto.EVP_CIPHER_CTX_cleanup(self._ctx)` 修改为 `libcrypto.EVP_CIPHER_CTX_reset(self._ctx)`

    全文共两处需要修改的地方，修改完保存退出，再次运行命令应该就没问题了

## 参考链接
* [ubuntu16.04配置shadowsocks client](http://www.stlswm.com/article/show_3_6_6.html)
* [Ubuntu下使用sslocal连接Shadowsocks](https://ipx.name/ubuntu-sslocal-shadowsocks/)
