# 入门指南

在本节中，我们将通过详细分析**用户界面**的结构，来了解 OpenRocket 是如何组织的。我们还会简要介绍可以从**文件（File）**菜单打开的**示例工程**。读完本节后，你将对 OpenRocket 的结构有透彻的理解，并可以着手设计属于自己的火箭。如果你已经了解本程序的组织方式，可以直接跳到下一节《基础火箭设计》。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/2023.01.Guide.User_Interface.png
:alt: OpenRocket 用户界面总览
:align: center

当前的开发界面：顶部是菜单和任务选项卡，中间是设计面板，下方是火箭视图。本页的入门截图使用的是自带的“A simple model rocket（一个简单的模型火箭）”示例。本页下方出现的图片均使用此示例。
```

# 用户界面

OpenRocket 的用户界面在水平方向上分为四个区域：

- 主菜单（Main Menu）
- 任务选项卡（Task Tabs）
- 火箭设计、发动机与配置、飞行模拟面板（Rocket Design, Motors & Configuration, and Flight Simulations pane）
- 火箭视图面板（Rocket Views Pane）

## 主菜单

**主菜单（Main Menu）**，有时也称为**菜单栏（Menu Bar）**或**应用程序功能区（Application Ribbon）**，位于 OpenRocket 窗口的顶部。在 macOS 上，主菜单位于屏幕顶部，嵌入在原生 macOS 菜单栏中。我们将逐一介绍主菜单中的各个菜单选项。

### 文件（File）

```{figure} https://openrocket.readthedocs.io/en/latest/_images/02.04.01.File_Menu.png
:alt: OpenRocket 文件菜单
:align: center

OpenRocket 的文件菜单
```

**文件菜单（File Menu）**按功能划分为五个部分：

1. **文件打开选项**：
   - **新建（New）**：在不关闭当前工程的情况下开始一个新工程。
   - **打开…（Open…）**：打开之前保存的 `*.ork` 文件。
   - **打开最近文件（Open Recent）**：打开最近打开过的文件。
   - **打开示例（Open Example）**：选择并打开 OpenRocket 自带的示例工程。
2. **文件保存选项**：
   - **保存（Save）**：将更改保存到当前工程。
   - **另存为…（Save as…）**：以不同的文件名或位置保存工程。
3. **导入与导出选项**：
   - **导出为（Export as）**：将工程导出为其他文件格式，例如 Rocksim 10（`.rkt`）。
   - **保存贴花图片（Save decal image）**：保存工程中使用的贴花图片文件。
   - **打印设计信息…（Print design info…）**：将火箭组件、尾翼组模板或火箭设计的技术细节打印或导出为 `*.pdf`。
4. **关闭**：
   - **关闭设计（Close design）**：退出当前工程（会提示保存未保存的更改）。
5. **退出**：
   - **退出（Quit）**：退出 OpenRocket，必要时保存每个已打开的工程。

### 编辑（Edit）

```{figure} https://openrocket.readthedocs.io/en/latest/_images/OR.Guide.User_Interface.04.02.File.png
:alt: OpenRocket 编辑菜单
:align: center

OpenRocket 的编辑菜单
```

**编辑菜单（Edit Menu）**分为三类操作：

1. 撤销（Undo）和重做（Redo）某个操作
2. 剪切（Cut）、复制（Copy）、粘贴（Paste）和删除（Delete）对象
3. 缩放（Scale）：缩放组件或整支火箭
4. 首选项（Preferences）：访问 OpenRocket 的系统首选项

### 工具（Tools）

```{figure} https://openrocket.readthedocs.io/en/latest/_images/OR.Guide.User_Interface.04.03.File.png
:alt: OpenRocket 工具菜单
:align: center

OpenRocket 的工具菜单
```

**工具菜单（Tools Menu）**提供以下设计工具：

- **组件分析（Component Analysis）**：分析特定组件的（空气动力学）效应
- **火箭优化（Rocket optimization）**：优化火箭的特定特性
- **自定义表达式（Custom expressions）**：创建用于专门分析的自定义表达式
- **摄影棚（Photo Studio）**：在摄影棚中以多种背景和效果用 3D 方式展示火箭

### 帮助（Help）

```{figure} https://openrocket.readthedocs.io/en/latest/_images/OR.Guide.User_Interface.04.04.File.png
:alt: OpenRocket 帮助菜单
:align: center

