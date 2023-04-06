---
title: 思源笔记源码解析之kernel篇（六）conf
date: 2023-04-06 19:45:07
categories:
 - [不看会后悔的实用技巧分享, 源码解析, 思源笔记]
tags: 
 - 思源笔记
---

## 总结

根据以上你自己的分析，对程序的整体功能和构架做出概括。然后用一张 markdown 表格整理每个文件的功能

该程序是一个开源的笔记应用，可以允许用户创建、编辑和存储笔记。程序主要分为以下几个模块：

* 界面：提供了一种用户友好的界面，允许用户浏览笔记和进行一些操作。
* 后端：维护笔记和标签的数据，并提供数据更新和存储的功能。
* 云同步：将笔记存储到云端，实现笔记的同步和备份，同时可以允许多个设备之间的数据访问和共享。

下表列出了每个程序文件及其对程序功能的贡献：

| 文件名        | 功能                                               |
| --------------- | ---------------------------------------------------- |
| account.go    | 用户账户的设置及管理                               |
| ai.go         | AI 平台数据访问响应                                |
| api.go        | 网络请求响应                                       |
| appearance.go | 界面的外表设置及管理                               |
| box.go        | “FileTree”的设置，其中包括笔记数据的组织结构     |
| editor.go     | 笔记的编辑器设置，用于创建、编辑、格式化和保存笔记 |
| export.go     | 笔记导出的设置                                     |
| filetree.go   | “FileTree”的实现，包括笔记和标签列表的管理       |
| flashcard.go  | 用于设置和管理闪存卡                               |
| graph.go      | 功能图的设置与管理                                 |
| lang.go       | 语言设置和管理                                     |
| layout.go     | 界面布局的设置和管理                               |
| Repo.go       | 仓库路径的设置和管理                               |
| search.go     | 搜索功能及搜索结果显示设置                         |
| snippet.go    | 快捷方式的设置和管理                               |
| stat.go       | 统计功能的设置和管理                               |
| sync.go       | 笔记同步的设置、管理和实现                         |
| system.go     | 系统设置                                           |
| tag.go        | 标签的设置及管理                                   |
| user.go       | 用户账户管理相关功能的实现                         |

总体而言，这些程序文件的功能都是为了组成一个完整的笔记应用。它们负责不同的功能，通过互相协作实现最终的目标：提供一个高效、可靠的笔记应用程序。

## [0/20] account.go

该文件是 SiYuan 工程中的配置文件 account.go，主要定义了一个结构体 Account 和一个 NewAccount 函数。Account 结构体中包含了两个布尔类型的属性：DisplayTitle 和 DisplayVIP，并且使用 json 标签来指定了它们在 json 格式中的名字。NewAccount 函数用于创建一个新的 Account 结构体，并初始化其中的属性值。

## [1/20] ai.go

该文件名是 ai.go，代表着这是一个 Go 语言程序文件。该程序中定义了两个结构体类型 AI 和 OpenAI。结构体类型 OpenAI 里定义了若干字段，用于保存与 OpenAI 接口相关的参数。函数 NewAI 返回了一个指向 AI 结构体的指针，其中包含一个指向 OpenAI 结构体的指针，并从环境变量中读取用于与 OpenAI 平台交互的相关数据的值。同时，该程序遵循 GNU Affero 通用公共许可证协议。

## [2/20] api.go

该程序文件是 api.go，它实现了一个名为 API 的结构体和 NewAPI()函数。结构体 API 包含一个字符串类型的 Token 字段，表示一个 API 的访问令牌。NewAPI()函数返回一个 API 类型的指针，该函数会生成 16 位随机字符串并将其赋值给 API 的 Token 字段。该程序文件截取自一个名为 SiYuan 的开源项目，它是一个数字花园构建工具并使用 GNU Affero General Public License 许可证。

## [3/20] appearance.go

该程序文件是 conf 目录下的一个名为 appearance.go 的 Go 语言源代码文件。

该文件定义了一个名为 Appearance 的结构体，该结构体包含多个属性字段，用于表示 SiYuan 笔记软件中的用户界面外观设置，例如黑暗模式、主题、图标、代码块主题等。其中还有一些附加属性，如界面语言、自定义 CSS 等。

