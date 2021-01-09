# Workflow and tools to track and visualize behavioural data from a Virtual Reality environment using a lightweight GIS

使用轻量级地理信息系统跟踪和可视化虚拟现实环境中的行为数据的工作流程和工具

## 摘要
评估虚拟现实中的用户行为是每一个参与设计和执行沉浸式环境实验的研究人员面临的挑战。行为信息可能会在存在感、参与度或例如玩家在 VR 体验中的情绪等方面得到相关发现。保存这类信息，并以适当的方式将其爆发出来，可以引导研究人员甚至游戏设计师识别相关的行为模式或相关性。在本文中，我们提出了一个简单的、可复制的工作流程和一套脚本工具，以获取用户的导航数据，并利用地理信息系统的固有功能将其可视化。我们的工作流程从使用 C# 在 Unity3D 中获取数据，到使用基于开源 GIS JavaScript 的 Leaflet 在地图中最终呈现，通过 XML 文件的预处理。使用 GIS 来可视化导航数据是一个灵活、生态、有效的解决方案，可以提高工作效率和对数据故事能力的认识。

Keywords: Virtual reality, User experience, Geographic information system, Human–computer interaction

---
代码元数据

| | |
| -- | -- |
| Current code version | 	v1.0 |
| Permanent link to code/repository used for this code version | https://github.com/ElsevierSoftwareX/SOFTX_2018_69 |
| Legal Code License | CC0 |
| Code versioning system used | none |
| Software code languages, tools, and services used | Javascript, C#,CSS |
| Compilation requirements, operating environments | Unity3D,Leaflet.js |
| If available Link to developer documentation/manual | |
| Support email for questions | jlsoler@florida-uni.es |

## 1. 动机和意义
在过去的五十年里，人们对虚拟现实（VR）作为不同领域的工具的兴趣[1]、[2]、[3]、[4]不断提高。从一开始，讲师、医生、培训师、教学设计师、心理学家和其他一些专业人士，都强调了 VR 的潜力，利用其沉浸感、参与感、测量和反馈能力来改善他们的活动。为了利用虚拟现实作为实现多学科目标的手段，已经制定了一些评估策略。他们中的大多数都集中在获得一些关于用户的感觉、情绪或认知的指标。这组指标通常是基于体验后的调查，具有一定的内在偏差。最近，这组指标它正在被心理生理学数据所取代，以获得完全客观的测量方法[5]。肌电图（EMG）、皮电活动（EDA）、脑电图（EEG）、功能磁共振成像（fMRI）是最常用、最有效的心理生理学特性和技术。另一个指标家族则与用户在虚拟环境内的行为有关。VR 研究人员试图记录每一个相关的互动，目的是找出用户的表现，或者，例如，他/她是如何在环境中导航的。导航是每一个数字环境中最基本的、无处不在的交互，无论是沉浸式还是非沉浸式的，它对存在感（实际在虚拟世界中的感觉）[6]或网络病[7]有很强的影响。为此，研究人员投入了大量的时间来设计和开发软件解决方案，以获取和利用用户的导航数据。为此，我们希望分享我们的工作流程和工具，旨在捕捉用户在特定和流行的游戏引擎开发的虚拟环境中的导航数据。Unity3D[8] 是最通用和最广泛的游戏引擎，并以创新的方式可视化，使用地理信息系统作为传单[9]。这种功能可以为其他研究者节省大量的时间，而且，可以提高专注于研究用户在虚拟环境中行为的实验的可复制性。

此外，由于技术支持虚拟环境中的多用户同时交互，VR 正在成为一个协作空间。这些新的功能允许用户在虚拟世界里面参与一个共同的任务[10]。设计和开发协作虚拟环境（CVE）最具挑战性的方面之一是测量正在执行一项任务的意识，这是协作工作的一部分[11]。与其他通常在 VR 环境中测量的参数（即存在感、共同存在感、舒适度）一样，一些问卷调查已经被开发出来[12]，但由于该调查通常是在体验之后进行的，因此有很大的偏差。我们提出的工作流程本质上是多用户的，因为每个参与者都有自己的跟踪器，可以在实时和体验后给出用户之间以及与环境之间的互动情况。

## 2. 以前的工作
随着互联网测绘的发展，一些 GIS 解决方案被开发出来，立刻，学术界强调了用其他方式探索空间数据可视化的必要性。自始至终，GIS 和 VR 之间的联系都是众所周知的，因为它们的互补性。GIS 处理的是原生的地理数据，而 VR 具有不可思议的自然交互能力。首先，这种 GIS 与 VR 的关系只建立在一种方式上：在 VR 中可视化 GIS 数据[13]、[14]、[15]、[16]。

之后，在证明了从 VR 体验到现实世界的可转移性之后，开发了一些研究，其中个人必须在环境的二维表示中识别他们最近的 VR 体验的一些元素[17]，[18]。这些研究选取了具有代表性的样本，要求参与者在纸质地图中写下他们在 HMD（头戴式显示器）中看到的事物或他们做出的决定。这种方法在 n（样本）值较高的情况下，处理起来比较困难和缓慢。

一些用于导航数据可视化的临时工具被创建出来（如[19]），但它们在功能上非常有限，在可重复使用性上有很高的限制，并且由于开发这种工具所需的努力而转移了研究团队对其原始研究问题的注意力。在本文中，我们提出了一种可复制的工作流程，并分享了一些工具，以使这种分析更容易，并具有更多潜在的定制可能性。

## 3. 软件说明
我们的主要贡献是完整的、经过测试的工作流程描述和两个软件工具，分别以两个脚本为代表，目的是获取数据并使其适应地理信息系统的使用（见图1）。

### 3.1 软件架构
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110020705.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110020705.png)

图 1：虚拟现实环境图。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110020814.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110020814.png)

图 2：迷宫场景的俯视图。

### 3.2 软件功能
#### 3.2.1 导航跟踪器
这个脚本最初是为 HTC Vive Camera Rig 设计的，非常简单，只要稍加修改就可以添加到每个角色控制器中。它基于两个主要的事件：StartMovement() 和 EndMovement()。这两个函数能在每次移动的开始和结束时获得用户头像的位置。同时，我们还存储了开始和结束的时间，以便计算用户移动的时间。有了这些信息，就很容易计算出每次移动的距离。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110021103.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110021103.png)

在每个运动结束后，我们可以将其添加到我们的主数据结构中：Movements 集合，定义为一个列表。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110021141.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110021141.png)

其功能如下：

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110021225.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110021225.png)

图 3：index.html。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110021329.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210110021329.png)

图 4：地图申报和创建。