OpenRocket 的帮助菜单
```

**帮助菜单（Help Menu）**分为三个部分：

1. 引导式游览（Guided tours）：演示 OpenRocket 的使用方法
2. 错误报告与调试日志（Bug reporting and Debug log）：帮助用户向开发者提供反馈的工具
3. 许可证与关于（License and About）：关于 OpenRocket 的其他一般信息

## 任务选项卡

下面展示的窗口使用了 OpenRocket 自带的“A simple model rocket（一个简单的模型火箭）”示例。

### 火箭设计（Rocket Design）

**火箭设计（Rocket Design）**选项卡分为三个部分：

- *（左侧）* **组件树（Component tree）**：以树状视图显示构成火箭的各个组件。
- *（中间）* **组件操作按钮（Component action buttons）**：用于编辑、移动或删除当前所选组件的按钮等。
- *（右侧）* **组件添加按钮（Component addition buttons）**：用于向火箭添加新组件的按钮。

OpenRocket 中可用的组件按功能分为四类：

1. **装配组件（Assembly Components）**
2. **箭体组件与尾翼组（Body Components and Fin Sets）**（外部组件）
3. **内部组件（Internal Components）**
4. **质量组件（Mass Components）**（包括电子设备和回收组件）

组件会显示**灰色（greyed out）**，直到将此类组件添加到当前所选组件变得恰当为止。例如，如果你在组件树中选定了一个尾翼组组件，那么头锥（nose cone）按钮就会变灰，因为你无法将头锥添加到尾翼组上。随着组件的不断添加，你会看到组件树（窗口左侧）随着每次添加而不断生长。

### 发动机与配置（Motors & Configuration）

**发动机与配置（Motors & Configurations）**选项卡用于选择发动机、回收事件和级间时序。发动机配置选项包括：

- **新建配置（New Configuration）**：创建一个新的飞行配置
- **重命名配置（Rename Configuration）**：重命名当前选中的配置
- **删除配置（Remove Configuration）**：删除当前选中的配置
- **复制配置（Copy Configuration）**：复制当前选中的配置

在选中某个具体配置后，你可以：

- **选择发动机（Select motor）**：为当前选中的发动机挂载位从发动机数据库中选择一台发动机。
- **移除发动机（Remove motor）**：从发动机挂载位移除当前选中的发动机。
- **选择点火（Select ignition）**：设置当前发动机的点火时序。
- **重置点火（Reset ignition）**：将当前发动机的点火时序重置为默认值。

### 飞行模拟（Flight Simulations）

**飞行模拟（Flight Simulations）**选项卡用于管理和运行飞行模拟以及飞行模拟绘图。在这里，你可以添加新的模拟，或编辑、运行、删除已有的模拟。选中单个模拟后，你甚至可以绘制并导出模拟结果。

## 火箭视图

下面展示的窗口使用了 OpenRocket 自带的“A simple model rocket（一个简单的模型火箭）”示例。

### 顶视图 / 侧视图 / 后视图（Top / Side / Back View）

**顶视图（Top View）**、**侧视图（Side View）**和**后视图（Back View）**是线条图，类似于蓝图，显示所有火箭组件及其位置。你几乎所有的设计工作都将在顶、侧、后视图中完成。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/Getting_Started.Rocket_Views.Top_View.jpg
:alt: 顶视图
:align: center

顶视图。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/Getting_Started.Rocket_Views.Side_View.jpg
:alt: 侧视图
:align: center

侧视图。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/Getting_Started.Rocket_Views.Back_View.jpg
:alt: 后视图
:align: center

后视图。
```

### 3D 实体图 / 3D 未完成（3D Figure / 3D Unfinished）

**3D 实体图（3D Figure）**和**3D 未完成（3D Unfinished）**视图让你可以看穿火箭外壳，查看许多内部组件。这些视图能帮助你更清楚地了解箭体内部不同组件之间的位置关系。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/Getting_Started.Rocket_Views.3D_Figure.jpg
:alt: 3D 实体图视图
:align: center

