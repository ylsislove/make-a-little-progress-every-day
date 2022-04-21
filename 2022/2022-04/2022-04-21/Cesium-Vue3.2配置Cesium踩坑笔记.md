---
title: Cesium-Vue3.2配置Cesium踩坑笔记
date: 2022/04/21 12:05:21
categories:
 - [GIS开发笔记, Cesium, 学习笔记]
tags: 
 - Cesium
---

## 前言
很早之前，我写过一篇 [Cesium-Vue3整合Cesium最简教程](https://blog.aayu.today/gis/cesium/learning-notes/20210701/) 教程，而最近我在学习最新版的 Vue3.2 和 TypeScript，并使用了 Vue Admin Plus 后台框架，发现在这个框架的基础上配置 Cesium 会有一些坑，便在此记录下来，希望能帮助到后面的小伙伴呀~~

## 环境
* NodeJS：16.14.2
* Vue：3.2.31
* Cesium：1.92.0
* @types/cesium：1.70.0
* copy-webpack-plugin：10.2.4
* @types/copy-webpack-plugin：10.1.0

## 配置步骤
1. 安装相关依赖

因为我是在现有 Vue Admin Plus 后台框架的基础上配置 Cesium 的，所以就省略了新建项目的步骤，直接安装依赖，如下
```
cnpm install Cesium
cnpm install @types/cesium
cnpm install copy-webpack-plugin -D
cnpm install @types/copy-webpack-plugin -D
```

这里我用 cnpm 安装，是因为 Vue Admin Plus 这个框架依赖就是用 cnpm 安装的，用 npm 安装可能会报 `Error: command failed: npm install --loglevel error` 的错误~~

安装 cnpm 可以用如下命令安装
```
# powershell 管理员模式安装
npm install cnpm -g --registry=https://registry.npmmirror.com

# powershell 获取管理员权限，选择A
set-ExecutionPolicy RemoteSigned
```

2. 配置 vue.config.js 文件

因为我用的 `copy-webpack-plugin` 是最新版的，而最新版的导入语法有点变化，所以参考 [这篇博文](https://blog.csdn.net/weixin_43276017/article/details/119379967) 的配置要有点变化，更改后如下

```ts
new CopyWebpackPlugin({
    patterns: [
        {
            from: path.join(cesiumSource, 'Workers'),
            to: 'Workers',
        },
        {
            from: path.join(cesiumSource, 'Assets'),
            to: 'Assets',
        },
        {
            from: path.join(cesiumSource, 'Widgets'),
            to: 'Widgets',
        },
        {
            from: path.join(cesiumSource, 'ThirdParty/Workers'),
            to: 'ThirdParty/Workers',
        },
    ],
}),
new webpack.DefinePlugin({
    CESIUM_BASE_URL: JSON.stringify('./'),
}),
```

3. 配置 main.ts 文件

如果按照下面这样导入
```ts
/**
 * @description 导入Cesium
 */
import 'cesium/Source/Widgets/widgets.css'
const Cesium = require('cesium/Source/Cesium')
```

会报错找不到模块的，如下
```
 error  in ./src/main.ts

Module not found: Error: Package path ./Source/Widgets/widgets.css is not exported from package E:\code\javascript\city-analysis-platform\node_modules\cesium (see exports field in E:\code\javascript\city-analysis-platform\node_modules\cesium\package.json)

 error  in ./src/main.ts

Module not found: Error: Package path ./Source/Cesium is not exported from package E:\code\javascript\city-analysis-platform\node_modules\cesium (see exports field in E:\code\javascript\city-analysis-platform\node_modules\cesium\package.json)
```

在查阅了一番资料后，终于参考了这篇：[Why did it fail to import css of Cesium in the packaging tool](https://programmer.ink/think/why-did-it-fail-to-import-css-of-cesium-in-the-packaging-tool.html) 找到了解决办法~~

解决办法就是首先在 `node_modules/cesium` 目录下找到它的 `package.json` 文件，然后修改 exports 字段如下
```json
"exports": {
    "./package.json": "./package.json",
    ".": {
        "require": "./index.cjs",
        "import": "./Source/Cesium.js"
    },
    "./Source/Widgets/widgets.css": "./Source/Widgets/widgets.css" 
},
```

主要就是添加了 `"./Source/Widgets/widgets.css": "./Source/Widgets/widgets.css" ` 才能让我们在项目中找到 Cesium 的 css 文件

修改完这个之后，再次在 `main.ts` 文件中导入 Cesium，如下
```ts
/**
 * @description 导入Cesium
 */
import 'cesium/Source/Widgets/widgets.css'
import * as Cesium from 'cesium'
// const Cesium = require('cesium/Source/Cesium')
```

然后启动项目，应该就不会报错啦~~

4. 编写测试页面

在 `src/views` 目录下新建个 `map.vue` 文件，编写如下
```ts
<template>
  <div id="cesiumContainer" class="map-container"></div>
</template>

<script>
  import { defineComponent, reactive, toRefs } from 'vue'

  export default defineComponent({
    name: 'Map',
    setup() {
      const state = reactive({})

      const Cesium = inject('$Cesium')
      onMounted(() => {
        let viewer = new Cesium.Viewer('cesiumContainer', {
          imageryProvider: new Cesium.ArcGisMapServerImageryProvider({
            url: 'https://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer',
          }),
        })
        console.info(viewer)
      })

      return {
        ...toRefs(state),
      }
    },
  })
</script>
<style>
  #cesiumContainer {
    width: 100%;
    height: 100%;
    padding: 0;
    margin: 0;
  }
</style>
```

配置好路由之后，启动项目，跳转到指定路由，就能看到一个蓝色的小破球啦，bingo

![](http://image.aayu.today/2022/04/21/62fe3f2f3a751.png)

## 参考链接
* [vue3+cesium+ts全过程](https://blog.csdn.net/weixin_43276017/article/details/119379967)
* [Why did it fail to import css of Cesium in the packaging tool](https://programmer.ink/think/why-did-it-fail-to-import-css-of-cesium-in-the-packaging-tool.html)
* [Can not import widgets.css file not exported from package.json #9212](https://github.com/CesiumGS/cesium/issues/9212)
