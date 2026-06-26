[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PbwMKW4u)
# 计算物理期末项目：基于蒙特卡洛方法的一维随机游走模拟与扩散规律验证

## 1. 项目简介

本项目使用 Monte Carlo（蒙特卡洛）方法模拟一维无偏随机游走（Random Walk），研究布朗运动的微观随机行为，并验证宏观扩散规律。

在统计物理中，大量粒子的随机运动会表现出扩散现象，其核心关系为：

[
\langle x^2(t) \rangle = 2Dt
]

其中：

* (\langle x^2(t) \rangle)：均方位移（Mean Square Displacement, MSD）
* (D)：扩散系数
* (t)：时间

本项目通过数值模拟验证：

1. 粒子轨迹具有随机性
2. 均方位移与时间呈线性关系
3. 粒子位置分布逐渐接近高斯分布

---

## 2. 项目结构

```bash
project/
│
├── main.py
├── physics.py
├── analysis.py
├── requirements.txt
└── README.md
```

---

## 3. 文件说明

### main.py（程序入口）

负责：

* 定义全部物理参数
* 初始化模拟环境
* 调用物理计算模块
* 调用分析与绘图模块
* 输出最终结果

主要参数：

* 粒子数量 `N`
* 时间步数 `T`
* 单步位移 `a`

---

### physics.py（物理 / 算法模块）

负责实现核心数值算法。

主要功能：

* Monte Carlo 随机游走模拟
* 粒子位置更新
* 轨迹记录

核心更新公式：

[
x_{n+1}=x_n+a\xi
]

其中：

[
\xi=
\begin{cases}
+1, & P=0.5 \
-1, & P=0.5
\end{cases}
]

说明：

每一步粒子有 50% 概率向左移动，50% 概率向右移动。

---

### analysis.py（分析与可视化模块）

负责：

* 计算均方位移（MSD）
* 线性拟合扩散系数
* 统计误差分析
* 绘制论文所需图像

输出图像包括：

1. 单粒子随机轨迹图
2. MSD 随时间变化图
3. 最终位置分布直方图
4. 理论与模拟结果对比图

均方位移定义：

[
\langle x^2(t)\rangle=
\frac{1}{N}
\sum_{i=1}^{N}
x_i^2(t)
]

---

## 4. 环境配置

推荐 Python 版本：

```bash
Python 3.9+
```

安装依赖：

```bash
pip install -r requirements.txt
```

---

## 5. requirements.txt

项目依赖：

```txt
numpy
matplotlib
scipy
```

---

## 6. 运行方法

运行主程序：

```bash
python main.py
```

运行后将得到：

* 单粒子轨迹图
* 均方位移图
* 扩散系数拟合结果
* 粒子位置分布图

终端输出示例：

```bash
Estimated diffusion coefficient D = 0.5021
```

---

## 7. 数值方法说明

本项目采用 Monte Carlo 随机抽样方法。

算法流程：

1. 初始化全部粒子位置为 0
2. 对每个时间步生成随机方向
3. 更新粒子位置
4. 记录所有轨迹
5. 计算各时刻 MSD
6. 进行线性拟合求扩散系数

时间复杂度：

[
O(NT)
]

其中：

* (N)：粒子数量
* (T)：模拟步数

---

## 8. 结果验证

本项目通过以下方式验证模拟正确性：

### 1）解析解对比

验证：

[
\langle x^2\rangle = 2Dt
]

检查模拟结果是否满足线性关系。

---

### 2）统计收敛性测试

改变粒子数：

* 100
* 1000
* 5000
* 10000

观察误差变化。

理论上：

粒子数越多，统计误差越小。

---

### 3）分布形态检验

绘制最终粒子位置直方图。

理论预测：

长时间后应近似高斯分布：

[
P(x,t)=
\frac{1}{\sqrt{4\pi Dt}}
\exp\left(
-\frac{x^2}{4Dt}
\right)
]

---

## 9. 代码规范

### 模块解耦

代码按功能拆分：

* 入口模块
* 算法模块
* 分析模块

禁止将所有逻辑写入单文件。

---

### 物理注释

必须对以下内容添加注释：

* 核心物理方程
* Monte Carlo 算法步骤
* MSD 计算方法
* 拟合过程

---

### 参数化设计

所有物理参数必须集中定义：

示例：

```python
NUM_PARTICLES = 5000
NUM_STEPS = 1000
STEP_SIZE = 1.0
```

要求：

* 禁止在循环中出现魔法数字
* 所有关键参数可修改

---

## 10. 参考文献

1. Wikipedia contributors. Monte Carlo Method. Wikipedia, 2026.
2. Hjorth-Jensen M. Computational Physics. University of Oslo, 2024.
3. Zingale M. Computational Astrophysics. Open Jupyter Book, 2024.

## 11. 声明
本项目使用 AI 辅助完成，包括代码结构设计、文档整理与注释优化。