3D 实体图视图。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/Getting_Started.Rocket_Views.3D_Unfinished.jpg
:alt: 3D 未完成视图
:align: center

3D 未完成视图。
```

### 3D 完成（3D Finished）

**3D 完成（3D Finished）**视图展示火箭完成后的样子。OpenRocket 允许你选择组件颜色、箭体管内外壁、尾翼的左侧或右侧，甚至创建透明组件——所有这些都可以选择是否带贴花（透明或不透明）。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/Getting_Started.Rocket_Views.3D_Finished.jpg
:alt: 3D 完成视图
:align: center

3D 完成视图。
```

## 熟悉 OpenRocket（示例工程）

对于 OpenRocket 的新用户，强烈建议在尝试创建自己的自定义火箭设计之前，先通过打开示例工程并观察其组装方式、对示例进行更改、了解如何模拟飞行，来熟悉 OpenRocket 的用户界面和公认的设计原则。

示例设计文件的位置如下：选择 **文件（File）** ‣ **打开示例（Open example）** 即可打开此列表：

```{figure} https://openrocket.readthedocs.io/en/latest/_images/2023.01.Open_Example.png
:alt: 示例设计文件的位置
:align: center

示例设计文件的所在位置。
```

OpenRocket 目前包含以下示例设计：

- **“标准（Standard）”设计**：
  - **A simple model rocket（一个简单的模型火箭）**：一个基础的火箭设计。这是新用户很好的起点。该设计包含标准火箭设计的所有要素，包括回收系统，以及尝试不同发动机的可能。
  - **Two-stage rocket（两级火箭）**：一个两级火箭设计。
  - **Three-stage rocket（三级火箭）**：一个三级火箭设计。
  - **TARC payload rocket（TARC 载荷火箭）**：演示由发动机弹出分别展开的载荷舱与助推器段。TARC = Team America Rocketry Challenge（美国火箭挑战赛）。
  - **3D Printable Nose Cone and Fins（可 3D 打印的头锥与尾翼）**：一个用于测试将头锥和尾翼导出为 OBJ 文件以进行 3D 打印的火箭设计。
- **“高级（Advanced）”设计**：
  - **Airstart timing（空中点火时序）**：演示不同空中点火时序对总体高度的影响。
  - **Base drag hack (short-wide)（底阻修正（短粗型））**：演示应用“底阻修正”来调整短粗型火箭（长径比小于 10:1）压心的方法。
  - **Chute release（降落伞释放）**：一个适配了电子降落伞释放装置的简单模型火箭示例。
  - **Dual parachute deployment（双降落伞展开）**：一个标准的无拉链（zipperless）玻璃纤维双部署火箭。
  - **Clustered motors（捆绑式发动机）**：一个采用捆绑式发动机的火箭设计。
  - **Parallel booster staging（并联助推器分级）**：演示并联助推器分级。
  - **Pods–airframes and winglets（吊舱–箭体与安定翼）**：演示吊舱的两种用法，既用于传统的“机翼吊舱”，也利用虚拟箭体管实现水平安定面的“尾翼上加尾翼”。
  - **Pods–powered with recovery deployment（吊舱–带动力与回收展开）**：演示使用吊舱实现带动力回收展开。
- **使用高级模拟的设计（例如扩展与脚本）**：
  - **Simulation extensions（模拟扩展）**：演示使用模拟扩展实现主动滚转控制与空中点火。主尾翼略有错位，从而产生滚转。
  - **Simulation scripting（模拟脚本）**：演示用 JavaScript 编写的模拟扩展实现主动滚转控制与空中点火。

# 使用 OpenRocket 的基础知识

## 火箭配置（Rocket Configuration）

要构建你的第一支火箭，请启动 OpenRocket，然后**双击组件树顶部的“Rocket（火箭）”标签**，打开**火箭配置（Rocket configuration）**弹出窗口。OpenRocket 允许你为设计命名、标明设计者、添加注释并创建修订历史。

默认的设计名称是 **Rocket**，但这个名称可以更改，更改设计名称同时也会更改组件树上显示的火箭名称。因此，请重命名你的设计，并填入你希望添加的设计者、注释和修订历史信息。

