# 前端-CSS选择器优先级

  - [特殊性](#%E7%89%B9%E6%AE%8A%E6%80%A7)
  - [重要性](#%E9%87%8D%E8%A6%81%E6%80%A7)
  - [继承](#%E7%BB%A7%E6%89%BF)
  - [层叠](#%E5%B1%82%E5%8F%A0)

## 特殊性
CSS选择器可以让我们有多种不同的方法选择元素。当我们使用多种规则的时候，我们必须要明确其中的优先级。在CSS选择器的规则中，称之为特殊性，特殊性越高，自然优先级越高。

这里有一个特殊性的说明：
* !important 特殊性最高
* 对于内联样式，加1000
* 对于选中器中给定的ID属性值，加0100
* 对于选择器中给定的类属性值，属性选择或伪类，加0010
* 对于选择器中给定的元素选择器和伪元素，加0001
* 结合符和通配符选择器对特殊性没有任何贡献，0000

![CSS选择器](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/CSS选择器.png)

下面亲自测试一下
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		/* id选择器 */
		#ID-selector { font-size: 10px; }
		/* 类选择器 */
		.class-selector { font-size: 12px; }
		/* 属性选择器 */
		*[proprty-selector] { font-size: 14px; }
		/* 伪类选择器 */
		*:first-child { font-size: 16px; }
		/* 元素选择器 */
		div { font-size: 18px; }
		/* 关系选择器 */
		* div { font-size: 20px; }
		/* 伪元素选择器 */
		*::first-line { font-size: 22px; }
		/* 通配符选择器 */
		* { font-size: 24px; }
	</style>
</head>
<body>
	<div style="font-size: 6px;" proprty-selector="true" id="ID-selector" class="class-selector">测试CSS选择器的特殊性</div>
</body>
</html>
```

在观察结果之前先明确两点：
* 当选择器出于同一种特殊性的时候，位于css文件下部的样式会覆盖上面的样式
* 通配符选择器对于特殊性没有任何贡献，所以下面我用了许多的通配符（强烈说明日常开发最好不要使用过多通配符，这里只是为了举例子）来代替div属性，是因为要将div自身的特殊性影响排除

![css优先级-chrome](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/css优先级-chrome.png)

和我们的css代码进行对比分析，注意，我书写的css代码是按照最上面的特殊性等级来书写的，在chrome中可以看到，处于同一层级的css选择器，下面的css样式会覆盖上面的css样式。

有同学可能会疑问，为什么伪元素选择器没有按照我说的那样去排列呢，而且还应用了样式，那岂不是说伪元素选择器要比内联样式的优先级还要高？其实不是的。

先回答第一个问题，伪元素选择器实际上就是和元素选择器以及关系选择器处于同一层级的，我们在IE浏览器里可以验证

![css优先级-ie](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/css优先级-ie.png)

可以看到在IE浏览器，选择器的优先级就完全按照最上面那幅图说明的那样去排列，且处于同一层级的css选择器，下面的css样式会覆盖上面的css样式。

再来回答第二个问题，为什么伪元素的样式会被应用？首先来看一副GIF图

![css选择器-ie](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/css选择器-ie.gif)

随着我取消/添加伪元素的样式，html 的字体会相应的变化。这里的解释就是，伪元素的样式应用是相当于添加一个元素，这里就是添加了一个 `<first-line>` 元素在 `div` 中，然后由于字体的样式是可以继承的，所以当前 first-line 中的样式继承了父元素的 first-line 的字体为 22px 的样式。可能你会问就算继承为什么不是继承最终的内联样式的属性，这里可能就是伪元素的规则了。

## 重要性
上面提到的是一般情况下，当然如果对于很复杂的页面样式来说，想让某一个样式将所有样式都覆盖，那么就需要使用特殊手段了。有时某个声明可能非常重要，超过了所有其他声明，CSS2.1称之为重要声明。重要声明在声明的结束分号之前插入!important来标志，如果!important放在声明的任何其他位置，整个声明都将无效

如果一个声明是重要声明，则超过所有的非重要声明。现在我们将上面的例子中的通配符样式加上重要说明：如下
```css
/* 通配符选择器 */
* { font-size: 24px !important; }
```

结果如下。可以看到通配符的属性被应用上啦

![css优先级-重要性声明](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/css优先级-重要性声明.png)


## 继承
继承是从一个元素向其后代元素传递属性值所采用的机制。基于继承机制，样式不仅可以应用到指定的元素，还会应用到它的后代元素。在两个比较特殊的情况需要注意：一个是在 `HTML` 中，应用到 `body` 元素的背景样式可以传递到 html 元素；另一个是 `<a>` 标签不会继承父元素的文本样式。

继承的属性没有特殊性，所以当我们对于元素进行添加选择器的时候，会直接覆盖掉继承来的属性。通配符具有特殊性，虽然特殊性是0，但是还是比继承高的。


## 层叠
因为一般我们的开发中不会只有简单的样式，而是很多的样式在一起，那么我们就需要一个规则去辨别最后渲染的样式。CSS层叠样式表的层叠特性就是让样式层叠在一起，通过特殊性、重要性、来源及继承机制来排列层叠样式的顺序及选出胜出者。

重要性和来源需要同时考虑，因为二者的结合使用与否会存在不同的顺序
* 不考虑来源的情况下，！important最高
* 在不考虑重要性的前提下，来源优先级顺序为
    * 读者的重要声明
    * 创作人员的重要声明
    * 创作人员的正常声明
    * 读者的正常声明
    * 用户代理声明
* 二者一起考虑的情况下，最终的优先级排序为：`user(用户)!important > author(作者)!important > author > user > user agent`

举个 🌰：
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<link rel="stylesheet" href="index.css">
</head>
<body>
	<div>测试CSS声明</div>
</body>
</html>
```

```css
/* index.css: author's style sheet  */
div {
    font-size: 14px;
}
 
div {
    font-size: 16px !important;
}
```

```css
/* user.css: user's style sheet */
div {
    font-size: 8px;
}
 
div {
    font-size: 10px !important;
}
 
```

我们可以看到上面有两个 css 文件，但是我们文件中只使用了 index.css 文件，这个就是创作人员的声明，对于 user.css 就是我们即将需要操作的 user 声明。

![css选择器-层叠样式表](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/css选择器-层叠样式表.gif)


1. 从上面的操作中可以看到，在没有应用 user.css 的时候，页面上的文字大小为 16px，但是当我们将 user.css 的样式应用之后，可以看到当前页面的样式变为 10px。这里的原因就是上面给的优先级顺序决定的。
2. 接着，对于非重要声明来说，按照特殊性排序。特殊性越高的规则，权重越大
3. 最后，如果特殊性相同，则按照出现顺序排序。声明在样式表或文档中越靠后出现，权重越大。如果样式表中有通过 `@import` 导入的样式表，一般认为出现在导入样式表中的声明在前，主样式表的所有声明在后。
