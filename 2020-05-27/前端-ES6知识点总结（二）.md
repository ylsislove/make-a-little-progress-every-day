# 前端-ES6知识点总结（二）

## 三点运算符
用来取代 arguments ，但比 arguments 灵活，只能放在形参的最后
```js
function fun(...values) {
    console.log(arguments);
    // arguments 是伪数组，没有 forEach 函数
    // arguments.forEach(function (item, index) {
    //     console.log(item, index);
    // });
    // 取代 arguments，是真正的数组
    console.log(values);
    values.forEach(function (item, index) {
        console.log(item, index);
    })
}
fun(1, 2, 3);

let arr = [2, 3, 4];
let arr1 = [1, ...arr, 5];
// 打印 [1, 2, 3, 4, 5]
console.log(arr1);
// 打印 1 2 3 4 5
console.log(...arr1);
```


## 形参默认值
形参的默认值----当不传入参数的时候默认使用形参里的默认值
```js
//定义一个点的坐标
function Point(x = 0, y = 0) {
    this.x = x;
    this.y = y;
}

// 打印 Point {x: 25, y: 36}
let point = new Point(25, 36);
console.log(point);

// 打印 Point {x: 0, y: 0}
let p = new Point();
console.log(p);
```

## Promise 对象
* 概念
    * 代表了未来某个将要发生的事件(通常是一个异步操作)
    * 有了 promise 对象, 可以将异步操作以同步的流程表达出来, 避免了层层嵌套的回调函数（俗称'回调地狱'）
    * ES6 的 Promise 是一个构造函数, 用来生成 promise 实例
* 创建 promise 的基本步骤
    * 创建 promise 对象
    * 调用 promise 的 then()
* promise 对象的三个状态
    * pending: 初始化状态
    * fullfilled: 成功状态
    * rejected: 失败状态
* 应用
    * 使用 promise 实现超时处理
    * 使用 promise 封装处理 ajax 请求
```js
// 创建一个 promise 实例对象
let promise = new Promise((resolve, reject) => {
    // 初始化 promise 的状态为 pending ----> 初始化状态
    // 同步操作
    console.log('1111');
    // 启动异步任务
    setTimeout(() => {
        console.log('3333');
        // 根据异步任务的返回结果去修改 promise的状态
        if (Math.random() > 0.5) {
            // 修改 promise 的状态 pending ----> fullfilled（成功状态）
            resolve('success');
        } else {
            // 修改 promise 的状态 pending ----> rejected（失败状态）
            reject('fail');
        }
    }, 1000)
});
promise.then((data) => {
    console.log('成功了 ' + data);
}, (error) => {
    console.log('失败了 ' + error);
});
console.log('2222');
```


## Promise 应用案例
* 需求
    * 向服务器请求新闻内容
    * 成功后，再向服务器请求评论信息
* 实现
    * 使用 promise 封装处理 ajax 请求
```js
// 定义一个请求 news 的方法
function getNews(url) {
    //创建一个 promise 对象
    let promise = new Promise((resolve, reject) => {
        //初始化 promise 状态为 pending
        //启动异步任务
        let request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if(request.readyState === 4) {
                if(request.status === 200) {
                    let news = request.response;
                    resolve(news);
                } else{
                    reject('暂时没有新闻内容');
                }
            }
        };
        request.responseType = 'json'; // 设置返回的数据类型
        request.open("GET", url); // 设置请求的方法和url
        request.send(); // 发送
    })
    return promise;
}

// 这儿 then 的连续使用体现了 promise 可以将异步操作以同步的流程表达出来
getNews('http://localhost:3000/news?id=2')
        .then((news) => {
            console.log(news);
            document.write(JSON.stringify(news));
            console.log('http://localhost:3000' + news.commentsUrl);
            // 再次请求评论信息
            return getNews('http://localhost:3000' + news.commentsUrl);
        }, (error) => {
            alert(error);
        })
        .then((comments) => {
            console.log(comments);
            document.write('<br><br><br><br><br>' + JSON.stringify(comments));
        }, (error) => {
            alert(error);
        })
```

