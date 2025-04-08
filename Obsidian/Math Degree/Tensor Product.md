## $\mathbb{C}$-Vector Spaces 
Let $V,W$ be $\mathbb{C}-$[[Vector Spaces]], define $X$ to be the $\mathbb{C}$-vector space with $V\times W$ a basis for $X$. (This is a very large, infinite dimensional vector space). Let $R$ denote the subspace of $X$ spanned by all vectors of the form:
- $(v_{1}+v_{2},w)-(v_{1},w)-(v_{2},w)$
- $(v,w_{1}+w_{2})-(v,w_{1})-(v,w_{2})$
- $(av,w)-a(v,w)$
- $(v,bw)-b(v,w)$
Where $v_{1},v_{2},v\in V$, $w_{1},w_{2},w\in W$, and $a,b\in\mathbb{C}$.
We form the [[Quotient Space]], $V\otimes W:=\frac{X}{{R}}$. Define an elementary tensor (basic tensor) as $v\otimes w$, the image of $(v,w)$ in $\frac{X}{R}$. In $V\otimes W,$ the above list becomes:
- $(v_{1}+v_{2})\otimes w=v_{1}\otimes w+v_{2}\otimes w$
- $v\otimes (w_{1}+w_{2})=v\otimes w_{1}+v\otimes w_{2}$
- $a(v\otimes w)=(av)\otimes w=v\otimes(aw)$
We can say that the maps:
$$*\otimes w:V\to V\otimes W,\qquad v\otimes *:W\to V\otimes W$$
Are both linear.
### Observation
Generally, $v\otimes w+x\otimes y$ has no further simplification, unless $v=x\lor w=y$.
### Spanning set
$V\otimes W=\{ \text{finite linear combinations of basic tensors} \}$
### Finite Dimensional Case
If $V,W$ have bases $\{ b_{1},\dots,b_n \},\,\{ d_{1},\dots,d_m \}$, then $\dim V\otimes W=mn$, and the basis for $V\otimes W$ takes the form $\{ b_i\otimes b_j:1\leq i\leq n, 1\leq j\leq m \}$.
### Linear maps on $V\otimes W$
Let $A:V\to V$, $B:W\to W$ be [[Linear Operators|Linear Map]]s. We can define $A\otimes B$ on basic tensors:
$$
(A\otimes B)(v\otimes w)=Av\otimes Bw
$$
And if we extend by linearity, we have a linear transformation on the whole tensor product.
This raises a nontrivial exercise about [[Well-Defined|Well-definedness]].