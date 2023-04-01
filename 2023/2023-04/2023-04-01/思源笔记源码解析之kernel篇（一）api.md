---
title: 思源笔记源码解析之kernel篇（一）api
date: 2023-04-01 22:06:19
categories:
 - [不看会后悔的实用技巧分享, 源码解析, 思源笔记]
tags: 
 - 思源笔记
---

- [总结](#总结)
- [\[0/38\]account.go](#038accountgo)
- [\[1/38\]ai.go](#138aigo)
- [\[2/38\]asset.go](#238assetgo)
- [\[3/38\] attr.go](#338-attrgo)
- [\[4/38\] av.go](#438-avgo)
- [\[5/38\] bazaar.go](#538-bazaargo)
- [\[6/38\] block.go](#638-blockgo)
- [\[7/38\] block\_op.go](#738-block_opgo)
- [\[8/38\] bookmark.go](#838-bookmarkgo)
- [\[9/38\] clipboard.go](#938-clipboardgo)
- [\[10/38\] export.go](#1038-exportgo)
- [\[11/38\] extension.go](#1138-extensiongo)
- [\[12/38\] file.go](#1238-filego)
- [\[13/38\] filetree.go](#1338-filetreego)
- [\[14/38\] format.go](#1438-formatgo)
- [\[15/38\] graph.go](#1538-graphgo)
- [\[16/38\] history.go](#1638-historygo)
- [\[17/38\] import.go](#1738-importgo)
- [\[18/38\] inbox.go](#1838-inboxgo)
- [\[19/38\] lute.go](#1938-lutego)
- [\[20/38\] notebook.go](#2038-notebookgo)
- [\[21/38\] notification.go](#2138-notificationgo)
- [\[22/38\] outline.go](#2238-outlinego)
- [\[23/38\] ref.go](#2338-refgo)
- [\[24/38\] repo.go](#2438-repogo)
- [\[25/38\] riff.go](#2538-riffgo)
- [\[26/38\] router.go](#2638-routergo)
- [\[27/38\] search.go](#2738-searchgo)
- [\[28/38\] setting.go](#2838-settinggo)
- [\[29/38\] snippet.go](#2938-snippetgo)
- [\[30/38\] sql.go](#3038-sqlgo)
- [\[31/38\] storage.go](#3138-storagego)
- [\[32/38\] sync.go](#3238-syncgo)
- [\[33/38\] system.go](#3338-systemgo)
- [\[34/38\] tag.go](#3438-taggo)
- [\[35/38\] template.go](#3538-templatego)
- [\[36/38\] transaction.go](#3638-transactiongo)
- [\[37/38\] workspace.go](#3738-workspacego)

## 总结

根据以上你自己的分析，对程序的整体功能和构架做出概括。然后用一张 markdown 表格整理每个文件的功能

根据我的分析，该程序是一个基于 API 的笔记管理系统，使用 Go 语言编写，基于 Gin 框架和 Lute 引擎。它包含了多个文件和模块，用于实现不同的功能，例如：笔记本管理、笔记管理、文本编辑、图表管理、导入/导出、同步/备份、用户管理等。可以通过 API 接口调用这些功能。以下是每个文件的功能：

| 文件名          | 功能                                         |
| ----------------- | ---------------------------------------------- |
| account.go      | 用于处理用户账户相关的 API 请求              |
| ai.go           | 提供 AI 语音合成的 API 接口                  |
| asset.go        | 用于上传、查看和下载笔记中使用的资源文件     |
| attr.go         | 提供来源快捷方式操作的 API 接口              |
| av.go           | 提供了音视频播放相关的 API 接口              |
| bazaar.go       | 提供了安装和管理 bazaar 主题插件的 API 接口  |
| block.go        | 处理块的增删改查请求，提供块层级、索引等信息 |
| block_op.go     | 提供文本处理的 API 接口                      |
| bookmark.go     | 提供了书签相关的 API 接口                    |
| clipboard.go    | 处理剪贴板相关的 API 请求                    |
| export.go       | 导出笔记文档的接口                           |
| extension.go    | 添加、删除、获取扩展插件的 API 接口          |
| file.go         | 管理笔记文件的 API 接口                      |
| filetree.go     | 管理笔记文件树的 API 接口                    |
| format.go       | 提供文本格式化相关的 API 接口                |
| graph.go        | 管理图表的 API 接口                          |
| history.go      | 提供操作历史记录的 API 接口                  |
| import.go       | 导入笔记文档的 API 接口                      |
| inbox.go        | 管理收件箱的 API 接口                        |
| lute.go         | 提供 markdown 文档渲染相关的 API 接口        |
| notebook.go     | 管理笔记本的 API 接口                        |
| notification.go | 管理通知的 API 接口                          |
| outline.go      | 获取文档纲要的 API 接口                      |
| ref.go          | 管理快捷方式的 API 接口                      |
| repo.go         | 处理仓库相关的 API 请求                      |
| riff.go         | 添加、删除和管理卡片包的 API 接口            |
| router.go       | 路由中间件级统一处理入口                     |
| search.go       | 管理全文搜索的 API 接口                      |
| setting.go      | 管理系统设置的 API 接口                      |
| snippet.go      | 管理代码片段的 API 接口                      |
| sql.go          | 处理 SQL 查询请求的 API 接口                 |
| storage.go      | 管理笔记存储相关的 API 接口                  |
| sync.go         | 处理同步/备份相关的 API 请求                 |
| system.go       | 管理系统功能的 API 接口                      |
| tag.go          | 处理标签相关的 API 请求                      |
| template.go     | 处理模板渲染相关的 API 请求                  |
| transaction.go  | 处理交易请求的 API 接口                      |
| workspace.go    | 管理工作空间的 API 接口                      |

## [0/38]account.go

此文件是 api 服务的账号相关接口实现的 Go 语言代码文件，主要包含了以下几个接口实现：

1. 开始免费试用（startFreeTrial）
2. 使用激活码（useActivationcode）
3. 检查激活码（checkActivationcode）
4. 注销账号（deactivateUser）
5. 用户登录（login）

每个接口都有相应的处理逻辑，并返回对应的结果。在实现过程中，还引用了一些第三方的 Go 语言库，如 gin, gulu 等。

## [1/38]ai.go

本文件名为 `api\ai.go`，是一个 Go 语言编写的应用程序文件，主要是关于人工智能的部分。程序使用了 Gin 框架和一些其他的依赖项库，如 gulu。

主要包含两个函数：chatGPT 和 chatGPTWithAction。这两个函数的作用是使用模型进行文本聊天，其中 chatGPT 使用模型回答用户提出的问题，而 chatGPTWithAction 使用模型执行动作并更新模型。函数通过 HTTP 响应的方式返回处理结果。

该程序遵守 GNU Affero 通用公共许可证，即可以自由地共享、使用和修改，但需要带上相应的协议声明和原始代码的许可证。

## [2/38]asset.go

该文件是 Golang 编写的 Siyuan 笔记应用程序的一个 API 模块，提供了一系列操作笔记中资源（如图片、附件等）的 HTTP 接口，具有上传、下载、修改、删除等功能。主要函数包括：

* renameAsset: 重命名资源文件
* getDocImageAssets: 获取笔记中图片资源
* setFileAnnotation/getFileAnnotation: 设置和读取资源注释文本
* resolveAssetPath: 解析资源文件相对路径并获取绝对路径
* removeUnusedAsset/removeUnusedAssets/getUnusedAssets: 删除和查询未使用的资源文件
* uploadCloud: 将本地笔记中的资源上传至云存储
* insertLocalAssets: 将本地资源文件插入到笔记中

此外，代码中还包含了一些错误处理代码（例如当发生错误时返回错误码和错误信息）和依赖库引用代码。

## [3/38] attr.go

该文件是 SiYuan 笔记应用的 API 包的一部分，包含了若干个函数，实现了获取书签标签、获取块（block）属性、设置块属性、重置块属性等功能。每个函数都是一个 RESTful API 端点，使用 HTTP 协议提供服务。

其中，`getBookmarkLabels` 函数用于获取所有的书签标签，`getBlockAttrs` 函数用于获取指定块的属性值，`setBlockAttrs` 函数用于设置指定块的属性值，`resetBlockAttrs` 函数用于将指定块的属性值重置为默认值。

代码实现了参数校验和错误处理机制，并使用第三方库 Gulu 和 Gin 简化了代码逻辑和响应操作。

## [4/38] av.go

该程序文件是 SiYuan 在构建数字花园时使用的一个 API 文件。

此文件提供了一个 HTTP 处理程序函数（`renderAttributeView`），该函数允许通过 HTTP 请求从服务器获取一个指定的属性视图。该属性视图的 ID 通过 HTTP 请求的 JSON 主体中的"id"字段传递。

此外，该程序文件还引入了其他依赖包，并使用了这些依赖包提供的工具类和函数。

## [5/38] bazaar.go

该程序文件名是 `api\bazaar.go`，代码主要是实现了一个 API 接口，用于处理集市（Bazaar）的相关操作。

其中包括：

* 获取 Bazaar 包的 README 文件
* 获取 Bazaar 小部件、获取已安装的小部件、安装 Bazaar 小部件、卸载 Bazaar 小部件
* 获取 Bazaar 图标、获取已安装的图标、安装 Bazaar 图标、卸载 Bazaar 图标
* 获取 Bazaar 模板、获取已安装的模板、安装 Bazaar 模板、卸载 Bazaar 模板
* 以及获取 Bazaar 主题、获取已安装的主题、安装 Bazaar 主题和卸载 Bazaar 主题等操作。

该程序主要基于 Golang 语言和 Gin 框架实现，其中还引入了其他第三方库进行支持。

## [6/38] block.go

该文件是 Siyuan 内核中的一个 API 文件，提供了一系列操作块的 RESTful API。

文件主要定义了一些函数，包括：

* 获取标题子级 ID、获取标题子级 DOM、获取标题删除事务、获取标题层级事务
* 获取文档信息
* 获取内容单词计数、获取树的统计信息、获取块的单词计数
* 转移块引用、交换块引用、设置块提醒、检查块是否折叠、检查块是否存在、获取最近更新的块、获取块引用文本、获取块引用 ID、根据文件注释 ID 获取块引用 ID、根据引用文本获取块定义 ID、获取块层级结构、获取块索引、获取块信息、获取块 DOM 和获取块 Kramdown 等。

## [7/38] block_op.go

该程序文件是一个 Go 语言编写的 api 包中的代码文件，文件名为 `block_op.go`。

这个文件实现了一些操作 block（块）的函数，如插入、删除、更新等。

这些操作将与文件系统交互，并且利用 gin 框架处理 HTTP 请求和响应。

其中，最重要的依赖是 siyuan-note 项目的模型、文件系统、Lute 引擎和一些公用库。这个文件的主要作用是提供用于块级操作的 API。

## [8/38] bookmark.go

该程序文件名为 `bookmark.go`，位于 `api\` 目录下。

代码为 Go 语言编写的 API 接口，主要实现了获取、删除和重命名书签的功能。

具体实现使用了 `gin` 框架提供的 API 开发接口。

其中获取书签的方法是 `getBookmark`，删除书签的方法是 `removeBookmark`，重命名书签的方法是 `renameBookmark`。该程序文件依赖于 `gulu` 和 `util` 两个引入包和 `model` 模块。

## [9/38] clipboard.go

该程序文件是一个 Go 语言编写的 API 接口，文件名为 `clipboard.go`，所在目录为 api，主要实现了读取剪贴板中的文件路径的功能。

该接口使用了第三方库 clipboard 和 gulu，其中 gulu 是作者自己开发的一个工具包。接口将获取到的文件路径作为 JSON 数据返回给请求方，当没有文件路径时返回一个空数组。

需要注意的是，在 Linux 平台下，不再支持“粘贴为纯文本”的操作，因此该接口在 Linux 平台下不会读取剪贴板中的文件路径。

该程序文件采用 GNU Affero General Public License 开源协议。

## [10/38] export.go

该程序文件名为 `api\export.go`，主要实现了 SiYuan 的导入和导出功能。

该文件包含了多个函数来导出不同格式的 SiYuan 笔记，包括 Markdown、HTML、PDF 等。其中，每个函数都接收一个参数 c*gin.Context，从中提取需要导出的笔记的 ID、文件名等信息。

这些函数都通过 model 包提供的接口来访问笔记本数据，将导出的结果返回给客户端。

## [11/38] extension.go

该文件名为 `api\extension.go` 的程序文件是一个 Go 语言写的 API 接口实现，主要实现了对 SiYuan 软件中的“拷贝到笔记”功能的支持，包含了上传文件、解析 HTML、替换图片等功能。具体包含函数 extensionCopy，其中主要包含了以下功能：

* 获取参数信息，包括 dom、notebook 等信息。
* 组织保存地址，处理文件名，防止文件名冲突。
* 读取上传文件数据并保存到指定地址。
* 解析 HTML 中的图片地址，将已上传的图片地址替换到 HTML 中。
* 将最终处理后的文本信息以 JSON 的格式返回给前端。

## [12/38] file.go

该程序实现了一个简单的用于操作文件的 API 接口，其中包括：

* `copyFile`：将一个文件从源位置复制到目标位置。
* `getFile`：获取一个文件，并在 HTTP 响应中返回。
* `readDir`：读取一个目录，并返回其中的所有文件和子目录。
* `removeFile`：删除指定位置的文件或目录。
* `putFile`：将一个文件或目录保存到指定位置。

这些函数实现了基本的 CRUD （创建、读取、更新、删除）操作，可以用于搭建简单的文件服务。除此之外，该文件还依赖了一些第三方库，如 `gin`、`filelock` 等。

## [13/38] filetree.go

该程序文件名为 `filetree.go`，位于 api 文件夹下。

该文件中定义了一系列接口函数，用以实现对 siyuan 笔记 app 中的文件树的一系列操作，包括获取、移动、删除、重命名笔记等。

具体实现中涉及到了 siyuan-note/siyuan 项目中的一些模块和库，如文件系统、模板渲染以及 gin web 框架等。

## [14/38] format.go

这个程序文件包含了名为“api”的包，它实现了两个名为“netImg2LocalAssets”和“autoSpace”的 API 端点，使用 gin 框架和 HTTP 协议。

这些端点是通过处理 HTTP POST 请求来调用“model”包中的“NetImg2LocalAssets”和“AutoSpace”函数。

这个程序的目的是在 Siyuan 笔记应用中提供这两个功能的 API 接口。

## [15/38] graph.go

此程序文件是一个 Go 语言编写的 API，使用了 Gin 数据库框架以及一些 SiYuan 笔记应用的应用程序接口。

它包含四个函数：resetGraph、resetLocalGraph、getGraph 和 getLocalGraph，这些函数的主要作用是重置全局或本地图表，获取全局或本地图表的信息。其中，resetGraph 和 resetLocalGraph 用于重置全局或本地图表，getGraph 和 getLocalGraph 用于获取全局或本地图表的信息。

每个函数都在不同的 URL 上运行，并返回固定格式的 JSON 数据。

## [16/38] history.go

该文件名是 `api\history.go`，是一个 Go 语言编写的 API 程序文件，提供了与笔记历史相关的功能函数，包括搜索笔记历史、获取历史记录项目、重建历史索引、清空工作区历史、获取文档历史内容、恢复文档历史、恢复资产历史、恢复笔记本历史。

该程序文件使用了第三方库 gin，以及 suyuan-note/siyuan/kernel/model、suyuan-note/siyuan/kernel/util 等模块。

程序代码使用了 GNU Affero 通用公共许可证。

## [17/38] import.go

这是一个 Go 语言编写的 API 程序，包含三个函数：`importSY`、`importData` 和 `importStdMd`。

其中 `importSY` 函数用于导入 `.sy.zip` 格式的笔记，`importData` 函数用于导入一般数据文件，`importStdMd` 函数用于导入标准 Markdown 格式的笔记。这些函数都是通过 HTTP POST 方法接收数据，并返回 JSON 类型的结果。

函数中使用了许多其它 Go 语言包来完成相关任务，如 `os`、`io`、`net/http`、`filepath` 等标准库，以及 `github.com/88250/gulu`、`github.com/gin-gonic/gin`、`github.com/siyuan-note/logging`、`github.com/siyuan-note/siyuan/kernel/model`、`github.com/siyuan-note/siyuan/kernel/util` 等第三方库。

## [18/38] inbox.go

该程序文件名为 inbox.go，位于 api 目录下。该程序实现了三个 HTTP API 接口，分别为：

1. removeShorthands：用于移除云端快捷方式，参数为 ids（待移除的快捷方式 ID 列表），返回值为成功移除的快捷方式数量。
2. getShorthand：用于获取云端快捷方式的具体内容，参数为 id（快捷方式 ID），返回值为快捷方式的具体内容。
3. getShorthands：用于获取云端快捷方式列表，参数为 page（页码），返回值为指定页码的快捷方式列表。

这些 API 接口通过 GIN 框架进行封装，通过 HTTP 返回值进行数据传输，使用了 Gulu 和 Siyuan-Note 库的一些函数和方法。

## [19/38] lute.go

该程序文件是一个 Go 语言编写的 API，文件名为 lute.go，位于 api 目录下。它实现了以下函数：

* copyStdMarkdown：将指定 ID 的脑图导出为标准 Markdown 格式。
* html2BlockDOM：将指定 HTML 转换为块级 DOM 并处理其中带有超链接的图片为本地引用。
* spinBlockDOM：将指定块级 DOM 中的语法转换为另一种语法。

该程序文件引用了许多其他的库和函数，包括：

* gin-gonic/gin：实现了 HTTP Web 框架。
* 88250/gulu：提供了一些 Go 语言工具库的封装。
* 88250/lute：一个 Go 语言实现的 Markdown 渲染器。
* siyuan-note/filelock：提供了一种获取并持有文件锁的方法，以防止多个程序同时修改同一个文件。

## [20/38] notebook.go

该文件名为 `api\notebook.go`，是一个 Golang 语言的程序文件。

该文件定义了一系列函数，用于处理有关于笔记本的 API 请求。其中包括设置笔记本图标、修改笔记本的排序、重命名笔记本、删除笔记本、创建笔记本、打开笔记本、关闭笔记本、获取笔记本的配置信息和列出所有笔记本等操作。

这些函数将在 API 服务的实现中得到调用，用于处理客户端的 API 请求，并返回相应的响应结果。

## [21/38] notification.go

该文件是一个 Go 语言编写的与 API 相关的文件，文件路径为 `api\notification.go`。

该文件的主要作用是为了实现在 SiYuan 系统中发送通知的功能，其中包括推送消息和推送错误消息。该文件主要使用了 `gin` 框架来处理请求，同时也引入了 `gulu` 和 `util` 工具包来辅助实现功能。具体来说，该文件实现了 `pushMsg()` 和 `pushErrMsg()` 两个函数，分别用于推送普通消息和错误消息。

在函数中会根据传入的参数构造一条推送消息，并调用 `util` 中的函数来将消息推送给相应的接收者。在消息发送成功后，会返回一个包含消息 ID 的 JSON 格式的响应。

## [22/38] outline.go

该程序文件是一个 Golang 语言编写的 API 文件，文件名为 `outline.go`，属于 api 目录下。

它提供了一个函数 getDocOutline，负责从指定的笔记文档中获取文档纲要（outline），并以 JSON 格式返回。该函数使用了 gin 和 gulu 库对 HTTP 请求和 JSON 数据进行处理，同时也引用了 model 和 util 库中的函数来实现所需的功能。

函数的实现过程中，通过请求参数指定了需要获取纲要的笔记文档的 ID，若参数错误则返回错误信息，若获取过程中出现异常也会返回错误信息。

## [23/38] ref.go

这是一个名为 `ref.go` 的 Go 语言程序文件，位于 api\目录下。它实现了 5 个函数：

1. refreshBacklink：刷新某个文档的反向链接。
2. getBackmentionDoc：获取某个文档被引用的文档列表。
3. getBacklinkDoc：获取某个文档引用的文档列表。
4. getBacklink2：获取某个文档的反向链接信息，包括反向链接列表、被反向链接的文档列表等。
5. getBacklink：获取某个文档的反向链接信息，与 getBacklink2 类似但参数和返回值有所不同。

## [24/38] repo.go

文件名为 `api\repo.go`，该文件是一个 Go 语言程序，主要提供了一系列操作仓库的 API 接口，包括如下函数：

1. func openRepoSnapshotDoc(c *gin.Context)，获取打开快照文档
2. func diffRepoSnapshots(c *gin.Context)，对比快照
3. func getCloudSpace(c *gin.Context)，获取云空间
4. func checkoutRepo(c *gin.Context)，检出仓库
5. func downloadCloudSnapshot(c *gin.Context)，下载云快照
6. func uploadCloudSnapshot(c *gin.Context)，上传云快照
7. func getRepoSnapshots(c *gin.Context)，获取仓库快照
8. func getCloudRepoTagSnapshots(c *gin.Context)，获取云仓库标签快照
9. func removeCloudRepoTagSnapshot(c *gin.Context)，删除云仓库标签快照
10. func getRepoTagSnapshots(c *gin.Context)，获取仓库标签快照
11. func removeRepoTagSnapshot(c *gin.Context)，删除仓库标签快照
12. func createSnapshot(c *gin.Context)，创建快照
13. func tagSnapshot(c *gin.Context)，标记快照
14. func importRepoKey(c *gin.Context)，导入仓库密钥
15. func initRepoKeyFromPassphrase(c *gin.Context)，从口令初始化仓库密钥
16. func initRepoKey(c *gin.Context)，初始化仓库密钥
17. func resetRepo(c *gin.Context)，重置仓库

这些 API 接口的实现依赖于一些 Go 包，如 gin-gonic 和 gulu。

## [25/38] riff.go

此文件为 SiYuan 笔记应用的 API 实现，包含以下功能：

* 获取笔记本中的卡片
* 获取树状结构中的卡片
* 获取卡包中的卡片
* 复习卡片
* 跳过卡片的复习
* 获取笔记本中的待复习卡片
* 获取树状结构中的待复习卡片
* 获取卡包中的待复习卡片
* 删除卡包中的卡片
* 添加卡片到卡包
* 重命名卡包
* 删除卡包
* 创建卡包
* 获取所有卡包的数据，包括 ID、名称、大小、创建时间、更新时间。

## [26/38] router.go

该文件是一个 Go 语言编写的 API 路由文件，用于处理各种 HTTP 请求。

其中，不需要鉴权的请求包括获取系统启动进度、获取系统版本号等；需要鉴权的请求包括设置工作空间、创建笔记本、搜索笔记等。

文件中主要使用了 Gin 框架来处理 HTTP 请求，同时还调用了其他模块中的函数来完成相应的业务逻辑。

## [27/38] search.go

这是一个 Go 语言的程序文件，文件名为 `search.go`，包含了一些用于搜索的 API 函数。

其中包括：findReplace、searchAsset、searchTag、searchWidget、removeTemplate、searchTemplate、searchEmbedBlock、searchRefBlock、fullTextSearchBlock 等函数。

这些函数用于查找、替换、删除、搜索各种不同类型的内容，如标签、模板、嵌入块、引用块等。这些搜索功能可以通过 API 调用，以便在程序中方便地使用。

## [28/38] setting.go

该程序文件实现了对 SiYuan 笔记应用的设置，包括 AI、闪卡、账户、编辑器、导出、文件树、搜索、快捷键、外观、云用户、自定义 CSS、表情等设置的修改和获取。

其中，每个设置对应了一个 HTTP 请求处理函数，通过接收请求中携带的参数来修改相应的配置项，以此实现对 SiYuan 笔记应用的个性化设置。

## [29/38] snippet.go

该程序文件是一个 Go 语言编写的 API 文件，文件名为 snippet.go，主要包含四个函数：serveSnippets、getSnippet、setSnippet 和 removeSnippet。

serveSnippets 函数用于处理访问 /snippets/ 文件路径下的资源，会先从配置文件中读取该资源的内容，如果加载失败则返回 404 错误，并且如果配置文件中匹配到了该资源的名称和类型则返回其配置文件中的内容，其他情况则在文件系统中查找该资源，并返回其内容。

getSnippet 函数用于读取配置文件中的所有代码片段，可按照类型和是否已禁用进行过滤，并返回查询到的代码片段数组。

setSnippet 函数用于修改配置文件中的代码片段，会根据请求参数中的 snippets 数组来更新相应的配置项。

removeSnippet 函数用于删除某个代码片段，并返回删除的代码片段。

## [30/38] sql.go

该程序是一个基于 Gin 框架的 API 服务，文件名为 `sql.go`。

它提供了一个名为 SQL 的函数，该函数接收来自 API 请求中的 SQL 语句语句，然后通过调用 Siyuan 的 SQL 内核组件来执行这些语句。如果 SQL 执行成功，则函数将返回查询结果。如果 SQL 执行时发生错误，则函数将返回一个错误代码和错误信息。

## [31/38] storage.go

本文件为 api 模块中的一个程序文件，文件名为 `storage.go`，主要包含了一组存储相关的函数方法。

其中包括获取最近文档、删除标准、设置标准、获取标准、删除本地存储值、设置本地存储值、设置本地存储、获取本地存储等方法。这些方法主要是通过调用 model 模块中的相关函数，来实现对存储的操作。

同时，也使用了一些第三方模块和工具函数，如 gin、gulu 和 util 等。最后，返回给调用者的数据都是通过 JSON 格式的数据结构来实现的。

## [32/38] sync.go

该程序是 Go 语言编写的一个用于支持云同步功能的 API 程序文件，文件名为 `sync.go`，属于 api 包，主要实现了以下功能：

* 查询是否已经进行启动同步（getBootSync）
* 执行同步（performSync）
* 执行启动同步（performBootSync）
* 列出云同步目录（listCloudSyncDir）
* 移除云同步目录（removeCloudSyncDir）
* 创建云同步目录（createCloudSyncDir）
* 设置同步生成冲突文档（setSyncGenerateConflictDoc）
* 设置同步启用（setSyncEnable）
* 设置同步模式（setSyncMode）
* 设置同步提供者（setSyncProvider）
* 设置同步提供者为 S3（setSyncProviderS3）<br />
* 设置同步提供者为 WebDAV（setSyncProviderWebDAV）
* 设置云同步目录（setCloudSyncDir）

## [33/38] system.go

该程序文件实现了 SiYuan 笔记系统的 API 功能。程序文件共包含多个函数：

* getEmojiConf 函数：获取表情包配置信息。
* checkUpdate 函数：检查系统更新。
* exportLog 函数：导出系统日志。
* getConf 函数：获取系统配置信息。
* setUILayout 函数：设置 UI 布局。
* setAccessAuthCode 函数：设置访问权限代码。
* getSysFonts 函数：获取系统字体。
* version 函数：获取系统版本。
* currentTime 函数：获取当前时间戳。
* bootProgress 函数：获取系统启动进程。
* setAppearanceMode 函数：设置系统外观模式。
* setNetworkServe 函数：设置网络服务。
* setGoogleAnalytics 函数：设置谷歌分析。
* setUploadErrLog 函数：设置上传错误日志。
* setAutoLaunch 函数：设置自动启动。
* setDownloadInstallPkg 函数：设置是否下载安装包。
* setNetworkProxy 函数：设置网络代理。
* addUIProcess 函数：添加 UI 进程。
* exit 函数：退出系统。

这些函数实现了系统的一些基本功能，例如获取配置信息、修改系统设置、检查系统更新、导出系统日志、退出系统等。

## [34/38] tag.go

该程序文件名为 `tag.go`，位于 api 目录下。程序使用了 Go 语言编写，实现了一些关于标签的 API 接口。

其中，getTag 函数用于获取所有标签；renameTag 函数用于重命名标签；removeTag 函数用于删除标签。

程序引用了其他的库，如 gin、gulu、model、util 等。该程序还使用了 GNU Affero General Public License 开源协议。

## [35/38] template.go

这是一个 Go 语言编写的 API 函数文件，文件名为 `template.go`，位于 api 目录下。该文件中包含 3 个处理 HTTP 请求的函数：renderSprig、docSaveAsTemplate 和 renderTemplate。

renderSprig 函数通过接受一个请求，用给定的模板参数进行渲染，最终将渲染结果作为返回值传递到请求的响应中。

docSaveAsTemplate 函数接受一个请求，将给定的文档 ID 的内容保存成模板。

renderTemplate 函数接受一个请求，渲染给定的模板，最终将渲染结果作为响应发送给请求端。其中，请求会传送两个参数：path 和 id，分别为模板路径和对应文档的 ID。

这些函数对不同的 HTTP 请求提供了不同的处理方式，可以供不同的客户端或应用程序使用。

## [36/38] transaction.go

该文件是一个 Go 语言编写的 API 模块，包含了一系列函数用于处理交易请求。该模块在接收到 HTTP 请求后，解析请求的 JSON 数据，将其转换成事务对象，并将该事务的状态与数据提供给 kernel 中的其他函数进行处理，最后将结果以 JSON 格式返回给客户端。其中函数 performTransactions 处理交易请求，函数 pushTransactions 用于将交易结果推送到客户端。

## [37/38] workspace.go

该文件是 SiYuan 组件的一部分，主要实现工作空间相关的 API 功能。程序通过框架 Gin 来提供 Web 服务，提供以下几个 API：

1. `/api/workspace/createWorkspaceDir`：用于创建工作空间文件夹；
2. `/api/workspace/removeWorkspaceDir`：用于删除已有的工作空间；
3. `/api/workspace/getMobileWorkspaces`：用于获取移动设备上的工作空间列表；
4. `/api/workspace/getWorkspaces`：用于获取所有工作空间列表信息；
5. `/api/workspace/setWorkspaceDir`：用于切换工作空间。

此外，还定义了一个 `Workspace` 结构体，主要用于展示工作空间信息。在实现各个 API 功能的过程中，还需要使用到其他模块提供的函数，例如：`util.ReadWorkspacePaths()` 读取工作空间路径列表等。
