# Cesium1.74+Vue2.6.12环境搭建

  - [环境介绍](#%E7%8E%AF%E5%A2%83%E4%BB%8B%E7%BB%8D)
  - [创建一个 Vue 项目](#%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA-vue-%E9%A1%B9%E7%9B%AE)
  - [项目代码结构介绍](#%E9%A1%B9%E7%9B%AE%E4%BB%A3%E7%A0%81%E7%BB%93%E6%9E%84%E4%BB%8B%E7%BB%8D)
  - [安装 Cesium 环境](#%E5%AE%89%E8%A3%85-cesium-%E7%8E%AF%E5%A2%83)
  - [设置 webpack 配置项，使其支持 cesium](#%E8%AE%BE%E7%BD%AE-webpack-%E9%85%8D%E7%BD%AE%E9%A1%B9%E4%BD%BF%E5%85%B6%E6%94%AF%E6%8C%81-cesium)
  - [编写Vue组件](#%E7%BC%96%E5%86%99vue%E7%BB%84%E4%BB%B6)
  - [禁用 ESLint 代码检查](#%E7%A6%81%E7%94%A8-eslint-%E4%BB%A3%E7%A0%81%E6%A3%80%E6%9F%A5)
  - [npm run dev 运行项目](#npm-run-dev-%E8%BF%90%E8%A1%8C%E9%A1%B9%E7%9B%AE)

## 环境介绍
| 项目环境 | 版本 | 命令 |
| ------- | ----- | --- |
| NodeJs | v12.18.3 | node --version |
| Npm | v6.14.6 | npm -v |
| vue/cli | v4.5.6 | vue --version |
| vue | v2.6.12 | npm list vue |
| webpack | v3.12.0 | npm list webpack |
| cesium | v1.74.0 | npm list cesium |

## 创建一个 Vue 项目
1. 全局安装 vue/cli 和 vue/cli-init

    ```bash
    npm install -g @vue/cli
    npm install -g @vue/cli-init
    ```
2. 创建一个基于 webpack 模板的的新项目 到当前目录的 cesiumlearn 文件夹中

    ```bash
    vue init webpack cesiumlearn
    ```

3. 填写项目相关参数

    ![项目相关参数](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201010140835.png)

4. 运行项目

    等待第三方 node 包下载完成，即可尝试运行项目。若下载速度慢，可以尝试去配置阿里淘宝的镜像源，或自己搭个梯子 😏

    ```bash
    cd cesiumlearn
    npm run dev
    ```

    ![编译完成](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201010142631.png)

    项目默认运行在 localhost:8080 地址上，若端口被占用，则会自动运行在 8081 端口上。输入网址即可看见 Vue 网页，说明 Vue 环境配好了

    ![初始界面](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201010142527.png)

## 项目代码结构介绍
- README.md：项目的说明文件
- package.json：依赖包，存放第三方模块依赖
- package-lock.json：package 的一个锁文件，帮助确定安装的第三方包版本，保证团队编程的统一
- LICENSE：开源协议的说明
- index.html：项目默认的首页模板文件
- .postcssrc.js：对 postcss 的一个配置项
- .gitignore：配置不想上传到线上的文件内容，里面的所提到的文件不会被提交到仓库之中
- .esclintrc.js：配置代码的规范，检测代码是否写的标准
- .eslintignore：里面的所提到的文件，不会受到 esclintrc.js 的代码规范的检测
- .editorconfig：配置编辑器中的语法，统一编辑器的自动化的代码格式化
- .babelrc：项目是 vue 单文件组件的写法，babelrc 语法解析器进行语法上的转换 转换成浏览器可以编译执行的代码
- static 目录下：存放静态资源，静态图片，json数据
- node_modules 目录下：项目依赖的第三方的 node 包
- src 目录下：存放整个项目的源代码，进行业务代码开发
    - main.js：项目的入口文件
    - App.vue：项目最原始的根组件
    - router/index.js：存放路由
    - components文件夹：存放项目中要用到的小组件
    - assets文件夹：存放项目中用到的图片类的资源
- config 文件夹：存放项目的配置文件
    - index.js：存放基础的配置信息
    - dev.env.js：开发环境的配置信息
    - prod.env.js：线上环境的配置信息
- build 目录下：项目打包的 webpack 配置的一些内容，vue-cli 自动构建好的 webpack 的集合
    - webpack.base.conf.js：基础的 webpack 配置项
    - webpack.dev.conf.js：开发环境中的 webpack 配置项
    - webpack.prod.conf.js：线上环境的 webpack 配置项

## 安装 Cesium 环境
1. 下载

    ```bash
    npm install cesium
    ```

2. 手动复制 Cesium 编译好的静态文件到 static 文件夹下

    进入 node_modules\cesium\Build 文件夹中，将编译好的Cesium 文件夹复制到根目录下的 static 中，并把其中 Cesium.js 删除，如下图所示

    ![复制后的目录结构](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201010143514.png)

    static 文件夹的作用是存放静态文件的 Webpack 在打包时会将其打包到生成 dist 文件夹中

2. build\webpack.dev.conf.js 及 build\webpack.prod.conf.js 确保有如下配置，默认应该就有的，没有的话自己加上

    ```js
    // copy custom static assets
    new CopyWebpackPlugin([
        {
            from: path.resolve(__dirname, '../static'),
            to: config.dev.assetsSubDirectory,
            ignore: ['.*']
        }
    ])
    ```

## 设置 webpack 配置项，使其支持 cesium
1. build\webpack.base.conf.js 添加配置如下

```js
output: {
    path: config.build.assetsRoot,
    filename: '[name].js',
    publicPath: process.env.NODE_ENV === 'production'
        ? config.build.assetsPublicPath
        : config.dev.assetsPublicPath,
    sourcePrefix: ' ' // 添加这条命令，让Webpack正确缩进cesium的多行字符串。
},
```

2. build\webpack.base.conf.js 添加配置如下

```js
module: {
    rules: [
    .....
    ]，
    unknownContextRegExp: /^.\/.*$/,//Webpack打印载入特定库时候的警告
    unknownContextCritical: false,//解决错误Error: Cannot find module "."
}
```

3. build\webpack.base.conf.js 添加配置如下

```js
{
    test: /\.js\.map$/,
    use: {
        loader: 'file-loader'
    },
},
```

整体 rules 配置如下

```js
module: {
    rules: [
    ...(config.dev.useEslint ? [createLintingRule()] : []),
    {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: vueLoaderConfig
    },
    {
        test: /\.js$/,
        loader: 'babel-loader',
        include: [resolve('src'), resolve('test'), resolve('node_modules/webpack-dev-server/client')]
    },
    {
        test: /\.js\.map$/,
        use: {
            loader: 'file-loader'
        },
    },
    {
        test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
        loader: 'url-loader',
        options: {
            limit: 10000,
            name: utils.assetsPath('img/[name].[hash:7].[ext]')
        }
    },
    {
        test: /\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/,
        loader: 'url-loader',
        options: {
            limit: 10000,
            name: utils.assetsPath('media/[name].[hash:7].[ext]')
        }
    },
    {
        test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
        loader: 'url-loader',
        options: {
            limit: 10000,
            name: utils.assetsPath('fonts/[name].[hash:7].[ext]')
        }
    }
    ],
    unknownContextRegExp: /^.\/.*$/,  // Webpack打印载入特定库时候的警告
    unknownContextCritical: false,    // 解决错误Error: Cannot find module "."
},
```

到此基本配置完成

## 编写Vue组件

环境配好了，那到底有没有问题呢，就用 Cesium 来测试一下吧

1. 新建一个 src\components\cesiumViewer.vue 组件

    ```html
    <template>
        <div id="cesiumContainer"></div>
    </template>

    <script>
        // 引入Cesium。Cesium1.6x版本后cesium不支持import的方式引入，改用require引入即可
        let Cesium = require("cesium/Source/Cesium");
        // 让Cesium知道静态资源在哪里的API
        import buildModuleUrl from "cesium/Source/Core/buildModuleUrl";
        // 导入必须的样式表
        import "cesium/Source/Widgets/widgets.css";

        export default {
            name: "cesiumContainer",
            mounted: function () {
                // 设置静态资源目录
                buildModuleUrl.setBaseUrl("../../static/Cesium/");
                // 加载自己的账户Token，没有的话会在显示版权信息的时候显示使用了默认Token的警告信息
                Cesium.Ion.defaultAccessToken = "自己的Token";
                // 创建viewer实例
                this.viewer = new Cesium.Viewer("cesiumContainer", {
                    animation: false, // 是否显示动画控件
                    shouldAnimate: false, // 是否初始时刻运动
                    homeButton: true, // 是否显示Home按钮
                    fullscreenButton: true, // 是否显示全屏按钮
                    baseLayerPicker: false, // 是否显示图层选择控件 去掉自带的图层选择器
                    geocoder: false, // 是否显示地名查找控件,设置为true，则无法查询
                    timeline: false, // 是否显示时间线控件
                    sceneModePicker: false, // 是否显示投影方式控件 三维/二维
                    navigationHelpButton: false, // 是否显示帮助信息控件
                    infoBox: false, // 是否显示点击要素之后显示的信息 信息框小部件
                    requestRenderMode: false, // true启用请求渲染模式:更新实体需拖动地图 视图才更新[true 加载完entity后requestRender一下]
                    scene3DOnly: false, // 每个几何实例将只能以3D渲染以节省GPU内存 如果设置为true，则所有几何图形以3D模式绘制以节约GPU资源
                    sceneMode: 3, // 初始场景模式 1 2D模式 2 2D循环模式 3 3D模式  Cesium.SceneMode
                    fullscreenElement: document.body, // 全屏时渲染的HTML元素
                    selectionIndicator: false, // 是否显示选取指示器组件
                    terrainProvider: Cesium.createWorldTerrain(), // 注释时相当于使用默认地形，解开注释相当于使用全球地形[世界地形数据]
                });
                // 隐藏版权信息
                this.viewer._cesiumWidget._creditContainer.style.display = "none";
            },
            data() {
                return {
                    viewer: {},
                };
            },
        };
    </script>

    <style scoped>
    </style>
    ```

2. 在 src\App.vue 中注册组件

    ```html
    <template>
        <div id="app">
            <router-view />
        </div>
    </template>

    <script>
        import cesiumViewer from "./components/cesiumViewer.vue";
        export default {
            name: "App",
            components: {
                cesiumViewer: cesiumViewer,
            },
        };
    </script>

    <style>
        /* 保证浏览器全屏幕显示，没有多余的白边 */
        html,
        body,
        #cesiumContainer {
            width: 100%;
            height: 100vh;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
    </style>
    ```

3. 修改 src\router\index.js 文件

    ```js
    import Vue from 'vue'
    import Router from 'vue-router'
    import cesiumViewer from '@/components/cesiumViewer'

    Vue.use(Router)

    export default new Router({
        routes: [
            {
                path: '/',
                name: 'cesiumViewer',
                component: cesiumViewer
            }
        ]
    })
    ```

## 禁用 ESLint 代码检查

ESLint 是用来规范代码书写的。但对于初学者来说，还是先禁用了好，要不然启动项目时会被各种代码不规范的爆红搞崩溃。

如果在创建项目时，ESLint 相关配置时选择 No，就可以不用下面的配置了；如果选择了 Yes，想要禁用 ESLint，就按照下面的配置来做就好啦

在项目根目录下的 .eslintrc.js 配置文件中，将 `'standard'` 这一行注释掉即可~

## npm run dev 运行项目

如果一切正常，运行项目之后，就能看见一个漂亮的蓝色地球啦

![小破球~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201010152827.png)