代码的最后定义了一个名为 NewAppearance 的函数，用于创建一个新的 Appearance 结构体实例。默认情况下，所有属性字段都有默认值。

该文件还包含了 GNU Affero 通用公共许可证的版权声明和许可条款。

## [4/20] box.go

该程序文件名为“box.go”，归属于“conf”软件包。程序代码定义了一个“BoxConf”类型，该类型维护了“.siyuan/conf.json”笔记本配置的各种参数，例如笔记本名称、排序方式、图标等。该程序文件还定义了一个“NewBoxConf()”函数，用于初始化配置参数，设置默认值。该程序文件依赖于“util”软件包，并使用了该软件包中的“SortModeFileTree”变量。程序代码还包括一些注释信息，介绍了该程序的版权及开源协议信息。

## [5/20] editor.go

该程序文件为一个 Go 语言程序的配置文件 editor.go，主要定义了一个名为 Editor 的 struct 类型，包括了编辑器的各种配置参数，如字体大小、字体、代码块是否显示行号、代码块中 Tab 转换空格数等。同时，该文件还定义了一个名为 NewEditor 的函数，返回一个 Editor 类型的指针，用来初始化一个编辑器实例。

## [6/20] export.go

这是一个 Go 语言编写的程序文件，文件名为 export.go，属于 conf 包。该文件定义了一个 Export 结构体及其构造函数 NewExport()，其中 Export 结构体包含了文档导出时的一些设置选项，如段落开头的空格、是否添加标题、内容块引用导出模式等等。同时，该文件还定义了 Export 结构体的默认值，其中大部分设置都是使用默认值。这些设置可以通过导出的功能进行修改。

## [7/20] filetree.go

该程序文件名为 filetree.go，其代码定义了一个名为 FileTree 的结构体类型，并声明了与该结构相关的变量和函数。所该结构体的字段具有不同的类型，包括 bool，string 和 int 等，而且它们的含义是关于文档管理器的一些布尔值或设置，例如是否总是在打开的文件中自动选择，是否在当前页签打开文件，打开文件时列出的最大数量等。此外，该程序文件中包含了一个名为 NewFileTree 的函数，该函数返回一个新的 FileTree 结构体，并将其字段初始化为预定义的值。

## [8/20] flashcard.go

该文件名为 flashcard.go，它实现了一个名为 Flashcard 的结构体以及一个名为 NewFlashcard()的函数。

Flashcard 结构体定义了以下五个字段：

* NewCardLimit：新卡的上限
* ReviewCardLimit：复习卡的上限
* Mark：标记制卡的启用状态
* List：列表块制卡的启用状态
* SuperBlock：超级块制卡的启用状态
* Deck：卡包制卡的启用状态

NewFlashcard()函数返回一个指向 Flashcard 结构体的指针，其中指定了每个字段的初始值。

## [9/20] graph.go

该程序文件为 Go 语言编写的一个配置文件，用于设置图形显示参数。其中，定义了 Graph、LocalGraph 和 GlobalGraph 三个结构体用于区分不同的图形参数，如局部图、全局图等。同时，也定义了 TypeFilter 和 D3 两个结构体用于设置图形显示的具体参数，如节点大小、连线粗细等。 该程序文件包含了构造函数 NewGraph、NewLocalGraph 和 NewGlobalGraph 以及 newD3 函数，用于生成各结构体的实例。同时，还定义了一些不同参数的默认值。

## [10/20] lang.go

该程序文件名为 `lang.go`，属于 `conf` 包下的一个 Go 程序文件。这个文件定义了一个名为 `Lang` 的结构体类型，该结构体包括两个字段：`Label` 和 `Name`，分别表示语言的名称和标签。同时，该结构体还包含了对应的 JSON 字段标签。该程序文件没有导入任何包。也提供了版权声明和 GNU Affero 通用公共许可证文件注释。

## [11/20] layout.go

该程序文件名为 layout.go，位于 conf 文件夹下，实现了两个类型定义：UILayout 和 Keymap。UILayout 是一个由字符串作为键，任何值作为值的映射类型，用于描述用户界面的布局。Keymap 是一个由字符串作为键，任何值作为值的映射类型，用于描述键盘快捷键的映射。这些类型定义可能会被程序的其他部分引用并使用。该程序还包含了版权声明和 GNU Affero General Public License 许可证。

