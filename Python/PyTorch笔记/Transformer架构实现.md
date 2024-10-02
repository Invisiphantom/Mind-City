
![](https://machinelearningmastery.com/wp-content/uploads/2021/08/attention_research_1.png =400x)


## 自注意力机制(Re-weighting)

![image.png](https://img.ethancao.cn/2024_05_22_WfPibwjr8HmoyvZ.png)

输入向量: $\{x_1,\cdots,x_n\}\in \mathbb{R}^{n\times d}$
权重矩阵: $W_q, W_k, W_v\in \mathbb{R}^{d\times k}$
Query: $Q(x_i)=W_q^T\cdot x_i$
Key: $K(x_i)=W_k^T\cdot x_i$
Value: $V(x_i)=W_v^T\cdot x_i$
Attention: $\text{Softmax}(\frac{QK^T}{\sqrt{k}})\cdot V$

对于向量$x_3$, 欲得到经过权重分配后的$z_3$
首先计算每个向量施加于$x_3$的依赖权重
$s_{31}=Q(x_3)\cdot K(x_1)$
$s_{32}=Q(x_3)\cdot K(x_2)$
$s_{33}=Q(x_3)\cdot K(x_3)$
$s_{34}=Q(x_3)\cdot K(x_4)$
然后对这些权重进行归一化(Softmax)
$\{w_{31},w_{32},w_{33},w_{34}\}=\text{Softmax}(\{s_{31},s_{32},s_{33},s_{34}\})$
然后按照权重分配到各个向量得到$z_3$
$z_3=w_{31}V(x_1)+w_{32}V(x_2)+w_{33}V(x_3)+w_{34}V(x_4)$



## LayerNorm

$\text{LayerNorm}(z,\gamma,\beta)=\gamma\cdot\frac{z-\mu_z}{\sigma_z}+\beta$
均值: $\mu_z=\frac{1}{k}\sum_{i=1}^kz_i$
标准差: $\sigma_z=\sqrt{\frac{1}{k}\sum_{i=1}^k(z_i-\mu_z)^2+\epsilon}$