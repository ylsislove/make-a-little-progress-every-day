# 前端-ES5知识点总结

## 严格模式
### 概念
* 除了正常运行模式(混杂模式)，ES5添加了第二种运行模式："严格模式"（strict mode）
* 顾名思义，这种模式使得Javascript在更严格的语法条件下运行

### 目的
* 消除Javascript语法的一些不合理、不严谨之处，减少一些怪异行为
* 消除代码运行的一些不安全之处，为代码的安全运行保驾护航
* 为未来新版本的Javascript做好铺垫

### 使用
* 在全局或函数的第一条语句定义为: 'use strict'
* 如果浏览器不支持, 只解析为一条简单的语句, 没有任何副作用

### 作用
* 必须使用var声明变量
```js
'use strict';
var age = 12;
console.log(age);
```
* 禁止自定义的函数中this指向window
```js
function Person(name, age) {
    this.name = name;
    this.age = age;
}
// 直接调用自定义函数，this指向window
// Person('yain', 21);
// 通过new关键字，this指向实例对象
new Person('yain', 21);
```
* 创建eval作用域
```js
var name = 'yain';
eval('var name = "ylsislove"; console.log(name);');
// 下面语句，非严格模式下会打印 ylsislove，严格模式下打印 yain
console.log(name);
```


