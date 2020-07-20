# Generative adversarial nets

## 英语知识点
### 生词 
* simultaneously adv. <br>Happening, existing, or done at the same time.
* discriminate n. <br>If you can discriminate between two things, you can recognize that they are different.
* arbitrary adj. <br>If you describe an action, rule, or decision as arbitrary, you think that it is not based on any principle, plan, or system. It often seems unfair because of this.
* demonstrate v. <br>To demonstrate a fact means to make it clear to people.
* qualitative adj. <br>qualitative means relating to the nature or stardand of something, rather than to its quantity.
* quantitative adj. <br>quantitative means relating to different sizes or amounts of things.
* ~
* approximating adj. <br>An approximate number, time, or position is close to the correct number, time, or position, but is not exact.
* intractable adj. <br>intractable problems or situations are very difficult to deal with.
* leverage n-uncount.<br> leverage is the ability to influence situations or people so that you can control what happens.

### 例句
* ... the advantages of quantitative and qualitative research. 定量研究与定性研究的优势


## 文章翻译
### 摘要
我们提出了一个通过对抗过程估计生成模型的新框架，在新框架中我们同时训练两个模型：一个用来捕获数据分布的生成模型 G，和一个用来估计样本是来自训练数据而不是 G 的概率的判别模型 D，G 的训练过程是最大化 D 产生错误的概率。这个框架相当于一个极小化极大的双方博弈。在任意函数 G 和 D 的空间中存在唯一的解，其中 G 恢复训练数据分布，并且 D 处处都等于 $\frac{1}{2}$。在 G 和 D 由多层感知器定义的情况下，整个系统可以用反向传播进行训练。在训练或生成样本期间不需要任何马尔科夫链或展开的近似推理网络。实验通过对生成的样品进行定性和定量评估来展示这个框架的潜力。

### 介绍
深度学习的任务是寻找丰富的层次模型，能够在人工智能领域里用来表达各种数据的概率分布，例如自然图像，包含语音的音频波形和自然语言语料库中的符号等。到目前位置，在深度学习领域，目前为止最成功的模型之一就是判别式模型，通常它们将高维丰富的感知器输入映射到类标签上。这些显著的成功主要是基于反向传播和丢弃算法来实现的，特别是具有良好梯度的分段线性单元。由于在最大似然估计和相关策略中出现的许多难以解决的概率计算的困难，以及很难利用在生成上下文中使用分段线性单元的好处，深度生成模型的影响很小。我们提出一个新的生成模型估计程序，来分步处理这些难题。

在提到的对抗网络框架中，生成模型对抗着一个对手：一个学习去判别一个样本是来自模型分布还是数据分布的判别模型。生成模型可以被认为是一个伪造团队，试图生产假货并在不被发现的情况下使用它，而判别模型类似于警察，试图检测假币。在这个游戏中的竞争驱使两个团队改进它们的方法，直到真假难分为止。

这个框架可以针对多种模型和优化算法提供特定的训练算法。在这篇文章中，我们探讨了生成模型通过将随机噪声传输到多层感知机来生成样本的特例，同时判别模型也是通过多层感知机实现的。我们称这个特例为对抗网络。在这种情况下，我们可以仅使用非常成熟的反向传播和丢弃算法训练两个模型，生成模型在生成样本时只使用前向传播算法。并且不需要近似推理和马尔科夫链作为前提。

### 对抗网络
当模型是多层感知机时，对抗模型框架是最直接应用的。为了学习生成器关于数据 $x$ 上的分布 $p_g$，我们定义输入噪声的先验变量 $p_z(z)$，然后使用 $G(z;\theta_g)$ 来代表数据空间的映射。