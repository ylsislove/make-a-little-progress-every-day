# python-解决pymysql无法连接MySQL的坑爹问题

报错如下：
```
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on xxxx
```

解决办法挺离谱的，需要把连接的代码写成如下这种“规范”形式：
```python
connect = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='python',
    charset='utf8'
)
```

写成一行就会给你报错 emmmm 哎反正最后解决了就好

## 原文链接
* [解决： pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on xxxx](https://blog.csdn.net/qq_29750461/article/details/80484182)
