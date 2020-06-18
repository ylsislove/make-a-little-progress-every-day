# GeoMesa-导入GDELT数据到HBase

  - [GDELT 介绍](#gdelt-%E4%BB%8B%E7%BB%8D)
  - [下载数据](#%E4%B8%8B%E8%BD%BD%E6%95%B0%E6%8D%AE)
  - [将数据解压并上传到 HDFS 中](#%E5%B0%86%E6%95%B0%E6%8D%AE%E8%A7%A3%E5%8E%8B%E5%B9%B6%E4%B8%8A%E4%BC%A0%E5%88%B0-hdfs-%E4%B8%AD)
  - [开始导入](#%E5%BC%80%E5%A7%8B%E5%AF%BC%E5%85%A5)
  - [HBase 查看](#hbase-%E6%9F%A5%E7%9C%8B)

## GDELT 介绍
GDELT 是国外一个大数据存储项目，它提供了自 1979 年至今的全球广播、印刷和网络新闻媒体报道的事件，并按时间和位置索引。其数据量十分庞大，类别也很丰富。本篇使用使用 2020 年 6 月 15 日的数据进行试验。

## 下载数据
```
wget http://data.gdeltproject.org/gdeltv2/20200615000000.export.CSV.zip
```

## 将数据解压并上传到 HDFS 中
```
[root@hadoop02 home]# hadoop fs -put 20200615000000.export.CSV /myhome/20200615.tsv
```

## 开始导入
执行如下的命令，geomesa 的命令行工具会启动一个 MapReduce 任务，将 hdfs 中的数据文件写入到数据库中，并构建索引。
```bash
[root@hadoop02 geomesa-hbase_2.11-2.4.1]# geomesa-hbase ingest --catalog <table> --feature-name gdelt --converter gdelt2 --spec gdelt2 "hdfs://hadoop02:9000/myhome/20200615.tsv"
```

其中 table 是要写入的表的名称

下面是输出结果

![输出结果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200618180646.png)

可以看到成功导入了 1655 条数据，66 条导入失败。部分失败可能是由于莫名的原因导致的，之后有空再细究吧

## HBase 查看
![查看HBase](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200618180914.png)

可以看到成功导入了 1655 条数据