## [12/20] Repo.go

该程序文件是 conf 目录下的 Repo.go 文件。该文件定义了一个名为“Repo”的结构体，包含一个 byte 类型的“Key”属性，用于存储 AES 密钥。此外，该文件还定义了一个“NewRepo”函数，用于创建新的“Repo”实例。还有一个名为“GetSaveDir”的函数，用于返回保存仓库的路径，该路径由“WorkspaceDir”和“repo”目录组成。

## [13/20] search.go

该文件是一段用 Go 语言编写的程序代码，命名为 "search.go"，属于 "conf" 路径下的文件。该程序声明了一个名为 "Search" 的结构体，该结构体定义了一些搜索相关的属性和方法。它包括类型筛选器、名称、别名、简介和指向外部文档的虚拟参考、回链注名、别名、锚点和文档等。还定义了 NAMFilter 方法用于在名称、别名和简介中过滤关键字，并返回匹配结果，以及 TypeFilter 方法用于通过所选类型筛选器来过滤匹配结果。该程序还包含一个 NewSearch 函数，该函数返回一个默认的 Search 结构体。

## [14/20] snippet.go

该程序文件名为 snippet.go，属于 conf 包下的。程序定义了 Snippet 结构体，包含一些 Snippet 实例变量。Snippet 结构体的实例变量包括 ID、Name、Memo、Type、Enabled 和 Content。其中，ID、Name、Memo、Type、Enabled 都是字符串类型，Content 是 Snippet 内容。这个程序文件可能在一个项目中被调用，提供配置信息的存储和读取等功能。

## [15/20] stat.go

该程序文件是一个 Go 语言的代码文件，文件名为 stat.go，位于 conf 文件夹下，是与配置相关的统计信息结构体定义文件。它定义了 Stat 结构体类型，包含了数目、大小等统计信息的属性，有一个方法 NewStat()返回一个指向该结构体类型的指针。此外，文件开头有版权声明和使用 GNU Affero 通用公共许可协议的声明。

## [16/20] sync.go

该程序文件是 conf 目录下的 sync.go 文件。该文件定义了两个结构体：Sync 和两个 Sync 结构体的内嵌结构体——S3 和 WebDAV。其中，Sync 结构体是同步配置相关的结构体，包括云端同步目录名称、是否开启同步、同步模式等信息；S3 结构体是存储于 S3 对象存储服务相关的信息；WebDAV 结构体则是存储于 WebDAV 服务相关的信息。该程序文件中还定义了一些常量和函数，例如：ProviderSiYuan、ProviderS3、ProviderWebDAV，以及 NewSyncProviderCheckURL() 函数等。

## [17/20] system.go

该程序文件名称为 system.go，位于 conf 文件夹下。该程序定义了一个 System 结构体和一个 NetworkProxy 结构体。System 结构体包含了 SiYuan 系统的各种属性，包括 ID、内核版本、操作系统、容器、文件夹路径等，还包括一些功能属性，如是否启用网络服务、是否上传错误日志等。NetworkProxy 结构体用于表示网络代理的信息，其中包括协议、主机和端口号。程序还提供了一个 NewSystem()函数，用于向外部提供一个新的 System 结构体实例。

## [18/20] tag.go

该文件是 SiYuan 软件中的配置文件之一，文件名为 tag.go。程序定义了一个名为 Tag 的结构体，该结构体包含一个名为 Sort 的属性，表示排序方式，并通过 json 标签将其序列化为 JSON 格式。 NewTag 函数返回一个新的初始化 Tag 结构体的指针。程序使用了 SiYuan 软件内部的 util 包中的 SortModeAlphanumASC 常量来表示标签排序方式。程序中还包含 GNU Affero 通用公共许可证的授权声明。

## [19/20] user.go

该文件是一个 Go 语言程序文件，文件名为“user.go”，定义了一个“User”结构体以及一个“UserTitle”结构体。

“User”结构体包括了用户的各种信息，如“userId”、“userName”、“userAvatarURL”等，其中部分字段为浮点数类型。

“UserTitle”结构体包括了用户称号的相关信息，如名称“name”、“描述”、“图标”等。

此外，“User”结构体还定义了一个名为“GetCloudRepoAvailableSize”的方法，返回用户云端仓库可用空间大小。


