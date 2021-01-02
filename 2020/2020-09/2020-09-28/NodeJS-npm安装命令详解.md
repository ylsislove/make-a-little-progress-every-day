# NodeJS-npm安装命令详解

## 安装参数详解
| 命令 | 解释 |
| ---- | ---- |
| npm install module | 安装某个 module 到本地项目的 node_modules，但不会把安装包的信息添加到 package.json 文件 |
| npm install module --save | 安装某个 module 到本地项目的 node_modules 文件夹，同时把相关模块依赖添加到 package.json 文件的 dependencies 中 |
| npm install module --save-dev	| 安装某个 module 到本地项目的 node_modules 文件夹，同时把相关模块依赖添加到 package.json 文件的 devDependencies |
| npm install module -g | 与 npm install module 一样，只是 module 的安装是全局的 |
| npm install module --save -g | 与 npm install module --save 一样，只是 module 的安装是全局的 |
| npm install module --save-dev -g | 与 npm install module --save-dev 一样，只是 module 的安装是全局的 |

## package.json中dependencies与devDependencies区别
| 属性 | 区别 |
| --- | --- |
| dependencies | 这些包都是你的应用程序在生产环境中所需要的 |
| devDependencies | 这些包只是在开发和测试中需要的 |

**devDependencies** 的理解：

我们在开发一个前端项目的时候，需要使用到 webpack 或者 gulp 来构建我们的开发和本地运行环境，这时我们就要安装到 devDependencies 里。webpack 或者 gulp 是用来打包压缩代码的工具，在项目实际运行的时候用不到，所以把 webpack 或者 gulp 放到 devDependencies 中就行了。

**dependencies** 的理解：

我们在项目中用到了 element-ui 或者 mint-ui，在生产环境中运行项目，当然也需要 element-ui 或者 mint-ui，所以我们把 element-ui 或者 mint-ui 安装到 dependencies 中。


更详细的解释可看
> https://www.cnblogs.com/ysk123/p/11655502.html
