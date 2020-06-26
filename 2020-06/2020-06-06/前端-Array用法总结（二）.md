# 前端-Array用法总结（二）

## bifurcate
* 描述
    * 把集合里面的元素分成两组。如果 `filter` 中的一个元素为真值时，在集合中与之相对应的元素就划分到第一组，否则就属于第二组。
* 提示
    * 使用 `Array.prototype.reduce()` 和 `Array.prototype.push()` 把集合中的元素添加到对应的分组中。
    * `filter` 需和集合中的元素保持一一对应。
* 代码
    ```js
    const bifurcate = (arr, filter) => arr.reduce(
        (acc, val, i) => {
            acc[filter[i] ? 0 : 1].push(val);
            return acc;
        },
        [[], []]
    );
    ```
* 示例
按照指定规则为集合中的元素分类：
```js
// 打印 [ [ 'beep', 'boop', 'bar' ], [ 'foo' ] ]
console.log(bifurcate(['beep', 'boop', 'foo', 'bar'], [true, true, false, true]));
```

## bifurcateBy
* 描述
    * 使用函数把集合中的元素分为两组，可通过函数来指定输入其中的元素被划分到哪一组。如果该函数返回真值，集合中的元素就属于第一组，否则就属于第二组。
* 提示
    * 使用 `Array.prototype.reduce()` 和 `Array.prototype.push()` 把元素添加到不同的组中。
    * 根据集合中的每一个元素在 `fn` 中的返回值来进行分组。
* 代码
    ```js
    const bifurcateBy = (arr, fn) => arr.reduce(
        (acc, val, i) => {
            acc[fn(val, i) ? 0 : 1].push(val);
            return acc;
        },
        [[], []]
    );
    ```
* 示例
    ```js
    // 打印 [ [ 'beep', 'boop', 'bar' ], [ 'foo' ] ]
    console.log(bifurcateBy(['beep', 'boop', 'foo', 'bar'], x => x[0] === 'b'));
    ```

