# Cesium-设置火焰特效

```js
// --------------------------- 设置火焰特效 -------------------------------------
//粒子系统的起点，发射源
var staticPosition = Cesium.Cartesian3.fromDegrees(102.23682170436231, 27.829707841795422, 2360);
var entity44 = viewer.entities.add({
    position: staticPosition
});
function computeModelMatrix(entity, time) {
    var position = Cesium.Property.getValueOrUndefined(entity.position);
    let modelMatrix = Cesium.Transforms.eastNorthUpToFixedFrame(position);
    return modelMatrix;
}
function computeEmitterModelMatrix() {
    let hpr = Cesium.HeadingPitchRoll.fromDegrees(0, 0, 0);
    let trs = new Cesium.TranslationRotationScale();
    trs.translation = Cesium.Cartesian3.fromElements(2.5, 4, 1);
    trs.rotation = Cesium.Quaternion.fromHeadingPitchRoll(hpr);
    let result = Cesium.Matrix4.fromTranslationRotationScale(trs);
    return result
}
viewer.scene.primitives.add(new Cesium.ParticleSystem({
    image: './Assets/SampleData/fire.png',
    startColor: Cesium.Color.RED.withAlpha(0.7),
    endColor: Cesium.Color.YELLOW.withAlpha(0.3),
    startScale: 0,
    endScale: 8,
    minimumParticleLife: 1,
    maximumParticleLife: 6,
    minimumSpeed: 1,
    maximumSpeed: 4,
    imageSize: new Cesium.Cartesian2(30, 30),
    // Particles per second.
    emissionRate: 4,
    lifetime: 160.0,
    emitter: new Cesium.CircleEmitter(5.0),
    modelMatrix: computeModelMatrix(entity44, Cesium.JulianDate.now()),
    emitterModelMatrix: computeEmitterModelMatrix()
}));
```