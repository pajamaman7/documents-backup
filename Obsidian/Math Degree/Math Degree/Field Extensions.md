---
aliases:
  - Algebraic Extension
  - Field Extension
  - Algebraic Extensions
---
If $F\subseteq E$ are fields and $F$ is a subring of $E$, we say $E$ is an extension of $F$.
In fact, $E$ is a $F$-[[Vector Spaces|Vector Space]].
## Finite extension
If $\dim_F E=n$, finite, we say $\dim_F E=[E:F]$
### Theorem
Let $F\subseteq E$ be a field extension. Let $u\in E$ and $[E:F]=n$. Then there exists a polynomial $f(x)\in F[x]$ with $\deg f\leq n$ and $f(u)=0$
### Characterization
$E\supseteq F$ is finite $\iff E= F(u_{1},\dots,u_n)$ with each $u_i$ algebraic over $F$.
### Multiplication Theorem
Let $F\subseteq E\subseteq K$ be finite field extension. Then $[E:F]$ is finite if and only if $[K:E]$ and $[E:F]$ are finite. In this case $[K:F]=[K:E][E:F]$. This is not too different from [[Lagrange's Theorem]].
## Algebraic Extension
If $F\subseteq E$, an element $u\in E$ is algebraic if $f(u)=0$ for some polynomial $f(x)\in F[x]$. Otherwise, $u$ is transcendental.
The extension $F\subseteq E$ is called algebraic if every $u\in E$ is algebraic.
### Theorems
- $e,\pi$ are transcendental in $\mathbb{Q}$ over $\mathbb{C}$ and $\mathbb{R}$.
### Minimal Polynomial
Let $m(x)$ be a monic polynomial of minimal degree and $u\in E$ be algebraic over $F$, where $m(u)=0$. Then if:
   - $m(x)$ is irreducible
   - If $f(x)\in F[x]$, $u$ is a root of $f$ $\iff m|f$
   - $m$ is uniquely determined by $u$.
We call $m$ the minimal polynomial of $u$, and say that the degree of $m$ is the degree of $u$.
### Eisenstein's Criterion
$f(x)=a_{0}+a_{1}x+\dots+a_nx^{n}$ is a minimal polynomial in $\mathbb{Z}[x]$ with $n\geq1, a_{n}\neq 0$. If there exists a prime $p \in \mathbb{Z}$ where:
- For $i=0,\dots n-1$, $p|a_i$
- $p\not\mid a_n$
- $p^{2}\not\mid a_{0}$
Then $f$ is irreducible, not only over $\mathbb{Z}[x]$ but also $\mathbb{Q}[x]$.
## Generated subfields of E over F 
Let $F\subseteq E$ and choose $u_{1},\dots,u_n\in E$. Define the field extension $F(u_{1},\dots,u_n)= \bigcap_{K}\{ K\supseteq F: K \text{ is a subfield of }E \text{ containing }u_{1},\dots u_n \}$
This is the smallest field contained in $E$ which contains both $F$ and $u_{1},\dots,u_n$.
### Lemma
Let $u_{1},\dots,u_n\in E$ .Then for $1\leq k\leq n,$
$$F(u_{1},\dots,u_n)=F(u_{1},\dots,u_k)(u_{k+1},\dots,u_n)$$
### Theorem 
Let $u\in E$ be algebraic over $F$ of degree $n$, with minimal polynomial $m$ Then:
- $F(u)=\{ a_{0}+a_{1}u+a_{k-q}u^{k-1}|a_i \in F, k\geq 0 \}=\{ f(u)|f(x)\in F[x] \}$
- $\{ 1,u,\dots,u^{n-1} \}$ is an $F$-basis of $F[u]$, so $[F(u):F]=n$.
- As a ring, $F[u]\cong F[x] / \left< m(x) \right>$. 