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

## 对象的 Symbol.iterator 属性
之前介绍 iterator 的时候，说过只有 Array、arguments、set、map、String 等天然具备 iterator 接口。也就是说，对象默认没有 iterator 接口，不能使用 for...of 遍历。但是，我们可以借助 Symbol 数据类型为对象添加一个 iterator 接口。
```js
// 对象的 Symbol.iterator 属性;
let myIterable = {};
// 为对象添加 Symbol.iterator 属性，指向一个 generator 函数
// generator 函数返回一个迭代器对象
myIterable[Symbol.iterator] = function* () {
    yield 1;
    yield 2;
    yield 4;
};
// 对象可以被迭代
for(let i of myIterable){
    console.log(i);
}
// 也可以使用三点运算符
let obj = [...myIterable];
// 打印 Array(3)
console.log(obj);
```

## Generator 应用案例
之前介绍 Promise 的时候，介绍过如何用 Promise 封装处理 ajax 请求。这里可以用 Generator 函数来实现一下。
* 需求
    1. 发送ajax请求获取新闻内容
    2. 新闻内容获取成功后再次发送请求，获取对应的新闻评论内容
    3. 新闻内容获取失败则不需要再次发送请求
```js
// 发送 get 请求
function getNews(url) {
    $.get(url, function (data) {
        console.log(data);
        let commentsUrl = data.commentsUrl;
        let url = 'http://localhost:3000' + commentsUrl;
        // 当获取新闻内容成功，发送请求获取对应的评论内容
        // 调用next传参会作为上次暂停是yield的返回值
        sx.next(url);
    })
}
// 声明一个 Generator 函数，里面有两个状态，获取新闻内容的状态和获取评论的状态
function* sendXml() {
    // url为next传参进来的数据
    let url = yield getNews('http://localhost:3000/news?id=2');
    yield getNews(url);
}

// 得到迭代器对象
let sx = sendXml();
// 发送请求获取新闻内容
sx.next();
```

## async 函数
* 概念
    * 真正意义上去解决异步回调的问题，同步流程表达异步操作
* 本质
    * Generator的语法糖
* 语法
    ```js
    async function foo(){
        await 异步操作;
        await 异步操作；
    }
    ```
* 特点
    * 不需要像 Generator 去调用next方法，遇到 await 等待，当前的异步操作完成就往下执行
    * 返回的总是 Promise 对象，可以用 then 方法进行下一步操作
    * async 取代 Generator 函数的星号 *，await 取代 Generator 的 yield
    * 语意更为明确
```js
// 一个异步任务
async function timeout(ms) {
    return new Promise(resolve => {
        setTimeout(resolve, ms);
    });
}
// 使用 async 函数去执行
// 遇到 await 等待，执行完毕后自动执行下一步的操作
async function asyncPrint(value, ms) {
    console.time('运算时间：')
    await timeout(ms);
    console.timeEnd('运算时间：')
    console.log(value);
}
// 打印 Promise {<pending>}
console.log(asyncPrint('hello async', 2000));

// 如果 promise 的状态是失败，则不会执行下面的操作
async function awaitTest() {
    let result = await Promise.resolve('执行成功');
    // 打印 执行成功
	console.log(result);
	// 控制台爆红，打印 Uncaught (in promise) 执行失败
    let result2 = await Promise.reject('执行失败');
    // 执行不了
    console.log(result2);
    let result3 = await Promise.resolve('还想执行一次');
    console.log(result3);
}
awaitTest();
```

## async 应用案例
依旧是那个获取新闻内容和评论的案例
* 需求
    1. 发送ajax请求获取新闻内容
    2. 新闻内容获取成功后再次发送请求，获取对应的新闻评论内容
    3. 新闻内容获取失败则不需要再次发送请求
```js
// 案例演示
async function sendXml(url) {
    return new Promise((resolve, reject) => {
        $.ajax({
            url,
            type: 'GET',
            success: data =>  resolve(data),
            error: error => reject(error)
        })
    });
}
async function getNews(url) {
    let data = await sendXml(url);
    console.log(data);
    data = await sendXml('http://localhost:3000' + data.commentsUrl);
    console.log(data);
}
getNews('http://localhost:3000/news?id=2')
```