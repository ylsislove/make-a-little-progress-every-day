# Cesium官方教程9-粒子系统

  - [官方教程地址](#%E5%AE%98%E6%96%B9%E6%95%99%E7%A8%8B%E5%9C%B0%E5%9D%80)
  - [粒子系统介绍](#%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E4%BB%8B%E7%BB%8D)
  - [什么是粒子系统](#%E4%BB%80%E4%B9%88%E6%98%AF%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F)
  - [粒子系统基本概念](#%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5)
  - [发射器（ Emitters）](#%E5%8F%91%E5%B0%84%E5%99%A8-emitters)
    - [BoxEmitter](#boxemitter)
    - [CircleEmitter](#circleemitter)
    - [ConeEmitter](#coneemitter)
    - [SphereEmitter](#sphereemitter)
  - [配置粒子系统](#%E9%85%8D%E7%BD%AE%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F)
    - [粒子发射速率](#%E7%B2%92%E5%AD%90%E5%8F%91%E5%B0%84%E9%80%9F%E7%8E%87)
    - [粒子的生命周期和粒子系统的生命周期](#%E7%B2%92%E5%AD%90%E7%9A%84%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E5%92%8C%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E7%9A%84%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F)
  - [粒子样式](#%E7%B2%92%E5%AD%90%E6%A0%B7%E5%BC%8F)
    - [颜色（Color）](#%E9%A2%9C%E8%89%B2color)
    - [大小（Size）](#%E5%A4%A7%E5%B0%8Fsize)
    - [运行速度（Speed）](#%E8%BF%90%E8%A1%8C%E9%80%9F%E5%BA%A6speed)
  - [更新回调（UpdateCallback）](#%E6%9B%B4%E6%96%B0%E5%9B%9E%E8%B0%83updatecallback)
  - [位置](#%E4%BD%8D%E7%BD%AE)
  - [更多示例代码](#%E6%9B%B4%E5%A4%9A%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81)

## 官方教程地址
> https://cesium.com/docs/

## 粒子系统介绍
这篇教程带你学习Cesium的粒子相关API，比如如何在你的项目里添加烟，火，火花等特效。

![粒子特效](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200927192600.gif)

## 什么是粒子系统
粒子系统是一种图形学技术，用来模拟复杂的物理效果。粒子系统是由一堆很小的图片组成，看起来就像一些复杂的“含糊不清（fuzzy）”对象，就像火、烟、天气、或者烟花。这些复杂效果其实是通过控制每一个独立的粒子的初始位置、速度、生命周期等属性来完成。
粒子系统通常在电影和游戏中应用广泛。比如，用来表示飞机的损伤过程，艺术家或者开发人员先用粒子系统来展示飞机引擎的爆炸效果，然后在用另一个粒子系统表示飞机坠毁过程中的烟雾轨迹。

## 粒子系统基本概念
先通过代码看下基本的粒子系统：

```js
var particleSystem = viewer.scene.primitives.add(new Cesium.ParticleSystem({
    // Particle appearance
    image : '../../SampleData/fire.png',
    imageSize : new Cesium.Cartesian2(20, 20);
    startScale : 1.0,
    endScale : 4.0,
    // Particle behavior
    particleLife : 1.0,
    speed : 5.0,
    // Emitter parameters
    emitter : new Cesium.CircleEmitter(0.5),
    emissionRate : 5.0,
    emitterModelMatrix : computeEmitterModelMatrix(),
    // Particle system parameters
    modelMatrix : computeModelMatrix(),
    lifetime : 16.0
}));
```

效果是这样的：

![效果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200927194714.gif)

上述代码里创建了 ParticleSystem 类的对象, 传递了一个对象参数，来控制每个独立粒子 Particle 的外观 。粒子从 ParticleEmitter 中生成，它有一个位置和类型、生存一段时间后，就消亡。

部分属性可以是动态的。注意示例代码里并非用了一个 color 属性，而是用了 startColor 和 endColor 两个颜色属性。在粒子的整个时间中，根据时间在两个颜色之间做插值。startScale 和 endScale 属性也是类似。

其他影响粒子系统效果的是 maximum 和 minimum 属性。对于每个有最小和最大参数配置的属性，在粒子的初始化过程中会在这个最小最大值范围内随机，然后整个粒子的生存周期内都不会变化。比如，设定粒子的初始运行速度，可以直接设置 speed 变量，也可以设置 minimumSpeed 和 maximumSpeed 变量做为随机速度的上下边界。允许类似设置的属性包括：imageSize, speed, life, 和 particleLife。

通过这些参数可以创建很多很多种粒子效果，具体可以试下 Sandcastle 的[粒子系统示例](https://cesiumjs.org/Cesium/Build/Apps/Sandcastle/index.html?src=Particle%20System.html&label=Showcases)。

掌握 Cesium 的粒子系统，等同于对这些不同参数非常熟悉。我们讨论一些属性的细节。

## 发射器（ Emitters）
[ParticleEmitter](http://cesiumjs.org/Cesium/Build/Documentation/ParticleEmitter.html) 控制了粒子产生时候的位置以及初始速度方向。发射器依据 emissionRate 来决定每秒产生多少粒子，根据发射器类型不同决定了粒子的随机速度方向。

Cesium 内置了各种粒子发射器。

### BoxEmitter
BoxEmitter 类在盒子里（box）里随机一个位置，沿着盒子的 6 个面的法向量向外运动。它接受一个 Cartesian3 参数，定义了盒子的长宽高。

```js
particleSystem : {
    image : '../../SampleData/fire.png',
    emissionRate: 50.0,
    emitter: new Cesium.BoxEmitter(new Cesium.Cartesian3(10.0, 10.0, 10.0))
}
```

![BoxEmitter](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200927195323.gif)

### CircleEmitter
圆形发射器使用 CircleEmitter 类在圆形面上随机一个位置，粒子方向是发射器的向上向量。它接受一个 float 参数指定了圆的半径。

```js
particleSystem : {
    image : '../../SampleData/fire.png',
    emissionRate: 50.0,
    emitter: new Cesium.CircleEmitter(5.0)
}
```

![circleemitter](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200927195837.gif)

如果没有指定发射器，默认使用圆形发射器。

### ConeEmitter
锥形发射器类使用 ConeEmitter 在椎体顶点产生粒子，粒子方向在椎体内随机一个角度向外。它接受一个 float 参数，制定了锥角。椎的方向沿着向上轴。

The ConeEmitter class initializes particles at the tip of a cone and directs them at random angles out of the cone. It takes a single float parameter specifying the angle of the cone. The cone is oriented along the up axis of the emitter.

```js
particleSystem : {
    image : '../../SampleData/fire.png',
    emissionRate: 50.0,
    emitter: new Cesium.ConeEmitter(Cesium.Math.toRadians(30.0))
}
```

![ConeEmitter](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200927200056.gif)

### SphereEmitter
球形发射器使用 SphereEmitter 类在球体内随机产生粒子，初始速度是沿着秋心向外。它接受一个 float 参数指定了球体半径。

```js
particleSystem : {
    image : '../../SampleData/fire.png',
    emissionRate: 50.0,
    emitter: new Cesium.SphereEmitter(5.0)
}
```


## 配置粒子系统
Cesium有很多选项来调整粒子效果。

### 粒子发射速率
emissionRate 属性控制每秒生成多少个粒子，用来调整粒子密度。

可以设定一个爆炸对象的数组，用来控制在某个特定时刻产生爆炸效果。这是添加各种爆炸效果的最好方法。

给粒子增加下面的属性：

```js
bursts : [
    new Cesium.ParticleBurst({time : 5.0, minimum : 300, maximum : 500}),
    new Cesium.ParticleBurst({time : 10.0, minimum : 50, maximum : 100}),
    new Cesium.ParticleBurst({time : 15.0, minimum : 200, maximum : 300})
],
```

在给定时刻，这些爆炸效果会产生随机个粒子，在设定最少和最多值之间。

### 粒子的生命周期和粒子系统的生命周期
一些参数控制了粒子系统的生命周期，默认粒子系统一直运行。

设置 lifetime 属性控制粒子的持续时间，同时需要设置 loop 属性为 false。比如设定一个粒子系统运行 5 秒：

```js
particleSystem : {
    lifetime: 5.0,
    loop: false
}
```

设置 particleLife 属性为 5.0 表示设置每个粒子的生命周期是 5 秒。为了每个粒子都有一个随机生命周期，我们可以设置 minimumParticleLife 和 maximumParticleLife。比如下面的代码设置了粒子生命周期在 5 秒和 10 秒之间：

```js
particleSystem : {
    minimumParticleLife: 5.0,
    maximumParticleLife: 10.0
}
```

## 粒子样式
### 颜色（Color）
除了设定 image 属性来控制粒子的纹理外，还可以设定一个颜色值，这个值可以在粒子的生命周期内变化。这个在创建动态变化效果非常有用。

比如，下面代码使火焰粒子产生的时候是淡红色，消亡的时候是半透明黄色。

```js
particleSystem : {
    startColor: Cesium.Color.RED.withAlpha(0.7),
    endColor: Cesium.Color.YELLOW.withAlpha(0.3)
}
```

### 大小（Size）
通常粒子大小通过 imageSize 属性控制。如果想设置一个随机大小，每个粒子的宽度在 minimumImageSize.x 和 maximumImageSize.x 之间随机，高度在 minimumImageSize.y 和 maximumImageSize.y 之间随机，单位为像素。

下面代码创建了像素大小在 30 ~ 60 之间的粒子:

```js
particleSystem : {
    minimumImageSize : new Cesium.Cartesian2(30.0, 30.0),
    maximumImageSize : new Cesium.Cartesian2(60.0, 60.0)
}
```

和颜色一样，粒子大小的倍率在粒子整个生命周期内，会在 startScale 和 endScale 属性之间插值。这个会导致你的粒子随着时间变大或者缩小。

下面代码使粒子逐渐变化到初始大小的 4 倍：

```js
particleSystem : {
    startScale: 1.0,
    endScale: 4.0
}
```

### 运行速度（Speed）
发射器控制了粒子的位置和方向，速度通过 speed 参数或者 minimumSpeed 和 maximumSpeed 参数来控制。下面代码让粒子每秒运行 5 ~ 10 米:

```js
particleSystem : {
    minimumSpeed: 5.0,
    maximumSpeed: 10.0
}
```


## 更新回调（UpdateCallback）
为了提升仿真效果，粒子系统有一个更新函数。这个是个手动更新器，比如对每个粒子模拟重力或者风力的影响，或者除了线性插值之外的颜色插值方式等等。

每个粒子系统在仿真过程种，都会调用更新回调函数来修改粒子的属性。回调函数传过两个参数，一个是粒子本身，另一个是仿真时间步长。大部分物理效果都会修改速率向量来改变方向或者速度。

下面是一个粒子响应重力的示例代码：

```js
var gravityScratch = new Cesium.Cartesian3();
function applyGravity(p, dt) {
    // 计算每个粒子的向上向量（相对地心） 
    var position = p.position;

    Cesium.Cartesian3.normalize(position, gravityScratch);
    Cesium.Cartesian3.multiplyByScalar(gravityScratch, viewModel.gravity * dt, gravityScratch);

    p.velocity = Cesium.Cartesian3.add(p.velocity, gravityScratch, p.velocity);
}
```

这个函数计算了一个重力方向，然后使用重力加速度（-9.8 米每秒平方）去修改粒子的速度方向。

然后设置粒子系统的更新函数：

```js
particleSystem: {
    forces: applyGravity
}
```

## 位置
粒子系统使用两个转换矩阵来定位:
* modelMatrix : 把粒子系统从模型坐标系转到世界坐标系。
* emitterModelMatrix : 在粒子系统的局部坐标系内变换粒子发射器。

我们提供两个属性也是为了方便，当然可以仅仅设置一个，把另一个设置为单位矩阵。为了学习创建这个矩阵，我们尝试把我们的粒子系统相对另一个 entity。

首先创建一个 entity。打开 Sandcastle 的 [Hello World](https://cesiumjs.org/Cesium/Build/Apps/Sandcastle/index.html?src=Hello%20World.html) 示例，敲入下面的代码:

```js
var entity = viewer.entities.add({
    // 加载飞机模型
    model : {
        uri : '../../SampleData/models/CesiumAir/Cesium_Air.gltf',
        minimumPixelSize : 64
    },
    position : Cesium.Cartesian3.fromDegrees(-112.110693, 36.0994841, 1000.0)
});
viewer.trackedEntity = entity;
```

在 viewer 里创建了一个飞机模型。

接下来，我们如何在场景种摆放我们的粒子系统？我们先给飞机的一个引擎上放一团火。首先给粒子系统创建一个模型矩阵，这个矩阵和飞机的位置和朝向完全相同。意思就是飞机的模型矩阵也要做为粒子系统的矩阵，这么设置 modelMatrix：

```js
function computeModelMatrix(entity, time) {
    var position = Cesium.Property.getValueOrUndefined(entity.position, time, new Cesium.Cartesian3());
    if (!Cesium.defined(position)) {
        return undefined;
    }
    var orientation = Cesium.Property.getValueOrUndefined(entity.orientation, time, new Cesium.Quaternion());
    if (!Cesium.defined(orientation)) {
        var modelMatrix = Cesium.Transforms.eastNorthUpToFixedFrame(position, undefined, new Cesium.Matrix4());
    } else {
        modelMatrix = Cesium.Matrix4.fromRotationTranslation(Cesium.Matrix3.fromQuaternion(orientation, new Cesium.Matrix3()), position, new Cesium.Matrix4());
    }
    return modelMatrix;
}
```

现在这个矩阵已经把粒子放到了飞机中心位置。可是我们想让粒子在飞机的一个引擎上产生，所以我们再创建一个在模型坐标系的平移矩阵。这么计算：

```js
function computeEmitterModelMatrix() {
    hpr = Cesium.HeadingPitchRoll.fromDegrees(0.0, 0.0, 0.0, new Cesium.HeadingPitchRoll());
    var trs = new Cesium.TranslationRotationScale();
    trs.translation = Cesium.Cartesian3.fromElements(2.5, 4.0, 1.0, new Cesium.Cartesian3());
    trs.rotation = Cesium.Quaternion.fromHeadingPitchRoll(hpr, new Cesium.Quaternion());
    return Cesium.Matrix4.fromTranslationRotationScale(trs, new Cesium.Matrix4());
}
```

现在就可以去计算偏移矩阵了，我们先用一些基本参数创建粒子系统，代码如下：

```js
var particleSystem = viewer.scene.primitives.add(new Cesium.ParticleSystem({
    image : '../../SampleData/fire.png',
    startScale : 1.0,
    endScale : 4.0,
    particleLife : 1.0,
    speed : 5.0,
    imageSize : new Cesium.Cartesian2(20, 20),
    emissionRate : 5.0,
    lifetime : 16.0,
    modelMatrix : computeModelMatrix(entity, Cesium.JulianDate.now()),
    emitterModelMatrix : computeEmitterModelMatrix()
}));
```

这就做到了前面示例里描述的效果，把粒子特效放到了飞机的引擎上。

![最终效果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200927194714.gif)

注意我们可以随时更改模型或者发射器矩阵。比如，我们想通过通过去更改粒子发射器相对飞机的位置，我们只需要修改 emitterModelMatrix，而保持 modelMatrix 不变。这样就非常容易的在模型空间重新定位了。

这种定位方式并非直接设定一个 position 属性，而是提供了一种有效的，灵活的矩阵变换方式，适应更多效果要求。

这就是粒子系统的基础知识，很期待看到你用他们做出来的效果。


## 更多示例代码
更多粒子系统特效，以及更高级的技术，请看更多粒子特效教程。

![烟花](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200927202351.gif)

* [粒子系统示例](https://cesiumjs.org/Cesium/Build/Apps/Sandcastle/index.html?src=Particle%20System.html&label=Showcases)
* [粒子系统烟花示例](https://cesiumjs.org/Cesium/Build/Apps/Sandcastle/index.html?src=Particle%20System%20Fireworks.html&label=Showcases)