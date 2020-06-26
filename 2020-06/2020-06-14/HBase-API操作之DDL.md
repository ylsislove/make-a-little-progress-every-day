# HBase-API操作之DDL

  - [创建 Admin 对象](#%E5%88%9B%E5%BB%BA-admin-%E5%AF%B9%E8%B1%A1)
  - [判断表是否存在](#%E5%88%A4%E6%96%AD%E8%A1%A8%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8)
  - [创建表](#%E5%88%9B%E5%BB%BA%E8%A1%A8)
  - [删除表](#%E5%88%A0%E9%99%A4%E8%A1%A8)
  - [创建命名空间](#%E5%88%9B%E5%BB%BA%E5%91%BD%E5%90%8D%E7%A9%BA%E9%97%B4)
  - [关闭资源](#%E5%85%B3%E9%97%AD%E8%B5%84%E6%BA%90)
  - [测试](#%E6%B5%8B%E8%AF%95)

## 创建 Admin 对象
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

## 判断表是否存在
```java
private static boolean isTableExist(String tableName) throws IOException {
    // 判断表是否存在
    boolean exists = admin.tableExists(TableName.valueOf(tableName));

    // 返回结果
    return exists;
}
```

## 创建表
```java
private static void createTable(String tableName, String... cfs) throws IOException {
    // 判断是否存在列族信息
    if (cfs.length <= 0) {
        System.out.println("请设置列族信息！");
        return;
    }
    // 判断表是否存在
    if (isTableExist(tableName)) {
        System.out.println(tableName + " 表已经存在");
        return;
    }
    // 创建表描述其
    HTableDescriptor hTableDescriptor = new HTableDescriptor(TableName.valueOf(tableName));
    // 循环添加列族信息
    for (String cf : cfs) {
        // 创建列族描述器
        HColumnDescriptor hColumnDescriptor = new HColumnDescriptor(cf);
        // 添加具体的列族信息
        hTableDescriptor.addFamily(hColumnDescriptor);
    }
    // 创建表
    admin.createTable(hTableDescriptor);
}
```

## 删除表
```java
private static void dropTable(String tableName) throws IOException {
    // 判断表是否存在
    if (!isTableExist(tableName)) {
        System.out.println(tableName + "表不存在");
        return;
    }
    // 使表下线
    admin.disableTable(TableName.valueOf(tableName));
    // 删除表
    admin.deleteTable(TableName.valueOf(tableName));
}
```

## 创建命名空间
```java
private static void createNameSpace(String ns) {
    // 创建命名空间描述器
    NamespaceDescriptor namespaceDescriptor = NamespaceDescriptor.create(ns).build();
    // 创建命令空间
    try {
        admin.createNamespace(namespaceDescriptor);
    } catch(NamespaceExistException e) {
        System.out.println(ns + "命名空间已存在");
    } catch (IOException e) {
        e.printStackTrace();
    }

}
```

## 关闭资源
```java
private static void close() {
    if (admin != null) {
        try {
            admin.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    if (connection != null) {
        try {
            connection.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## 测试
```java
public static void main(String[] args) throws IOException {

    // 测试表是否存在
//        System.out.println(isTableExist("stu"));

    // 创建表测试
    createTable("yain:stu", "info");

    // 删除表测试
//        dropTable("stu");
//        System.out.println(isTableExist("stu"));

    // 创建命名空间测试
//        createNameSpace("yain");

    // 关闭资源
    close();

}
```