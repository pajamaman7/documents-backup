---
aliases:
  - Modular Congruence
  - Integer solutions for polynomial equations
  - Modular Equations
  - modulo
  - Modulus
  - modulus
  - Modulo
  - Modular Irreducibility Test
tags:
  - NumThry
---
Two integers $a,b$ are said to be congruent modulo $n$ if $n|a-b$. $n$ is called the modulus, and we write:
$$a\equiv b \pmod n$$
## Properties
The following rules hold true in modular arithmetic for some $x,y,a,b,d\in\mathbb{Z}$.
If:
$$a\equiv x\pmod d$$
And:
$$b\equiv y \pmod d$$
Then:
$$\begin{align*} 
a+b&\equiv x+y\pmod d\\
a-b&\equiv x-y\pmod d\\
ab&\equiv xy\pmod d\\
a^{m}&\equiv x^{m}\pmod d  \:\forall m\in\mathbb{Z},m\geq1
\end{align*}$$
Also note that *modular congruence* is an [[Equivalence Relation]].
## Existence of multiplicative inverse
Given $a\in\mathbb{Z}_n$, $\exists x\in \mathbb{Z}_n: ax\equiv 1 \pmod n\iff GCD(a,n)=1$. 
## Cancellation property
If $GCD(a,n)=1$ then $ax\equiv ay \pmod n\implies x\equiv y \pmod n$.

Further, $ax\equiv ay \implies x\equiv y \pmod p$ whenever $p\nmid a$.
## Modular Irreducibility Test
Let $E$ be an equation of polynomials in any number of variables. If $E$ has an integer solution, then for any modulo $m, (E\mod m)$ has a solution.
The contrapositive states that if $\exists m\in\mathbb{Z}$ such that $(E\mod m)$ does not have an integer solution, then $E$ does not have an integer solution.
The converse does not necessarily hold.