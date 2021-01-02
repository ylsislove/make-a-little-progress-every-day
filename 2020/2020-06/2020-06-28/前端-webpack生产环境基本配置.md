# 前端-webpack生产环境基本配置

  - [提取 css 成单独文件](#%E6%8F%90%E5%8F%96-css-%E6%88%90%E5%8D%95%E7%8B%AC%E6%96%87%E4%BB%B6)
  - [css 兼容性处理](#css-%E5%85%BC%E5%AE%B9%E6%80%A7%E5%A4%84%E7%90%86)
  - [压缩 css](#%E5%8E%8B%E7%BC%A9-css)
  - [js 语法检查](#js-%E8%AF%AD%E6%B3%95%E6%A3%80%E6%9F%A5)
  - [js 兼容性处理](#js-%E5%85%BC%E5%AE%B9%E6%80%A7%E5%A4%84%E7%90%86)
  - [js 压缩](#js-%E5%8E%8B%E7%BC%A9)
  - [HTML 压缩](#html-%E5%8E%8B%E7%BC%A9)
  - [生产环境配置汇总](#%E7%94%9F%E4%BA%A7%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE%E6%B1%87%E6%80%BB)

## 提取 css 成单独文件

1. 下载 plugin
    ```bash
    npm i mini-css-extract-plugin -D
    ```

2. 修改配置文件
    ```js
    const { resolve } = require('path');
    const HtmlWebpackPlugin = require('html-webpack-plugin');
    const MiniCssExtractPlugin = require('mini-css-extract-plugin');

    module.exports = {
        entry: './src/js/index.js',
        output: {
            filename: 'js/built.js',
            path: resolve(__dirname, 'build')
        },
        module: {
            rules: [
                {
                    test: /\.css$/,
                    use: [
                        // 这个 loader 取代 style-loader。作用：提取 js 中的 css 成单独文件
                        MiniCssExtractPlugin.loader,
                        // 将 css 文件整合到 js 文件中
                        'css-loader'
                    ]
                }
            ]
        },
        plugins: [
            new HtmlWebpackPlugin({
                template: './src/index.html'
            }),
            new MiniCssExtractPlugin({
                // 对输出的css文件进行重命名
                filename: 'css/built.css'
            })
        ],
        mode: 'development'
    };
    ```

3. 运行指令：webpack


## css 兼容性处理

1. 下载 loader
    ```bash
    npm i postcss-loader postcss-preset-env -D
    ```

2. 修改配置文件
    ```js
    const { resolve } = require('path');
    const HtmlWebpackPlugin = require('html-webpack-plugin');
    const MiniCssExtractPlugin = require('mini-css-extract-plugin');

    // 设置nodejs环境变量
    // process.env.NODE_ENV = 'development';

    module.exports = {
        entry: './src/js/index.js',
        output: {
            filename: 'js/built.js',
            path: resolve(__dirname, 'build')
        },
        module: {
            rules: [
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    // 修改 loader 的配置
                    {
                        loader: 'postcss-loader',
                        options: {
                            ident: 'postcss',
                            plugins: () => [
                                // postcss 的插件
                                require('postcss-preset-env')()
                            ]
                        }
                    }
                ]
            }
            ]
        },
        plugins: [
            new HtmlWebpackPlugin({
            template: './src/index.html'
            }),
            new MiniCssExtractPlugin({
            filename: 'css/built.css'
            })
        ],
        mode: 'development'
    };
    ```

3. 修改 package.json，添加如下配置
    ```json
    "browserslist": {
        "development": [
            "last 1 chrome version",
            "last 1 firefox version",
            "last 1 safari version"
        ],
        "production": [
            ">0.2%",
            "not dead",
            "not op_mini all"
        ]
    }
    ```

4. 运行指令：webpack


## 压缩 css

1. 下载 plugin
    ```bash
    npm i optimize-css-assets-webpack-plugin -D
    ```

2. 修改配置文件
    ```js
    const { resolve } = require('path');
    const HtmlWebpackPlugin = require('html-webpack-plugin');
    const MiniCssExtractPlugin = require('mini-css-extract-plugin');
    const OptimizeCssAssetsWebpackPlugin = require('optimize-css-assets-webpack-plugin')

    // 设置nodejs环境变量
    // process.env.NODE_ENV = 'development';

    module.exports = {
        entry: './src/js/index.js',
        output: {
            filename: 'js/built.js',
            path: resolve(__dirname, 'build')
        },
        module: {
            rules: [
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    {
                        loader: 'postcss-loader',
                        options: {
                            ident: 'postcss',
                            plugins: () => [
                                // postcss的插件
                                require('postcss-preset-env')()
                            ]
                        }
                    }
                ]
            }
            ]
        },
        plugins: [
            new HtmlWebpackPlugin({
                template: './src/index.html'
            }),
            new MiniCssExtractPlugin({
                filename: 'css/built.css'
            }),
            // 压缩css
            new OptimizeCssAssetsWebpackPlugin()
        ],
        mode: 'development'
    };
    ```

3. 运行指令：webpack


## js 语法检查

1. 下载安装包
    ```bash
    npm i eslint-loader eslint eslint-config-airbnb-base eslint-plugin-import -D
    ```

2. 修改配置文件
    ```js
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
                test: /\.js$/,
                // 注意：只检查自己写的源代码，第三方的库是不用检查的
                exclude: /node_modules/,
                loader: 'eslint-loader',
                options: {
                    // 自动修复 eslint 的错误
                    fix: true
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

3. 配置 package.json
    ```json
    "eslintConfig": {
        "extends": "airbnb-base"
    }
    ```

4. 运行指令：webpack


## js 兼容性处理

1. 下载安装包
    ```bash
    npm i babel-loader @babel/core @babel/preset-env @babel/polyfill core-js -D
    ```

2. 修改配置文件
    ```js
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
            /*
                js兼容性处理：babel-loader @babel/core 
                1. 基本js兼容性处理 --> @babel/preset-env
                    问题：只能转换基本语法，如promise高级语法不能转换
                2. 全部js兼容性处理 --> @babel/polyfill  
                    问题：我只要解决部分兼容性问题，但是将所有兼容性代码全部引入，体积太大了~
                3. 需要做兼容性处理的就做：按需加载  --> core-js
            */  
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                options: {
                // 预设：指示babel做怎么样的兼容性处理
                presets: [
                    [
                        '@babel/preset-env',
                        {
                            // 按需加载
                            useBuiltIns: 'usage',
                            // 指定core-js版本
                            corejs: {
                                version: 3
                            },
                            // 指定兼容性做到哪个版本浏览器
                            targets: {
                                chrome: '60',
                                firefox: '60',
                                ie: '9',
                                safari: '10',
                                edge: '17'
                            }
                        }
                    ]
                ]
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


## js 压缩

生产环境会自动压缩 js 代码。所以只需更改 mode 为 production 即可。如下

```js
const { resolve } = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/js/index.js',
  output: {
    filename: 'js/built.js',
    path: resolve(__dirname, 'build')
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html'
    })
  ],
  // 生产环境下会自动压缩js代码
  mode: 'production'
};
```

运行指令：webpack


## HTML 压缩

1. 修改配置文件
    ```js
    const { resolve } = require('path');
    const HtmlWebpackPlugin = require('html-webpack-plugin');

    module.exports = {
        entry: './src/js/index.js',
        output: {
            filename: 'js/built.js',
            path: resolve(__dirname, 'build')
        },
        plugins: [
            new HtmlWebpackPlugin({
                template: './src/index.html',
                // 压缩html代码
                minify: {
                    // 移除空格
                    collapseWhitespace: true,
                    // 移除注释
                    removeComments: true
                }
            })
        ],
        mode: 'production'
    };
    ```

2. 运行指令：webpack


## 生产环境配置汇总
```js
const { resolve } = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCssAssetsWebpackPlugin = require('optimize-css-assets-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

// 定义nodejs环境变量：决定使用browserslist的哪个环境
process.env.NODE_ENV = 'production';

// 复用loader
const commonCssLoader = [
  MiniCssExtractPlugin.loader,
  'css-loader',
  {
    // 还需要在package.json中定义browserslist
    loader: 'postcss-loader',
    options: {
      ident: 'postcss',
      plugins: () => [require('postcss-preset-env')()]
    }
  }
];

module.exports = {
  entry: './src/js/index.js',
  output: {
    filename: 'js/built.js',
    path: resolve(__dirname, 'build')
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [...commonCssLoader]
      },
      {
        test: /\.less$/,
        use: [...commonCssLoader, 'less-loader']
      },
      /*
        正常来讲，一个文件只能被一个loader处理。
        当一个文件要被多个loader处理，那么一定要指定loader执行的先后顺序：
          先执行eslint 在执行babel
      */
      {
        // 在package.json中eslintConfig --> airbnb
        test: /\.js$/,
        exclude: /node_modules/,
        // 优先执行
        enforce: 'pre',
        loader: 'eslint-loader',
        options: {
          fix: true
        }
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        options: {
          presets: [
            [
              '@babel/preset-env',
              {
                useBuiltIns: 'usage',
                corejs: {version: 3},
                targets: {
                  chrome: '60',
                  firefox: '50'
                }
              }
            ]
          ]
        }
      },
      {
        test: /\.(jpg|png|gif)/,
        loader: 'url-loader',
        options: {
          limit: 8 * 1024,
          name: '[hash:10].[ext]',
          outputPath: 'imgs',
          esModule: false
        }
      },
      {
        test: /\.html$/,
        loader: 'html-loader'
      },
      {
        exclude: /\.(js|css|less|html|jpg|png|gif)/,
        loader: 'file-loader',
        options: {
          outputPath: 'media'
        }
      }
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'css/built.css'
    }),
    new OptimizeCssAssetsWebpackPlugin(),
    new HtmlWebpackPlugin({
      template: './src/index.html',
      minify: {
        collapseWhitespace: true,
        removeComments: true
      }
    })
  ],
  mode: 'production'
};
```