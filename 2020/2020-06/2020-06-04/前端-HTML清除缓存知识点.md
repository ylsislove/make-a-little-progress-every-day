# 前端-HTML清除缓存知识点

- [缓存及优点](#%E7%BC%93%E5%AD%98%E5%8F%8A%E4%BC%98%E7%82%B9)
- [缓存带来的问题](#%E7%BC%93%E5%AD%98%E5%B8%A6%E6%9D%A5%E7%9A%84%E9%97%AE%E9%A2%98)
- [解决方案](#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)
- [扩展](#%E6%89%A9%E5%B1%95)

### 缓存及优点
浏览器的缓存可以临时存储一些文件，因此当页面切换或者再次加载相同页面时就不需要去重新下载这些文件。服务端可以设置头部告诉浏览器在一定时间内存储这些文件。这样不仅可以大幅度加快网站的速度还可以节省你的带宽。

### 缓存带来的问题
然而当开发者对站点进行修改时就可能会带来一些问题：某些用户可能仍在访问那些修改之前的文件。这样就会导致那些用户使用以前的功能或者访问一个坏了的站点（当服务端渲染的页面元素被删除、移动或重命名后，那些被缓存的 CSS 和 JavaScript 文件对这些元素的操作就会出现错误）

### 解决方案

解决缓存的关键就是强制让浏览器下载最新的文件。这只需要给那些旧的文件一个新的名字，或者修改服务端的头部。

比较简单常用的技术就是在文件结尾添加一个查询字符串，使其强制让浏览器重新下载新的文件。如下所示：
```
src="js/script.js"
src="js/script.js?v=2"
```
这样一来，在不需要修改文件名的前提下，浏览器就会将其视为不同的文件。

### 扩展

* 服务端头部相关设置为 [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag)
* [Service Workers](https://hacpai.com/article/1520483961387) 及 [Cache Storage](https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage)
* 网站的速度很大程度上会影响 SEO 评分
* 缓存和命名被誉为编程届的两大难题
* 使用 webpack 相关的项目在框架层面上已经比较完美的自动解决此问题