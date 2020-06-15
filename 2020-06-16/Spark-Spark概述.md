# Spark-Spark概述

  - [什么是Spark](#%E4%BB%80%E4%B9%88%E6%98%AFspark)
    - [定义](#%E5%AE%9A%E4%B9%89)
    - [历史](#%E5%8E%86%E5%8F%B2)
  - [Spark 内置模块](#spark-%E5%86%85%E7%BD%AE%E6%A8%A1%E5%9D%97)
    - [Spark Core](#spark-core)
    - [Spark SQL](#spark-sql)
    - [Spark Streaming](#spark-streaming)
    - [Spark MLlib](#spark-mllib)
    - [集群管理器](#%E9%9B%86%E7%BE%A4%E7%AE%A1%E7%90%86%E5%99%A8)
  - [Spark 的特点](#spark-%E7%9A%84%E7%89%B9%E7%82%B9)

开始攻坚 Spark

## 什么是Spark

### 定义
Spark是一种基于内存的快速、通用、可扩展的大数据分析引擎

### 历史
* 2009 年诞生于加州大学伯克利分校 AMPLab，项目采用 Scala 编写
* 2010 年开源
* 2013 年 6 月成为 Apache 孵化项目
* 2014 年 2 月成为 Apache 顶级项目

## Spark 内置模块
![内置模块](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200616035548.png)


### Spark Core
实现了 Spark 的基本功能，包含任务调度、内存管理、错误恢复、与存储系统交互等模块。Spark Core 中还包含了对弹性分布式数据集 (Resilient Distributed DataSet，简称RDD) 的 API 定义。

### Spark SQL
是 Spark 用来操作结构化数据的程序包。通过 Spark SQL，我们可以使用 SQL 或者 Apache Hive 版本的 SQL 方言 (HQL) 来查询数据。Spark SQL 支持多种数据源，比如 Hive 表、Parquet 以及 JSON 等。

### Spark Streaming
是 Spark 提供的对实时数据进行流式计算的组件。提供了用来操作数据流的 API，并且与 Spark Core 中的 RDD API 高度对应。

### Spark MLlib
提供常见的机器学习 (ML) 功能的程序库。包括分类、回归、聚类、协同过滤等，还提供了模型评估、数据 导入等额外的支持功能。

### 集群管理器
Spark 设计为可以高效地在一个计算节点到数千个计算节点之间伸缩计算。为了实现这样的要求，同时获得最大灵活性，Spark 支持在各种集群管理器 (Cluster Manager) 上运行，包括 Hadoop YARN、Apache Mesos，以及 Spark 自带的一个简易调度器，叫作独立调度器。

Spark 得到了众多大数据公司的支持，这些公司包括 Hortonworks、IBM、Intel、Cloudera、MapR、Pivotal、百度、阿里、腾讯、京东、携程、优酷土豆。当前百度的 Spark 已应用于大搜索、直达号、百度大数据等业务；阿里利用 GraphX 构建了大规模的图计算和图挖掘系统，实现了很多生产系统的推荐算法；腾讯 Spark 集群达到 8000 台的规模，是当前已知的世界上最大的 Spark 集群。

## Spark 的特点
1. 快：与 Hadoop 的 MapReduce 相比，Spark 基于内存的运算要快 100 倍以上，基于硬盘的运算也要快 10 倍以上。Spark 实现了高效的 DAG 执行引擎，可以通过基于内存来高效处理数据流。计算的中间结果是存在于内存中的。

2. 易用：Spark支持 Java、Python 和 Scala 的 API，还支持超过 80 种高级算法，使用户可以快速构建不同的应用。而且 Spark 支持交互式的 Python 和 Scala 的 Shell，可以非常方便地在这些 Shell 中使用 Spark 集群来验证解决问题的方法。

3. 通用：Spark 提供了统一的解决方案。Spark 可以用于批处理、交互式查询（Spark SQL）、实时流处理（Spark Streaming）、机器学习（Spark MLlib）和图计算（GraphX）。这些不同类型的处理都可以在同一个应用中无缝使用。减少了开发和维护的人力成本和部署平台的物力成本。

4. 兼容性：Spark 可以非常方便地与其他的开源产品进行融合。比如 Spark 可以使用 Hadoop 的 YARN 和 Apache Mesos 作为它的资源管理和调度器，并且可以处理所有 Hadoop 支持的数据，包括 HDFS、HBase 等。这对于已经部署 Hadoop 集群的用户来说特别重要，因为不需要做任何数据迁移就可以使用 Spark 的强大处理能力。