1. **双击组件树中的“Rocket（火箭）”**

   ```{figure} https://openrocket.readthedocs.io/en/latest/_images/04.01.02.Rocket_Configuration.png
   :alt: 打开火箭配置窗口
   :align: center

   打开火箭配置窗口。
   ```

2. **重命名“Rocket（火箭）”**

   ```{figure} https://openrocket.readthedocs.io/en/latest/_images/04.01.05.Rocket_Configuration.Rename.png
   :alt: 更改火箭名称
   :align: center

   更改你的火箭名称。
   ```

## 添加外部组件

现在，是时候开始组装各个组件来构建火箭设计了。组装火箭设计普遍接受的方式是自上而下、从头到尾（从机头到尾部）。因此，我们将先添加头锥。

### 添加头锥（Adding a Nose Cone）

在选中**级（Stage）**的情况下，点击**头锥（Nose Cone）**按钮，将弹出**头锥配置（Nose Cone configuration）**窗口。然后，点击配置窗口右上角的**零件库（Parts Library）**按钮。这将打开一个新窗口——**组件预设窗口（Component preset window）**。在这里，你可以从列表中选择各厂商内置的头锥预设。选择下图所示的头锥，然后点击**关闭（Close）**按钮关闭**头锥配置（Nose Cone configuration）**窗口。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.01.03.Rocket_Build.Nose_Cone.png
:alt: 向火箭添加头锥
:align: center

向火箭添加头锥。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/Getting_Started.Components.Nose_Cone.Parts_Library.Highlighted.jpg
:alt: 点击零件库按钮
:align: center

点击零件库（Parts Library）按钮（位于头锥配置窗口右上角），从零件数据库中选择一个头锥。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/Getting_Started.Components.Nose_Cone.jpg
:alt: 头锥已添加到火箭
:align: center

头锥已添加到火箭。
```

恭喜，你刚刚添加了第一个组件！ 🎉

### 添加载荷舱（Adding a Payload Bay）

接下来，我们要在头锥之后添加一个载荷舱。为此，在选中**级（Stage）**或**头锥（Nose Cone）**的情况下，点击**箭体管（Body Tube）**按钮，将弹出**箭体管配置（Body Tube configuration）**窗口。与头锥一样，点击**零件库（Parts Library）**打开**组件预设窗口（Component preset window）**。选择下图所示的箭体管，然后点击**关闭（Close）**按钮关闭**箭体管配置（Body Tube configuration）**窗口。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.02.01.Rocket_Build.Payload_Bay.png
:alt: 向火箭添加载荷舱
:align: center

向火箭添加载荷舱。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.02.05.Rocket_Build.Payload_Bay.png
:alt: 从零件数据库中选择箭体管
:align: center

从零件数据库中选择一个箭体管。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.02.06.Rocket_Build.Payload_Bay.png
:alt: 载荷舱已添加到火箭
:align: center

载荷舱已添加到火箭。
```

### 添加过渡段（Adding a Transition）

过渡段（Transition）最常用于连接直径不同的箭体管。但过渡段也可以用于连接两根直径相同的箭体管，这里就要这样做。在选中**级（Stage）**或**载荷舱（Payload Bay）**的情况下，点击**过渡段（Transition）**按钮，将弹出**过渡段配置（Transition configuration）**窗口。默认的**过渡段配置（Transition Configuration）**选项卡是**常规（General）**选项卡。在该选项卡上，将下图中圈出区域的输入值修改为与所示一致。然后，点击**肩台（Shoulder）**选项卡，将下图中圈出区域的输入值修改为与所示一致。然后，点击**关闭（Close）**按钮。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.03.01.Rocket_Build.Transition.png
:alt: 在载荷舱之后添加过渡段
:align: center

在载荷舱之后添加过渡段。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.03.06.Rocket_Build.Transition.png
:alt: 设置过渡段参数
:align: center

在常规（General）选项卡和肩台（Shoulder）选项卡中设置过渡段参数。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.03.07.Rocket_Build.Transition.png
:alt: 过渡段已添加到火箭
:align: center

