---
aliases:
  - Span
  - Basis
  - Linear independence
  - Linearly independent
  - Finite Dimensional
  - Infinite Dimensional
  - Finite Dimension
  - Infinite Dimension
  - Subspace
  - Spanning Set
  - Spans
  - Vector Space
---
A vector space $V$ is a set $V$ equipped with operations $+,\cdot$ ($V$ is an abelian group under $+$) and an associated [[Fields|Field]] $F$ and the following axioms for vectors $u,v$ and scalars $a,b\in F$:
- $a(u+v)=au+av$
- $(a+b)v=av+bv$
- $a(bv)=(ab)v$
- $1v=v$
Other properties can be derived from this:
- $av=0\iff a=0$ or $v=0$ 
- $-1v=-v$
- $(-a)v=a(-v)$
## Subspaces
$U\subseteq V$ is a subspace of $V$ if and only if $U$ is a subspace under the same operations as $V$.
### Subspace test
A nonempty subset $U\subseteq V$ is subspace of $V$ iff $U$ is closed under addition and scalar multiplication.
## Span
Let $v_{1},v_{2},\dots ,v_i \in V$. Then $span\{ v_{1},\dots,v_i \}$ is the smallest subspace of $V$ containing $v_{1},\dots,v_i$. In fact:
$$span\{ v_{1},\dots,v_i \}=\{ a_{1}v_{1}+\dots+a_iv_i:a_{1},\dots,a_i\in F \}$$
A vector space is called finite dimensional when there is a finite set that spans it.
## Linear independence
A set of vectors $A=\{ v_{1},\dots v_i \}$ is said to be linearly independent if any linear combination of the elements of $A$ is trivial.
## Basis
A set $B\subseteq V$ is called a basis if it is linearly independent and spans $V$.
We say that $|B|$ is the dimension of $V$. Every vector space has a basis, and its size is unique.
If $v\in V$, $v$ has a unique representation as a linear combination of elements in $B$.
### Fundamental Theorem of Vector Spaces/Invariance
Dimension is well defined, and if $B$ is a basis, and $\{  u_{1},\dots,u_m\}\leq U$ is linearly independent, then $|U|\leq|V|$ 
### Case of finite fields
If $|F|=q=p^{n}$, then any $n-$dimensional vector space has exactly $q^n$ elements.
### Trick question
What is the dimension of $\mathbb{C}$? Over $\mathbb{R}$, it's 2. Over $\mathbb{C}$, it's 1. We denote $\dim_FV$ as the dimension of $V$ over $F$.