# Cesium-基于CZML模型的转向问题

  - [model 的模型转向](#model-%E7%9A%84%E6%A8%A1%E5%9E%8B%E8%BD%AC%E5%90%91)
  - [billboard 的模型转向](#billboard-%E7%9A%84%E6%A8%A1%E5%9E%8B%E8%BD%AC%E5%90%91)
  - [billboard 多模型转向](#billboard-%E5%A4%9A%E6%A8%A1%E5%9E%8B%E8%BD%AC%E5%90%91)
  - [原文地址](#%E5%8E%9F%E6%96%87%E5%9C%B0%E5%9D%80)

## model 的模型转向
```js
var czml = [{
    "id" : "document",
    "name" : "CZML Point - Time Dynamic",
    "version" : "1.0"
},{
    "id" : "point",
    "availability" :"2012-08-04T16:00:00Z/2012-08-04T16:05:00Z",
    "position" : {
        "epoch" : "2012-08-04T16:00:00Z",
         "cartographicDegrees" : [
             0,   70, 20, 150000,
             100, -80, 44, 150000,
             200, -90, 18, 150000,
             300, -98, 52, 150000, 
         ]
    },
     "model": {
        "gltf" : "../SampleData/models/CesiumAir/Cesium_Air.glb",
        "scale" : 2.0,
        "minimumPixelSize": 128
    },
    path : {
        resolution : 1,
        material : new Cesium.PolylineGlowMaterialProperty({
            glowPower : 0.1,
            color : Cesium.Color.YELLOW
        }),
        width :3
    },
}];
 
var viewer = new Cesium.Viewer('cesiumContainer', {
    shouldAnimate : true,
    sceneMode: 2, 
});
 
viewer.dataSources.add(Cesium.CzmlDataSource.load(czml)).then(function(ds){
    var s = ds.entities.getById("point");
    s.orientation = new Cesium.VelocityOrientationProperty(s.position);
});
```

效果如图所示

![效果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200930172841.png)


## billboard 的模型转向
```js
var czml = [{
    "id" : "document",
    "name" : "CZML Point - Time Dynamic",
    "version" : "1.0"
},{
    "id" : "point",
    "availability" :"2012-08-04T16:00:00Z/2012-08-04T16:05:00Z",
    "position" : {
        "epoch" : "2012-08-04T16:00:00Z",
         "cartographicDegrees" : [
             0,   70, 20, 150000,
             100, -80, 44, 150000,
             200, -90, 18, 150000,
             300, -98, 52, 150000, 
         ]
    },
    "billboard" : {
        "image" : "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTgzNDY3MTIyNzY1IiBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM2MDMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+PGRlZnM+PHN0eWxlIHR5cGU9InRleHQvY3NzIj48L3N0eWxlPjwvZGVmcz48cGF0aCBkPSJNNTc5LjQ2MzUyOSAyMDYuMDA0NzA2Yy0zMC4xMTc2NDctMTQ2Ljk3NDExOC02MC4yMzUyOTQtMTYyLjYzNTI5NC02MC4yMzUyOTQtMTYyLjYzNTI5NC00LjgxODgyNC00LjgxODgyNC0xMC44NDIzNTMtNC44MTg4MjQtMTUuNjYxMTc2IDAgMCAwLTMwLjExNzY0NyAxNS42NjExNzYtNjAuMjM1Mjk0IDE2Mi42MzUyOTQgMCAwLTE5LjI3NTI5NCAxMDIuNC0xOS4yNzUyOTQgMTg1LjUyNDcwNlY1NTQuMTY0NzA2YzAgNDUuNzc4ODI0IDE3NC42ODIzNTMgNDAuOTYgMTc0LjY4MjM1MyAzLjYxNDExOFYzOTEuNTI5NDEyYzEuMjA0NzA2LTgzLjEyNDcwNi0xOS4yNzUyOTQtMTg1LjUyNDcwNi0xOS4yNzUyOTUtMTg1LjUyNDcwNnpNNTY2LjIxMTc2NSAzMTAuODE0MTE4YzAgNi4wMjM1MjktMS4yMDQ3MDYgNC44MTg4MjQtNi4wMjM1MyA2LjAyMzUyOWgtMTAuODQyMzUzcy0xNC40NTY0NzEtMTc4LjI5NjQ3MS0yNy43MDgyMzUtMjMzLjcxMjk0MWMwIDAgNDguMTg4MjM1IDEyMS42NzUyOTQgNDQuNTc0MTE4IDIyNy42ODk0MTJ6TTQ1NC4xNzQxMTggODM2LjA2NTg4Mmw3LjIyODIzNS0yMDkuNjE4ODIzYy02LjAyMzUyOS0yLjQwOTQxMi0xMC44NDIzNTMtNC44MTg4MjQtMTUuNjYxMTc3LTcuMjI4MjM1bDguNDMyOTQyIDIxNi44NDcwNTh6TTQzMS4yODQ3MDYgNzQ4LjEyMjM1M2w0LjgxODgyMy0xMzYuMTMxNzY1Yy0zLjYxNDExOC0zLjYxNDExOC03LjIyODIzNS03LjIyODIzNS05LjYzNzY0Ny0xMi4wNDcwNTlsNC44MTg4MjQgMTQ4LjE3ODgyNHpNNDgzLjA4NzA1OSA4OTUuMDk2NDcxbDkuNjM3NjQ3LTI2MS40MjExNzdjLTYuMDIzNTI5IDAtMTIuMDQ3MDU5LTEuMjA0NzA2LTE2Ljg2NTg4Mi0yLjQwOTQxMmw3LjIyODIzNSAyNjMuODMwNTg5ek01NzMuNDQgODMyLjQ1MTc2NWw3LjIyODIzNS0yMTUuNjQyMzUzYy0zLjYxNDExOCAzLjYxNDExOC04LjQzMjk0MSA2LjAyMzUyOS0xNC40NTY0NyA4LjQzMjk0MWw3LjIyODIzNSAyMDcuMjA5NDEyek01MDMuNTY3MDU5IDYzNC44OGw5LjYzNzY0NyAzNTAuNTY5NDEyIDkuNjM3NjQ3LTM1MC41Njk0MTJjLTYuMDIzNTI5IDAtMTMuMjUxNzY1IDEuMjA0NzA2LTE5LjI3NTI5NCAwek01OTIuNzE1Mjk0IDc1Mi45NDExNzZsNC44MTg4MjQtMTQ5LjM4MzUyOWMtMi40MDk0MTIgMy42MTQxMTgtNi4wMjM1MjkgNi4wMjM1MjktOS42Mzc2NDcgOS42Mzc2NDdsNC44MTg4MjMgMTM5Ljc0NTg4MnpNNTQ0LjUyNzA1OSA4OTAuMjc3NjQ3bDkuNjM3NjQ3LTI2MC4yMTY0NzEtMTguMDcwNTg4IDMuNjE0MTE4IDguNDMyOTQxIDI1Ni42MDIzNTN6IiBwLWlkPSIzNjA0IiBmaWxsPSIjZDgxZTA2Ij48L3BhdGg+PC9zdmc+",
        "scale" : 0.5,
    },
    path : {
        resolution : 1,
        material : new Cesium.PolylineGlowMaterialProperty({
            glowPower : 0.1,
            color : Cesium.Color.YELLOW
        }),
        width :3
    },
}];
 
var viewer = new Cesium.Viewer('cesiumContainer', {
    shouldAnimate : true,
    sceneMode: 2, 
});
 
viewer.dataSources.add(Cesium.CzmlDataSource.load(czml)).then(function(ds){
    var s = ds.entities.getById("point");
    s.orientation = new Cesium.VelocityOrientationProperty(s.position);
    s.billboard.alignedAxis = new Cesium.VelocityVectorProperty(s.position, true)
});
```

效果如图所示

![效果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200930172335.png)


## billboard 多模型转向
```js
var czml = [{
    "id" : "document",
    "name" : "CZML Point - Time Dynamic",
    "version" : "1.0"
},{
    "id" : "point1",
    "availability" :"2012-08-04T16:00:00Z/2012-08-04T16:05:00Z",
    "position" : {
        "epoch" : "2012-08-04T16:00:00Z",
         "cartographicDegrees" : [
             0,   70, 20, 150000,
             100, -80, 44, 150000,
             200, -90, 18, 150000,
             300, -98, 52, 150000, 
         ]
    },
    "billboard" : {
        "image" : "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTgzNDY3MTIyNzY1IiBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM2MDMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+PGRlZnM+PHN0eWxlIHR5cGU9InRleHQvY3NzIj48L3N0eWxlPjwvZGVmcz48cGF0aCBkPSJNNTc5LjQ2MzUyOSAyMDYuMDA0NzA2Yy0zMC4xMTc2NDctMTQ2Ljk3NDExOC02MC4yMzUyOTQtMTYyLjYzNTI5NC02MC4yMzUyOTQtMTYyLjYzNTI5NC00LjgxODgyNC00LjgxODgyNC0xMC44NDIzNTMtNC44MTg4MjQtMTUuNjYxMTc2IDAgMCAwLTMwLjExNzY0NyAxNS42NjExNzYtNjAuMjM1Mjk0IDE2Mi42MzUyOTQgMCAwLTE5LjI3NTI5NCAxMDIuNC0xOS4yNzUyOTQgMTg1LjUyNDcwNlY1NTQuMTY0NzA2YzAgNDUuNzc4ODI0IDE3NC42ODIzNTMgNDAuOTYgMTc0LjY4MjM1MyAzLjYxNDExOFYzOTEuNTI5NDEyYzEuMjA0NzA2LTgzLjEyNDcwNi0xOS4yNzUyOTQtMTg1LjUyNDcwNi0xOS4yNzUyOTUtMTg1LjUyNDcwNnpNNTY2LjIxMTc2NSAzMTAuODE0MTE4YzAgNi4wMjM1MjktMS4yMDQ3MDYgNC44MTg4MjQtNi4wMjM1MyA2LjAyMzUyOWgtMTAuODQyMzUzcy0xNC40NTY0NzEtMTc4LjI5NjQ3MS0yNy43MDgyMzUtMjMzLjcxMjk0MWMwIDAgNDguMTg4MjM1IDEyMS42NzUyOTQgNDQuNTc0MTE4IDIyNy42ODk0MTJ6TTQ1NC4xNzQxMTggODM2LjA2NTg4Mmw3LjIyODIzNS0yMDkuNjE4ODIzYy02LjAyMzUyOS0yLjQwOTQxMi0xMC44NDIzNTMtNC44MTg4MjQtMTUuNjYxMTc3LTcuMjI4MjM1bDguNDMyOTQyIDIxNi44NDcwNTh6TTQzMS4yODQ3MDYgNzQ4LjEyMjM1M2w0LjgxODgyMy0xMzYuMTMxNzY1Yy0zLjYxNDExOC0zLjYxNDExOC03LjIyODIzNS03LjIyODIzNS05LjYzNzY0Ny0xMi4wNDcwNTlsNC44MTg4MjQgMTQ4LjE3ODgyNHpNNDgzLjA4NzA1OSA4OTUuMDk2NDcxbDkuNjM3NjQ3LTI2MS40MjExNzdjLTYuMDIzNTI5IDAtMTIuMDQ3MDU5LTEuMjA0NzA2LTE2Ljg2NTg4Mi0yLjQwOTQxMmw3LjIyODIzNSAyNjMuODMwNTg5ek01NzMuNDQgODMyLjQ1MTc2NWw3LjIyODIzNS0yMTUuNjQyMzUzYy0zLjYxNDExOCAzLjYxNDExOC04LjQzMjk0MSA2LjAyMzUyOS0xNC40NTY0NyA4LjQzMjk0MWw3LjIyODIzNSAyMDcuMjA5NDEyek01MDMuNTY3MDU5IDYzNC44OGw5LjYzNzY0NyAzNTAuNTY5NDEyIDkuNjM3NjQ3LTM1MC41Njk0MTJjLTYuMDIzNTI5IDAtMTMuMjUxNzY1IDEuMjA0NzA2LTE5LjI3NTI5NCAwek01OTIuNzE1Mjk0IDc1Mi45NDExNzZsNC44MTg4MjQtMTQ5LjM4MzUyOWMtMi40MDk0MTIgMy42MTQxMTgtNi4wMjM1MjkgNi4wMjM1MjktOS42Mzc2NDcgOS42Mzc2NDdsNC44MTg4MjMgMTM5Ljc0NTg4MnpNNTQ0LjUyNzA1OSA4OTAuMjc3NjQ3bDkuNjM3NjQ3LTI2MC4yMTY0NzEtMTguMDcwNTg4IDMuNjE0MTE4IDguNDMyOTQxIDI1Ni42MDIzNTN6IiBwLWlkPSIzNjA0IiBmaWxsPSIjZDgxZTA2Ij48L3BhdGg+PC9zdmc+",
        "scale" : 0.3,
    },
    path : {
        resolution : 1,
        material : new Cesium.PolylineGlowMaterialProperty({
            glowPower : 0.1,
            color : Cesium.Color.YELLOW
        }),
        width :3
    },
},{
    "id" : "point",
    "availability" :"2012-08-04T16:00:00Z/2012-08-04T16:05:00Z",
    "position" : {
        "epoch" : "2012-08-04T16:00:00Z",
         "cartographicDegrees" : [
             0,   70, 200, 150000,
             100, 80, 144, 150000,
             200, 90, 118, 150000,
             300, 98, 152, 150000, 
         ]
    },
    
    "billboard" : {
        "image" : "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTgzNDY3MTIyNzY1IiBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM2MDMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+PGRlZnM+PHN0eWxlIHR5cGU9InRleHQvY3NzIj48L3N0eWxlPjwvZGVmcz48cGF0aCBkPSJNNTc5LjQ2MzUyOSAyMDYuMDA0NzA2Yy0zMC4xMTc2NDctMTQ2Ljk3NDExOC02MC4yMzUyOTQtMTYyLjYzNTI5NC02MC4yMzUyOTQtMTYyLjYzNTI5NC00LjgxODgyNC00LjgxODgyNC0xMC44NDIzNTMtNC44MTg4MjQtMTUuNjYxMTc2IDAgMCAwLTMwLjExNzY0NyAxNS42NjExNzYtNjAuMjM1Mjk0IDE2Mi42MzUyOTQgMCAwLTE5LjI3NTI5NCAxMDIuNC0xOS4yNzUyOTQgMTg1LjUyNDcwNlY1NTQuMTY0NzA2YzAgNDUuNzc4ODI0IDE3NC42ODIzNTMgNDAuOTYgMTc0LjY4MjM1MyAzLjYxNDExOFYzOTEuNTI5NDEyYzEuMjA0NzA2LTgzLjEyNDcwNi0xOS4yNzUyOTQtMTg1LjUyNDcwNi0xOS4yNzUyOTUtMTg1LjUyNDcwNnpNNTY2LjIxMTc2NSAzMTAuODE0MTE4YzAgNi4wMjM1MjktMS4yMDQ3MDYgNC44MTg4MjQtNi4wMjM1MyA2LjAyMzUyOWgtMTAuODQyMzUzcy0xNC40NTY0NzEtMTc4LjI5NjQ3MS0yNy43MDgyMzUtMjMzLjcxMjk0MWMwIDAgNDguMTg4MjM1IDEyMS42NzUyOTQgNDQuNTc0MTE4IDIyNy42ODk0MTJ6TTQ1NC4xNzQxMTggODM2LjA2NTg4Mmw3LjIyODIzNS0yMDkuNjE4ODIzYy02LjAyMzUyOS0yLjQwOTQxMi0xMC44NDIzNTMtNC44MTg4MjQtMTUuNjYxMTc3LTcuMjI4MjM1bDguNDMyOTQyIDIxNi44NDcwNTh6TTQzMS4yODQ3MDYgNzQ4LjEyMjM1M2w0LjgxODgyMy0xMzYuMTMxNzY1Yy0zLjYxNDExOC0zLjYxNDExOC03LjIyODIzNS03LjIyODIzNS05LjYzNzY0Ny0xMi4wNDcwNTlsNC44MTg4MjQgMTQ4LjE3ODgyNHpNNDgzLjA4NzA1OSA4OTUuMDk2NDcxbDkuNjM3NjQ3LTI2MS40MjExNzdjLTYuMDIzNTI5IDAtMTIuMDQ3MDU5LTEuMjA0NzA2LTE2Ljg2NTg4Mi0yLjQwOTQxMmw3LjIyODIzNSAyNjMuODMwNTg5ek01NzMuNDQgODMyLjQ1MTc2NWw3LjIyODIzNS0yMTUuNjQyMzUzYy0zLjYxNDExOCAzLjYxNDExOC04LjQzMjk0MSA2LjAyMzUyOS0xNC40NTY0NyA4LjQzMjk0MWw3LjIyODIzNSAyMDcuMjA5NDEyek01MDMuNTY3MDU5IDYzNC44OGw5LjYzNzY0NyAzNTAuNTY5NDEyIDkuNjM3NjQ3LTM1MC41Njk0MTJjLTYuMDIzNTI5IDAtMTMuMjUxNzY1IDEuMjA0NzA2LTE5LjI3NTI5NCAwek01OTIuNzE1Mjk0IDc1Mi45NDExNzZsNC44MTg4MjQtMTQ5LjM4MzUyOWMtMi40MDk0MTIgMy42MTQxMTgtNi4wMjM1MjkgNi4wMjM1MjktOS42Mzc2NDcgOS42Mzc2NDdsNC44MTg4MjMgMTM5Ljc0NTg4MnpNNTQ0LjUyNzA1OSA4OTAuMjc3NjQ3bDkuNjM3NjQ3LTI2MC4yMTY0NzEtMTguMDcwNTg4IDMuNjE0MTE4IDguNDMyOTQxIDI1Ni42MDIzNTN6IiBwLWlkPSIzNjA0IiBmaWxsPSIjZDgxZTA2Ij48L3BhdGg+PC9zdmc+",
        "scale" : 0.3,
    },
    path : {
        resolution : 1,
        material : new Cesium.PolylineGlowMaterialProperty({
            glowPower : 0.1,
            color : Cesium.Color.YELLOW
        }),
        width :3
    },
}];
 
var viewer = new Cesium.Viewer('cesiumContainer', {
    shouldAnimate : true,
    sceneMode: 2, 
});
 
viewer.dataSources.add(Cesium.CzmlDataSource.load(czml)).then(ds=>{
    for(var i = 1;i <= czml.length; i++){
        var s = ds.entities.getById(czml[i].id);
        s.orientation = new  Cesium.VelocityOrientationProperty(s.position);
        s.billboard.alignedAxis = new Cesium.VelocityVectorProperty(s.position, true)
    }
});
```

效果如图所示

![效果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200930172559.png)


## 原文地址
[Cesium基于czml billboard的模型转向](https://blog.csdn.net/yangwqi/article/details/105415328)