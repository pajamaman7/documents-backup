---
aliases:
  - Normal Operator
---
$N:V\to V$, a [[Linear Operators|Linear Operator]] on a [[Vector Spaces|Finite Dimensional]] [[Inner Product Space]] is a normal operator if $N^{*}N=NN^{*}$.
## Properties
For a normal $N:V\to V$;
- $\| Nv \|=\| N^{*}v \|$
- $\ker N=\ker N^{*}=\text{ran }N^{\perp}$, or $V=\ker N \oplus \text{ran }N$
- If $\lambda \in\sigma(N)$, $\bar{\lambda}\in\sigma(N^{*})$, or $\sigma(N)=\overline{\sigma(N^{*})}$.
	- $\ker(N-\lambda I)=\ker(N^{*}-\bar{\lambda}I)$
- If $\lambda,\mu \in\sigma(N)$ are distinct, then $\ker(N-\lambda I)\perp \ker(N-\mu I)$.
## Classification of all normal operators
$N$ is normal if and only if $\| Nv \|=\| N^{*}v \|\forall v\in V$
## Examples
- [[Adjoints|Self-Adjoint]] operators, including [[Orthogonality|Orthogonal]] projections
- [[Adjoints|Unitary]] operators
- [[Diagonal]] operators, and unitarily diagonalizable operators.
