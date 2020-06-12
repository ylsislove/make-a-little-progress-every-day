# HBase-命令行操作

  - [基本操作](#%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C)
  - [表的操作](#%E8%A1%A8%E7%9A%84%E6%93%8D%E4%BD%9C)

## 基本操作
1. 进入 HBase 客户端命令行
    ```bash
    [root@hadoop02 hbase-1.3.1]# bin/hbase shell
    ```
2. 查看帮助命令
    ```
    hbase(main):001:0> help
    ```
3. 查看当前数据库中有哪些表
    ```
    hbase(main):002:0> list
    ```

## 表的操作
1. 创建表
    ```
    hbase(main):003:0> create 'student','info'
    ```
2. 插入数据到表
    ```
    hbase(main):008:0> put 'student','1001','info:sex','male'
    hbase(main):009:0> put 'student','1001','info:age','18'
    hbase(main):010:0> put 'student','1002','info:name','Yain'
    hbase(main):011:0> put 'student','1002','info:sex','female'
    hbase(main):012:0> put 'student','1002','info:age','20'
    ```
3. 扫描查看表数据
    ```
    hbase(main):013:0> scan 'student'
    ROW                                 COLUMN+CELL                                                                                           
    1001                               column=info:age, timestamp=1591983519797, value=18                                                    
    1001                               column=info:sex, timestamp=1591983495451, value=male                                                  
    1002                               column=info:age, timestamp=1591983578545, value=20                                                    
    1002                               column=info:name, timestamp=1591983546299, value=Yain                                                 
    1002                               column=info:sex, timestamp=1591983562853, value=female                                                
    2 row(s) in 0.2470 seconds

    hbase(main):014:0> scan 'student',{STARTROW => '1001', STOPROW => '1001'}
    ROW                                 COLUMN+CELL                                                                                           
    1001                               column=info:age, timestamp=1591983519797, value=18                                                    
    1001                               column=info:sex, timestamp=1591983495451, value=male                                                  
    1 row(s) in 0.1330 seconds

    hbase(main):015:0> scan 'student',{STARTROW => '1001'}
    ROW                                 COLUMN+CELL                                                                                           
    1001                               column=info:age, timestamp=1591983519797, value=18                                                    
    1001                               column=info:sex, timestamp=1591983495451, value=male                                                  
    1002                               column=info:age, timestamp=1591983578545, value=20                                                    
    1002                               column=info:name, timestamp=1591983546299, value=Yain                                                 
    1002                               column=info:sex, timestamp=1591983562853, value=female                                                
    2 row(s) in 0.1280 seconds
    ```
4. 查看表结构
    ```
    hbase(main):016:0> describe 'student'
    ```
5. 更新指定字段的数据
    ```
    hbase(main):019:0> put 'student','1001','info:name','Apple'
    hbase(main):020:0> put 'student','1001','info:age','25'
    ```
6. 查看“指定行”或“指定列族：列”的数据
    ```
    hbase(main):022:0> get 'student','1001'
    hbase(main):023:0> get 'student','1001','info:name'
    ```
7. 统计表数据行数
    ```
    hbase(main):024:0> count 'student'
    ```
8. 删除数据

    删除某 rowkey 的全部数据
    ```
    hbase(main):025:0> deleteall 'student','1001'
    ```

    删除某 rowkey 的某一列数据
    ```
    hbase(main):027:0> delete 'student','1002','info:sex'
    ```

9. 清空表数据
    ```
    hbase(main):029:0> truncate 'student'
    ```
    从系统的输出上可以看到，清空表的操作顺序为先 disable，然后再 truncate。

10. 删除表

    首先需要让该表变为 disable 状态
    ```
    hbase(main):030:0> disable 'student'
    ```

    然后才能 drop 这个表
    ```
    hbase(main):031:0> drop 'student'
    ```
    如果直接 drop 表，会报错哦：ERROR: Table student is enabled. Disable it first.

11. 变更表信息

    将 info 列族中的数据存放 3 个版本：
    ```
    hbase(main):032:0> create 'student','info'
    hbase(main):034:0> alter 'student', {NAME => 'info', VERSIONS => 3}
    ```

    如果 info 列族中某一列的数据存在多个版本，就可以查看多个版本的数据了
    ```
    hbase(main):035:0> get 'student', '1001', {COLUMN => 'info:name', VERSIONS => 3}
    ```

12. 退出
    ```
    hbase(main):041:0> quit
    ```