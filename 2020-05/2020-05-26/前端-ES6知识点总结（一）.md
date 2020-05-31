# 前端-ES6知识点总结（一）

  - [let 和 const 关键字](#let-%E5%92%8C-const-%E5%85%B3%E9%94%AE%E5%AD%97)
    - [let 关键字](#let-%E5%85%B3%E9%94%AE%E5%AD%97)
    - [const 关键字](#const-%E5%85%B3%E9%94%AE%E5%AD%97)
  - [变量的解构赋值](#%E5%8F%98%E9%87%8F%E7%9A%84%E8%A7%A3%E6%9E%84%E8%B5%8B%E5%80%BC)
    - [对象的解构赋值](#%E5%AF%B9%E8%B1%A1%E7%9A%84%E8%A7%A3%E6%9E%84%E8%B5%8B%E5%80%BC)
    - [数组的解构赋值](#%E6%95%B0%E7%BB%84%E7%9A%84%E8%A7%A3%E6%9E%84%E8%B5%8B%E5%80%BC)
  - [模板字符串](#%E6%A8%A1%E6%9D%BF%E5%AD%97%E7%AC%A6%E4%B8%B2)
  - [简化的对象写法](#%E7%AE%80%E5%8C%96%E7%9A%84%E5%AF%B9%E8%B1%A1%E5%86%99%E6%B3%95)
  - [箭头函数](#%E7%AE%AD%E5%A4%B4%E5%87%BD%E6%95%B0)

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
// let age = 13;
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


## 简化的对象写法
* 省略同名的属性值
* 省略方法的function
```js
let name = 'yain';
let age = 21;
// 普通的写法
let obj = {
    name : name,
    age : age,
    getName : function () {
        return this.name;
    }
};
console.log(obj);
// 简化的写法
let obj1 = {
    name,
    age,
    getName(){
        return this.name;
    }
};
console.log(obj1);
console.log(obj1.getName());
```


## 箭头函数
* 作用
    * 定义匿名函数
* 基本语法
    * 没有参数：() => console.log('xxxx')
    * 一个参数：i => i+2
    * 大于一个参数：(i,j) => i+j
    * 函数体不用大括号：默认返回结果
    * 函数体如果有多个语句, 需要用{}包围，若有需要返回的内容，需要手动返回
* 特点
    * 语法更加简介
    * 箭头函数没有自己的 this，箭头函数的 this 不是调用的时候决定的，而是在定义的时候处在的对象就是它的 this
    * 扩展理解：箭头函数的 this 看外层的是否有函数，如果有，外层函数的this就是内部箭头函数的 this，如果没有，则 this 是window
* 应用场景
    * 多用来定义回调函数
```js
// 函数的普通定义方式
let fun = function () {
    console.log('fun()');
};
// 打印 fun()
fun();

// 没有形参，并且函数体只有一条语句
let fun1 = () => console.log('fun1()');
// 打印 fun1() undefined
console.log(fun1());

// 一个形参，并且函数体只有一条语句
let fun2 = x => x;
// 函数体没有使用大括号，默认返回结果。打印 5
console.log(fun2(5));

// 形参是一个以上
let fun3 = (x, y) => x + y;
// 打印 20
console.log(fun3(5, 15));

// 函数体有多条语句
let fun4 = (x, y) => {
    return x + y;
};
// 打印 10
console.log(fun4(4, 6));

// 打印 定时函数：window
setTimeout(() => {
    console.log("定时函数：", this);
},1000)

let btn = document.getElementById('btn');
// 普通方式定义的函数，this 是在调用时决定的
btn.onclick = function () {
    // 打印 btn
    console.log(this);
};

// 箭头函数，this 是在定义时的环境决定的
let btn2 = document.getElementById('btn2');
btn2.onclick = () => {
    // 打印 window
    console.log(this);
};

let btn3 = document.getElementById('btn3');
let obj = {
    name : 'yain',
    age : 21,
    getName : () => {
        btn3.onclick = () => {
            // 打印 window
            console.log(this);
        };
    }
};
obj.getName();

function Person() {
    this.obj = {
        showThis : () => {
            // 打印 Person{...}
            console.log(this);
        }
    }
}
let fun5 = new Person();
fun5.obj.showThis();
```

