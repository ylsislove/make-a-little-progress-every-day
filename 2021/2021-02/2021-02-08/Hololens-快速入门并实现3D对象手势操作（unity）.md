# Hololens-快速入门并实现3D对象手势操作（unity）

## 环境
* Windows 10
* Unity 2019.4.19f1c1
* Visual Studio 2019
* MRTK 2.5.4

## 创建项目
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209001910.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209001910.png)

## 配置项目
1. 在菜单栏“File -> Build Settings”，将平台转换为 `通用Windows平台`

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209002604.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209002604.png)

2. 导入 MRTK 开发工具包，下载链接：[MRTK](https://github.com/microsoft/MixedRealityToolkit-Unity/releases/)
    - 在菜单栏 “Assets -> Import Package -> Custom Package”，选择刚刚下载的 MRTK 工具包。
    - 选择“All”，然后导入。

3. 在自动打开的 MRTK 项目配置器中，确保所有选项都被选上，如下图，然后点击应用。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209003450.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209003450.png)

    如果 MRTK 项目配置器没有自动打开，可以在在菜单栏“Mixed Reality Toolkit -> Utilities -> Configure Unity Project”手动打开。

4. 在菜单栏“Edit -> Project Settings”打开项目设置
    - 找到“Player -> XR Settings”，勾选 Virtual Reality Supported 复选框。
    - 在自动弹出的 MRTK 项目配置器中，设置空间音频，然后点击应用，如下图。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209004035.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209004035.png)

    - 在 XR Settings 中，设置深度格式为 16-bit 深度，如下

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209004300.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209004300.png)

    - 找到“Player -> Publishing Settings”，设置“Package name”为“MRTKLearning”。

5. 在菜单栏“File -> New Scene”新建场景，按“Ctrl S”将新场景保存到 Scenes 文件夹下，场景名为 Main

6. 在菜单栏“Mixed Reality Toolkit -> Add to Scene and Configure”添加配置文件。

7. （可选）选中层次结构选项卡中的 MixedReality Toolkit 对象，在配置器中选择 Copy & Customize，以拷贝默认配置文件，如下图

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209005105.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209005105.png)

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209005147.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209005147.png)

    - 在 Spatial Awareness 选项卡，取消`允许空间感知系统`复选框，如下图

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209005425.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209005425.png)

8. 记得 Ctrl S 保存项目

## 添加 Cube 并实现手势操作
1. 在层次结构面板的空白处右击，选择 3D Object 的 Cube，往场景中添加一个 Cube。

2. 设置 Cube 的 Y 为 -0.6，Z 为 2。Unity 中的 1 个单位在现实世界中约为 1 米。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209005810.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209005810.png)

3. 在 Cube 对象上添加 `Object Manipulator` 和 `NearInteractionGrabbable` 组件。`Constraint Manager` 是依赖项，会被自动添加，如下图

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209010115.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209010115.png)

4. 可以在 Object Manipulator 设置双手可以实现哪些操作，一般默认即可。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209010228.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209010228.png)

5. Ctrl S 保存。

## 打包部署
1. 在菜单栏“File -> Build Settings”，先点击 `Add Open Scene` 将当前场景添加，然后点击 Build，可以新建一个 Builds 文件夹保存打包后的文件。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209010505.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209010505.png)

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209010711.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209010711.png)

2. 等待打包完成。

3. 双击打开 .sln 文件，打开 VS 2019。

4. 选择 Master，ARM64，远程计算机。在项目上右击，选择属性，配置远程计算机 IP 地址。

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209011228.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209011228.png)

    [![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209011319.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209011319.png)

5. 确保 Hololens 设备处于唤醒状态。选择菜单“生成 -> 部署解决方案”即可将应用部署到 Hololens 设备上。如果是第一次部署，需要输入 Pin，Pin 可以在 Hololens 的“设置 -> 更新和安全 -> 开发者选项 -> 配对”找到。

6. 愉快的玩耍~

## 结果展示
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209013904.gif)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210209013904.gif)

