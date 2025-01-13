---
aliases:
  - Inner Product
  - Inner Product Spaces
---
An inner product space is a [[Vector Spaces|Vector Space]] $V$ over $\mathbb{C}$ or $\mathbb{R}$ along with a binary operation $(\cdot,\cdot):V\times V\to F$, satisfying the following properties for $x,y,z\in V$ and $a,b$ scalars:
- $(x,y)=\overline{(y,x)}$, conjugate symmetry
- $(ax+by,z)=a(x,z)+b(y,z)$, linearity
	- $(z,ax+by)=\bar{a}(z,x)+\bar{b}(z,y)$
- $(x,x)\geq 0$, non-negativity
- $(x,x)=0\iff x=0$, non-degeneracy
This operation is called an inner product.
## Other Properties
- $x=0\iff(x,y)=0\forall y\in V$.