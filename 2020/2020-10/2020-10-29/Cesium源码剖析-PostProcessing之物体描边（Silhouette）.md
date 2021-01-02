# Cesium源码剖析-PostProcessing之物体描边（Silhouette）

  - [前言](#%E5%89%8D%E8%A8%80)
  - [实验效果](#%E5%AE%9E%E9%AA%8C%E6%95%88%E6%9E%9C)
  - [后期处理的原理](#%E5%90%8E%E6%9C%9F%E5%A4%84%E7%90%86%E7%9A%84%E5%8E%9F%E7%90%86)
  - [Cesium添加后期处理的流程](#cesium%E6%B7%BB%E5%8A%A0%E5%90%8E%E6%9C%9F%E5%A4%84%E7%90%86%E7%9A%84%E6%B5%81%E7%A8%8B)
  - [Silhouette实现原理](#silhouette%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86)
    - [开启物体描边功能](#%E5%BC%80%E5%90%AF%E7%89%A9%E4%BD%93%E6%8F%8F%E8%BE%B9%E5%8A%9F%E8%83%BD)
    - [原理介绍](#%E5%8E%9F%E7%90%86%E4%BB%8B%E7%BB%8D)
    - [LinearDepth](#lineardepth)
    - [EdgeDetection](#edgedetection)
    - [Silhouette](#silhouette)
  - [总结](#%E6%80%BB%E7%BB%93)
  - [原文链接](#%E5%8E%9F%E6%96%87%E9%93%BE%E6%8E%A5)

## 前言
Cesium 在 1.46 版本中新增了对整个场景的后期处理(Post Processing)功能，包括模型描边、黑白图、明亮度调整、夜视效果、环境光遮蔽等。对于这么炫酷的功能，我们绝不犹豫，先去翻一翻它的源码，掌握它的实现原理。

## 实验效果
![实验效果1](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201029204418.png)

![实验效果2](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201029204607.gif)

## 后期处理的原理
后期处理的过程有点类似于照片的 PS。生活中拍摄了一张自拍照，看到照片后发现它太暗了，于是我们增加亮度得到了一张新的照片。在增加亮度后发现脸上的痘痘清晰可见，这可不是我们希望的效果，于是再进行一次美肤效果处理。在这之后可能还会进行 n 次别的操作，直到满足我们的要求。上述这个过程和三维里面的后期处理流程非常类似：拍的原始照片相当于三维场景中实际渲染得到的效果，在此基础上进行物体描边、夜视效果、环境光遮蔽等后期处理，最后渲染到场景中的图片相当于定版的最终照片。整个过程如下图所示：

![后期处理的原理](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201029204744.png)

## Cesium添加后期处理的流程
在介绍Cesium添加后期处理流程之前，首先对用到的相关类进行说明：
- `PostProcessStage`：对应于某个具体的后期处理效果，它的输入为场景渲染图或者上一个后期处理的结果图，输出结果是一张处理后的图片。
- `PostProcessStageComposite`：一个集合对象，存储类型为 PostProcessStage 或者 PostProcessStageComposite 的元素。
- `PostProcessStageLibrary`：负责创建具体的后期处理效果，包括 Silhouette、Bloom、AmbientOcclusion 等，创建返回的结果是 PostProcessStageComposite 或者 PostProcessStage 类型。
- `PostProcessStageCollection`：是一个集合类型的类，负责管理和维护放到集合中的元素 ，元素的类型是 PostProcessStage 或者 PostProcessStageComposite。

Cesium 中添加后期处理的流程是：首先通过 PostProcessStageLibrary 创建一个或者多个后处理效果对象，得到多个 PostProcessStage 或者 PostProcessStageComposite，然后将他们加入到 PostProcessStageCollection 对象中。这样 PostProcessStageCollection 对象就会按照加入的顺序进行屏幕后期处理，在所有的效果都处理完毕后，执行 FXAA，最后绘制到屏幕上。下面对 Silhouette 实现原理进行介绍。

## Silhouette实现原理
### 开启物体描边功能
silhouette 的效果可以理解为物体轮廓、描边，相当于把物体的外轮廓线勾勒出来。在 Cesium 中开启 silhouette 的功能只需要简单的四行代码~

```js
var collection = viewer.scene.postProcessStages;
var silhouette = collection.add(Cesium.PostProcessStageLibrary.createSilhouetteStage());
silhouette.enabled = true;
silhouette.uniforms.color = Cesium.Color.YELLOW;
```

效果如开头所示~

### 原理介绍
创建 Stage 的函数是实现功能的关键所在，Cesium.PostProcessStageLibrary.createSilhouetteStage() 这个函数的具体内容如下：

```js
PostProcessStageLibrary.createSilhouetteStage = function() {
    var silhouetteDepth = new PostProcessStage({
        name : 'czm_silhouette_depth',
        fragmentShader : LinearDepth
    });
    var edgeDetection = new PostProcessStage({
        name : 'czm_silhouette_edge_detection',
        fragmentShader : EdgeDetection,
        uniforms : {
            length : 0.25,
            color : Color.clone(Color.BLACK)
        }
    });
    var silhouetteGenerateProcess = new PostProcessStageComposite({
        name : 'czm_silhouette_generate',
        stages : [silhouetteDepth, edgeDetection]
    });
    var silhouetteProcess = new PostProcessStage({
        name : 'czm_silhouette_color_edges',
        fragmentShader : Silhouette,
        uniforms : {
            silhouetteTexture : silhouetteGenerateProcess.name
        }
    });

    var uniforms = {};
    defineProperties(uniforms, {
        length : {
            get : function() {
                return edgeDetection.uniforms.length;
            },
            set : function(value) {
                edgeDetection.uniforms.length = value;
            }
        },
        color : {
            get : function() {
                return edgeDetection.uniforms.color;
            },
            set : function(value) {
                edgeDetection.uniforms.color = value;
            }
        }
    });
    return new PostProcessStageComposite({
        name : 'czm_silhouette',
        stages : [silhouetteGenerateProcess, silhouetteProcess],
        inputPreviousStageTexture : false,
        uniforms : uniforms
    });
};
```

通过查看代码发现，该函数最后的返回结果是 `PostProcessStageComposite` 对象，该对象包含了 `silhouetteGenerateProcess` 和 `silhouetteGenerateProcess` 两个元素，其中 `silhouetteGenerateProcess` 又是一个 `PostProcessStageComposite` 类型，包括 `silhouetteDepth` 和 `edgeDetection` 两部分。在后期处理过程中真正起作用的是 `PostProcessStage` 类型的对象，此处包括 `silhouetteDepth`、`edgeDetection`、`silhouetteProcess` 三个对象，也就是说这三个对象的顺序执行实现了物体描边效果。下面对这三个对象中的代码进行详细分析。

### LinearDepth
LinearDepth 的代码如下：

```c
uniform sampler2D depthTexture;

varying vec2 v_textureCoordinates;

float linearDepth(float depth)
{
    float far = czm_currentFrustum.y;
    float near = czm_currentFrustum.x;
    return (2.0 * near) / (far + near - depth * (far - near));
}

void main(void)
{
    float depth = czm_readDepth(depthTexture, v_textureCoordinates);
    gl_FragColor = vec4(linearDepth(depth));
}
```

代码比较简单，一共才 10 多行，目的就是将深度图中的深度值进行线性拉伸。`depthTexture` 代表场景中的深度图，`v_textureCoordinates` 代表屏幕采样点坐标。首先通过 `czm_readDepth` 读取场景中的深度值，然后利用 `linearDepth` 函数(该函数通过远近裁剪面对输入值做了一个线性变换)进行线性拉伸。其实质是把深度值转换成视空间下的 z 值，然后将这个 z 值除以 far，得到一个 0-1 的值，该值的大小可以反应屏幕像素点在视空间下的 z 值大小。最后将得到的深度值赋值给 `gl_FragColor` 变量，相当于把深度值隐藏在颜色中。这样就得到了一张经过线性拉伸后的深度图，用于后面的处理。

### EdgeDetection
EdgeDetection 的代码如下：

```c
uniform sampler2D depthTexture;
uniform float length;
uniform vec4 color;

varying vec2 v_textureCoordinates;

void main(void)
{
    float directions[3];
    directions[0] = -1.0;
    directions[1] = 0.0;
    directions[2] = 1.0;

    float scalars[3];
    scalars[0] = 3.0;
    scalars[1] = 10.0;
    scalars[2] = 3.0;

    float padx = 1.0 / czm_viewport.z;
    float pady = 1.0 / czm_viewport.w;

    float horizEdge = 0.0;
    float vertEdge = 0.0;

    for (int i = 0; i < 3; ++i) {
        float dir = directions[i];
        float scale = scalars[i];

        horizEdge -= texture2D(depthTexture, v_textureCoordinates + vec2(-padx, dir * pady)).x * scale;
        horizEdge += texture2D(depthTexture, v_textureCoordinates + vec2(padx, dir * pady)).x * scale;

        vertEdge -= texture2D(depthTexture, v_textureCoordinates + vec2(dir * padx, -pady)).x * scale;
        vertEdge += texture2D(depthTexture, v_textureCoordinates + vec2(dir * padx, pady)).x * scale;
    }

    float len = sqrt(horizEdge * horizEdge + vertEdge * vertEdge);
    float alpha = len > length ? 1.0 : 0.0;
    gl_FragColor = vec4(color.rgb, alpha);
}
```

通过 shader 的名字就可以大体猜到这段代码的作用就是对边界进行检测。`depthTexture` 是通过 `linearDepth` 拉伸后的深度图，`length` 是设置的物体边界长度判断值，`color` 是设置的边界颜色，`v_textureCoordinates` 是屏幕采样点的坐标。在 `main` 函数中首先定义了 `directions` 和 `scalars` 两个数组。`directions` 代表进行边界检测的方向，`scalars` 表示边界检测的权重值。`padx` 表示每个像素在 `x` 方向上的坐标跨度，`pady` 表示每个像素在 `y` 方向上的坐标跨度。`horizEdge` 表示水平方向的边界值，`vertEdge` 表示竖直方向边界值。然后就是通过 `for` 循环在以该像素为中心的九宫格中计算水平方向的深度差值和垂直方向的深度差值，计算的过程可以用下图表示：

![EdgeDetection](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20201029210915.png)

通过上面这张图可以清晰的看出，边界检测的过程其实是对周围八个像素点计算 `z` 坐标差值，包括水平坐标差值 `horizEdge` 和竖直差值 `vertEdge`。通过这两个值得到总差值 `len`，通过 `length` 和 `len` 的大小设置颜色的透明度为 `1` 或者 `0`，输出一张图。

### Silhouette
Silhouette 的代码如下：

```c
uniform sampler2D colorTexture;
uniform sampler2D silhouetteTexture;

varying vec2 v_textureCoordinates;

void main(void)
{
    vec4 silhouetteColor = texture2D(silhouetteTexture, v_textureCoordinates);
    gl_FragColor = mix(texture2D(colorTexture, v_textureCoordinates), silhouetteColor, silhouetteColor.a);
}
```

`silhouette` 的代码非常简单，其中 `colorTexture` 代表原始场景图， `silhouetteTexture` 是通过 `EdgeDetection` 得到的图。通过 `silhouetteColor.a` 进行两张图的混合，就可以得到最终的结果。

## 总结
后期处理其实是一个叠加修改的过程，通过不同步骤的加工，最后得到想要的结果。本文所讲的物体描边其实是对整个屏幕中的要素进行边界检测，检测出为边界的地方就将其颜色改为设定的值。花了大半天时间写完了，希望对感兴趣的同学有所帮助。晚上我要出去玩，玩，玩！！！

## 原文链接
[Cesium源码剖析---Post Processing之物体描边（Silhouette）](https://www.cnblogs.com/webgl-angela/p/9272810.html)