---
title: 思源笔记源码解析之kernel篇（二）av
date: 2023-04-04 00:39:25
categories:
 - [不看会后悔的实用技巧分享, 源码解析, 思源笔记]
tags: 
 - 思源笔记
---

## 总结

根据以上你自己的分析，对程序的整体功能和构架做出概括。然后用一张markdown表格整理每个文件的功能

根据以上分析，该程序的整体功能是提供属性视图的相关实现，用于数据的存储、管理和查询。程序的核心结构包括 Cell、Column 和 Row，其中 Cell 表示单元格，Column 表示表的一列，包括列 ID、列名、列类型、关联的属性视图 ID、目标关联列 ID 以及选项列表等信息，Row 表示表的一行，其中包含多个 Cell。

下表是对每个文件功能的概括和简要说明：

| 文件名    | 功能概述                                                                                                                          | 主要函数和结构体说明                                                                                                                                                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| av.go     | 提供属性视图的列名列出、插入列、读取和保存 AttributeView 结构体、删除列和表等功能                                                 | GetColumnNames(), InsertColumn(), ParseAttributeView(), SaveAttributeView(), getAttributeViewDataPath(), dropAttributeViewTableColumn(), addAttributeViewTableColumn(), dropAttributeViewTable(), createAttributeViewTable() |
| cell.go   | 定义 Cell 结构体，表示属性视图中的单元格，具有两个成员变量 ID 和 Value，并可序列化为 JSON 格式                                    | Cell 结构体                                                                                                                                                                                                                  |
| column.go | 定义 ColumnType（列类型）、Column（列基础结构）和 ColumnSelectOption（选项列表）等结构体，提供 NewColumn 方法创建新的 Column 对象 | ColumnType 结构体，Column 结构体，ColumnSelectOption 结构体，NewColumn() 方法                                                                                                                                                |
| row.go    | 定义 Row 结构体，表示属性视图中的一行，具有 ID 和 Cells 两个成员变量，同时提供 NewRow 方法创建一个 Row 结构体指针                 | Row 结构体，NewRow() 方法                                                                                                                                                                                                    |

## [0/4] av.go

该文件为SiYuan笔记应用的属性视图（Attribute View）相关实现代码文件，包含了AttributeView以及其相关的结构体和函数实现。该文件的主要实现了以下功能：

1.列出属性视图的列名 函数：`GetColumnNames()`

2.在指定的位置插入一个Column对象 函数：`InsertColumn()`

3.读取指定ID的属性视图的JSON数据并返回其相应结构体 函数：`ParseAttributeView()`

4.保存指定的AttributeView结构体数据到JSON文件中 函数：`SaveAttributeView()`

5.获取指定ID的AttributeView数据的JSON文件路径 函数：`getAttributeViewDataPath()`

6.在属性视图的数据库表中删除指定的一个列 函数：`dropAttributeViewTableColumn()`

7.在属性视图的数据库表中增加指定的一个列 函数：`addAttributeViewTableColumn()`

8.删除指定ID的属性视图的数据库表 函数：`dropAttributeViewTable()`

9.在属性视图的数据库中创建一个指定ID的表，建立id和指定列的对应关系 函数：`createAttributeViewTable()`

## [1/4] cell.go

该程序文件名为 cell.go，是一段 Go 语言代码。程序定义了一个名为 Cell 的结构体，该结构体有两个成员，分别是 ID 和 Value，均为字符串类型。其中，结构体的成员都被打上了 json 标记，表明这些成员可以被序列化为 JSON 格式。该程序文件可能是某个软件或系统的一部分，用于对单元格进行数据的存储和管理。

## [2/4] column.go

该文件名为column.go，主要包含了属性视图的基础结构的定义，包括ColumnType（列类型）、Column（列基础结构）、ColumnSelectOption（选项列表）等。其中，ColumnType 包含了 block、date、number、relation、rollup、select 和 text 这几种列类型，Column 包含了列 ID、列名、列类型、关联的属性视图 ID、目标关联列 ID 以及选项列表等信息，并提供了 NewColumn 方法，用于创建新的 Column 对象。

## [3/4] row.go

该代码文件为Go语言编写的程序，属于av目录下的一个名为"row.go"的文件。该文件定义了一个名为"Row"的结构体，其中包含有一个"ID"的string类型成员变量以及一个"Cells"的指向"Cell"结构体的切片类型变量。同时该文件还定义了一个"NewRow()"方法用于返回一个新的"Row"结构体指针。该文件依赖于"ast"模块，使用了其中的"NewNodeID()"函数。同时，该代码文件还包含着版权声明和GNU Affero通用公共许可证的相关信息。

