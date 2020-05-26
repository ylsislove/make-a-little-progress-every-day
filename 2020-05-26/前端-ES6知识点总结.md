# 前端-ES6知识点总结

## let 和 const 关键字
### let 关键字
* 作用
    * let 与 var 类似，用于声明一个变量
* 特点：
    * 在块作用域中有效
    * 不能重复声明
    * 不会预处理，不存在变量提升
* 应用：
    * 循环遍历加监听
    * 使用let取代var是趋势
```js
// 报错：age is not defined
// console.log(age);
let age = 12;
// 不能重复声明
//let age = 13;
console.log(age);
let btns = document.getElementsByTagName('button');
// let 关键字使块级作用域成为可能
for(let i = 0; i<btns.length; i++){
    btns[i].onclick = function () {
        alert(i);
    }
}
```

### const 关键字
* 作用
    * const 用于定义一个常量
* 特点
    * 不能修改
    * 其他特点同let
* 应用
    * 保存不用改变的数据
```js
const sex = '男';
console.log(sex);
// 不能修改 const 关键字定义的变量
// sex = '女';   
console.log(sex);
```