过渡段已添加到火箭。
```

### 添加箭体管（Adding a Body Tube）

现在，执行与上面添加**载荷舱（Payload Bay）**相同的操作，但从零件数据库中选择这根箭体管：

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.04.01.Rocket_Build.Body_Tube.png
:alt: 添加另一根箭体管
:align: center

在过渡段之后添加另一根箭体管，并从零件数据库中选择它。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.04.02.Rocket_Build.Body_Tube.png
:alt: 箭体管已添加到火箭
:align: center

箭体管已添加到火箭。
```

### 添加尾翼（Adding Fins）

最底部的组件是尾翼。OpenRocket 提供四种类型的尾翼：**梯形（Trapezoidal）**、**椭圆（Elliptical）**、**自由形状（Free Form）**和**管状尾翼（Tube Fins）**。本设计将使用**梯形（Trapezoidal）**尾翼。在选中**箭体管（Body Tube）**的情况下，点击**梯形尾翼（Trapezoidal fins）**按钮，将弹出**梯形尾翼组配置（Trapezoidal Fin Set configuration）**窗口。在默认的**常规（General）**选项卡上，将输入值修改为与所示一致。然后，点击**关闭（Close）**按钮。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.05.01.Rocket_Build.Fins.png
:alt: 在第二根箭体管内添加梯形尾翼
:align: center

在第二根箭体管内添加梯形尾翼。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.05.02.Rocket_Build.Fins.png
:alt: 尾翼组配置窗口
:align: center

尾翼组配置窗口
```

尾翼附着于另一个组件，在本例中是**箭体管（Body Tube）**。如下图所示，在组件树上，尾翼显示在**箭体管（Body Tube）**的下方。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.05.03.Rocket_Build.Fins.png
:alt: 梯形尾翼组已添加到火箭
:align: center

梯形尾翼组已添加到火箭。
```

### 添加发射导轨（Adding a Launch Guide）

OpenRocket 包含两种发射导轨：**导轨滑块（Rail Buttons）**和**发射卡箍（Launch Lug）**。由于箭体管的直径，本设计将使用**发射卡箍（Launch Lug）**。与尾翼一样，发射导轨附着于另一个组件，在本例中是箭体管。按照之前组件的模式，打开**发射卡箍配置（Launch Lug configuration）**窗口。然后，将规格修改为与下图所示一致。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.06.02.Rocket_Build.Launch_Lug.png
:alt: 发射卡箍配置窗口
:align: center

发射卡箍配置窗口。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.06.03.Rocket_Build.Launch_Lug.png
:alt: 发射卡箍已添加到箭体管
:align: center

发射卡箍已添加到箭体管。
```

### 添加降落伞和减震绳（Adding a Parachute and Shock Cord）

接下来，我们将为火箭添加**降落伞（Parachute）**和**减震绳（Shock Cord）**用于回收。选中箭体管，添加**降落伞（Parachute）**和**减震绳（Shock Cord）**。降落伞和减震绳附着在箭体管上。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.07.03.Rocket_Build.Parachute.png
:alt: 降落伞零件库与配置窗口
:align: center

降落伞零件库（左）与配置窗口（右）。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.08.01.Rocket_Build.Parachute.png
:alt: 减震绳配置窗口
:align: center

减震绳配置窗口。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.08.02.Rocket_Build.Parachute.png
:alt: 降落伞和减震绳已添加到箭体管
:align: center

降落伞和减震绳已添加到箭体管。
```

### 添加发动机挡板（Adding an Engine Block）

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.09.01.Rocket_Build.Engine_Block.png
:alt: 发动机挡板配置窗口
:align: center

发动机挡板配置窗口。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.09.02.Rocket_Build.Engine_Block.png
:alt: 发动机挡板已添加到箭体管
:align: center

发动机挡板已添加到箭体管。
```

## 查看您的设计

箭体完成后，你可以以 2D（如上）或三种 3D 视图查看你的设计。其中最常用的视图是**3D 未完成（3D Unfinished）**和**3D 完成（3D Finished）**。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.06.03.Rocket_Build.3D_Unfinished.png
:alt: 3D 未完成视图
:align: center

3D 未完成视图（箭体管呈半透明，以便可见内部组件）。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/11.06.04.Rocket_Build.3D_Finished.png
:alt: 3D 完成视图
:align: center

3D 完成视图（你最终成品的样子）。
```

