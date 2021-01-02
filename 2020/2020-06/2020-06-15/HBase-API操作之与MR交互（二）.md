# HBase-API操作之与MR交互（二）

目标：实现将 HDFS 中的数据写入到 HBase 表中

1. 构建 Mapper 用于读取 HDFS 中的文件数据
    ```java
    package com.yaindream.mr1;

    import org.apache.hadoop.io.LongWritable;
    import org.apache.hadoop.io.Text;
    import org.apache.hadoop.mapreduce.Mapper;

    import java.io.IOException;

    /**
     * Created with IntelliJ IDEA.
     * User: WangYu
     * Date: 2020/6/15
     * Time: 19:11
     * Description:
     */
    public class FruitMapper extends Mapper<LongWritable, Text, LongWritable, Text> {

        @Override
        protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            context.write(key, value);
        }
    }
    ```

2. 构建 Reducer 类用于对读入的数据进行处理
    ```java
    package com.yaindream.mr1;

    import org.apache.hadoop.hbase.client.Put;
    import org.apache.hadoop.hbase.mapreduce.TableReducer;
    import org.apache.hadoop.hbase.util.Bytes;
    import org.apache.hadoop.io.LongWritable;
    import org.apache.hadoop.io.NullWritable;
    import org.apache.hadoop.io.Text;

    import java.io.IOException;

    /**
     * Created with IntelliJ IDEA.
     * User: WangYu
     * Date: 2020/6/15
     * Time: 19:11
     * Description:
     */
    public class FruitReducer extends TableReducer<LongWritable, Text, NullWritable> {

        @Override
        protected void reduce(LongWritable key, Iterable<Text> values, Context context) throws IOException, InterruptedException {

            // 1. 遍历values
            for (Text value : values) {

                // 2. 获取每一行数据
                String[] fields = value.toString().split("\t");

                // 3. 构建put对象
                Put put = new Put(Bytes.toBytes(fields[0]));

                // 4. 给put对象赋值
                put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("name"), Bytes.toBytes(fields[1]));
                put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("color"), Bytes.toBytes(fields[2]));

                // 5. 写出
                context.write(NullWritable.get(), put);
            }
        }
    }
    ```
    
3. 构建 Driver 类组装 Job
    ```java
    package com.yaindream.mr1;

    import org.apache.hadoop.conf.Configuration;
    import org.apache.hadoop.fs.Path;
    import org.apache.hadoop.hbase.mapreduce.TableMapReduceUtil;
    import org.apache.hadoop.io.LongWritable;
    import org.apache.hadoop.io.Text;
    import org.apache.hadoop.mapreduce.Job;
    import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
    import org.apache.hadoop.util.Tool;
    import org.apache.hadoop.util.ToolRunner;

    /**
     * Created with IntelliJ IDEA.
     * User: WangYu
     * Date: 2020/6/15
     * Time: 19:12
     * Description:
     */
    public class FruitDriver implements Tool {

        // 定义一个Configuration
        private Configuration configuration = null;

        public int run(String[] args) throws Exception {

            // 1. 获取Job对象
            Job job = Job.getInstance(configuration);

            // 2. 设置驱动类路径
            job.setJarByClass(FruitDriver.class);

            // 3. 设置Mapper & Mapper输出的KV类型
            job.setMapperClass(FruitMapper.class);
            job.setMapOutputKeyClass(LongWritable.class);
            job.setMapOutputValueClass(Text.class);

            // 4. 设置Reducer类
            TableMapReduceUtil.initTableReducerJob(args[1], FruitReducer.class, job);

            // 5. 设置输入参数
            FileInputFormat.setInputPaths(job, new Path(args[0]));

            // 6. 提交任务
            boolean result = job.waitForCompletion(true);

            return result ? 0 : 1;
        }

        public void setConf(Configuration conf) {
            configuration = conf;
        }

        public Configuration getConf() {
            return configuration;
        }

        public static void main(String[] args) {

            try {
                Configuration configuration = new Configuration();
                int run = ToolRunner.run(configuration, new FruitDriver(), args);
                System.exit(run);

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
    ```
    
4. 通过 IDEA 将程序打包成 Jar 包。
![打包](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200615224753.png)

5. 在 HBase 上创建 `fruit2` 表
```
hbase(main):001:0> create 'fruit2','info'
```

6. 将 Jar 包上传到集群上，然后运行。yarn 命令是 `/opt/module/hadoop-2.7.2/bin/yarn`。如果配置了环境变量就可以直接使用。
```
[root@hadoop02 hbase-1.3.1]# yarn jar hbase-demo-1.0-SNAPSHOT.jar com.yaindream.mr1.FruitDriver /fruit.tsv fruit1
```

7. 运行结果
![运行结果](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200615225442.png)
![运行结果2](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200615225506.png)
