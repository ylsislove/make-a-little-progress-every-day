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
我们提出了一个通过对抗过程估计生成模型的新框架，在新框架中我们同时训练两个模型：一个用来捕获数据分布的生成模型 $G$，和一个用来估计样本是来自训练数据而不是 $G$ 的概率的判别模型 $D$，$G$ 的训练过程是最大化 $D$ 产生错误的概率。这个框架相当于一个极小化极大的双方博弈。在任意函数 $G$ 和 $D$ 的空间中存在唯一的解，其中 $G$ 恢复训练数据分布，并且 $D$ 处处都等于 $\frac{1}{2}$。在 $G$ 和 $D$ 由多层感知器定义的情况下，整个系统可以用反向传播进行训练。在训练或生成样本期间不需要任何马尔科夫链或展开的近似推理网络。实验通过对生成的样品进行定性和定量评估来展示这个框架的潜力。

### 介绍
深度学习的任务是寻找丰富的层次模型，能够在人工智能领域里用来表达各种数据的概率分布，例如自然图像，包含语音的音频波形和自然语言语料库中的符号等。到目前位置，在深度学习领域，目前为止最成功的模型之一就是判别式模型，通常它们将高维丰富的感知器输入映射到类标签上。这些显著的成功主要是基于反向传播和丢弃算法来实现的，特别是具有良好梯度的分段线性单元。由于在最大似然估计和相关策略中出现的许多难以解决的概率计算的困难，以及很难利用在生成上下文中使用分段线性单元的好处，深度生成模型的影响很小。我们提出一个新的生成模型估计程序，来分步处理这些难题。

在提到的对抗网络框架中，生成模型对抗着一个对手：一个学习去判别一个样本是来自模型分布还是数据分布的判别模型。生成模型可以被认为是一个伪造团队，试图生产假货并在不被发现的情况下使用它，而判别模型类似于警察，试图检测假币。在这个游戏中的竞争驱使两个团队改进它们的方法，直到真假难分为止。

这个框架可以针对多种模型和优化算法提供特定的训练算法。在这篇文章中，我们探讨了生成模型通过将随机噪声传输到多层感知机来生成样本的特例，同时判别模型也是通过多层感知机实现的。我们称这个特例为对抗网络。在这种情况下，我们可以仅使用非常成熟的反向传播和丢弃算法训练两个模型，生成模型在生成样本时只使用前向传播算法。并且不需要近似推理和马尔科夫链作为前提。

### 对抗网络
当模型是多层感知机时，对抗模型框架是最直接应用的。为了学习生成器关于数据 $x$ 上的分布 $p_g$，我们定义输入噪声的先验变量 $p_z(z)$，然后使用 $G(z;\theta_g)$ 来代表数据空间的映射。这里 $G$ 是一个由含有参数 $\theta_g$ 的多层感知机表示的可微函数。我们再定义了一个多层感知机 $D(x;\theta_d)$ 用来输出一个单独的标量。$D(x)$ 代表 $x$ 来自于真实数据分布而不是 $p_g$ 的概率，我们训练 $D$ 来最大化分配正确标签给不管是来自于训练样例还是 $G$ 生成的样例的概率。我们同时训练 $G$ 来最小化 $log(1-D(G(z)))$。换句话说，$D$ 和 $G$ 的训练是关于值函数 $V(G,D)$ 的极小化极大的二人博弈问题。

$$\min_G\max_DV(D,G)=\mathbb{E_{x\sim p_{data}(x)}}[\log D(x)]+\mathbb{E_{z\sim p_z(z)}}[\log(1-D(G(z)))]\tag{1}$$

在下一节中，我们提出了对抗网络的理论分析，基本上表明基于训练准则可以恢复数据生成分布，因为 $G$ 和 $D$ 被给予足够的容量，即在非参数极限。如图 1 展示了该方法的一个非正式却更加直观的解释。实际上，我们必须使用迭代数值方法来实现这个过程。在训练的内部循环中优化 $D$ 到完成的计算是禁止的。并且有限的数据集将导致过拟合。相反，我们在优化 $D$ 的 k 个步骤和优化 $G$ 的一个步骤之间交替。只要 $G$ 变化足够慢，可以保证 $D$ 保持在其最佳解附近。该过程如算法 1 所示。

