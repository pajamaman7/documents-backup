---
aliases:
  - Quotient Topology
---
Given a set $X$ with a [[Topology]] $\mathcal{T}$, let $\sim$ be an equivalence relation on $X$. We define $X / \sim$ as the set of equivalence classes of $\sim$.  A topology is defined on $X / \sim$, where $U$ is open if and only if
$$
\bigcup\limits_{[x] \in U}^{}[x]\subseteq X
$$
is open in $X$.
## Universal Property
Let $f:X\to Y$ be a continuous function on topological spaces, and $\sim$ an equivalence relation on $X$. Then if $\pi:X\to X /\sim$ is the projection $\pi(x)=[x],$ there is a unique continuous function $\bar{f}:X /\sim\to Y$  satisfying $\bar{f}\pi=f$
## Quotient Map
If $\rho:X\to Y$ is [[Continuity|Continuous]] and [[Functions|Surjective]], with the additional condition that $\rho ^{-1}(U)$ open implies $U$ open, we say $\rho$ is a quotient map.