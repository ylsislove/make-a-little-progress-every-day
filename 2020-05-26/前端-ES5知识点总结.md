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


## JSON 对象
### JSON.stringify(obj/arr)
* js 对象或数组转换为 json 对象或数组（字符串）
```js
var obj = {
    name : 'yain',
    age : 39
};
obj = JSON.stringify(obj);
// 打印 string 
console.log(typeof obj);
```

### JSON.parse(json)
* json 对象或数组（字符串）转换为js 对象或数组
```js
var obj = {
    name : 'yain',
    age : 39
};
obj = JSON.stringify(obj);
console.log(typeof obj);
obj = JSON.parse(obj);
console.log(obj);
```


## Object 扩展
ES5 给 Object 扩展了2个常用的静态方法

### Object.create(prototype, [descriptors])
#### 作用
* 以指定对象为原型创建新的对象
* 为新的对象指定新的属性, 并对属性进行描述
    * value : 指定值
    * writable : 标识当前属性值是否是可修改的, 默认为false
    * configurable: 标识当前属性是否可以被删除 默认为false
    * enumerable： 标识当前属性是否能用for in 枚举 默认为false

#### 使用
```js
var obj = {name : 'yain', age : 21}
var obj1 = {};
obj1 = Object.create(obj, {
    sex : {
        value : '男',
        writable : true,
        configurable: true,
        enumerable: true
    }
});
// 打印 男
console.log(obj1.sex);
obj1.sex = '女';
// writable : true，所以会打印 女
console.log(obj1.sex);
// enumerable: true，所以会打印 sex name age
for (var item in obj1) {
    console.log(item);
}
delete obj1.sex;
// configurable: true，所以会打印 undefined
console.log(obj1.sex);
```

### Object.defineProperties(object, descriptors)
#### 作用
* 为指定对象定义扩展多个属性
* get ：用来获取当前属性值得回调函数
* set ：修改当前属性值得触发的回调函数，并且实参即为修改后的值

#### 使用
```js
var obj2 = {
    firstName : 'apple',
    lastName : 'yain'
};
Object.defineProperties(obj2, {
    fullName : {
        get : function () {
            return this.firstName + '-' + this.lastName
        },
        set : function (data) {
            var names = data.split('-');
            this.firstName = names[0];
            this.lastName = names[1];
        }
    }
});
// 打印 apple-yain
console.log(obj2.fullName);
obj2.firstName = 'banana';
obj2.lastName = 'yain';
// 打印 banana-yain
console.log(obj2.fullName);
obj2.fullName = 'orange-yain';
// 设置了set方法，会打印 orange-yain，否则打印 banana-yain
console.log(obj2.fullName);
```

#### 补充
* 对象本身的两个方法
    * get propertyName(){} 用来得到当前属性值的回调函数
    * set propertyName(){} 用来监视当前属性值变化的回调函数
```js
var obj = {
    firstName : 'apple',
    lastName : 'yain',
    get fullName(){
        return this.firstName + '-' + this.lastName;
    },
    set fullName(data){
        var names = data.split('-');
        this.firstName = names[0];
        this.lastName = names[1];
    }
};
// 打印 apple-yain
console.log(obj.fullName);
obj.fullName = 'orange-yain';
// 设置了set方法，会打印 orange-yain，否则打印 apple-yain
console.log(obj.fullName);
```


## Array 扩展
### Array.prototype.indexOf(value)
* 得到值在数组中的第一个下标
```js
var arr = [1, 4, 6, 2, 5, 6];
// 打印 2
console.log(arr.indexOf(6));
```

### Array.prototype.lastIndexOf(value)
* 得到值在数组中的最后一个下标
```js
var arr = [1, 4, 6, 2, 5, 6];
// 打印 5
console.log(arr.lastIndexOf(6));
```

### Array.prototype.forEach(function(item, index){})
* 遍历数组
```js
var arr = [1, 4, 6, 2, 5, 6];
arr.forEach(function (item, index) {
    console.log(item, index);
});
```

### Array.prototype.map(function(item, index){})
* 遍历数组返回一个新的数组，返回加工之后的值
```js
var arr = [1, 4, 6, 2, 5, 6];
var arr1 = arr.map(function (item, index) {
    return item + 10
});
// 打印 [11, 14, 16, 12, 15, 16]
console.log(arr1);
```

### Array.prototype.filter(function(item, index){})
* 遍历过滤出一个新的子数组
```js
var arr = [1, 4, 6, 2, 5, 6];
var arr2 = arr.filter(function (item, index) {
    return item > 4
});
// 打印 [6, 5, 6]
console.log(arr2);
```
