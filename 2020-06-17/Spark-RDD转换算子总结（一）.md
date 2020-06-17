# Spark-RDD转换算子总结（一）

  - [编程模型](#%E7%BC%96%E7%A8%8B%E6%A8%A1%E5%9E%8B)
  - [RDD 的转换算子](#rdd-%E7%9A%84%E8%BD%AC%E6%8D%A2%E7%AE%97%E5%AD%90)
  - [Value 类型](#value-%E7%B1%BB%E5%9E%8B)
    - [map(func)](#mapfunc)
    - [mapPartitions(func)](#mappartitionsfunc)
    - [mapPartitionsWithIndex(func)](#mappartitionswithindexfunc)
    - [flatMap(func)](#flatmapfunc)
    - [glom()](#glom)
    - [groupBy(func)](#groupbyfunc)
    - [filter(func)](#filterfunc)

## 编程模型
在 Spark 中，RDD 被表示为对象，通过对象上的方法调用来对 RDD 进行转换。经过一系列的 transformations 定义 RDD 之后，就可以调用 actions 触发 RDD 的计算，action 可以是向应用程序返回结果（count, collect等），或者是向存储系统保存数据（saveAsTextFile等）。在 Spark 中，只有遇到 action，才会执行 RDD 的计算(即延迟计算)，这样在运行时可以通过管道的方式传输多个转换。

## RDD 的转换算子
整体上可分为 Value 类型和 Key-Value 类型

## Value 类型

### map(func)

作用：返回一个新的 RDD，该 RDD 由每一个输入元素经过 func 函数转换后组成

需求：创建一个 1-10 数组的 RDD，将所有元素 * 2 形成新的 RDD

代码：
```scala
package com.yaindream.bigdata.spark

import org.apache.spark.{SparkConf, SparkContext}

object Spark_Map {

  def main(args: Array[String]): Unit = {

    System.setProperty("hadoop.home.dir", "E:/_ThirdSDK/hadoop-2.7.2")

    // 创建 spark conf 对象
    // 设定 spark 计算框架的运行（部署）环境
    val config = new SparkConf().setMaster("local").setAppName("map")

    // 创建 spark 上下文对象
    val sc = new SparkContext(config)

    // map 算子
    val listRDD = sc.makeRDD(1 to 10)

    val mapRDD = listRDD.map(x => x * 2)

    mapRDD.collect().foreach(println)

  }
  
}
```

### mapPartitions(func)

作用：类似于 map，但独立地在 RDD 的每一个分片上运行，因此在类型为 T 的 RDD 上运行时，func 的函数类型必须是 Iterator[T] => Iterator[U]。假设有 N 个元素，有 M 个分区，那么 map 的函数的将被调用 N 次,而 mapPartitions 被调用 M 次,一个函数一次处理所有分区。即 map 和元素个数有关，mapPartitions 和分区个数有关

map() 和 mapPartition() 的区别：
1. map()：每次处理一条数据
2. mapPartition()：每次处理一个分区的数据，这个分区的数据处理完后，原 RDD 中分区的数据才能释放，可能导致 OOM
3. 开发指导：当内存空间较大的时候建议使用 mapPartition()，以提高处理效率

需求：创建一个 RDD，使每个元素 * 2 组成新的 RDD

代码
```scala
package com.yaindream.bigdata.spark

import org.apache.spark.{SparkConf, SparkContext}

object Spark_MapPartitions {

  def main(args: Array[String]): Unit = {

    System.setProperty("hadoop.home.dir", "E:/_ThirdSDK/hadoop-2.7.2")

    // 创建 spark conf 对象
    // 设定 spark 计算框架的运行（部署）环境
    val config = new SparkConf().setMaster("local").setAppName("mapPartitions")

    // 创建 spark 上下文对象
    val sc = new SparkContext(config)

    // mapPartitions 算子
    val listRDD = sc.makeRDD(1 to 10)

    // mapPartitions 可以对一个 RDD 中的所有分区进行遍历
    // mapPartitions 效率优于 map 算子，减少了发送到执行器执行交互次数
    // mapPartitions 可能会出现内存溢出（OOM）
    val mapPartitionsRDD = listRDD.mapPartitions(datas => {
      datas.map(data => data * 2)
    })

    mapPartitionsRDD.collect().foreach(println)

  }

}
```

### mapPartitionsWithIndex(func)

作用：类似于 mapPartitions，但 func 带有一个整数参数表示分片的索引值，因此在类型为 T 的 RDD 上运行时，func 的函数类型必须是 (Int, Interator[T]) => Iterator[U]

需求：创建一个 RDD，使每个元素跟所在分区形成一个元组组成一个新的 RDD

代码
```scala
package com.yaindream.bigdata.spark

import org.apache.spark.{SparkConf, SparkContext}

object Spark_MapPartitionsWithIndex {

  def main(args: Array[String]): Unit = {

    System.setProperty("hadoop.home.dir", "E:/_ThirdSDK/hadoop-2.7.2")

    // 创建 spark conf 对象
    // 设定 spark 计算框架的运行（部署）环境
    val config = new SparkConf().setMaster("local").setAppName("mapPartitionsWithIndex")

    // 创建 spark 上下文对象
    val sc = new SparkContext(config)

    // mapPartitionsWithIndex 算子，指定两个分区
    val listRDD = sc.makeRDD(1 to 10, 2)

    val tupleRDD = listRDD.mapPartitionsWithIndex {
      case (num, datas) => {
        datas.map((_, "分区号：" + num))
      }
    }

    tupleRDD.collect().foreach(println)

  }

}
```

### flatMap(func)

作用：类似于 map，但是每一个输入元素可以被映射为 0 或多个输出元素（所以 func 应该返回一个序列，而不是单一元素）

需求：将二维数组映射为一维数组

代码
```scala
package com.yaindream.bigdata.spark

import org.apache.spark.{SparkConf, SparkContext}

object Spark_FlatMap {

  def main(args: Array[String]): Unit = {

    System.setProperty("hadoop.home.dir", "E:/_ThirdSDK/hadoop-2.7.2")

    // 创建 spark conf 对象
    // 设定 spark 计算框架的运行（部署）环境
    val config = new SparkConf().setMaster("local").setAppName("flatMap")

    // 创建 spark 上下文对象
    val sc = new SparkContext(config)

    // flatMap 算子
    val listRDD = sc.makeRDD(Array(List(1, 2), List(3, 4)))

    val flatMapRDD = listRDD.flatMap(datas => datas)
    
    flatMapRDD.collect().foreach(println)

  }

}
```

### glom()

作用：将每一个分区形成一个数组，形成新的 RDD 类型时 RDD[Array[T]]

需求：创建一个 4 个分区的 RDD，并将每个分区的数据放到一个数组

代码
```scala
package com.yaindream.bigdata.spark

import org.apache.spark.{SparkConf, SparkContext}

object Spark_Glom {

  def main(args: Array[String]): Unit = {

    System.setProperty("hadoop.home.dir", "E:/_ThirdSDK/hadoop-2.7.2")

    // 创建 spark conf 对象
    // 设定 spark 计算框架的运行（部署）环境
    val config = new SparkConf().setMaster("local").setAppName("glom")

    // 创建 spark 上下文对象
    val sc = new SparkContext(config)

    // glom 算子
    val listRDD = sc.makeRDD(1 to 10, 4)

    val glomRDD = listRDD.glom()

    glomRDD.collect().foreach(array => {
      println(array.mkString(","))
    })

  }

}
```

### groupBy(func)

作用：分组，按照传入函数的返回值进行分组。将相同的 key 对应的值放入一个迭代器

需求：创建一个 RDD，按照元素模以 2 的值进行分组

代码
```scala
package com.yaindream.bigdata.spark

import org.apache.spark.{SparkConf, SparkContext}

object Spark_GroupBy {

  def main(args: Array[String]): Unit = {

    System.setProperty("hadoop.home.dir", "E:/_ThirdSDK/hadoop-2.7.2")

    // 创建 spark conf 对象
    // 设定 spark 计算框架的运行（部署）环境
    val config = new SparkConf().setMaster("local").setAppName("groupBy")

    // 创建 spark 上下文对象
    val sc = new SparkContext(config)

    // groupBy 算子
    val listRDD = sc.makeRDD(1 to 10)

    val groupByRDD = listRDD.groupBy(x => x % 2)

    groupByRDD.collect().foreach(println)

  }

}
```

### filter(func)

作用：过滤。返回一个新的 RDD，该 RDD 由经过 func 函数计算后返回值为 true 的输入元素组成

需求：创建一个 RDD，按照元素模以 2 的值是否为 0 进行分组

代码
```
package com.yaindream.bigdata.spark

import org.apache.spark.{SparkConf, SparkContext}

object Spark_Filter {

  def main(args: Array[String]): Unit = {

    System.setProperty("hadoop.home.dir", "E:/_ThirdSDK/hadoop-2.7.2")

    // 创建 spark conf 对象
    // 设定 spark 计算框架的运行（部署）环境
    val config = new SparkConf().setMaster("local").setAppName("filter")

    // 创建 filter 上下文对象
    val sc = new SparkContext(config)

    // groupBy 算子
    val listRDD = sc.makeRDD(1 to 10)

    val filterRDD = listRDD.filter(x => x % 2 == 0)

    filterRDD.collect().foreach(println)

  }

}
```