# 前端-JS中唯一自己不等于自己的值是谁？

  - [答案](#%E7%AD%94%E6%A1%88)
  - [`isNaN()` 和 `Number.isNaN()`的区别](#isnan-%E5%92%8C-numberisnan%E7%9A%84%E5%8C%BA%E5%88%AB)
    - [isNaN](#isnan)
    - [Number.isNaN](#numberisnan)
    - [二者的区别](#%E4%BA%8C%E8%80%85%E7%9A%84%E5%8C%BA%E5%88%AB)
  - [小彩蛋](#%E5%B0%8F%E5%BD%A9%E8%9B%8B)
    - [ES6 Object.is() 的使用](#es6-objectis-%E7%9A%84%E4%BD%BF%E7%94%A8)
    - [`Object.is()` 与 `===` 的区别](#objectis-%E4%B8%8E--%E7%9A%84%E5%8C%BA%E5%88%AB)

## 答案
`NaN (Not a Number)` 无论使用什么比较运算符进行比较时，他是唯一不等于自身的值。`NaN` 通常是没有意义的数学计算的结果，因此两个 `NaN` 值被认为相等是没有意义的。

## `isNaN()` 和 `Number.isNaN()`的区别

### isNaN
当我们向 isNaN 传递一个参数，它的本意是通过 Number() 方法尝试将这参数转换成 Number 类型，如果成功返回 false，如果失败返回 true。所以 isNaN 只是判断传入的参数是否能转换成数字，并不是严格的判断是否等于 NaN。
```js
// 输出 NaN
Number('测试') 
// true
console.log(isNaN('测试')) 
```

### Number.isNaN
判断传入的参数是否严格的等于NaN(也就是 ===)。
那一般在什么情况下会用到Number.isNaN呢？
当两个变量进行运算时，我们可以使用Number.isNaN来判断它的值是否为NaN。
```js
// 输出 true
console.log(Number.isNaN(1/'测试')); 
```

### 二者的区别
Number.isNaN与isNaN最的区别是，Number.isNaN不存在类型转换的行为。
```js
isNaN(NaN);         // true
isNaN('A String');  // true
isNaN(undefined);   // true
isNaN({});          // true
Number.isNaN(NaN);          // true
Number.isNaN('A String');   // false
Number.isNaN(undefined);    // false
Number.isNaN({});           // false
```

## 小彩蛋
使用 ES6 的 `Object.is` 方法时，`NaN` 终于等于了自己。

### ES6 Object.is() 的使用
* 定义：方法判断两个值是否是相同的值
* 语法：Object.is(value1, value2)
    * value1：第一个需要比较的值
    * value2：第二个需要比较的值
* 返回值：表示两个参数是否相同的布尔值
```js
Object.is('foo', 'foo');     // true
Object.is(window, window);   // true

Object.is('foo', 'bar');     // false
Object.is([], []);           // false

var foo = { a: 1 };
var bar = { a: 1 };
Object.is(foo, foo);         // true
Object.is(foo, bar);         // false

Object.is(null, null);       // true

// 特例
Object.is(0, -0);            // false
Object.is(-0, -0);           // true
Object.is(NaN, 0/0);         // true
```

### `Object.is()` 与 `===` 的区别
```js
+0 === -0           // true
NaN === NaN         // false

Object.is(+0, -0)   // false
Object.is(NaN, NaN) // true
```