实际上，方程 1 可能无法为 G 提供足够的梯度来学习。训练初期，当 G 的生成效果很差时，$D$ 会以高置信度来拒绝生成样本，因为它们与训练数据明显不同。因此，$\log(1-D(G(z)))$ 饱和。因此我们选择最大化 $\log D(G(z))$ 而不是最小化 $\log(1-D(G(z)))$ 来训练 $G$，该目标函数使 $G$ 和 $D$ 的动力学稳定点相同，并且在训练初期，该目标函数可以提供更强大的梯度。

![图一](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200721210006.png)

图1. 生成网络在被训练的同时，更新判别分布模型（$D$，蓝色虚线）使 $D$ 能区分训练数据分布 $p_x$（黑色虚线）中的样本和生成分布 $p_g$（$G$，绿色分布）中的样本。下面的水平线为均匀采样 $z$ 的区域，上面的水平线为 $x$ 的部分区域。朝上的箭头显示映射 $x=G(z)$ 如何将非均匀分布 $p_g$ 作用在转换后的样本上。$G$ 在 $p_g$ 高密度区域收缩，且在 $p_g$ 的低密度区域扩散。(a) 考虑一个接近收敛的对抗模型对：$p_g$ 与 $p_{data}$ 相似，且 $D$ 是个部分准确的分类器。(b) 算法的内循环中，训练 $D$ 来判别数据中的样本，收敛到：$D^*(x)=\frac{p_{data}(x)}{p_{data}(x)+p_g(x)}$。(c) 在 $G$ 的 1 次更新后，$D$ 的梯度引导 $G(z)$ 流向更可能分类为数据的区域。(d) 训练若干步后，如果 $G$ 和 $D$ 的性能足够，它们接近某个稳定点并都无法继续提高性能，因为此时 $p_g=p_{data}$。判别器将无法区分训练数据分布和生成数据分布，即 $D(x)=\frac{1}{2}$。

---
算法 1. 生成对抗网络的 minibatch 随机梯度下降训练。判别器的训练步数，$k$，是一个超参数。在我们的试验中使用 $k=1$，使消耗最小。

![算法1](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200722205004.png)

---

### 理论结果
当 $z\sim p_z$ 时，获得样本 $G(z)$，生成器 $G$ 隐式的定义概率分布 $p_g$ 为 $G(z)$ 获得的样本的分布。因此，如果模型容量和训练时间足够大时，我们希望算法 1 收敛为 $p_{data}$ 的良好估计量。本节的结果是在非参数设置下完成的，例如，我们通过研究概率密度函数空间中的收敛来表示具有无限容量的模型。

我们将在 4.1 节中展示，这个极小化极大问题的全局最优解为 $p_g=p_{data}$。我们将在 4.2 节中展示使用算法 1 来优化等式 1，从而获得期望的结果。

#### 4.1 全局最优：$p_g=p_{data}$ 

对于任意给定的生成器 $G$，我们首先考虑最优判别器 $D$。

命题 1. 固定 $G$，最优判别器为：

$$D_G^*(x)=\frac{p_{data}(x)}{p_{data}(x)+p_g(x)}\tag{2}$$

证明. 给定任意生成器 $G$，判别器 $D$ 的训练标准为最大化目标函数 $V(G,D)$：

$$
\begin{aligned}
V(G,D)&=\int_x{p_{data}(x)\log(D(x))dx}+\int_z{p_z(z)\log(1-D(g(z)))dz} \\
&=\int_x{p_{data}(x)\log(D(x))+p_g(x)\log(1-D(x))dx}\tag{3}
\end{aligned}
$$ 

对于任意的 $(a,b)\in\Bbb{R^2}$ \ $\{0,0\}$，函数 $y\to a\log(y)+b\log(1-y)$ 在 $[0,1]$ 中的 $\frac{a}{a+b}$ 处达到最大值。无需在 $Supp(p_{data}) \cup Supp(p_g)$ 外定义判别器，证毕。

注意到，判别器 $D$ 的训练目标可以看作为条件概率 $P(Y=y|x)$ 的最大似然估计，当 $y=1$ 时，$x$ 来自于 $p_{data}$；当 $y=0$ 时，$x$ 来自 $p_g$。公式 1 中的极小化极大问题可以变形为：

