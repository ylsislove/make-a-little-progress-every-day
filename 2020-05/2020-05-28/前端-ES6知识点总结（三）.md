# 前端-ES6知识点总结（三）

## iterator 接口机制
* 概念
    * iterator是一种接口机制，为各种不同的数据结构提供统一的访问机制
    * 其工作原理和 C++ 的 iterator 很相似
* 作用
    * 为各种数据结构，提供一个统一的、简便的访问接口
    * 使得数据结构的成员能够按某种次序排列
    * ES6 创造了一种新的遍历命令 for...of 循环，Iterator 接口主要为 for...of 服务
* 工作原理
    * 创建一个指针对象，指向数据结构的起始位置
    * 第一次调用next方法，指针自动指向数据结构的第一个成员
    * 接下来不断调用next方法，指针会一直往后移动，直到指向最后一个成员
    * 每调用next方法返回的是一个包含value和done的对象，{value: 当前成员的值,done: 布尔值}
        * value表示当前成员的值，done对应的布尔值表示当前的数据的结构是否遍历结束
        * 当遍历结束的时候返回的value值是undefined，done值为false
* 应用
    * Array、arguments、set、map、String 等天然具备 iterator 接口（可用 for...of 遍历）
* 扩展
    * 使用`解构赋值`以及`三点运算符`时会自动调用 iterator 接口
```js
// iterator 原理解析
// 自定义 iterator 生成指针对象
function myIterator(arr) {
    let nextIndex = 0;
    return {
        next: function () {
            return nextIndex < arr.length ? {value: arr[nextIndex++], done: false} : {value: undefined, done: true};
        }
    }
}

let arr = [1, 2, 3];
// 获取迭代器对象
let iteratorObj = myIterator(arr);
// 打印 {value: 1, done: false}
console.log(iteratorObj.next());
// 打印 {value: 2, done: false}
console.log(iteratorObj.next());
// 打印 {value: 3, done: false}
console.log(iteratorObj.next());
// 打印 {value: undefined, done: true}
console.log(iteratorObj.next());

// 原生测试 数组
let arr3 = [1, 2, 'yain', true];
for(let i of arr3){
    console.log(i);
}
// 字符串 string
let str = 'abcdefg';
for(let item of str){
    console.log(item);
}

// 三点运算符
let arr = [2, 3, 4, 5];
let arr2 = [1, ...arr, 6];
// 打印 [1, 2, 3, 4, 5, 6]
console.log(arr2);
```

## Generator 函数
* 概念
    * ES6 提供的解决异步编程的方案之一
    * Generator 函数是一个状态机，内部封装了不同状态的数据，用来生成遍历器对象
    * 也称为可暂停函数(惰性求值)，yield 可暂停，next 方法可启动。每次返回的是 yield 后的表达式结果
* 特点
    1. function 与函数名之间有一个星号
    2. 内部用 yield 表达式来定义不同的状态
    ```js
    // 例如
    function* generatorExample(){
        let result = yield 'hello';  // 状态值为 hello
        yield 'generator'; // 状态值为 generator
    }
    ```
    3. generator 函数返回的是指针对象（刚刚介绍的iterator），而**不会执行函数内部逻辑**
    4. 调用 next 方法函数内部逻辑开始执行，遇到 yield 表达式停止，返回 `{value: yield后的表达式结果/undefined, done: false/true}` 
    5. 再次调用 next 方法会从上一次停止时的 yield 处开始，直到最后
    6. yield 语句返回结果通常为 undefined， 当调用 next 方法时传参内容会作为启动时 yield 语句的返回值
```js
// 小试牛刀
function* generatorTest() {
    console.log('函数开始执行');
    yield 'hello';
    console.log('函数暂停后再次启动');
    let result = yield 'generator';
    // 这里会打印从外部 next 函数传进来的值
    // 打印 我被传进去了
    console.log(result);
    console.log('函数执行完毕');
}
// 生成遍历器对象
let Gt = generatorTest();
// 打印 generatorTest 对象
console.log(Gt);
// 执行函数，遇到yield后即暂停
// 函数执行,遇到yield暂停
let result = Gt.next();
// 打印 {value: "hello", done: false}
console.log(result);
// 函数再次启动
result = Gt.next(); 
// 打印 {value: 'generator', done: false}
console.log(result); 
result = Gt.next('我被传进去了');
// 表示函数内部状态已经遍历完毕
// 打印 {value: undefined, done: true}
console.log(result); 
```