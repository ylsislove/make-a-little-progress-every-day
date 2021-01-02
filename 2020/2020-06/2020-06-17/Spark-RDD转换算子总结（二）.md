# Spark-RDD转换算子总结（二）

  - [Value 类型](#value-%E7%B1%BB%E5%9E%8B)
    - [sample(withReplacement, fraction, seed)](#samplewithreplacement-fraction-seed)
    - [distinct([numPartitions]))](#distinctnumpartitions)
    - [coalesce(numPartitions)](#coalescenumpartitions)
    - [repartition(numPartitions)](#repartitionnumpartitions)
    - [sortBy(func,[ascending], [numTasks])](#sortbyfuncascending-numtasks)

## Value 类型

### sample(withReplacement, fraction, seed)

作用：以指定的随机种子随机抽样出数量为 fraction 的数据，withReplacement 表示是抽出的数据是否放回，true 为有放回的抽样，false 为无放回的抽样，seed 用于指定随机数生成器种子

需求：创建一个 RDD（1-10），从中选择放回和不放回抽样

代码
```scala
package com.yaindream.bigdata.spark

import org.apache.spark.{SparkConf, SparkContext}

object Spark_Sample {

  def main(args: Array[String]): Unit = {

    System.setProperty("hadoop.home.dir", "E:/_ThirdSDK/hadoop-2.7.2")

    // 创建 spark conf 对象
    // 设定 spark 计算框架的运行（部署）环境
    val config = new SparkConf().setMaster("local").setAppName("sample")

    // 创建 spark 上下文对象
    val sc = new SparkContext(config)

    // sample 算子
    val listRDD = sc.makeRDD(1 to 10)

    val sampleRDD = listRDD.sample(false, 0.4, 1)
//    val sampleRDD = listRDD.sample(true, 2, 1)

    sampleRDD.collect().foreach(println)

  }

}
```

### distinct([numPartitions]))

作用：对源 RDD 进行去重后返回一个新的 RDD。默认情况下，结果返回默认的分区数，但是可以传入一个可选的 numPartitions 参数改变它。

需求：创建一个 RDD，使用 distinct() 对其去重

代码
```scala
package com.yaindream.bigdata.spark

import org.apache.spark.{SparkConf, SparkContext}

object Spark_Distinct {

  def main(args: Array[String]): Unit = {

    System.setProperty("hadoop.home.dir", "E:/_ThirdSDK/hadoop-2.7.2")

    // 创建 spark conf 对象
    // 设定 spark 计算框架的运行（部署）环境
    val config = new SparkConf().setMaster("local").setAppName("distinct")

    // 创建 spark 上下文对象
    val sc = new SparkContext(config)

    // distinct 算子
    val listRDD = sc.makeRDD(List(1, 2, 1, 5, 2, 9, 6, 1))

//    val distinctRDD = listRDD.distinct()
    // 使用 distinct 算子对数据去重，但是因为去重后会导致数据减少，所以可以改变默认的分区数量
    val distinctRDD = listRDD.distinct(2)

    distinctRDD.collect().foreach(println)

  }

}
```

### coalesce(numPartitions)

作用：缩减分区数，用于大数据集过滤后，提高小数据集的执行效率

需求：创建一个 4 个分区的 RDD，对其缩减分区

代码
```scala
package com.yaindream.bigdata.spark

import org.apache.spark.{SparkConf, SparkContext}

object Spark_Coalesce {

  def main(args: Array[String]): Unit = {

    System.setProperty("hadoop.home.dir", "E:/_ThirdSDK/hadoop-2.7.2")

    // 创建 spark conf 对象
    // 设定 spark 计算框架的运行（部署）环境
    val config = new SparkConf().setMaster("local").setAppName("coalesce")

    // 创建 spark 上下文对象
    val sc = new SparkContext(config)

    // coalesce 算子
    val listRDD = sc.makeRDD(1 to 16, 4)

    println("缩减分区前 = " + listRDD.partitions.size)

    val coalesceRDD = listRDD.coalesce(3)

    println("缩减分区后 = " + coalesceRDD.partitions.size)

    coalesceRDD.collect().foreach(println)

  }

}
```

### repartition(numPartitions)

作用：根据分区数，重新通过网络随机洗牌所有数据

需求：创建一个 4 个分区的 RDD，对其重新分区

1. 创建一个 RDD
    ```
    scala> var rdd = sc.makeRDD(1 to 16, 4)
    rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[0] at makeRDD at <console>:24
    ```

2. 查看 RDD 的分区数
    ```
    scala> rdd.partitions.size
    res0: Int = 4
    ```

3. 查看数据
    ```
    scala> rdd.collect()
    res1: Array[Int] = Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16) 
    ```

4. 对 RDD 重新分区
    ```
    scala> var rerdd = rdd.repartition(2)
    rerdd: org.apache.spark.rdd.RDD[Int] = MapPartitionsRDD[4] at repartition at <console>:26
    ```

5. 查看新 RDD 的分区数
    ```
    scala> rerdd.partitions.size
    res2: Int = 2
    ```

6. 查看洗牌过后的数据
    ```
    scala> rerdd.collect
    res3: Array[Int] = Array(1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14, 16)
    ```

coalesce 和 repartition 的区别

coalesce 重新分区，可以选择是否进行 shuffle 过程。由参数 shuffle: Boolean = false/true 决定。

repartition 实际上是调用的 coalesce，默认是进行 shuffle 的。源码如下：
```scala
def repartition(numPartitions: Int)(implicit ord: Ordering[T] = null): RDD[T] = withScope {
  coalesce(numPartitions, shuffle = true)
}
```

### sortBy(func,[ascending], [numTasks])

作用；使用 func 先对数据进行处理，按照处理后的数据比较结果排序，默认为正序

需求：创建一个 RDD，按照不同的规则进行排序

1. 创建一个 RDD
    ```
    scala> var rdd = sc.makeRDD(List(2, 1, 3, 4))
    rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[5] at makeRDD at <console>:24
    ```

2. 按照自身大小排序
    ```
    scala> rdd.sortBy(x => x).collect()
    res4: Array[Int] = Array(1, 2, 3, 4)
    ```

3. 按照与 3 余数的大小排序
    ```
    scala> rdd.sortBy(x => x % 3).collect()
    res5: Array[Int] = Array(3, 1, 4, 2)
    ```