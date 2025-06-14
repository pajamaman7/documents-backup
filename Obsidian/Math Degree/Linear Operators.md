---
aliases:
  - Linear Transformation
  - Vector Space Homomorphism
  - Linear Operator
  - Linear Map
---
A mapping $T$ from [[Vector Spaces|Vector Spaces]] $V\to W$ is called a linear operator if and only if:
- $T(v_{1}+v_{2})=T(v_{1})+T(v_{2})$
- $T(av)=aT(v)$
## Image
The image (Range so as not to be confused with $\mathrm{Im}$, the imaginary part), $ran T=\{ Tv|v\in V \}$. This is a subspace of $W$
## Kernel
The kernel of a linear transformation $\ker T=\{ v|Tv=0 \}$ which is a subspace of $V$.
# Linear Operators in Real and Complex Spaces
## Isometries
The transformation $U:V\to W$ on normed spaces $W,V$ is an isometry if and only if $\left| Uv \right|=|v|$.
### Theorem
A Transformation $U$ is an isometry if and only if it preserves the [[Inner Product Space|Inner Product]]; $(x,y)=(Ux,Uy)$ for all $x,y\in V$.
### Inverse of an isometry
$U:V\to W$ is an isometry if and only if $U^{*}U=I$; $U^{*}=U^{-1}$; the conjugate transpose is the inverse of $U$.