# 前端-webpack开发环境基本配置

  - [创建配置文件](#%E5%88%9B%E5%BB%BA%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)
  - [打包样式资源](#%E6%89%93%E5%8C%85%E6%A0%B7%E5%BC%8F%E8%B5%84%E6%BA%90)
  - [打包 HTML 资源](#%E6%89%93%E5%8C%85-html-%E8%B5%84%E6%BA%90)
  - [打包图片资源](#%E6%89%93%E5%8C%85%E5%9B%BE%E7%89%87%E8%B5%84%E6%BA%90)
  - [打包其他资源](#%E6%89%93%E5%8C%85%E5%85%B6%E4%BB%96%E8%B5%84%E6%BA%90)
  - [devserver](#devserver)
  - [开发环境配置汇总](#%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE%E6%B1%87%E6%80%BB)

## 创建配置文件
1. 创建文件 webpack.config.js

2. 配置内容如下
    ```js
    // node 内置核心模块，用来处理路径问题
    // resolve 用来拼接绝对路径的方法
    const { resolve } = require('path');

    module.exports = {
        // 入口起点
        entry: './src/js/index.js',
        // 输出
        output: {
            // 输出文件名
            filename: './built.js',
            // 输出路径
            // __dirname nodejs 的变量，代表当前文件的目录绝对路径
            path: resolve(__dirname, 'build/js')
        },
        // 模式
        mode: 'development'
        // mode: 'production'
    }
    ```

3. 运行指令：webpack

4. 结论：此时功能与上节一致


## 打包样式资源
1. 创建 css、less 文件

2. 下载安装 loader 包
    ```bash
    npm i css-loader style-loader less-loader less -D
    ```

3. 修改配置文件

    ```js
    // resolve用来拼接绝对路径的方法
    const { resolve } = require('path');

    module.exports = {
        entry: './src/index.js',
        output: {
            // 输出文件名
            filename: 'built.js',
            // 输出路径
            // __dirname nodejs的变量，代表当前文件的目录绝对路径
            path: resolve(__dirname, 'build')
        },
        // loader的配置
        module: {
            rules: [
                // 详细loader配置
                // 不同的文件必须配置不同的loader处理
                {
                    // 匹配哪些文件
                    test: /\.css$/,
                    // 使用哪些loader进行处理
                    use: [
                        // use数组中loader执行顺序，从右往左，从下到上 依次执行
                        // 创建一个style标签，将js中的样式资源插入进行，添加到head中生效
                        'style-loader',
                        // 将css文件变成commonjs模块加载js中，里面内容是样式字符串
                        'css-loader'
                    ]
                },
                {
                    test: /\.less$/,
                    use: [
                        'style-loader',
                        'css-loader',
                        // 将less文件编译为css文件
                        // 需要下载 less-loader 和 less
                        'less-loader'
                    ]
                }
            ]
        },
        // plugins的配置
        plugins: [
            // 详细plugins的配置
        ],
        // 模式
        mode: 'development'
        // mode: 'production'
    }
    ```

4. 运行指令：webpack


## 打包 HTML 资源
1. 创建 html 文件

2. 下载安装 plugin 包
    ```bash
    npm i html-webpack-plugin -D
    ```

3. 修改配置文件
    ```js
    /**
     * loader: 1.下载 2.使用（配置loader）
     * plugins: 1.下载 2.引入 3.使用
     */
    const { resolve } = require('path');
    const HtmlWebpackPlugin = require('html-webpack-plugin');

    module.exports = {
        entry: './src/index.js',
        output: {
            filename: 'built.js',
            path: resolve(__dirname, 'build')
        },
        module: {
            rules: [
                // loader 的配置
            ]
        },
        plugins: [
            // plugins 的配置
            new HtmlWebpackPlugin({
                // 复制 ./src/index.html 文件，并自动引入打包输出的所有资源（js/css）
                template: './src/index.html'
            })
        ],
        mode: 'development'
    }
    ```

4. 运行指令：webpack


## 打包图片资源
1. 创建 png、jpg 文件

2. 下载安装 loader 包
    ```
    npm i html-loader url-loader file-loader -D
    ```

3. 修改配置文件
    ```js
    const {resolve} = require('path');
    const HtmlWebpackPlugin = require('html-webpack-plugin');

    module.exports = {
        entry: './src/index.js',
        output: {
            filename: 'built.js',
            path: resolve(__dirname, 'build')
        },
        module: {
            rules: [
                {
                    test: /\.less$/,
                    // 要使用多个 loader 处理时用 use
                    use: ['style-loader', 'css-loader', 'less-loader']
                },
                {
                    // 处理图片资源
                    test: /\.(jpg|png|gif)$/,
                    loader: 'url-loader',
                    options: {
                        // 图片大小小于8kb，就会被base64处理
                        // 优点：减少请求数量（减轻服务器压力）
                        // 缺点：图片体积会更大（文件请求速度更慢）
                        limit: 8 * 1024,
                        // 问题：因为url-loader默认使用es6模块化解析，而html-loader引入图片是commonjs
                        // 解析时会出问题：[object Module]
                        // 解决：关闭url-loader的es6模块化，使用commonjs解析
                        esModule: false,
                        // 给图片进行重命名
                        // [hash:10]取图片的hash的前10位
                        // [ext]取文件原来扩展名
                        name: '[hash:10].[ext]'
                    }
                },
                {
                    test: /\.html$/,
                    // 处理 Html 文件中的 img 图片（负责引入 img，从而能被 url-loader 进行处理）
                    loader: 'html-loader'
                }
            ]
        },
        plugins: [
            new HtmlWebpackPlugin({
                template: './src/index.html'
            })
        ],
        mode: 'development'
    };
    ```

4. 运行指令：webpack


## 打包其他资源
1. 创建 ttf、woff、svg、eot 等文件

2. 修改配置文件
    ```js
    const { resolve } = require('path');
    const HtmlWebpackPlugin = require('html-webpack-plugin');

    module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'built.js',
        path: resolve(__dirname, 'build')
    },
    module: {
        rules: [
        {
            test: /\.css$/,
            use: ['style-loader', 'css-loader']
        },
        // 打包其他资源(除了html/js/css资源以外的资源)
        {
            // 排除css/js/html资源
            exclude: /\.(css|js|html|less)$/,
            loader: 'file-loader',
            options: {
            name: '[hash:10].[ext]'
            }
        }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
        template: './src/index.html'
        })
    ],
    mode: 'development'
    };
    ```

3. 运行指令：webpack


## devserver
1. 修改配置文件
    ```js
    const { resolve } = require('path');
    const HtmlWebpackPlugin = require('html-webpack-plugin');

    module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'built.js',
        path: resolve(__dirname, 'build')
    },
    module: {
        rules: [
        {
            test: /\.css$/,
            use: ['style-loader', 'css-loader']
        },
        // 打包其他资源(除了html/js/css资源以外的资源)
        {
            // 排除css/js/html资源
            exclude: /\.(css|js|html|less)$/,
            loader: 'file-loader',
            options: {
            name: '[hash:10].[ext]'
            }
        }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
        template: './src/index.html'
        })
    ],
    mode: 'development',
    // 开发服务器 devServer：用来自动化（自动编译，自动打开浏览器，自动刷新浏览器~~）
    // 特点：只会在内存中编译打包，不会有任何输出
    // 启动 devServer 指令为：npx webpack-dev-server
    devServer: {
        // 项目构建后路径
        contentBase: resolve(__dirname, 'build'),
        // 启动gzip压缩
        compress: true,
        // 端口号
        port: 3000,
        // 自动打开浏览器
        open: true
    }
    };
    ```

2. 运行指令：npx webpack-dev-server


## 开发环境配置汇总
1. 创建文件

    ![文件目录](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200628171251.png)

2. 编辑配置文件
    ```js
    /*
    开发环境配置：能让代码运行
        运行项目指令：
        webpack 会将打包结果输出出去
        npx webpack-dev-server 只会在内存中编译打包，没有输出
    */
    const { resolve } = require('path');
    const HtmlWebpackPlugin = require('html-webpack-plugin');

    module.exports = {
    entry: './src/js/index.js',
    output: {
        filename: 'js/built.js',
        path: resolve(__dirname, 'build')
    },
    module: {
        rules: [
        {
            // 处理less资源
            test: /\.less$/,
            use: ['style-loader', 'css-loader', 'less-loader']
        },
        {
            // 处理css资源
            test: /\.css$/,
            use: ['style-loader', 'css-loader']
        },
        {
            // 处理图片资源
            test: /\.(jpg|png|gif)$/,
            loader: 'url-loader',
            options: {
            limit: 8 * 1024,
            name: '[hash:10].[ext]',
            // 关闭es6模块化
            esModule: false,
            outputPath: 'imgs'
            }
        },
        {
            // 处理html中img资源
            test: /\.html$/,
            loader: 'html-loader'
        },
        {
            // 处理其他资源
            exclude: /\.(html|js|css|less|jpg|png|gif)/,
            loader: 'file-loader',
            options: {
            name: '[hash:10].[ext]',
            outputPath: 'media'
            }
        }
        ]
    },
    plugins: [
        // plugins的配置
        new HtmlWebpackPlugin({
        template: './src/index.html'
        })
    ],
    mode: 'development',
    devServer: {
        contentBase: resolve(__dirname, 'build'),
        compress: true,
        port: 3000,
        open: true
    }
    };
    ```

3. 运行指令：npx webpack-dev-server

