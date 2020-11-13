# Cesium官方教程12-材质（Fabric）

## 介绍
Fabric 是 Cesium 中基于 JSON 格式来描述 materials 的机制。材质描述多边形、折线、椭球等对象的外观特征。材质可以简单的是覆盖一张图片，或者是条纹或者棋盘图案。使用 Fabric 和 GLSL，可以从零开始写脚本新建材质，也可以从现有的材质中派生。比如潮湿碎裂的砖块可以使用程序生成的纹理、凹凸贴图和反射贴图来组合。

对象通过 material 属性来支持材质效果。当前这些对象是多边形、折线、椭球等（这篇文章写的较早，其实现在已经很多几何体都支持材质了）。

```js
polygon.material = Material.fromType('Color');
```

上面，Color 是一个内置材质，它表示了包含透明度在内的一个颜色值。Material.fromType 是简略写法，完整的 Fabric 的 JSON 应该是这样的：

```js
polygon.material = new Cesium.Material({
  fabric : {
    type : 'Color'
  }
});
```

每一个材质包含 0 或者更多个 uniforms，uniform 是一种输入参数变量，在创建材质时或者创建材质后修改。比如，Color 有一个 color uniform，它包含 red，green，blue，和 alpha 四个参数。

```js
polygon.material = new Cesium.Material({
  fabric : {
    type : 'Color',
    uniforms : {
      color : new Cesium.Color(1.0, 0.0, 0.0, 0.5)
    }
  }
});

// 把红色半透明修改为 白色不透明
polygon.material.uniforms.color = Cesium.Color.WHITE;
```

