# Cesium-键盘控制3D飞机模型的移动

  - [最终效果](#%E6%9C%80%E7%BB%88%E6%95%88%E6%9E%9C)
  - [主要思路](#%E4%B8%BB%E8%A6%81%E6%80%9D%E8%B7%AF)
  - [相关代码](#%E7%9B%B8%E5%85%B3%E4%BB%A3%E7%A0%81)

## 最终效果
![最终效果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200929161349.gif)

## 主要思路
1. 添加数据模型
2. 监听键盘按键
3. 计算坐标
4. 移动小车

## 相关代码
```js
var scene = viewer.scene;
// 旋转角度
let radian = Cesium.Math.toRadians(3.0);
// 移动速度
let speed = 60;
// 速度矢量
let speedVector = new Cesium.Cartesian3();
// 起始位置
let position = Cesium.Cartesian3.fromDegrees(102.23292685840103, 27.825718192817853, 2500.0);

// 用于设置模型方向
let hpRoll = new Cesium.HeadingPitchRoll();
let fixedFrameTransforms = Cesium.Transforms.localFrameToFixedFrameGenerator('north', 'west');

let modelPrimitive = scene.primitives.add(Cesium.Model.fromGltf({
    url: 'Assets/SampleData/models/CesiumAir/Cesium_Air.glb',
    modelMatrix: Cesium.Transforms.headingPitchRollToFixedFrame(position, hpRoll, Cesium.Ellipsoid.WGS84, fixedFrameTransforms),
    minimumPixelSize: 128
}));

// 状态标志
let flag = {
    moveUp: false,
    moveDown: false,
    moveLeft: false,
    moveRight: false
};

// 根据键盘按键返回标志
function setFlagStatus(key, value) {
    switch (key.keyCode) {
        case 37:
            // 左
            flag.moveLeft = value;
            break;
        case 38:
            // 上
            flag.moveUp = value;
            break;
        case 39:
            // 右
            flag.moveRight = value;
            break;
        case 40:
            flag.moveDown = value;
            // 下
            break;
    }
}

document.addEventListener('keydown', (e) => {
    setFlagStatus(e, true);
});

document.addEventListener('keyup', (e) => {
    setFlagStatus(e, false);
});

viewer.clock.onTick.addEventListener((clock) => {

    if (flag.moveUp) {

        if (flag.moveLeft) {
            hpRoll.heading -= radian;
        }

        if (flag.moveRight) {
            hpRoll.heading += radian;
        }
        moveModel(true);
    }

    if (flag.moveDown) {
        if (flag.moveLeft) {
            hpRoll.heading += radian;
        }

        if (flag.moveRight) {
            hpRoll.heading -= radian;
        }
        moveModel(false);
    }
});

// 移动
function moveModel(isUP) {
    // 计算速度矩阵
    if (isUP > 0) {
        speedVector = Cesium.Cartesian3.multiplyByScalar(Cesium.Cartesian3.UNIT_X, speed, speedVector);
    } else {
        speedVector = Cesium.Cartesian3.multiplyByScalar(Cesium.Cartesian3.UNIT_X, -speed, speedVector);
    }
    // 根据速度计算出下一个位置的坐标
    position = Cesium.Matrix4.multiplyByPoint(modelPrimitive.modelMatrix, speedVector, position);
    // 模型移动
    Cesium.Transforms.headingPitchRollToFixedFrame(position, hpRoll, Cesium.Ellipsoid.WGS84, fixedFrameTransforms, modelPrimitive.modelMatrix);
}
```