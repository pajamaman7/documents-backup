---
aliases:
  - Orthogonal
  - Orthogonal Basis
  - Orthonormal
  - Orthonormal Basis
---
- Two vectors in an [[Inner Product Space]] are said to be orthogonal if $\left< v,w \right>=0$. We may write $v\perp w$.
- Two subspaces $V,W$ are orthogonal if $\left< v,w \right>=0$ for $v\in V,w\in W$. We may write $V\perp W$
- The set $\{ v_{1},\dots,v_n \}$ of nonzero vectors is orthogonal if $\left< v_i,v_j \right> =0$ for $i\neq j$. If all these vectors have $\| v_j \|=1,$ we say the system is orthogonal.
## Pythagoras
Let $V$ be an [[Inner Product Space]] with an orthogonal system  $\{ v_{1},\dots,v_m \}$. Then:
$$
\| \sum\limits_{j=1}^{m}\alpha_jv_j \| =\sum\limits_{j=1}^{m}|\alpha_j|^{2}\| v_j \| ^{2}
$$
## Properties
- An orthogonal set is linearly independent
- Suppose $v_{1},\dots,v_m$ is orthogonal to $S\subseteq V$. Then $span\{ v_1,\dots,v_m \}$ is orthogonal to $S$.
## Orthogonal Complement
Given $S\subseteq V$, the orthogonal complement of $S$ in $V$ is $S^{\perp}=\{ w\in V|\left< v,w \right>=0\forall v\in S \}$. The orthogonal complement of any subset $S \subseteq V$ is a [[Vector Spaces|Subspace]] of $V$.
### "Fourier" expansion of a vector
Let $V$ be a [[Vector Spaces|Finite Dimensional]] [[Inner Product Space]] with orthogonal basis $\{ b_{1},\dots,b_n \}$. Then for any $v\in V$, we have 
$$
v=\sum\limits_{j=1}^{n} \frac{\left< v,b_j \right> }{\| b_j \| ^{2}}b_j
$$
## Orthogonal Projections
Let $E$ be a subspace of a finite dimensional [[Inner Product Space]] $V$. For $v\in V$, we wish to define a new vector $P_Ev$ called the Orthogonal Projection of $v$ onto $E$, satisfying:
- $P_Ev\in E$
- $E\perp v-P_Ev$
- $P_Ev$ is unique
- $\| v-P_Ev \|=\inf_{w\in E}\| v-w \|$
### Definition
The projection above is given by $P_Ev=\sum\limits_{j=1}^{m} \frac{\left< v,v_j \right>}{\| v_j \|^{2}}v_j$