# 技巧-Hexo下next主题Changyan（畅言）评论同步问题的解决方案

捣鼓了一晚上，终于解决啦

更改 `hexo-theme-next/scripts/filters/comment/changyan.js` 脚本，将其中的

```js
injects.comment.raw('changyan', '<div class="comments" id="SOHUCS"></div>', {}, {cache: true});
```

更改为

```js
injects.comment.raw('changyan', '<div class="comments" id="SOHUCS" sid="{{ page.title }}"></div>', {}, {cache: false});
```

这样就可以将 SourceID 设置为文章标题，我们只需要确保小站内没有同名文章就好啦~

评论同步问题解决，开心~
