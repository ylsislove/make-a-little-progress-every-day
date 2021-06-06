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

## 添加自定义图表（Bilibili）
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

## 参考链接
* [用 Hexo 和 GitHub Pages 搭建博客](https://ryanluoxu.github.io/2017/11/24/%E7%94%A8-Hexo-%E5%92%8C-GitHub-Pages-%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2/)
* [hexo博客搭建浅谈](https://fightinggg.github.io/Q8AYFB.html)
* [又见苍岚](https://www.zywvvd.com/)
* [Hexo](https://hexo.io/zh-cn/)
* [NexT](https://theme-next.js.org/)
* [Hexo功能增强插件](https://sulin.me/2019/Z726F8.html)
