On $\mathbb{R}$, we define a [[Measure]], starting with open intervals:
For an open interval $I$, define:
$$
\mu(I)=\begin{cases}
b-a&\text{if }I=(a,b)\\
0&\text{if }I=\varnothing\\
\infty&\text{if }I=\mathbb{R}\\
\infty&\text{if }I=(a,\infty )\text{ or }I=(-\infty,a)\\
\end{cases}
$$
Then for any set in $\mathbb{R}$, we define the measure of $A$ as an infimum over all open covers of $A$:
$$
\mu(A)=\inf\left\{  \sum\limits_{\alpha}^{}\mu(I_\alpha):A\subseteq \bigcup\limits_{\alpha}^{}I_\alpha  \right\}
$$
Where there are [[Countable and Uncountable sets|At most Countable]] $\alpha$.
## Properties
- Singletons, finite, and countable sets all have outer measure $0$. This means $\mathbb{N},\mathbb{Z},\mathbb{Q}$ all have measure zero in $\mathbb{R}$.