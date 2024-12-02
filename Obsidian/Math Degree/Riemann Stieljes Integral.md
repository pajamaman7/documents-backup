
Let $[a,b]\subseteq \mathbb{R}$. A partition of the interval $\{ x_i \}_{j=1}^{\infty}, a=x_{0}<x_{1}<\dots<x_n$, and the set of all partitions $\mathcal{P}([a,b])$, and $\Delta \alpha_i=\alpha_i-\alpha_{i-1}$, $\alpha:[a,b]\to\mathbb{R}$ monotonically increasing.
$$U(P,f,\alpha)=\sum\limits_{i=1 }^{n}M_i \Delta \alpha_i$$
Where $M_i=\sup f(x)$ on $[x_{i-1},x_i]$
$$L(P,f,\alpha)=\sum\limits_{i=1 }^{n}m_i \Delta \alpha_i$$
Where $m_i=\inf f(x)$ on $[x_{i-1},x_i]$
The upper integral is given by
$$
\overline{\int_{a}^{b}} f \, d\alpha = \inf_{P\in\mathcal{P}(a,b)} U(P,f,\alpha)
$$
The lower integral is given by
$$
\underline{\int_{a}^{b}} f \, d\alpha = \sup_{P\in\mathcal{P}(a,b)} L(P,f,\alpha)
$$
We say that $f$ is Riemann Steiljes integrable if:
$$
\underline{\int_{a}^{b}} f \, d\alpha= \overline{\int_{a}^{b}} f \, d\alpha  ={\int_{a}^{b}} f \, d\alpha 
$$
Denote that $\mathcal{R}(\alpha)=\{ f:[a,b]\to\mathbb{R}\text{, bounded, Reimann-Steiljes Integrable over }\alpha \}$
## Refinement
If $Q,P$ are partitions of $[a,b]$, then $Q$ is a refinement of $P$ when $Q\supseteq P$.
### Theorem
If $Q$ is a refinement of $P$, then 
$$
L(Q,f,\alpha)\geq L(P,f,\alpha)
$$
$$
U(Q,f,\alpha)\leq U(P,f,\alpha)
$$
### Theorem
If $P_{1},P_{2}$ are partitions in $\mathcal{P(a,b)},$ then $L(P_{1},f,\alpha)<U(P_{2},f,\alpha)$.
### Theorem
$f\in\mathcal{R}(\alpha)$ $\iff$ $\forall\varepsilon>0$, there exists a partition $P$ such that $U(P,f,\alpha)-L(P,f,\alpha)<\varepsilon$.
### Theorem
$U(P,f,\alpha)-L(P,f,\alpha)<\varepsilon$ for some $\varepsilon>0$. Then:
- If $Q \supseteq P$ then $U(Q,f,\alpha)-L(Q,f,\alpha)<\varepsilon$
- If $s_i,t_i\in[x_{i-1},x_i]$ then
$$
\sum\limits_{i=1 }^{n}\left| f(s_i)-f(t_i) \right| \Delta\alpha_i<\varepsilon
$$
- If $f\in\mathcal{R}(\alpha)$ and $s_i\in[x_{i-1},x_i]$, then
$$
\left|\sum\limits_{i=0 }^{n} f(s_i)\Delta\alpha_i -\int_{a}^{b} f \, d\alpha  \right| <\varepsilon
$$
## Riemann-Stieljes integrable functions
- If $f$ is continuous in $[a,b]$, then $f\in\mathcal{R}(\alpha)$. (For any $\alpha$ increasing)
- If $f$ is monotonic on $[a,b]$ and $\alpha$ is continuous on $[a,b]$, then $f\in\mathcal{R}(\alpha)$.
- If $f$ is bounded and has finitely many discontinuities on $[a,b]$, and at each discontinuity $\alpha$ is continuous. Then $f\in\mathcal{R}(\alpha)$.
## Composition