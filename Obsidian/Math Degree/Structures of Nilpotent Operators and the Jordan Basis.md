---
aliases:
  - Jordan Basis
---
Suppose $N$ is a nilpotent operator. A set of generalized eigenvectors $\{ v_{1},\dots,v_k \}$ is called a cycle of length $k$ if:
$$
\begin{align}
Nv_{1}&=0 \\
Nv_{2}&=v_{1} \\
&\vdots \\
Nv_k&=v_{k-1}
\end{align}
$$
A basis of cycles is called a Jordan Basis for $N$.
## Theorem
Let $N:V\to V$ be nilpotent with $C_{1},\dots,C_m$ cycles of lengths $p_{1},\dots,p_m$. If the initial vectors in each $C_i$ (each in $\ker N$), are [[Vector Spaces|Linearly independent]], then $C_{1}\cup\dots\cup C_m$ is also linearly independent, and the cycles are disjoint.
## Existence of a Jordan Basis
For any $N:V\to V$, there is a Jordan Basis of cycles for $N$. The longest cycle length is the depth of $0$, also equal to the index of nilpotency.