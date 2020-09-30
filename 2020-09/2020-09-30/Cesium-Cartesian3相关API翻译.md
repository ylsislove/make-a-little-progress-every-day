# Cesium-Cartesian3相关API翻译

坐标转换相关文章可看：[Cesium-坐标系统详解](../2020-09-24/Cesium-坐标系统详解.md)

Cartesian3 相关 API 如下：

| API |	说明 |
| --- | --- |
| Cesium.Cartesian3.abs(cartesian, result)	| 计算绝对值 |
| Cesium.Cartesian3.add(left, right, result) | 计算两个笛卡尔的分量和 |
| Cesium.Cartesian3.angleBetween(left, right) | 计算角度(弧度制) |
| Cesium.Cartesian3.cross(left, right, result) | 计算叉积 |
| Cesium.Cartesian3.distance(left, right) | 计算两点距离 |
| Cesium.Cartesian3.distanceSquared(left, right) | 计算两点平方距离 |
| Cesium.Cartesian3.divideByScalar(cartesian, scalar, result) | 计算标量除法 |
| Cesium.Cartesian3.divideComponents(left, right, result) | 计算两点除法 |
| Cesium.Cartesian3.dot(left, right) | 计算点乘 |
| Cesium.Cartesian3.equals(left, right) | 比较两点是否相等 |
| Cesium.Cartesian3.fromArray(array, startingIndex, result) | 从数组中提取3个数构建笛卡尔坐标 |
| Cesium.Cartesian3.fromDegrees(longitude, latitude, height, ellipsoid, result) | 将将纬度转换为笛卡尔坐标(单位是度°) |
| Cesium.Cartesian3.fromDegreesArray(coordinates, ellipsoid, result) | 返回给定经度和纬度值数组（以度为单位）的笛卡尔位置数组。 |
| Cesium.Cartesian3.fromDegreesArrayHeights(coordinates, ellipsoid, result) | 返回给定经度，纬度和高度的笛卡尔位置数组 |
| Cesium.Cartesian3.fromElements(x, y, z, result) | 创建一个新的笛卡尔坐标 |
| Cesium.Cartesian3.fromRadians(longitude, latitude, height, ellipsoid, result) | 返回笛卡尔坐标以弧度制的经纬度 |
| Cesium.Cartesian3.fromRadiansArray(coordinates, ellipsoid, result) | 返回笛卡尔坐标以弧度制的经纬度数组 |
| Cesium.Cartesian3.fromRadiansArrayHeights(coordinates, ellipsoid, result) | 返回笛卡尔坐标以弧度制的经纬度高度数组 |
| Cesium.Cartesian3.fromSpherical(spherical, result) | 将提供的球面转换为笛卡尔系 |
| Cesium.Cartesian3.lerp(start, end, t, result) | 使用提供的笛卡尔数来计算t处的线性插值或外推。 |
| Cesium.Cartesian3.magnitude(cartesian) | 计算笛卡尔长度 |
| Cesium.Cartesian3.magnitudeSquared(cartesian) | 计算提供的笛卡尔平方量级 |
| Cesium.Cartesian3.maximumByComponent(first, second, result) | 比较两个笛卡尔并计算包含所提供笛卡尔最大成分的笛卡尔。 |
| Cesium.Cartesian3.maximumComponent(cartesian) | 计算所提供笛卡尔坐标系的最大分量的值 |
| Cesium.Cartesian3.midpoint(left, right, result) | 计算右笛卡尔和左笛卡尔之间的中点 |
| Cesium.Cartesian3.minimumByComponent(first, second, result) | 比较两个笛卡尔并计算包含所提供笛卡尔的最小分量的笛卡尔 |
| Cesium.Cartesian3.minimumComponent(cartesian) | 计算所提供笛卡尔坐标系的最小分量的值 |
| Cesium.Cartesian3.mostOrthogonalAxis(cartesian, result) | 返回与提供的笛卡尔坐标最正交的轴 |
| Cesium.Cartesian3.multiplyByScalar(cartesian, scalar, result) | 将提供的笛卡尔分量乘以提供的标量 |
| Cesium.Cartesian3.multiplyComponents(left, right, result) | 计算两个笛卡尔的分量积 |
| Cesium.Cartesian3.normalize(cartesian, result) | 计算所提供笛卡尔的规范化形式 |
| Cesium.Cartesian3.pack(value, array, startingIndex) | 将提供的实例存储到提供的数组中 |
| Cesium.Cartesian3.projectVector(a, b, result) | 将向量a投影到向量b上 |
| Cesium.Cartesian3.subtract(left, right, result) | 计算两个笛卡尔分量差 |
| Cesium.Cartesian3.unpack(array, startingIndex, result) | 从压缩的数组中检索实例 |
| Cesium.Cartesian3.unpackArray(array, result) | 将笛卡尔分量数组解包为笛卡尔数组 |
