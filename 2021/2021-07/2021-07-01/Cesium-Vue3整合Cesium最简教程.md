# Cesium-Vue3整合Cesium最简教程

  - [前言](#%E5%89%8D%E8%A8%80)
  - [配置](#%E9%85%8D%E7%BD%AE)
    - [创建 Vue3 项目](#%E5%88%9B%E5%BB%BA-vue3-%E9%A1%B9%E7%9B%AE)
    - [安装 Cesium](#%E5%AE%89%E8%A3%85-cesium)
    - [编写 Vue 组件](#%E7%BC%96%E5%86%99-vue-%E7%BB%84%E4%BB%B6)
    - [运行项目](#%E8%BF%90%E8%A1%8C%E9%A1%B9%E7%9B%AE)
  - [可能遇到的问题](#%E5%8F%AF%E8%83%BD%E9%81%87%E5%88%B0%E7%9A%84%E9%97%AE%E9%A2%98)

## 前言
我之前写过一篇博客，关于 [Cesium1.74+Vue2.6.12环境搭建](https://ylsislove.github.io/2020/10/10/2SMQNJ3.html)，最近在学习 Vue3，又正好了解到有一款 Vue 整合 Cesium 的插件神器，它可以让我们在 vue-cli 中零配置使用 Cesium，简直不要太方便。下面介绍详细的配置过程~

## 配置
### 创建 Vue3 项目
1. 全局安装 vue/cli
```
npm install -g @vue/cli
```

2. 创建一个新的 vue 项目
```
vue create cesium-learning
```

3. 填写项目相关参数

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702102633.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702102633.png)
选择第三项，手动配置

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702102941.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702102941.png)
选择这六项配置（这里可以根据个人需求选择）

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103028.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103028.png)
选择 vue3

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103131.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103131.png)
选择非历史模型路由（这里可以根据个人需求选择）

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103239.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103239.png)
选择 node-sass（这里可以根据个人需求选择）

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103334.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103334.png)
选择 ESLint + Prettier（这里可以根据个人需求选择）

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103417.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103417.png)
选择保存时进行代码规范检查（这里可以根据个人需求选择）

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103500.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103500.png)
选择配置文件分开，而不是合并到 package.json 文件里（这里可以根据个人需求选择）

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103632.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702103632.png)
是否将以上配置选择保存，选择 n（这里可以根据个人需求选择）

等待项目配置结束，项目创建成功如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702104141.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702104141.png)

4. 运行项目
```
cd cesium-learning
npm run serve
```

项目默认运行在 localhost:8080 地址上，若端口被占用，则会自动运行在 8081 端口上。输入网址即可看见 Vue 网页，说明 Vue 环境配好了

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702134753.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702134753.png)

### 安装 Cesium
介绍的一个插件项目 `vue-cli-plugin-cesium`
> 项目地址：https://www.npmjs.com/package/vue-cli-plugin-cesium

当前插件只支持 `VueCLI3.0+` 版本哦

安装只需一行命令搞定所有的事，不用再去关心 `webpack` 如何配置了，不用再去关心如何安装 `cesium` 了，它都帮你搞定了，而且不会给你的工程添加任何文件，保证了项目的简洁。

```
vue add vue-cli-plugin-cesium
```

安装过程中会有三个询问，我们可以选择安装最新版的 Cesium、自动在全局引入 Cesium 样式文件、和添加示例组件到项目 components 目录。

更多详细步骤可以看那个项目地址哦

### 编写 Vue 组件
用 `vue-cli-plugin-cesium` 插件安装好 Cesium 之后，环境到底配好了吗，编写一些代码来测试一下吧~

修改 `App.vue` 如下
```vue
<template>
  <router-view />
</template>

<style lang="scss">
#app {
}
</style>
```

在 views 目录下新建 `Map.vue` 文件，编写如下
```vue
<template>
  <div class="layer-cesium">
    <div id="cesiumContainer"></div>
  </div>
</template>

<script>
export default {
  name: "",
  mounted() {
    // eslint-disable-next-line no-undef
    var viewer = new Cesium.Viewer("cesiumContainer");

    // eslint-disable-next-line no-console
    console.log(viewer);
  },
};
</script>
<style lang="scss" scoped>
.layer-cesium {
  width: 100%;
  height: 100vh;
  #cesiumContainer {
    height: 100%;
  }
}
</style>
```

修改 `router/index.js` 如下
```js
import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Map",
    component: () => import("../views/Map.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
```

### 运行项目
如果一切正常，运行项目之后，就能看见一个漂亮的蓝色地球啦~

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702142950.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702142950.png)

## 可能遇到的问题
在创建 vue3 项目时，遇到创建项目成功，但项目却无法启动的问题，主要报错 `error in ./node_modules/@vue/reactivity/dist/reactivity.esm-bundler.js`，如下图

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702143426.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210702143426.png)

在 vue-cli 的 issues 里找到了解决办法
```
npm uninstall vue
npm install vue@3.1.2
```

参考：[Error on npm run serve for default 3.x template #6562](https://github.com/vuejs/vue-cli/issues/6562)
