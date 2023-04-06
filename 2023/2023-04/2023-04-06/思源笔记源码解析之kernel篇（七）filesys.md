---
title: 思源笔记源码解析之kernel篇（七）filesys
date: 2023-04-06 19:47:12
categories:
 - [不看会后悔的实用技巧分享, 源码解析, 思源笔记]
tags: 
 - 思源笔记
---

## 总结

根据以上你自己的分析，对程序的整体功能和构架做出概括。然后用一张 markdown 表格整理每个文件的功能

### 程序整体功能和构架概述

该程序为一个文件系统模块，提供了文件树的结构和相关操作，主要包括两个子模块：文件树模块和 JSON 解析模块。

文件树模块包括 `tree.go ​`，提供了文件树的加载、存储以及一些辅助函数，通过读写磁盘、解析 JSON 数据等方式来构建和维护文件树的结构和属性。

JSON 解析模块包括 `json_parser.go ​`，提供了将 JSON 解析成 `parse.Tree` 数据结构的功能，同时能处理一些历史数据并做修正。

### 模块功能概述

| 模块名称      | 文件路径               | 模块功能                                                                       |
| --------------- | ------------------------ | -------------------------------------------------------------------------------- |
| 文件树模块    | filesys\tree.go        | 提供文件树的加载、存储以及一些辅助函数。                                       |
| JSON 解析模块 | filesys\json_parser.go | 提供将 JSON 解析成 parse.Tree 数据结构的功能，同时能处理一些历史数据并做修正。 |

注：parse.Tree 是一个内部数据结构，表示 Markdown 的语法树。

## [0/2] json_parser.go

该文件是一个与 JSON 相关的解析器，主要提供了两个函数 `ParseJSONWithoutFix` 和 `ParseJSON` ，用于将 JSON 解析成 parse.Tree 数据结构，其中 `ParseJSON` 函数还能解析一些历史数据并做修正。具体来说：

* `ParseJSONWithoutFix` 函数接收 JSON 字符串 `jsonData` 和解析选项 `options`，使用 `goccy/go-json` 的库将 JSON 转成 `ast.Node`，随后递归遍历 `ast.Node` 构建 `parse.Tree`。该函数不做历史数据修正。
* `ParseJSON` 函数的功能基本与 `ParseJSONWithoutFix` 相同，只是多了一些历史数据修正的功能。对于某些历史数据，该函数将对一些不规范的格式和空内容的节点做修正，同时如果发现数据版本是小于 1.5.0 的，会标记需要将数据迁移至版本 1.5.0 及以上才能正常解析。

除了以上两个函数外，还提供了 `genTreeByJSON` 和 `fixLegacyData` 两个辅助函数。其中 `genTreeByJSON` 函数实现了递归遍历 `ast.Node` 后生成 `parse.Tree` 的过程，同时在递归的过程中如果遇到需要修正的节点，则委托 `fixLegacyData` 函数处理该节点。而 `fixLegacyData` 则是一个历史数据修正的函数，主要处理块的 ID、块尾软换行、空列表、空引述、空公式等问题。

## [1/2] tree.go

该程序文件为文件系统模块的一个子模块，主要实现了文件树的加载、存储以及一些辅助函数。函数主要包括：

* `LoadTree`：从指定路径加载文件树。
* `LoadTreeByData`：从数据中加载文件树。
* `WriteTreeWithoutChangeTime` 和 `WriteTree`：将文件树数据写入磁盘。
* `prepareWriteTree`：准备将文件树写入磁盘前的操作。
* `afterWriteTree`：文件树写入磁盘后更新缓存的相关操作。
* `parseJSON2Tree`：将 JSON 数据解析为文件树的操作。
* `ReadDocIAL`：读取文件中的属性集合。

该程序文件主要是文件树模块中的核心操作，它们通过读写磁盘、解析 JSON 数据等方式来构建和维护文件树的结构和属性。
