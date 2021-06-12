# 技巧-Hexo下next主题Changyan（畅言）评论同步问题的解决方案

捣鼓了一晚上，终于解决啦

更改 `hexo-theme-next/scripts/filters/comment/changyan.js` 脚本，将其中的

```js
injects.comment.raw('changyan', '<div class="comments" id="SOHUCS"></div>', {}, {cache: true});
...
{% else %}
  <a title="changyan" href="{{ url_for(post.path) }}#SOHUCS" itemprop="discussionUrl">
    <span id="url::{{ post.permalink }}" class="cy_cmt_count" data-xid="{{ post.path }}" itemprop="commentCount"></span>
  </a>
{% endif %}
```

更改为

```js
injects.comment.raw('changyan', '<div class="comments" id="SOHUCS" sid="{{ page.title }}"></div>', {}, {cache: false});
...
{% else %}
  <a title="changyan" href="{{ url_for(post.path) }}#SOHUCS" itemprop="discussionUrl">
    <span id="sourceId::{{ post.title }}" class="cy_cmt_count" data-xid="{{ post.path }}" itemprop="commentCount"></span>
  </a>
{% endif %}
```

这样就可以将 SourceID 设置为文章标题，我们只需要确保小站内没有同名文章就好啦~

注意，Home 页的评论数统计更新会有 15 分钟的延迟，这个需要注意一下~

评论同步问题解决，开心~

## 参考
* [织梦dede标签模板首页或列表页面调用畅言的评论数](https://www.dedesos.com/study/biaoqiandiaoyong/3394.html)