$$
\begin{aligned}
    C(G) &= \max_D V(G,D) \\
         &= \mathbb{E_{x\sim p_{data}}}[\log D_G^*(x)] + \mathbb{E_{z\sim p_z}}[\log(1-D_G^*(G(z)))] \\
         &= \mathbb{E_{x\sim p_{data}}}[\log D_G^*(x)] + \mathbb{E_{x\sim p_g}}[\log(1-D_G^*(x))] \\
         &= \mathbb{E_{x\sim p_{data}}}\left[\log\frac{p_{data}(x)}{p_{data}(x)+p_g(x)}\right] + \mathbb{E_{x\sim p_g}}\left[\log\frac{p_g(x)}{p_{data}(x)+p_g(x)}\right]
         \tag{4}
\end{aligned}
$$

定理 1. 当且仅当 $p_g=p_{data}$ 时，$C(G)$ 达到全局最小。此时，$C(G)$ 的值为 $-\log4$。

证明. $p_g=p_{data}$ 时，$D_G^*(x)=\frac{1}{2}$（公式 2）。再根据公式 4 可得，$C(G)=\log\frac{1}{2}+\log\frac{1}{2}=-\log4$。为了看仅当 $p_g=p_{data}$ 时 $C(G)$ 是否为最优的，观测：

$$
\mathbb{E_{x\sim p_{data}}}[-\log2] + \mathbb{E_{x\sim p_g}}[-\log2] = -\log4
$$

然后从 $C(G)=V(D_G^*,G)$ 减去上式，可得：

$$
C(G) = -\log(4) + KL\left(p_{data}\|\frac{p_{data}+p_g}{2}\right) + KL\left(p_g\|\frac{p_{data}+p_g}{2}\right)\tag{5}
$$

其中 KL 为 Kullback-Leibler 散度。我们在表达式中识别出了模型判别和数据生成过程之间的 Jensen-Shannon 散度：

$$
C(G) = -\log(4) + 2\ ·\ JSD(p_{data}\|p_g)\tag{6}
$$

由于两个分布之间的 Jensen-Shannon 散度总是非负的，并且当两个分布相等时，值为 0。因此 $C^*=-\log(4)$ 为 $C(G)$ 的全局最小值，并且唯一解为 $p_g=p_{data}$ 即生成模型能够完美的复制数据的生成过程。

#### 4.2 算法 1 的收敛性
命题 2. 如果 $G$ 和 $D$ 有足够的性能，对于算法 1 中的每一步，给定 $G$ 时，判别器能够达到它的最优，并且通过更新 $p_g$ 来提高这个判别准则。

$$
\mathbb{E_{x\sim p_{data}}}[\log D_G^*(x)] + \mathbb{E_{x\sim p_g}}[\log(1-D_G^*(x))]
$$

则 $p_g$ 收敛为 $p_{data}$。

证明. 如上述准则，考虑 $V(G,D)=U(p_g,D)$ 为关于 $p_g$ 的函数。注意到 $U(p_g,D)$ 为 $p_g$ 的凸函数。该凸函数上确界的一次导数包括达到最大值处的该函数的导数。换句话说，如果 $f(x)=\sup_{\alpha\sim A}f_\alpha(x)$ 且对于每一个 $\alpha$，$f_\alpha(x)$ 是关于 $x$ 的凸函数，那个如果 $\beta=\arg\sup_{\alpha\sim A}f_\alpha(x)$，则 $\partial f_\beta(x) \in \partial f$。这等价于给定对应的 $G$ 和最优的 $D$，计算 $p_g$ 的梯度更新。如定理 1 所证明，$\sup_D U(p_g,D)$ 是关于 $p_g$ 的凸函数且有唯一的全局最优解，因此，当 $p_g$ 的更新足够小时，$p_g$ 收敛到 $p_x$，证毕。

实际上，对抗网络通过函数 $G(z;\theta_g)$ 表示 $p_g$ 分布的有限簇，并且我们优化 $\theta_g$ 而不是 $p_g$ 本身。使用一个多层感知机来定义 $G$ 在参数空间引入了多个临界点。而且，尽管缺乏理论证明，但在实际中多层感知机的优良性能表明了这是一个合理的模型。

### 实验
我们在一系列数据集上，包括 MNIST、多伦多面数据库（TFD）和 CIFAR-10，来训练对抗网络。生成器的激活函数包括修正线性激活（ReLU）和 sigmoid 激活，而判别器使用 maxout 激活。Dropout 被用于判别器网络的训练。虽然理论框架可以在生成器的中间层使用 Dropout 和其他噪声，但是这里仅在生成网络的最底层使用噪声输入。

