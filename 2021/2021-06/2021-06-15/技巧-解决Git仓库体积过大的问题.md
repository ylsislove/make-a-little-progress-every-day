# 技巧-解决Git仓库体积过大的问题

## 前言
适用于从一个git项目中，将体积较大的资源彻底从git中删除，包括历史提交记录。
如果仅仅在目录中删除一个文件是不够的，只要在提交记录中有这个文件，那么 .git 中就会有这个文件的信息。
用 filter-branch 可以强制修改提交信息，将某个文件的历史提交痕迹也抹去，就像从来没有过这个文件一样。

## 解决办法
1. 在项目根目录下运行
```bash
git rev-list --objects --all | grep -E `git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -10 | awk '{print$1}' | sed ':a;N;$!ba;s/\n/|/g'`
```
或
```bash
git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -15 | awk '{print$1}')"
```
或
```bash
git rev-list --all | xargs -rL1 git ls-tree -r --long | sort -uk3 | sort -rnk4 | head -10
```


2. 改写历史，去除大文件
> 注意：下方命令中的 `path/to/large/files` 是大文件所在的路径，千万不要弄错！
```bash
git filter-branch --tree-filter 'rm -f path/to/large/files' --tag-name-filter cat -- --all
git push origin --tags --force
git push origin --all --force
```

如果在 `git filter-branch` 操作过程中遇到如下提示，需要在 `git filter-branch` 后面加上参数 `-f`
```bash
Cannot create a new backup.
A previous backup already exists in refs/original/
Force overwriting the backup with -f
```

并告知所有组员，push 代码前需要 pull rebase，而不是 merge，否则会从该组员的本地仓库再次引入到远程库中，导致仓库在此被 Gitee 系统屏蔽。

## 参考链接
* [仓库体积过大，如何减小？](https://gitee.com/help/articles/4232)
* [彻底删除git中的较大文件（包括历史提交记录）](https://blog.csdn.net/HappyRocking/article/details/89313501)
