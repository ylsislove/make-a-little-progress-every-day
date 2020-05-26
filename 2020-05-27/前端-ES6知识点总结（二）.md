# 前端-ES6知识点总结（二）

## 三点运算符
* 作用
    * 用来取代 arguments ，但比 arguments 灵活，只能放在形参的最后
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

