# 技巧-用 Hexo 和 GitHub Pages 搭建博客

## 给文章增加结束语
新增文件 `source/_data/post-body-end.njk`

```html
<div>
	<div>
	    {% if not is_index %}
	    <div style="text-align:center;color: #ccc;font-size:14px;">-----------------------<span style="margin: 0 10px;">本文结束</span><i class="fa fa-paw"></i><span style="margin: 0 10px;">感谢您的阅读</span>-----------------------</div>
	    {% endif %}
	</div>
</div>
```

修改 `_config.next.yml`

```yml
custom_file_path:
  postBodyEnd: source/_data/post-body-end.njk
```

## 脚注添加网站运行时间
新增文件 `source/_data/footer.njk`

```html
<div>
  <span id="timeDate" style="">载入天数...</span><span id="times">载入时分秒...</span>
</div>
<script>
    var now = new Date(); 
    function createtime() { 
        var grt= new Date("05/20/2020 00:00:00");//在此处修改你的建站时间，格式：月/日/年 时:分:秒
        now.setTime(now.getTime()+250); 
        days = (now - grt ) / 1000 / 60 / 60 / 24; dnum = Math.floor(days); 
        hours = (now - grt ) / 1000 / 60 / 60 - (24 * dnum); hnum = Math.floor(hours); 
        if(String(hnum).length ==1 ){hnum = "0" + hnum;} minutes = (now - grt ) / 1000 /60 - (24 * 60 * dnum) - (60 * hnum); 
        mnum = Math.floor(minutes); if(String(mnum).length ==1 ){mnum = "0" + mnum;} 
        seconds = (now - grt ) / 1000 - (24 * 60 * 60 * dnum) - (60 * 60 * hnum) - (60 * mnum); 
        snum = Math.round(seconds); if(String(snum).length ==1 ){snum = "0" + snum;} 
        document.getElementById("timeDate").innerHTML = "本站已安全运行 "+dnum+" 天 "; 
        document.getElementById("times").innerHTML = hnum + " 小时 " + mnum + " 分 " + snum + " 秒"; 
    } 
    setInterval("createtime()",250);
</script>
```

修改 `_config.next.yml`

```yml
custom_file_path:
  footer: source/_data/footer.njk
```

## 添加友链
1. 创建 `hexo new page links`
2. 在 `_config.next.yml` 中的 `menu` 添加 `links: /links/ || fa fa-link`
3. 创建 `source/_data/languages.yml`
4. 增加中文描述
```yml
# language
zh-CN:
  # items
  menu:
    links: 友链
```

