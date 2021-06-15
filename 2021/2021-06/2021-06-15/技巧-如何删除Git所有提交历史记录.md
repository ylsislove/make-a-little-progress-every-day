# 技巧-如何删除Git所有提交历史记录

## 前言
如果直接删除 `.git` 文件夹肯定会导致 git 存储库出现问题，那么如果要删除所有提交历史记录，但将代码保持在当前状态，该如何安全的操作呢，请看下文~
<!-- more -->

## 解决办法
1. 尝试运行 `git checkout --orphan latest_branch`
2. 添加所有文件 `git add -A`
3. 提交更改 `git commit -am "commit message"`
4. 删除分支 `git branch -D master`
5. 将当前分支重命名 `git branch -m master`
6. 最后，强制更新存储库 `git push -f origin master`
7. 解决！

## 参考链接
* [如何删除git所有提交历史](https://www.cnblogs.com/ezhar/p/13881075.html)
