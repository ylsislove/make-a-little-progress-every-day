---
title: 动态规划：第N个泰波那契数
date: 2022/07/25
categories:
 - [数据结构与算法, 动态规划]
tags: 
 - 动态规划
---

## 注意
GitHub 的 Markdown 渲染功能不足，文章的完整渲染欢迎来我的 [博客小站](https://blog.aayu.today/) 查看~~

## 题目描述
![](http://image.aayu.today/2022/07/25/b08130d1eee33.png)

## 思路与题解
;;;id1 思路
和昨天的[斐波那契数](https://blog.aayu.today/algorithm/dp/20220724/)思路一样，用滚动数组的思想，关键点在于设置 p、q、t、r 的初值，我们知道，r = p + q + t，第一个要计算的值是 Fn(3)，T_3 = 0 + 1 + 1，这是滚动之后的，所以 p、q、t、r 的初值应该是 0、0、1、1，这样滚动过后才能变成 0、1、1，就能算出 Fn(3) = r = 0 + 1 + 1。Easy~
;;;

;;;id1 我的代码
```cpp
class Solution {
public:
    int tribonacci(int n) {
        if (n < 2) return n;
        if (n == 2) return 1;
        int p = 0, q = 0, t = 1, r = 1;
        for (int i = 3; i <= n; ++i) {
            p = q;
            q = t;
            t = r;
            r = p + q + t;
        }
        return r;
    }
};
```
;;;
