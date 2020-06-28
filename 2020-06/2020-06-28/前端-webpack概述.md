# 前端-webpack概述

  - [webpack 是什么](#webpack-%E6%98%AF%E4%BB%80%E4%B9%88)
  - [webpack 五个核心概念](#webpack-%E4%BA%94%E4%B8%AA%E6%A0%B8%E5%BF%83%E6%A6%82%E5%BF%B5)

## webpack 是什么
webpack 是一种前端资源构建工具，一个静态模块打包器（module bundler）。在 webpack 看来，前端的所有资源文件（js/json/css/img/less/...）都会作为模块处理。它将根据模块的依赖关系进行静态分析，打包生成对应的静态资源（bundle）。

![webpack](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200628155446.png)


## webpack 五个核心概念

1. Entry

    入口（Entry）指示 webpack 以哪个文件为入口起点开始打包，分析构建内部依赖图。

2. Output

    输出（Output）指示 webpack 打包后的资源 bundles 输出到哪里去，以及如何命名。

3. Loader

    Loader 让 webpack 能够去处理那些非 JavaScript 文件（webpack 自身只理解 JavaScript）

4. Plugins

    插件（Plugins）可以用于执行范围更广的任务。插件的范围包括，从打包优化和压缩，一直到重新定义环境中的变量等。

5. Mode

    模式（Mode）指示 webpack 使用相应模式的配置

    | 选项 | 描述 | 特点|
    | ---- | ---- | --- |
    | development | 会将 DefinePlugin 中 process.env.NODE_ENV 的值设置为 development。启用 NamedChunksPlugin 和 NamedModulesPlugin | 能让代码本地调试运行的环境 | 
    | production | 会将 DefinePlugin 中 process.env.NODE_ENV 的值设置为 production。启用 FlagDependencyUsagePlugin，FlagIncludedChunksPlugin，ModuleConcatenationPlugin，NoEmitOnErrorsPlugin，OccurrenceOrderPlugin，SideEffectsFlagPlugin 和 TerserPlugin | 能让代码优化上线运行的环境 | 

