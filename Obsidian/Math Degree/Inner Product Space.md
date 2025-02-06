---
aliases:
  - Inner Product
  - Inner Product Spaces
---
An inner product space is a [[Vector Spaces|Vector Space]] $V$ over $\mathbb{C}$ or $\mathbb{R}$ along with a binary operation $\left< \cdot,\cdot \right>$ or $(\cdot,\cdot):V\times V\to F$, satisfying the following properties for $x,y,z\in V$ and $a,b$ scalars:
- $(x,y)=\overline{(y,x)}$, conjugate symmetry
- $(ax+by,z)=a(x,z)+b(y,z)$, linearity
	- $(z,ax+by)=\bar{a}(z,x)+\bar{b}(z,y)$
- $(x,x)\geq 0$, non-negativity (this ordering makes sense since $(x,x)\in\mathbb{R}$ necessarily)
- $(x,x)=0\iff x=0$, non-degeneracy
This operation is called an inner product.
## Other Properties
- $x=0\iff(x,y)=0\forall y\in V$.
## Examples
- $\mathbb{R}^{n}$ is an inner product space with the typical [[Dot Product]]
- $\mathbb{C}^{n}$ is an inner product space with $\left< \vec{z},\vec{w} \right>=\sum\limits_{j=1 }^{n}z_j\bar{w}_j$.
- $\mathbb{M}_{mn}(\mathbb{C})$ is an inner product space with $\left< A,B \right>= \mathrm{Tr}(AB^{*})$
## Norm through inner product
Given an inner product space $(V,\left< \cdot,\cdot \right>)$, define $\left| v \right|=\sqrt{ \left< v,v \right> }$.
### Cauchy-Schwartz
For the space $(V,\left< \cdot,\cdot \right>)$, $|\left< v,w \right>|\leq|v||w|$.
