---
aliases:
  - Pointwise Bounded
  - Uniformly Bounded
  - Uniformly Equicontinuous
---
## Pointwise Bounded
Let $(E,d)$ be a [[Metric Spaces|Metric Space]], and $U\subseteq E$. $\mathcal{F}$ is a family of functions from $U$ to $\mathbb{R}$. We say that $\mathcal{F}$ is pointwise bounded on a subset $S\subseteq U$, if for every $x\in S$, there exists some $M_x>0$ so that $f(x)<M_x$ for any $f\in\mathcal{F}$.
## Uniformly Bounded
Let $(E,d)$ be a [[Metric Spaces|Metric Space]], and $U\subseteq E$. $\mathcal{F}$ is a family of functions from $U$ to $\mathbb{R}$. We say that $\mathcal{F}$ is pointwise bounded on a subset $S\subseteq U$, if there exists some $M>0$ so that $f(x)<M_x$ for any $f\in\mathcal{F}$ and $x\in S$.
(Or, $\| f \|_U\leq M$ for the sup-norm).
## Uniformly Equicontinous
Let $(E,d)$ be a [[Metric Spaces|Metric Space]], and $U\subseteq E$. $\mathcal{F}$ is a family of functions from $U$ to $\mathbb{R}$. $\mathcal{F}$ is uniformly equicontinuous if, for every $\varepsilon>0,\exists\delta>0$: for any $f\in\mathcal{F}$,
$$
|x-y|<\delta\implies |f(x)-f(y)|<\varepsilon
$$
