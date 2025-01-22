---
aliases:
  - Riemann Integrable
---
Let $g:[a,b]\to\mathbb{R}$ be bounded, and $S=\{ x_{0}=a,x_{1},\dots,x_{n-1},x_n=b \}$ with $x_{i}<x_{i+1}$ called a **partition**. To this we associate the sums
$$U(g,S)=\sum\limits_{j=1 }^{n}\sup_{[x_{j-1},x_j]} g(x)(x_j-x_{j-1})$$
$$L(g,S)=\sum\limits_{j=1 }^{n}\inf_{[x_{j-1},x_j]} g(x)(x_j-x_{j-1})$$
called the upper and lower Darboux sums respectively. These follow the property that $L(g,S_{2})\leq U(g,S_{1})$ for any partitions $S_{1},S_{2}$. 
## Refinements
We say that $S_{2}$ is finer that $S_{1}$ if $S_{1}\subseteq S_{2}$ (think that the "slices" in $S_{2}$ are smaller).
If $S_{2}$ is finer than $S_{1}$, then 
$$
L(g,S_{1})\leq L(g,S_{2})\leq U(g,S_{2})\leq U(g,S_{1})
$$
All this is to say that with finer partitions, the upper and lower Darboux sums get closer.
## Definition
We say that $f\in \mathcal{R}([a,b])$ if $\sup L(g,S)=\inf U(g,S)$ over the set $\sigma$ of all partitions. This value is called the Riemann integral of $g$ notated
$$
\int_{a}^{b} g(x) \, dx =\int_{a}^{b} g(x)
$$
### Theorem
$g$ is Riemann integrable in $[a,b]$ if, $\forall\varepsilon>0$, there exists a partition $S_\varepsilon$ so that $U(g,S_\varepsilon)-L(g,S_\varepsilon)<\varepsilon$.
## Properties of the Riemann Integral
For Riemann integrable $f,g$ on $[a,b]$, and constants $\alpha,\beta$
- $\int_{a}^{b} \alpha f+\beta g \, dx=\alpha\int_{a}^{b} f \, dx+\beta\int_{a}^{b} g \, dx$.
- $\left| \int_{a}^{b} f \, dx \right|\leq \int_{a}^{b} |f| \, dx$.