# HBase-API操作之DML

  - [创建 connection 对象](#%E5%88%9B%E5%BB%BA-connection-%E5%AF%B9%E8%B1%A1)
  - [插入数据](#%E6%8F%92%E5%85%A5%E6%95%B0%E6%8D%AE)
  - [获取数据（get）](#%E8%8E%B7%E5%8F%96%E6%95%B0%E6%8D%AEget)
  - [获取数据（scan）](#%E8%8E%B7%E5%8F%96%E6%95%B0%E6%8D%AEscan)
  - [删除数据](#%E5%88%A0%E9%99%A4%E6%95%B0%E6%8D%AE)
  - [测试](#%E6%B5%8B%E8%AF%95)

## 创建 connection 对象
```java
private static Connection connection = null;
private static Admin admin = null;

static {
    try {
        // 获取配置文件信息
        Configuration configuration = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "hadoop02,hadoop03,hadoop04");

        // 创建连接对象
        connection = ConnectionFactory.createConnection(configuration);

        // 创建Admin对象
        admin = connection.getAdmin();

    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

## 插入数据
```java
// 向表插入数据
public static void putData(String tableName, String rowKey, String cf, String cn, String value) throws IOException {
    // 获取表对象
    Table table = connection.getTable(TableName.valueOf(tableName));
    // 创建put对象
    Put put = new Put(Bytes.toBytes(rowKey));
    // 给put对象赋值
    put.addColumn(Bytes.toBytes(cf), Bytes.toBytes(cn), Bytes.toBytes(value));
    // 插入数据
    table.put(put);
    // 关闭连接
    table.close();
}
```

## 获取数据（get）
```java
// 获取数据（get)
private static void getData(String tableName, String rowKey, String cf, String cn) throws IOException {
    // 1. 获取表对象
    Table table = connection.getTable(TableName.valueOf(tableName));
    // 2. 创建get对象
    Get get = new Get(Bytes.toBytes(rowKey));
    // 2.1 可选：指定获取的列族
//        get.addFamily(Bytes.toBytes(cf));
    // 2.2 可选：指定列族和列
    get.addColumn(Bytes.toBytes(cf), Bytes.toBytes(cn));
    // 2.3 设置获取数据的版本数
    get.setMaxVersions();
    // 3. 获取数据
    Result result = table.get(get);
    // 4. 解析result并打印
    for (Cell cell : result.rawCells()) {
        // 打印数据
        System.out.println("CF: " + Bytes.toString(CellUtil.cloneFamily(cell)) +
                ", CN: " + Bytes.toString(CellUtil.cloneQualifier(cell)) +
                ", Value: " + Bytes.toString(CellUtil.cloneValue(cell)));

    }
    // 5. 关闭表连接
    table.close();
}
```

## 获取数据（scan）
```java
// 获取数据（Scan）
private static void scanTable(String tableName) throws IOException {
    // 1. 获取表对象
    Table table = connection.getTable(TableName.valueOf(tableName));
    // 2. 构建一个scan对象
    Scan scan = new Scan(Bytes.toBytes("1001"), Bytes.toBytes("1002"));
    // 3. 扫描表
    ResultScanner scanner = table.getScanner(scan);
    // 4. 解析scanner
    for (Result result : scanner) {
        // 5. 解析result并打印
        for (Cell cell : result.rawCells()) {
            // 打印数据
            System.out.println("RK: " + Bytes.toString(CellUtil.cloneRow(cell)) +
                    ", CF: " + Bytes.toString(CellUtil.cloneFamily(cell)) +
                    ", CN: " + Bytes.toString(CellUtil.cloneQualifier(cell)) +
                    ", Value: " + Bytes.toString(CellUtil.cloneValue(cell)));
        }
    }
    // 6. 关闭表连接
    table.close();
}
```

## 删除数据
```java
// 删除数据
private static void deleteData(String tableName, String rowKey, String cf, String cn) throws IOException {

    // 1. 获取表数据
    Table table = connection.getTable(TableName.valueOf(tableName));

    // 2. 构建delete对象，删除标记是 deleteFamily
    Delete delete = new Delete(Bytes.toBytes(rowKey));

    // 2.1 （加s）可选：设置删除的列（删除所有版本）
    // 若加时间戳，则删除小于等于该时间戳的所有数据，删除标记是 deleteColumn
//        delete.addColumns(Bytes.toBytes(cf), Bytes.toBytes(cn));

    // 2.1 （不加s）可选：生产环境慎用：设置删除的列（删除最新的版本）。可能会造成已经被覆盖的版本复现
    // 若加时间戳，则只删除该时间戳的数据，删除标记是 delete
//        delete.addColumn(Bytes.toBytes(cf), Bytes.toBytes(cn));

    // 2.2 删除指定的列族
    delete.addFamily(Bytes.toBytes(cf));

    // 3. 执行删除操作
    table.delete(delete);

    // 4. 关闭连接
    table.close();
}
```

## 测试
```java
public static void main(String[] args) throws IOException {

    // 插入数据测试
//        putData("student", "1001", "info", "name", "zhangsan");
//        putData("student", "1001", "info", "sex", "male");
//        putData("student", "1002", "info", "name", "lisi");
//        putData("student", "1002", "info", "sex", "female");

    // 获取单行数据
//        getData("student", "1001", "info", "name");

    // 测试扫描数据
//        scanTable("student");

    // 测试删除
    deleteData("student", "1001", "info", "name");

    // 关闭资源
    close();

}
```