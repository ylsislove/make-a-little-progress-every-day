# nodejs-http请求头和响应头

```js
router.param('id', (req, res, next, id) => {
    req.params = {
      id
    }

    // 设置允许跨域的域名*代表允许任意域名跨域
    res.setHeader("Access-Control-Allow-Origin","*");
    //允许的header类型
    res.setHeader("Access-Control-Allow-Headers","content-type");
    //跨域允许的请求方式
    res.setHeader("Access-Control-Allow-Methods","DELETE,PUT,POST,GET,OPTIONS");

    next()
})
```

## 参考链接
* [nodejs 中http请求头，响应头](https://my.oschina.net/shuaihong/blog/1545010)
* [NodeJs中Ajax跨域问题分析](https://blog.csdn.net/TDCQZD/article/details/82047632)
* [Node.js如何设置允许跨域](https://blog.csdn.net/u012149969/article/details/81145144)
