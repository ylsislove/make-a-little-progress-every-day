# 前端-Array用法总结（一）

## all
* 描述
    * 当提供的断言函数对集合中的所有元素都返回 `true` 时，就返回  `true`，否则返回 `false`
* 提示
    * 使用 `Array.prototype.every()` 来测试集合中的所有元素在 `fn` 中是否返回 `true`
    * 第二个参数为 `fn`，可使用 `Boolean` 作为默认值
* 代码
    ```js
    const all = (arr, fn = Boolean) => arr.every(fn);
    ```
* 示例
    * 检测数组中的每一个元素是否都满足条件：
    ```js
    // true
    console.log(all([1, 2, 3]));
    // false
    console.log(all([1, 2, 3, 4], x => x > 2));
    ```

## allEqual
* 描述
    * 检测数组中的元素是否都相等
* 提示
    * 使用 `Array.prototype.every()` 检测数组中的所有元素是否和第一个元素相等
* 代码
    ```js
    const allEqual = arr => arr.every(val => val === arr[0]);
    ```
* 示例
    * 检测数组中的元素是否都相等
    ```js
    // false
    console.log(allEqual([1, 2, 1]));
    // true
    console.log(allEqual([1, 1, 1, 1]));
    ```

## any
* 描述
    * 如果提供的函数对集合中的任意一个元素返回 `true`，那么就返回 `true`，否则返回 `false`
* 提示
    * 使用 `Array.prototype.some()` 进行检测，如果 `fn` 对集合中的任意元素返回 `true`，那么就返回 `true`
    * 第二个参数为 `fn`，默认值为 `Boolean`
* 代码
    ```js
    const any = (arr, fn = Boolean) => arr.some(fn);
    ```
* 示例
    检测数组中的元素是否有满足条件的
    ```js
    // false
    console.log(any([1, 2, 1], x => x > 5));
    // true
    console.log(any([1, 2, 3, 10], x => x > 5));
    ```

## arrayToCSV
* 描述
    * 把一个二维数组转换为使用逗号分隔符（CSV）的字符串
* 提示
    * 使用 `Array.prototype.map()` 和 `Array.prototype.join(delimiter)` 把一维数组转换为使用逗号分割的字符串
    * 使用 `Array.prototype.join('\n')` 将二维数组中的行组合为 CSV 字符串，每一行都使用换行符作为分割
    * 第二个参数 `delimiter` 可省略，默认值为 `,`
* 代码
    ```js
    const arrayToCSV = (arr, delimiter = ',') => arr.map(
        // 遍历每层数组
        v => v.map(
            // 遍历每一个元素
            x => isNaN(x) ? `"${x.replace(/"/g, '""')}"` : x
        ).join(delimiter)
    ).join('\n');
    ```
* 示例
    * 将一个二维数组按照指定的规则转换为字符串
    ```js
    // 打印 "a","b"\n"c","d"
    console.log(arrayToCSV([
        ['a', 'b'], 
        ['c', 'd']
    ]));

    // 打印 "a";"b"\n"c";"d"
    console.log(arrayToCSV([
        ['a', 'b'], 
        ['c', 'd']
    ], ';'));

    // 打印 "a","""b"" great"\n"c",3.1415926
    console.log(arrayToCSV([
        ['a', '"b" great'], 
        ['c', 3.1415926]
    ]));
    ```