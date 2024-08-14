近世代数
线性代数
数学分析原理
概率导论
统计学习方法
计算理论
组合数学与图论
数据结构与算法
博客网站搭建



单环的定义(Simple Ring)
如果环R的理想只有$\{e\},R$, 则称R是单环

可交换的单环 $\iff$ 域
$\impliedby$: 域具有乘法逆元$\implies\forall a\in I\neq\{0\},\exists a^{-1}\in R,a^{-1}a=1\in I\implies I=R$
$\implies$: R是交换环$\implies(a)=\{\sum xay|x,y\in R\}=\{ra|r\in R\}$
    非零理想只有R$\implies\forall a\in R\setminus\{0\},1\in(a)\implies\exists ra=1\implies a^{-1}=r$

已知单环R, 则$\text{char}R=0\lor \text{char}R=p$
证明: 记$k=\text{char}R$, 则$kR=\{\sum_kr|r\in R\}=\{0\}$
因为R是单环, 所以$\forall 0<m<k,mR\neq\{0\}\land mR是理想\implies mR=R$
倘若k是合数, 那么存在分解$k=mn\implies kR=m(nR)=m(R)=R\neq\{0\}$, 得出矛盾






域的特征的定义(Characteristic)
已知域$[F,+]$, 称F的特征为$\mathrm{char}(F)$,当且仅当
存在正整数n,使得$n\times 1=\underbrace{1+1+\cdots+1}_{n\text{个}}=0$
将最小的n记为$\mathrm{char}(F)$, 如果这样的n不存在, 则$\mathrm{char}(F)=0$

已知域$[F,+]$, 令n是F的加法子群中1的阶, 则$\mathrm{char}(F)=
\left\{\begin{aligned}
      n ,n<\infty \\
      0 ,n=\infty
\end{aligned}\right.$

<br>

已知域$[F,+]$, 而$\mathrm{char}(F)\neq0$, 则$\mathrm{char}(F)=p$是素数
用反证法证明: 假设$\mathrm{char}(F)=p$是合数, 那么$\exists a,b\in \mathbb{N},p=ab, (1<a,b<p)$
$\underbrace{(1+\cdots+1)}_{a\text{个}}\cdot\underbrace{(1+\cdots+1)}_{b\text{个}}=\underbrace{1+\cdots+1}_{p\text{个}}=0\implies(\underbrace{1+\cdots+1}_{a\text{个}}=0)\lor(\underbrace{1+\cdots+1}_{b\text{个}}=0)$
这与p是最小正整数矛盾, 所以$\mathrm{char}(F)=p$是素数

<br>

引理
已知域$[F,+]$, 则映射$f:\mathbb{Z}\to F:a\in\mathbb{Z}:f(a)=\underbrace{1+\cdots+1}_{a\text{个}}$是环同态, 
且$\mathbb{Z}\rhd\ker(f)=(\mathrm{char}(F))=\mathrm{char}(F)\cdot\mathbb{Z}$
证明: f是环同态: 加法保持, 乘法保持, 乘法单位元保持
因为$\mathrm{char}(F)\times 1=\underbrace{1+\cdots+1}_{\mathrm{char}(F)\text{个}}=0$, 所以$\mathrm{char}(F)\in\ker(f)\implies(\mathrm{char}(F))\subseteq\ker(f)$
因为$\mathbb{Z}$是主理想整环,且$\ker(f)$是理想,所以有$\ker(f)=(n)\implies n|\mathrm{char}(F)$
又因为$\mathrm{char}(F)$是最小的n,所以$\ker(f)=(\mathrm{char}(F))$

推论
已知域$[F,+]$, 且$\mathrm{char}(F)=p$, 那么存在域同态$f:\mathbb{Z}_p\to F$
由于域同态都是单射, 所以$f(\mathbb{Z}_p)<F$, 即存在从有限域到域F的嵌入(单态射)
证明: 映射$f:\mathbb{Z}\to F:a\in\mathbb{Z}:f(a)=\underbrace{1+\cdots+1}_{a\text{个}}$是环同态
根据环同构第一定理可知, $\mathbb{Z_p}=\mathbb{Z}/\ker(f)\cong f(\mathbb{Z})\subseteq F$, 所以存在域同态$f:\mathbb{Z_p}\to F$

<br>

已知域$[F,+]$, 而$\mathrm{char}(F)=0$, 则存在域同态$f:\mathbb{Q}\to F$
由于域同态都是单射, 所以$f(\mathbb{Q})<F$, 即存在从有理数域到域F的嵌入(单态射)
证明: 定义映射$f:\mathbb{Q}\to F:a\in\mathbb{Z},b\in\mathbb{N}\setminus\{0\}:f(\frac{a}{b})=\frac{\overbrace{1+\cdots+1}^{a项}}{\underbrace{1+\cdots+1}_{b项}}$
由于$\mathrm{char}(F)=0$, 所以分母$b\times1=\underbrace{1+1+\cdots+1}_{b\text{个}}\neq0$, 故$f(\frac{a}{b})$是良定义的
接着证明f是域同态: 加法保持, 乘法保持, 乘法单位元保持, 得证

<br><br>

环的特征的定义(Characteristic)
已知环$[R,+,\cdot]$, 称R的特征为$\mathrm{char}(R)$,当且仅当
存在正整数n,使得$n\times 1=\underbrace{1+1+\cdots+1}_{n\text{个}}=0$
将最小的n记为$\mathrm{char}(R)$, 如果这样的n不存在, 则$\mathrm{char}(R)=0$


已知 特征为素数p的 域$[F,+]$, 则F上的Frobenius自同态是域同态
如果域是有限域, 那么F上的Frobenius自同态还是域同构(单射,且定义域与陪域等大)




