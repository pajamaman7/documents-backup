---
aliases:
  - Measurable Space
  - Measurable
---
Given a set $X$, a collection of subsets $\mathfrak{R}$ is said to be an Algebra on $X$ if:
- $X\in\mathfrak{R}$
- For any $A\in\mathfrak{R}$, $A^{c}\in\mathfrak{R}$
- $A_n\in\mathfrak{R}, n=1,2,3,\dots\implies \bigcup_{n=1}^{\infty}A_n\in\mathfrak{R}$
If these properties hold, we call $X$ a measurable space, and members of $\mathfrak{R}$ are called measurable sets.
If the third property holds for [[Countable and Uncountable sets|Countable]] unions, we call $\mathfrak{R}$ a $\sigma$-algebra. If it only holds for finite unions, we call $\mathfrak{R}$ an algebra.
## Measurable function
If $X$ is a measurable space, and $Y$ is a [[Topology|Topological Space]], then a function $f:X\to Y$ is called measurable function if $f^{-1}(V)\in\mathfrak{R}$ for every $V$ open in $Y$.
## Measures and Topology
Let $X,Y,Z$ be [[Topology|Topological Spaces]], and $g:Y\to Z$ be [[Continuity|Continuous]]. Then:
- If $f:X\to Y$ is continuous, then $g\circ f$ is continuous
- If $f:X\to Y$ is measurable, then $g\circ f$ is measurable.
# Positive Measure
A positive measure is a function $\mu$ defined on a $\sigma$-algebra $\mathfrak{R}$, whose range is in $[0,\infty]$, and is countably additive; if $\{ A_i \}$ is a disjoint countable collection of members of $\mathfrak{R}$, then
$$\mu \left(  \bigcup\limits_{i=1 }^{\infty}\right)=\sum\limits_{i=1}^{\infty}\mu(A_i)$$
A measure space is a measurable space which has a positive measure defined on the $\sigma$-algebra of its measurable sets.
A complex measure is a complex-valued countably additive function defined on a $\sigma-$algebra