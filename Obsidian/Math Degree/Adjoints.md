---
aliases:
  - Isometry
  - Unitary
  - Self-Adjoint
  - Hermitian
---
## For $M_{mn}(\mathbb{C})$
We define $A^{*}=[\overline{a_{ji}}]$ for $A=[a_{ij}]$
For the [[Inner Product Space|Inner Product]] $\left< x,y \right>= \sum\limits_{j=1}^{n}x_j\bar{y}_j$, we may now write this as $y^{*}x$.
### With an inner product
And, $\left< Ax,y \right>=\left< x,A^{*}y \right>$.
## For general inner product spaces
Suppose $V,W$ are [[Vector Spaces|Finite Dimensional]] [[Inner Product Space|Inner Product Spaces]]. For any $T:V\to W$, there is a unique [[Linear Operators|Linear Map]] $T^{*}:W\to V$, satisfying 
$$ \left< Tv,w \right> _W=\left< v,T^{*}w \right> _V $$
### Properties on kernel and image
Let $T:V\to W$. Then:
- The map $T\mapsto T^{*}$ is a conjugate linear map:
	- $(aT)^{*}=\bar{a}T^{*}$
	- $(T+S)^{*}=T^{*}+S^{*}$
- $(ST)^{*}=T^{*}S^{*}$
- ${T^{*}}^{*}=T$
- $\ker T^{*}=(ran T)^\perp$
- $ran T^{*}=(\ker T)^\perp$
- $\ker T^{*}=(ran T^{*})^\perp$
- $ran T=(\ker T^{*})^\perp$
- $\ker T= \ker T^{*}T$
- $rank T =rank T^{*}T$
- If $\ker T=\{ 0 \},$ $T$ is left invertible
- If $ran T=W$, $T$ is right invertible
## Isometry
An isometry is a linear transformation $U:V\to W$ that preserves the [[norm]]; $\| Uv \|_W=\| v \|_V$
A operator is an isometry if and only if we have $TT^{*}=I$
### Polarization Identity
$$
\left< v_{1},v_{2} \right> =\frac{1}{4}\left( \| v_{1}+v_{2} \| ^{2}-\| v_{1}-v_{2} \| ^{2}+i\| v_{1}+iv_{2} \| ^{2}-i\| v_{1}-iv_{2} \| ^{2} \right) 
$$
### IAAAP Proposition
Isometries preserve angles; If $U:V\to W$ is an isometry, 
$$ \left< Uv_{1},Uv_{2} \right> =\left< v_{1},v_{2} \right>  $$
The converse to this is also true.
## Unitary
An isometry $U:V\to W$ is called unitary if $U$ is invertible.
All isometries are [[One-to-One|Injective]] 
### TFAE
For an isometry $U:V\to W$, TFAE:
- $\dim V=\dim W$
- $U$ is unitary
- $U^{*}U=I$
### Properties
- If $U$ is an isometry and $\{ b_{1},\dots,b_n \}$ is orthogonal in $V$, then $\{ Ub_{1},\dots,Ub_m \}$ is orthogonal in $W$
- The composition of isometries is an isometry
- If $U$ is an isometry and $\beta$ a basis for $V$, then the columns of the [[Matrix Representations of Linear Maps]] for $U$ form an orthogonal set.
- If $U$ is unitary from $V\to V$, then the rows and columns of $[U]_\beta$ each form an orthonormal basis for $V$.
- If $U$ is unitary, then $\det U=1$.
- If $\lambda \in\sigma(U)$, then $|\lambda|=1$.
### Unitarily Equivalent
We say $T,S:V\to V$ are unitarily equivalent if there exists some unitary $U:V\to V$ so that $U^{*}TU=S$. We write $T\sim_U S$ and claim this is an [[Relation|Equivalence Relation]]. 
#### Properties
If $A$ is unitarily equivalent to $B$, 
- $tr(A)=tr(B)$.
- $tr(A^*A)=tr(B^*B)$ Unitary equivalence is isometric w.r.t the trace norm on $M_N(\mathbb{C})$
### Unitarily Diagonalizable
$T$ is unitarily diagonalizable if and only if $T\sim_UD$ for some diagonal $D$.
#### Properties
- $T$ is unitarily diagonalizable iff $T$ has an orthonormal basis of eigenvectors.
- If $T$ is unitarily diagonalizable, and $\lambda,\mu \in\sigma(T)$ distinct, then $\ker(\lambda I-T)\perp \ker(\mu I-T)$.
## Hermitian/Self-Adjoint
We call a matrix $T:V\to V$ self-adjoint or hermitian if $T=T^{*}$
### Properties
For a self-adjoint $A$
- $\sigma(A)\subseteq \mathbb{R}$
- If $\lambda\neq\mu \in\sigma(A),$ then $\ker(A-\lambda I)\perp \ker(A-\mu I)$.
- $(\ker A)^\perp=ran\,A$, or $V=\ker A\oplus ran \,A$
- Self-adjoints span the space of linear maps from $V\to V$.1
### Examples
- $A+A^{*}$ is self adjoint
- $AA^{*}, A^{*}A$ is self adjoint
- $D=\text{diag }\{ \lambda_{1},\dots,\lambda_n \}$ is self-adjoint $\iff\lambda_j\in\mathbb{R}$.
- If $A$ is unitarily diagonalizable, then $A=A^{*}$ if and only if $\sigma(A)\subseteq \mathbb{R}$
- Any orthogonal [[Orthogonality|Projection]] has $P=P^{2}=P^{*}$