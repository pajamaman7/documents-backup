---
aliases:
  - Sequence of Functions
---
# Real Case
## Convergence
Let $E\subseteq \mathbb{R}$ and $\{ f_n \}_{n\geq 1}$ be a sequence of functions from $E$ to $\mathbb{R}$. 
If, for $x\in E$ fixed, the sequence $\{ f_n (x)\}_{n\geq 1}$ converges. If $I\subseteq E$ is the set for which $\{ f_n \}$ converges to some function $\lim\limits_{ n \to \infty }f_n=f(x)$, we say  that $\{ f_n \}_{n\geq 1}$ is pointwise convergent to $f$ and write $f_n\xrightarrow[I]{c.p} f$.
## Uniform Convergence
Let $\{ f_n \}_{n\geq 1}$ be as above. We say this sequence is uniformly convergent if and only if $\forall\varepsilon>0 \exists N: n\geq N\implies |f_n(x)-f(x)|<\varepsilon$ for every $x \in E$. 
## Squeeze Theorem 
Let $\{ f_n \}, \{ g_n \},\{ h_n \}$ be sequences of functions $X\to\mathbb{R}$ so that for any $x\in X$, $g_n(x)\leq f_n(x)\leq h_n(x)$, and $g_n,h_n$ both converge to the same $f(x)$, then $f_n(x)\to f(x)$.
## Boundedness
Let $\{ f_n \}$ be a sequence of bounded functions convergent to $f(x)$, then $f$ is a bounded function and $\{ f_n \}$ is uniformly bounded, there is some $M\in\mathbb{R}$ so that $|f_n(x)|<M$ for all $x\in X$ and $n\geq 1$.
## Continuity
If $\{ f_n \}$ is a sequence of continuous bounded functions which is uniformly convergent to $f(x)$, then $f(x)$ is bounded and continuous.
## Derivatives
## Integrals
Let $\{ f_n \}$ be a sequence of functions, each Riemann integrable in $[a,b]$, and $f_n$ convergent uniformly to $f$ on $[a,b]$. Then
$$
\lim\limits_{ n \to \infty } \int_{a}^{b} f_n(x) \, dx =\int_{a}^{b} f(x) \, dx 
$$
In fact, the convergence of $f_n$ is superfluous, a proof exists for the [[Lebesgue Integral]] without this condition, called the [[Bounded Convergence Theorem]] 