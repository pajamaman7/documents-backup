---
tags:
  - Algebra
aliases:
  - First Isomorphism Theorem
  - Second Isomorphism Theorem
  - Third Isomorphism Theorem
---
## First Isomorphism Theorem
Let $f:G\to H$ be a homomorphism, and recall that $\ker f\trianglelefteq G$, and $\mathrm{Im}f\leq H$. Then:
$$G/ \ker f\cong\mathrm{Im}f$$
This holds true for a ring (with its [[Ideals]]).
### CRT Link
From [[Chinese Remainder Theorem]]:
Let $R$ be a commutative ring, and $I,J$ be ideals of $R$ such that $I+J=R$. Then
$$R /I\cup J \cong R /I \times R /J$$
## Second Isomorphism Theorem
Let $H$, $K$ be subgroups of $G$ and $K\trianglelefteq G$ 
- $HK$ is a normal subgroup of $G$, with $K\trianglelefteq HK$
- $H\cap K$ is a normal subgroup of $H$
$$
\frac{HK}{K}\cong \frac{H}{H\cap K}
$$
## Third Isomorphism Theorem
Let $K\leq H\leq G$ subgroups, and $K\trianglelefteq G$ and $H\trianglelefteq G$. Then $\frac{H}{K}\trianglelefteq \frac{G}{K}$
$$
\frac{G/K}{H /K}\cong \frac{G}{H}
$$