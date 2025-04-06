---
aliases:
  - Functionals
  - Dual Basis
---
Let $V$ be a [[Vector Spaces|Vector Space]], not necessarily [[Vector Spaces|Finite Dimensional]]. The set of linear maps $V^{*}=\mathcal{L}(V,\mathbb{C})$ is called the dual to $V$. This forms its own vector space. [[Linear Operators]] in this space are called [[Dual Space|Functionals]].
## Theorem
If $V$ is finite-dimensional, then $\dim V=\dim V^{*}$. Otherwise the cardinality of $V^{*}$ may be much larger than $V$.
## Dual Basis
Let $\{ b_{1},\dots,b_n \}$ a basis for $V$. Define the functionals: $\delta_i(b_j)=\delta_{ij}$. These form a basis for $V^{*}$.
## Double Dual
The (algebraic) double dual of $V$ is $V^{**}=(V^{*})^{*}$. If $\dim V=n$, then $\dim V^{*}=n$, and $\dim V^{**}=n$.
### Evaluation map
Given each $v\in V$, we can define $E_v:V^{*}\to\mathbb{C}$ by 
$$
E_v(f)=f(v)
$$
This is linear and $E_v\in V^{**}$.
Define $\Phi:V\to V^{**}$, $\Phi(v)=E_v$.
## Theorem
$\Phi:V\to V^{* *}$ given above is an [[Group Homomorphism and Isomorphism|Isomorphism]]. 