---
title: K折交叉验证和F1-Score学习笔记
date: 2023-07-25 19:00:36
categories:
 - [人工智能, 基础知识]
tags: 
 - F1-Score
---

## 前言

最近在做模型评估，看到有论文涉及到 18 折交叉验证和 F1 分数以及宏观 F1 分数，有点被搞晕了，遂查了些资料，记录于此

## K 折交叉验证

K 折交叉验证实际上可以有两种功能，模型选择，和模型评估。参考：[N 折交叉验证的作用（如何使用交叉验证）](https://zhuanlan.zhihu.com/p/113623623)

重点如下：

> 1. N 折交叉验证有两个用途：**模型评估、模型选择**。
> 2. N 折交叉只是一种划分数据集的策略**。**想知道它的优势，可以拿它和传统划分数据集的方式进行比较。它可以避免固定划分数据集的局限性、特殊性，这个优势在小规模数据集上更明显。
> 3. **把这种策略用于划分训练集和测试集，就可以进行模型评估**；**把这种策略用于划分训练集和验证集，就可以进行模型选择**。
> 4. 不用 N 折交叉验证就不能进行模型评估和模型选择了吗？当然不是。只要有测试集，就能进行模型评估；只要有验证集，就能进行模型选择。所以 N 折交叉验证只是在做这两件事时的一种可选的优化手段。

所以我在阅读 TapID 论文里 3 折交叉验证和 18 折交叉验证就是”**把这种策略用于划分训练集和测试集，就可以进行模型评估**“，是模型评估。

也有网友评论的我觉得很有道理

> 我觉得有些讲复杂了。
> 交叉验证就是一种模型评估方法。
> 模型选择本质上是通过评估不同模型的性能好坏来选择出最优的模型。
> 文中所说的模型选择实质上是使用交叉验证来评估不同模型的好坏。
> 实际使用过程中，可以直接将数据集划分为测试集和训练集，然后通过交叉验证选择出最优的模型。
> **如果是论文发表的话，可以将 K 个模型的性能取平均值作为最后的结果**。
> 如果是实际部署的话，则需要加一步，使用所有数据训练最优的模型。
> 如有不妥，请大家批评指教。

还有一点需要注意的是，在 K 折交叉验证中，每一折都需要重新初始化模型进行训练，这样才能评估模型的好坏。所以在论文中，为了验证自己所搭模型的优劣，就可以将 K 个模型的性能取平均值作为最后的结果，来证明自己模型的性能不错~

### 参考

* [Should I be re-initializing the whole model between loops of K-fold Cross-validation? And how do I do that?](https://stackoverflow.com/questions/59513602/should-i-be-re-initializing-the-whole-model-between-loops-of-k-fold-cross-valida)
* [pytorch - K 折交叉验证过程说明及实现](https://blog.csdn.net/foneone/article/details/104445320)
* [pytorch Kfold 数据集划分](https://blog.csdn.net/qq_44761480/article/details/113393421)
* [交叉验证--关于最终选取模型的疑问](https://blog.csdn.net/u011698800/article/details/107607829)

## F1-Score

### 首先理解查准率（precision）

指的是预测值为 1 且真实值也为 1 的样本==在预测值为 1 的所有样本==中所占的比例。以西瓜问题为例，==算法挑出来的西瓜中有多少比例是好西瓜==。

### 召回率（recall）

也叫查全率，指的是预测值为 1 且真实值也为 1 的样本==在真实值为 1 的所有样本==中所占的比例。==所有的好西瓜中有多少比例被算法挑了出来==。

### F1 分数（F1-Score）

又称为平衡 F 分数（BalancedScore），它被定义为精确率和召回率的调和平均数。

$$
F_1=2\cdot\frac{precision\cdot recall}{precision+recall}
$$

## sklearn 中的评估报告

```python
sklearn.metrics.classification_report(y_true, y_pred, labels=None, target_names=None, sample_weight=None, digits=2, output_dict=False)
```

### 参数

* y_true：类别的真实标签值，类标签的列表
* y_pred：预测值的标签，类标签的列表
* labels：报告中要包含的标签索引的可选列表；这个参数一般不需要设置（如果要设置，比如 200 个类别，那么就应该如此设置：lable= range(200);  然后在 sklearn.metrics.classification_report 中将 labels=label），可是有的时候不设置就会出错，之所以会出错是因为：比如你总共的类别为 200 个类，但是，你的测试集中真实标签包含的类别只有 199 个，有一个类别缺失数据，如果不设置这个参数就会报错
* target_name：与标签匹配的名称，就是一个字符串列表，在报告中显示；也即是显示与 labels 对应的名称
* digits：这个参数是用来设置你要输出的格式位数，就是几位有效数字吧，大概就是这个意思，即指定输出格式的精确度
* sample_weight：暂时不知道有啥用
* output_dict：如果为 True，则将输出作为 dict 返回

### 指标分析

```python
>>> from sklearn.metrics import classification_report
>>> y_true = [0, 1, 2, 2, 2]
>>> y_pred = [0, 0, 2, 2, 1]
>>> target_names = ['class 0', 'class 1', 'class 2']
>>> print(classification_report(y_true, y_pred, target_names=target_names))
              precision    recall  f1-score   support
 
     class 0       0.50      1.00      0.67         1
     class 1       0.00      0.00      0.00         1
     class 2       1.00      0.67      0.80         3
 
   micro avg       0.60      0.60      0.60         5
   macro avg       0.50      0.56      0.49         5
weighted avg       0.70      0.60      0.61         5
```

* y\_true 为样本真实标签，y\_pred 为样本预测标签；
* support：当前行的类别在测试数据中的样本总量，如上表就是，在 class 0 类别在测试集中总数量为 1；
* precision：精度\=正确预测的个数(TP)/被预测正确的个数(TP+FP)；人话也就是模型预测的结果中有多少是预测正确的
* recall：召回率\=正确预测的个数(TP)/预测个数(TP+FN)；人话也就是某个类别测试集中的总量，有多少样本预测正确了；
* f1-score：F1 \= 2*精度\*召回率/(精度 + 召回率)
* micro avg：计算所有数据下的指标值，假设全部数据 5 个样本中有 3 个预测正确，所以 micro avg 为 3/5\=0.6
* macro avg：每个类别评估指标未加权的平均值，比如准确率的 macro avg，(0.50+0.00+1.00)/3\=0.5
* weighted avg：加权平均，就是测试集中样本量大的，我认为它更重要，给他设置的权重大点；比如第一个值的计算方法，(0.501 + 0.01 + 1.0\*3)/5 \= 0.70

> 补充一下现在不再有 micro avg 了,因为这个指标指的是全体样本的准确率，所以简化成了一个指标 accuracy

### 参考

* [sklearn.metrics.classification_report 模块使用与指标分析(生成混淆矩阵评价分类指标)](https://blog.csdn.net/comway_Li/article/details/102758972)
* [python - 如何显示每个交叉验证折叠的混淆矩阵和报告(召回率、精度、fmeasure)](https://www.coder.work/article/4758272)