## 添加外观设置

如果你希望 OpenRocket 中的设计在外观上接近你想要建造的样子，可以更改组件的外观。更改**外观（Appearance）**设置时，最好处于**3D 完成（3D Finished）**面板中，这样你就能看到正在做的更改。因此，让我们先将视图切换到**3D 完成（3D Finished）**。

### 更改颜色

要做的第一个更改是选择头锥的颜色并更改头锥颜色。在组件树中双击头锥，打开**头锥配置（Nose Cone configuration）**窗口，然后选择**外观（Appearance）**选项卡。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.10.01.Rocket_Build_Appearance.Nose_Cone.png
:alt: 头锥外观选项卡
:align: center

配置窗口中的头锥外观（Appearance）选项卡。
```

现在，取消勾选**外观（Appearance）**的**使用默认（Use default）**复选框。然后，点击**颜色（Color）**框，打开**选择颜色（Choose color）**窗口。选择你中意的颜色（这里将使用紫色）。点击**确定（OK）**使用你的选择，然后关闭**头锥配置（Nose Cone configuration）**窗口。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.10.05.Rocket_Build_Appearance.Nose_Cone.png
:alt: 更改头锥颜色
:align: center

更改头锥颜色。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.10.06.Rocket_Build_Appearance.Nose_Cone.png
:alt: 头锥颜色已更改
:align: center

头锥颜色已更改。
```

对**过渡段（Transition）**、**箭体管（Body Tube）**、**梯形尾翼组（Trapezoidal Fin Set）**和**发射卡箍（Launch Lug）**重复上述步骤；箭体管、发射卡箍和尾翼还有一个**纹理（Texture）**需要设置为**无（none）**。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.10.07.Rocket_Build_Appearance.Nose_Cone.png
:alt: 所有外部组件已上色
:align: center

除载荷舱外，所有外部组件现在都已上色。
```

现在来点小魔法。打开**载荷舱（Payload Bay）**的外观选项卡，取消勾选**外观（Appearance）**的**使用默认（Use default）**复选框，并将**纹理（Texture）**设置为 `<none>`。然后，点击**颜色（Color）**框打开**选择颜色（Choose color）**窗口。点击一种浅蓝色（下图中带 **X** 的框），然后点击**确定（OK）**。现在，将**不透明度（Opacity）**设置为 **20%** 并关闭载荷舱配置窗口，你就得到了一个透明的载荷舱。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.10.11.Rocket_Build_Appearance.Nose_Cone.png
:alt: 更改载荷舱颜色与不透明度
:align: center

将载荷舱颜色更改为浅蓝色，并将不透明度降低到 20%。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.10.12.Rocket_Build_Appearance.Nose_Cone.png
:alt: 半透明载荷舱
:align: center

你现在拥有了一个半透明的载荷舱！
```

### 添加贴花

最后再来点魔法，让我们在透明的载荷舱上贴一张贴花。不过，在开始之前，请将下图保存到你的设备。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.10.13.Rocket_Build_Appearance.Decal.png
:alt: 贴花图片
:align: center

