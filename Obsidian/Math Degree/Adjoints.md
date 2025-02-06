---
aliases:
  - Isometry
  - Unitary
---
## For $M_{mn}(\mathbb{C})$
We define $A^{*}=[\overline{a_{ji}}]$ for $A=[a_{ij}]$
For the [[Inner Product Space|Inner Product]] $\left< x,y \right>= \sum\limits_{j=1}^{n}x_j\bar{y}_j$, we may now write this as $y^{*}x$.
### With an inner product
And, $\left< Ax,y \right>=\left< x,A^{*}y \right>$.
## For general inner product spaces
Suppose $V,W$ are [[Vector Spaces|Finite Dimensional]] [[Inner Product Space|Inner Product Spaces]]. For any $T:V\to W$, there is a unique [[Linear Operators|Linear Map]] $T^{*}:W\to V$, satisfying 
$$ \left< Tv,w \right> _W=\left< v,T^{*}w \right> _V $$
### Properties
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
## Unitary Operator
A unitary operator is one with $TT^{*}=I$
## Isometry
An isometry is a linear transformation $U:V\to W$that preserves the [[norm]]; $\| Uv \|_W=\| v \|_V$
### Polarization Identity
$$
\left< v_{1},v_{2} \right> =\frac{1}{4}\left( \| v_{1}+v_{2} \| ^{2}-\| v_{1}-v_{2} \| ^{2}+i\| v_{1}+iv_{2} \| ^{2}-i\| v_{1}-iv_{2} \| ^{2} \right) 
$$
### IAAAP Proposition
Isometries preserve angles; If $U:V\to W$ is an isometry, 
$$ \left< Uv_{1},Uv_{2} \right> =\left< v_{1},v_{2} \right>  $$
The converse to this is also true.