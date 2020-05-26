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


## 变量的解构赋值
### 对象的解构赋值
* 概念
    * 从对象中提取数据, 并赋值给变量(多个)，根据key赋值
* 使用
    * let {n, a} = {n:'tom', a:12}
* 用途
    * 给多个形参赋值
```js
let obj = {name : 'yain', age : 21};
let {age} = obj;
console.log(age);
// 不用解构赋值
function person(p) {
    console.log(p.name, p.age);
}
person(obj);
// 使用解构赋值，其实等价于 {name, age} = obj
function person1({name, age}) {
    console.log(name, age);
}
person1(obj);
```

### 数组的解构赋值
* 概念
    * 从数组中提取数据, 并赋值给变量(多个)，根据下标赋值
* 使用
    * let [a, b] = [1, '2'];
```js
let arr = ['abc', 23, true];
let [, b, c] = arr;
// 打印 23 true
console.log(b, c);
```


## 模板字符串
* 简化字符串的拼接
* 模板字符串必须用``包含（Tab键上方的那个键）
* 变量的变化部分使用${xxx}定义
```js
let obj = { name : 'yain', age : 21 };
// 传统的拼接写法
console.log('我叫：' + obj.name + ', 我的年龄是：' + obj.age);
// 模板字符串写法
console.log(`我叫：${obj.name}, 我的年龄是：${obj.age}`);
```

