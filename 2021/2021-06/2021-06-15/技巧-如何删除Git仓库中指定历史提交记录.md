# 技巧-如何删除Git仓库中指定历史提交记录

## 前言
我们在 git 操作过程中，如果遇到 push 某个 log 有问题，要删除此记录，怎么办？请看下文~
<!-- more -->

## 做法一
1. 执行 `git log` 找到要回退到的历史提交记录的 `hash` 码
2. 执行 `git reset --hard xxxxxxxxxxxxxxxxxxxxxxxxxx`（后面是要回退到的 hash 码）
3. 执行 `git push origin HEAD --force`

## 做法二
1. 执行 `git log` 找到要删除那次提交 `之前` 的提交记录
2. 执行 `git rebase -i xxxxxxxxxxxxxxxxxxxxxxxxxxx`
3. 将要删除的那条记录前面的 `pick` 关键词改为 `drop`
4. wq，保存退出，可能还要解冲突，然后可以git log查看一下新的提交记录
5. 执行 `git push origin --force`

## 参考链接
* [Git 删除某个历史记录](https://www.jianshu.com/p/520f8661659c)
* [git删除历史提交记录](https://blog.csdn.net/ioth5/article/details/104183498)
