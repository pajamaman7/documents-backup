---
aliases:
  - Quotient Topology
---
Given a set $X$ with a [[Topology]] $\mathcal{T}$, let $X^{*}$ be a collection of disjoint subsets of $X$, and the union of all $A\in X^{*}$ equal $X$. Then let $\rho:X\to X^{*}$ be determined by sending any $x\in X$ to the subset in which it is contained. This is a surjection, and $X^{*}$ is called a Quotient space of $X$.
## Quotient Map
If $\rho:X\to Y$ is [[Continuity|Continuous]] and [[Functions|Surjective]], with the additional condition that $\rho ^{-1}(U)$ open implies $U$ open, we say $\rho$ is a quotient map.
## Quotient Topology
Let $X$ be a topological space, $A$ be a set, and $\rho:X\to A$ be a surjection. Then there is a unique topology induced by $\rho$, in which open sets $U$ in $A$ have $\rho ^{-1}(U)$ open in $X$.