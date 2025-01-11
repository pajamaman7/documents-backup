---
aliases:
  - Subnormal Series
  - Composition Series
  - Solvable Series
  - Derived Series
---
A series of [[Groups|Subgroup]]s is a chain of subgroups:
$$G= G_{0}\geq\dots\geq G_n=\{ e \}$$.
## Subnormal Series
Let $G$ be a group. A subnormal series for $G$ is a chain of subgroups
$$
G\geq G_{1}\geq G_{2}\geq\dots G\geq G_n=\{ 1 \}
$$
Where $G_{i+1}\trianglelefteq G_i$.
## Composition Series
If $G$ is a group, a subnormal series
$$
G=G_{0}\trianglerighteq G_{1}\trianglerighteq\dots\trianglerighteq G_n=\{ e \}
$$
is called a composition series if $\frac{G_{i+1}}{G}$ is [[Simple Group|Simple]].
Every finite group has a composition series.
In fact, a group is simple iff its composition series has length 1.
### Examples
- The trivial series $\{ 1 \}\trianglelefteq G$
- Groups of order $2p$ have $\{ 1 \}\trianglelefteq H\trianglelefteq G$, where $H$ is a Sylow $p$-subgroup
- $\{ 1 \}\trianglelefteq H\trianglelefteq K\trianglelefteq A_{4}\trianglelefteq S_{4}$, where $K=\{ e,(12)(34),(13)(24),(14)(23) \}$, $H=\{ e,(12)(34) \}$
## Solvable Series
A composition series
$$
G=G_{0}\trianglerighteq G_{1}\trianglerighteq\dots\trianglerighteq G_n=\{ e \}
$$
Is solvable when each $G_i/G_{i+1}$ is abelian. Groups with this property are called [[Solvable Groups]].
### Construction for Solvable Series
Let $G$ be a group. The Derived Series for $G$ is constructed as follows:
Let $G'$ be the [[Commutator Subgroup]] of $G$, $G'=\{ [a,b]:a,b\in G \}$. Recall this is normal and the quotient is abelian. (In fact, $G_i\trianglelefteq G$ for any $i$, under this construction.)
Let $G=G_{0},G'=G_{1},G''=G_{2},\dots$. Then clearly the series:
$$
G_{0}\trianglerighteq G_{1}\trianglerighteq \dots\trianglerighteq G_n
$$
is a solvable series provided $G_n=\{ e \}$.
### Theorem for solvable groups
A group $G$ is solvable $\iff G_n=\{ e \}$ for some $n\geq 1$. 