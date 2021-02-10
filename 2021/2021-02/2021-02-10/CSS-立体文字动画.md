# CSS-立体文字动画

## 代码
```html
<h1>Hello World</h1>
```

```css
body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #FFCD00;
  
  perspective: 2500px;
}

h1 {
  padding: 0;
  margin: 0;
  position: relative;
  color: #fff;
  font-size: 5rem;
  animation: 5s rotate ease-in-out infinite;
}

@keyframes rotate {
  0%, 100% {
    transform: rotate3d(0, 1, 0, -20deg);
  }
  50% {
    transform: rotate3d(0, 1, 0, 20deg);
  }
}

h1::before,
h1::after {
  content: 'Hello World';
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}

h1::after {
  z-index: -2;
}

h1::before {
  color: #009CDE;
  animation: 5s h1-before ease-in-out infinite;
}

@keyframes h1-before {
  0%, 100% {
    transform: translate3d(5px, 2px, -10px);
  }
  50% {
    transform: translate3d(-5px, 2px, -10px);
  }
}

h1::after {
  color: #003C71;
  animation: 5s h1-after ease-in-out infinite;
}

@keyframes h1-after {
  0%, 100% {
    transform: translate3d(10px, 4px, -20px);
  }
  50% {
    transform: translate3d(-10px, 4px, -20px);
  }
}
```

## 结果展示
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210211003913.gif)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210211003913.gif)
