---
aliases:
  - Measureable Space
  - Measurable
---
Given a set $X$, a collection of subsets $\mathfrak{R}$ is said to be an Algebra on $X$ if:
- $X\in\mathfrak{R}$
- For any $A\in\mathfrak{R}$, $A^{c}\in\mathfrak{R}$
- $A_n\in\mathfrak{R}, n=1,2,3,\dots\implies \bigcup_{n=1}^{\infty}A_n\in\mathfrak{R}$
If these properties hold, we call $X$ a measurable space, and members of $\mathfrak{R}$ are called measurable sets.
If $X$ is a measurable space, and $Y$ is a [[Topology|Topological Space]], then a function $f:X\to Y$ is called measurable function if $f^{-1}(V)\in\mathfrak{R}$ for every $V$ open in $Y$.
If the third property holds for [[Countable and Uncountable sets|Countable]] unions, we call $\mathfrak{R}$ a $\sigma$-algebra. If it only holds for finite unions, we call $\mathfrak{R}$ an algebra.