[将此贴花图片保存到你的电脑](https://openrocket.readthedocs.io/en/latest/_downloads/e9be7409e5b0dc6c17729abb479c8518/12.10.13.Rocket_Build_Appearance.Decal.png)
```

贴花已保存到你的设备后，就可以开始了。

#### 从文件选择贴花（Select Decal from File）

打开载荷舱配置窗口并选择**外观（Appearance）**选项卡。点击**纹理类型（Texture type）**以激活选择下拉框，并选择**从文件…（From file…）**。现在，导航到你保存贴花的位置，并选择它。

#### 贴花类型、尺寸与位置（Decal Type, Size and Position）

要调整贴花的尺寸和位置，首先将**重复（Repeat）**类型更改为**贴纸（Sticker）**（你只想在载荷舱上放一个符号），然后将**缩放（Scale）**以及 **x、y 偏移（Offset x and y）** 的值更改为下图所示。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.10.19.Rocket_Build_Appearance.Payload_Bay.Decal.png
:alt: 更改重复类型与缩放偏移
:align: center

更改重复（Repeat）类型，并设置 x 和 y 的缩放（Scale）与偏移（Offset）值。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.10.20.Rocket_Build_Appearance.Payload_Bay.Decal.png
:alt: 贴花已添加并调整
:align: center

贴花已添加到载荷舱，并正确调整了尺寸和位置。
```

好了，这就是透明的载荷舱上的贴花！那么，来看看你学到了什么，并拓展你的知识。看看你能否在没有说明的情况下，按照下面的截图操作。请将下图保存到你的设备。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.10.21.Rocket_Build_Appearance.Fins.png
:alt: 尾翼贴花图片
:align: center

[将此贴花图片保存到你的电脑](https://openrocket.readthedocs.io/en/latest/_downloads/3f48516d2ec43b656c5f21e758ec7e26/12.10.21.Rocket_Build_Appearance.Fins.png)
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.11.03.Rocket_Build_Appearance.Fins.png
:alt: 拆分尾翼
:align: center

在**梯形尾翼组配置窗口（Trapezoidal Fin Set configuration window）**中拆分尾翼（左）。拆分后，你会在组件树中看到独立的尾翼实例（右）。
```

拆分尾翼后，**保存并重新打开设计文件**，然后在**3D 完成（3D Finished）**中查看。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.11.11.Rocket_Build_Appearance.Fins.png
:alt: 更改尾翼外观
:align: center

更改**尾翼 #2（Fin #2）**和**尾翼 #3（Fin #3）**的外观。
```

## 在摄影棚中查看（Viewing in Photo Studio）

那么，这只“鸟”飞起来会是什么样？为此，我们可以使用**摄影棚（Photo Studio）**工具。如果你希望预览包含排气效果，请先添加一台发动机。

### 选择发动机

在用户界面的任务选项卡中，选择**发动机与配置（Motors & Configuration）**选项卡。然后，在点击**新建配置（New Configuration）**之前，确保左侧的**发动机挂载（Motor mounts）**列表中所选的是正确的发动机管。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.12.02.Rocket_Build.Motor.png
:alt: 添加新飞行配置
:align: center

在发动机与配置选项卡中添加新的飞行配置。
```

点击**新建配置（New Configuration）**后，会打开**发动机选择（Motor Selection）**窗口。本例中选择 **Estes D-12-7**，然后点击**确定（OK）**。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.12.03.Rocket_Build.Motor.png
:alt: 选择 Estes D-12-7 发动机
:align: center

在**发动机选择（Motor Selection）**窗口中选择 Estes D-12-7 火箭发动机。
```

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.12.05.Rocket_Build.Motor.png
:alt: 选择 D-12-7 作为飞行配置
:align: center

将 D-12-7 选为**飞行配置（Flight Configuration）**。
```

### 在摄影棚中飞行（Flying in Photo Studio）

准备好看看你的火箭飞起来了吗？那么，从**工具（Tools）**菜单打开**摄影棚（Photo Studio）**。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.12.01.Rocket_Build.Photo_Studio.png
:alt: 打开摄影棚
:align: center

打开**摄影棚（Photo Studio）**。
```

你现在可以在 3D 中查看你的作品并与之交互。你可以更改背景、火箭朝向、相机设置，甚至添加一些炫酷的效果。

```{figure} https://openrocket.readthedocs.io/en/latest/_images/12.12.02.Rocket_Build.Photo_Studio.png
:alt: 摄影棚中的火箭
:align: center

摄影棚中的火箭。
```

为什么在进入摄影棚之前要添加发动机？排气效果只为所选飞行配置中的发动机制作渲染。请转到**效果（Effects）**选项卡并启用**火焰（Flame）**效果。现在，尽情调整设置吧！

---

本中文版根据 OpenRocket 23.09 官方文档《Getting Started》翻译整理，仅供学习参考。所有图片均直接引用官方原始资源（openrocket.readthedocs.io），未作修改。如官方内容有更新，请以英文原版为准。原文版权归 OpenRocket 项目所有，本翻译版保留署名并注明出处。