我们通过对 $G$ 生成的样本应用高斯 Parzen 窗口并计算此分布下的对数似然，来估计测试集数据的概率。高斯的 $\sigma$ 参数通过对验证集的交叉验证获得。Breuleux 等人引入该过程且用于不同的似然难解的生成模型上。结果报告在表 1 中。该方法估计似然的方差较大且高维空间中表现不好，但确实是目前我们认为最好的方法。生成模型的优点是可采样而不直接估计似然，从而促进了该模型评估的进一步研究。

![表1](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200722192830.png)

表 1. 基于 Parzen 窗口的对数似然估计。MNIST 上报告的数字是测试集上的平均对数似然以及在样本上平均计算的标准误差。在 TFD 上，我们计算数据集的不同折之间的标准误差，在每个折的验证集上选择不同的 $\sigma$。在 TFD 上，在每一个折上对 $\sigma$ 进行交叉验证并计算平均对数似然函数。对于 MNIST，我们与真实值（而不是二进制）版本的数据集的其他模型进行比较。

训练后的生成样本如下图 2、图 3 所示。我们并未声明该方法生成的样本比其他方法生成的样本更好，但我们相信这些样本至少和文献中更好的生成模型相比依然具有竞争力，也突出了对抗框架的潜力。

![图2](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200722193822.png)

图 2. 来自模型的样本可视化。最右边列出了相邻样本的最近训练示例，以便证明该模型没有记住训练集。样品是完全随机抽取，而不是精心挑选。与其他大多数深度生成模型的可视化不同，这些图像显示来自模型分布的实际样本。此外，这些样本是完全不相关的，因为采样过程并不依赖马尔科夫链混合。a) MNIST；b) TFD；c) CIFAR-10（全连接模型）；d) CIFAR-10（卷积判别器和“解卷积”生成器）

![图3](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200722195330.png)

图 3. 通过在完整模型的 $z$ 空间的坐标之间进行线性内插获得的数字。

### 优势和劣势
新框架相比以前的模型框架有其优缺点。缺点主要为 $p_g(x)$ 的隐式表示，且训练期间 $D$ 和 $G$ 必须很好地同步（特别是，在不更新 $D$ 时 $G$ 不必过度训练，以避免“Helvetica 情景”。否则，$x$ 值相同时 $G$ 丢失过多 $z$ 值以至于模型 $p_{data}$ 多样性不足），正如 Boltzmann 机在学习步间的不断更新。其优点是无需马尔科夫链，仅用反向传播来获得梯度，学习间无需推理，且模型中可融入多种函数。表 2 总结了生成对抗网络与其他生成模型方法的比较。

![表2](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200722202104.png)

表 2. 生成建模中的挑战：对涉及模型的每个主要操作的深度生成建模的不同方法遇到的困难的总结。

上述优势主要在计算上。对抗模型通过数据实例，和仅流过判别器的梯度，也可能从间接更新的生成模型中获得一些统计优势。这意味输入部分未直接复制进生成器的参数。对抗网络的另一个优点是可以表示尖锐、甚至退化的分布，而基于马尔科夫链的方法为混合模式而要求模糊的分布。

### 结论和未来的研究方向
该框架允许许多直接的扩展：

1. 条件生成模型 $p(x\ \vert\ c)$ 可以通过将 $c$ 作为 $G$ 和 $D$ 的输入来获得。
2. 给定 $x$，可以通过训练一个任意的模型来学习近似推理，以预测 $z$。这和 wake-sleep 算法训练出的推理网络类似，但是它具有一个优势，就是在生成器训练完成后，这个推理网络可以针对固定的生成器进行训练。
3. 能够用来近似模型所有的条件概率 $p(x_S\ \vert\ x_\$)$，其中 $S$ 通过训练共享参数的条件模型簇的关于 $x$ 索引的一个子集。本质上，可以使用生成对抗网络来随机拓展 MP-DBM。
4. 半监督学习：当标签数据有限时，判别网络或推理网络的特征会提高分类器效果。
5. 效率改善：为协调 $G$ 和 $D$ 设计更好的方法，或训练期间确定更好的分布来采样 $z$，能够极大的加速训练。

本文已经展示了对抗模型框架的可行性，表明这些研究方向是有用的。