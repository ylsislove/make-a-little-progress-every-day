# Generative adversarial nets

## 英语知识点
## 生词 
* simultaneously adv. <br>Happening, existing, or done at the same time.
* discriminate n. <br>If you can discriminate between two things, you can recognize that they are different.
* arbitrary adj. <br>If you describe an action, rule, or decision as arbitrary, you think that it is not based on any principle, plan, or system. It often seems unfair because of this.
* demonstrate v. <br>To demonstrate a fact means to make it clear to people.
* qualitative adj. <br>qualitative means relating to the nature or stardand of something, rather than to its quantity.
* quantitative adj. <br>quantitative means relating to different sizes or amounts of things.

## 例句
* ... the advantages of quantitative and qualitative research. 定量研究与定性研究的优势


## 文章翻译
### 摘要
我们提出了一个通过对抗过程估计生成模型的新框架，在新框架中我们同时训练两个模型：一个用来捕获数据分布的生成模型 G，和一个用来估计样本是来自训练数据而不是 G 的概率的判别模型 D，G 的训练过程是最大化 D 产生错误的概率。这个框架相当于一个极小化极大的双方博弈。在任意函数 G 和 D 的空间中存在唯一的解，其中 G 恢复训练数据分布，并且 D 处处都等于 $\frac{1}{2}$。在 G 和 D 由多层感知器定义的情况下，整个系统可以用反向传播进行训练。在训练或生成样本期间不需要任何马尔科夫链或展开的近似推理网络。实验通过对生成的样品进行定性和定量评估来展示这个框架的潜力。

