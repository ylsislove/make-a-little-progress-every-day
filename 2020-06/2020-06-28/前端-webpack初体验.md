# 前端-webpack初体验

  - [初始化配置](#%E5%88%9D%E5%A7%8B%E5%8C%96%E9%85%8D%E7%BD%AE)
  - [编译打包应用](#%E7%BC%96%E8%AF%91%E6%89%93%E5%8C%85%E5%BA%94%E7%94%A8)

## 初始化配置

1. 初始化 package.json

    ```bash
    npm init
    ```

2. 下载并安装 webpack

    ```bash
    npm install webpack webpack-cli -g
    npm install webpack webpack-cli -D
    ```

## 编译打包应用

1. 创建文件

2. 运行文件

    开发环境指令：webpack src/js/index.js -o build/js/built.js --mode=development

    功能：webpack 能够编译打包 js 和 json 文件，并且能将 es6 的模块化语法转换成浏览器能识别的语法

    生产环境指令：webpack src/js/index.js -o build/js/built.js --mode=production

    功能：在开发配置功能上多一个功能，压缩代码

3. 结论

    webpack 能够编译打包 js 和 json 文件。

    能将 es6 的模块化语法转换成浏览器能识别的语法。

    能压缩代码

4. 问题

    不能编译打包 css、img 等文件。

    不能将 js 的 es6 基本语法转换为 es5 以下语法。

