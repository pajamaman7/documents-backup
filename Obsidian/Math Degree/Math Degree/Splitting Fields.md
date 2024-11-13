---
aliases:
  - Kronecker's Theorem
  - Algebraic Closure
  - Algebraically Closed
tags:
  - Algebra
---
A Splitting Field of the polynomial $f$ over the [[Fields|Field]] $F$ is a field extension with:
- $E=F(u_{1},\dots,u_n), n=\deg f\geq 1$ 
- $f(x)=a(x-u_{1})\dots(x-u_n)$
A splitting field for $f$ always exists, is finite degree, and has $[E:F]\leq n!$
## Kronecker's Theorem
If $f(x)\in F[x]$ is non-constant, then there is a field extension $E$ of $F$ in which $f(x)$ has a root.
## Algebraically Closed
For a field $C$, the following are equivalent
- Every non constant polynomial in $C[x]$ has a root in $C$
- Every irreducible polynomial in $C[x]$ has degree $1$
- Every nonconstant polynomial in $C[x]$ splits into linear factors (in $C$).
- If $E\supseteq C$ is an algebraic extension, then $E=C$.
A field satisfying these conditions is called algebraically closed. If the field $C$ contains a subfield, $C$ is the *Algebraic Closure* of that field.
### Theorem
If $C$ is the algebraic closure of a field $F$, then 
$$
A=\{ u\in C| u \text{ is algebraic in } C\}
$$
is an algebraically closed field, and $A=C$.