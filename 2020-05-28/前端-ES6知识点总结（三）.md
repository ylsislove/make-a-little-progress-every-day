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
