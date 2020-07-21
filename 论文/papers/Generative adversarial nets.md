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
当模型是多层感知机时，对抗模型框架是最直接应用的。为了学习生成器关于数据 $x$ 上的分布 $p_g$，我们定义输入噪声的先验变量 $p_z(z)$，然后使用 $G(z;\theta_g)$ 来代表数据空间的映射。这里 $G$ 是一个由含有参数 $\theta_g$ 的多层感知机表示的可微函数。我们再定义了一个多层感知机 $D(x;\theta_d)$ 用来输出一个单独的标量。$D(x)$ 代表 $x$ 来自于真实数据分布而不是 $p_g$ 的概率，我们训练 $D$ 来最大化分配正确标签给不管是来自于训练样例还是 $G$ 生成的样例的概率。我们同时训练 $G$ 来最小化 $log(1-D(G(z)))$。换句话说，$D$ 和 $G$ 的训练是关于值函数 $V(G,D)$ 的极小化极大的二人博弈问题。

$$\min_G\max_DV(D,G)=\mathbb{E_{x\sim p_{data}(x)}}[logD(x)]+\mathbb{E_{z\sim p_z(z)}}[log(1-D(G(z)))]\tag{1}$$

在下一节中，我们提出了对抗网络的理论分析，基本上表明基于训练准则可以恢复数据生成分布，因为 $G$ 和 $D$ 被给予足够的容量，即在非参数极限。如图 1 展示了该方法的一个非正式却更加直观的解释。实际上，我们必须使用迭代数值方法来实现这个过程。在训练的内部循环中优化 $D$ 到完成的计算是禁止的。并且有限的数据集将导致过拟合。相反，我们在优化 $D$ 的 k 个步骤和优化 $G$ 的一个步骤之间交替。只要 $G$ 变化足够慢，可以保证 $D$ 保持在其最佳解附近。该过程如算法 1 所示。

实际上，方程 1 可能无法为 G 提供足够的梯度来学习。训练初期，当 G 的生成效果很差时，$D$ 会以高置信度来拒绝生成样本，因为它们与训练数据明显不同。因此，$log(1-D(G(z)))$ 饱和。因此我们选择最大化 $logD(G(z))$ 而不是最小化 $log(1-D(G(z)))$ 来训练 $G$，该目标函数使 $G$ 和 $D$ 的动力学稳定点相同，并且在训练初期，该目标函数可以提供更强大的梯度。

![图一](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200721210006.png)

图1. 生成网络在被训练的同时，更新判别分布模型（$D$，蓝色虚线）使 $D$ 能区分训练数据分布 $p_x$（黑色虚线）中的样本和生成分布 $p_g$（$G$，绿色分布）中的样本。下面的水平线为均匀采样 $z$ 的区域，上面的水平线为 $x$ 的部分区域。朝上的箭头显示映射 $x=G(z)$ 如何将非均匀分布 $p_g$ 作用在转换后的样本上。$G$ 在 $p_g$ 高密度区域收缩，且在 $p_g$ 的低密度区域扩散。(a) 考虑一个接近收敛的对抗模型对：$p_g$ 与 $p_{data}$ 相似，且 $D$ 是个部分准确的分类器。(b) 算法的内循环中，训练 $D$ 来判别数据中的样本，收敛到：$D^*(x)=\frac{p_{data}(x)}{p_{data}(x)+p_g(x)}$。(c) 在 $G$ 的 1 次更新后，$D$ 的梯度引导 $G(z)$ 流向更可能分类为数据的区域。(d) 训练若干步后，如果 $G$ 和 $D$ 的性能足够，它们接近某个稳定点并都无法继续提高性能，因为此时 $p_g=p_{data}$。判别器将无法区分训练数据分布和生成数据分布，即 $D(x)=\frac{1}{2}$。

---
算法 1. 生成对抗网络的 minibatch 随机梯度下降训练。判别器的训练步数，$k$，是一个超参数。在我们的试验中使用 $k=1$，使消耗最小。

![算法1](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200721233456.png)

---