## 添加自定义图标（Bilibili）
参考：[Custom Icon Image](https://theme-next.js.org/docs/advanced-settings/custom-files.html#Custom-Icon-Image)

样式编辑如下：

```yml
.fa-bilibili {
	background: url(/images/bilibili.svg);
	//background-position: 50% 50%;
	//background-attachment: fixed;
	background-repeat: no-repeat;
	background-size: 100% 100%;
	height: 1em;
	width: 1em !important;
	margin-bottom: -1px;
	margin-right: 3px !important;
}
```

## 添加标签云
文档地址：[Hexo Tag Cloud](https://github.com/D0n9X1n/hexo-tag-cloud/blob/master/README.ZH.md)
1. 安装 `npm i hexo-tag-cloud -S`
2. 在 `source/_data/sidebar.njk` 文件中添加
```js
{% if site.tags.length > 1 %}
<script type="text/javascript" charset="utf-8" src="{{ url_for('/js/tagcloud.js') }}"></script>
<script type="text/javascript" charset="utf-8" src="{{ url_for('/js/tagcanvas.js') }}"></script>
<div class="widget-wrap">
    <div id="myCanvasContainer" class="widget tagcloud">
        <canvas width="250" height="250" id="resCanvas" style="width:100%">
            {{ list_tags() }}
        </canvas>
    </div>
</div>
{% endif %}
```
3. 修改 `_config.next.yml`，放开 `custom_file_path` 中的 `sidebar` 注释
4. 在 `_config.yml` 添加
```yml
# hexo-tag-cloud
tag_cloud:
  textFont: Trebuchet MS, Helvetica
  textColor: '#333'
  textHeight: 15
  outlineColor: '#E2E1D1'
  maxSpeed: 0.05
  pauseOnSelected: true # true 意味着当选中对应 tag 时,停止转动
```
5. 然后使用 `hexo clean && hexo g && hexo s` 来享受属于你自己的独一无二的标签云吧。

## 添加看板娘
参考：[Hexo -5- 添加 live2d 看板动画](https://www.zywvvd.com/2020/03/09/hexo/5_hexo_add_live2d/add-live2d/)

## 文章置顶
1. `npm uninstall hexo-generator-index --save`
2. `npm install hexo-generator-index-pin-top --save`
3. 在需要置顶的文章的`Front-matter`中加上 `top: true` 或者 `top: 任意数字`，比如：（top中数字越大，文章越靠前）
```yml
---
reward_settings:
  enable: true
  comment: Buy me a coffee
top: 10
---
```
4. 在 `layout\_partials\post\post-meta.njk` 文件中编辑如下
```js
{% if post.top %}
  <span class="post-meta-item">
    <span class="post-meta-item-icon">
      <i class="fa fa-thumbtack" style="color: #EB6D39"></i>
    </span>
    <span class="post-meta-item-text"><font color=EB6D39>置顶</font></span>
  </span>
{% endif %}
```

## 音乐播放器
参考：[Hexo NexT主题中添加网页音乐播放器功能](https://asdfv1929.github.io/posts/2018/05/26/next-add-music.html)

1. 点击访问Aplayer源码：[GitHub Aplayer](https://github.com/MoePlayer/APlayer)。下载到本地，解压后将 `dist` 文件夹复制到 `themes\next\source` 文件夹下。
2. 新建 `themes\next\source\dist\music.js` 文件，添加内容：
```js
const ap = new APlayer({
    container: document.getElementById('aplayer'),
    fixed: true,
    autoplay: false,
    audio: [
      {
        name: "PDD洪荒之力",
        artist: '徐梦圆',
        url: 'http://up.mcyt.net/?down/39868.mp3',
        cover: 'http://oeff2vktt.bkt.clouddn.com/image/84.jpg',
      },
      {
        name: '9420',
        artist: '麦小兜',
        url: 'http://up.mcyt.net/?down/45967.mp3',
        cover: 'http://oeff2vktt.bkt.clouddn.com/image/8.jpg',
      },
      {
        name: '风筝误',
        artist: '刘珂矣',
        url: 'http://up.mcyt.net/?down/46644.mp3',
        cover: 'http://oeff2vktt.bkt.clouddn.com/image/96.jpg',
      }
    ]
});
```
3. 在 `layout\_partials\post\body-end.njk` 文件中编辑如下：
```html
<link rel="stylesheet" href="/dist/APlayer.min.css">
<div id="aplayer"></div>
<script type="text/javascript" src="/dist/APlayer.min.js"></script>
<script type="text/javascript" src="/dist/music.js"></script>
```
4. 为了解决切换页面播放中断问题，只需要在 `_config.next.yml` 中，将 `pjax: false` 改为 `pjax: true` 即可~

## 目前的缺陷
修改了 NexT 的源码，主要是 `changyan.js`、`footer.njk` 和 `post-mate.njk`，后面会用 inject 技术解决这个问题。

## 参考链接
* [用 Hexo 和 GitHub Pages 搭建博客](https://ryanluoxu.github.io/2017/11/24/%E7%94%A8-Hexo-%E5%92%8C-GitHub-Pages-%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2/)
* [hexo博客搭建浅谈](https://fightinggg.github.io/Q8AYFB.html)
* [又见苍岚](https://www.zywvvd.com/)
* [Hexo](https://hexo.io/zh-cn/)
* [NexT](https://theme-next.js.org/)
* [Hexo功能增强插件](https://sulin.me/2019/Z726F8.html)
