---
aliases:
  - Galois Group
  - Galois Field
  - Separable Polynomial
---
## Galois Field

[[Finite Fields]] are sometimes called Galois Fields.
## Galois Group
 If $E\supseteq F$ are fields, Galois theory is concerned with the automorphisms $\sigma{:}E\to E$ that fix $F$ in the sense that $\sigma(a)=a$ for all $a\in F.$ In this case, $\sigma$ is called an $F$-automorphism $E$.
 The set of all these automorphisms on a particular field form a group; $gal(E:F)=\{ \sigma:E\to E| \sigma \text{ is an automorphism},  \forall a\in F,\sigma(a)=a \}$
### Examples
$gal(\mathbb{C}:\mathbb{R})$ must have $\sigma(x)=x$ for real $x$. Then $\sigma(a+bi)=\sigma(a)+\sigma(i)b$. But $\sigma(i^{2})=\sigma(i)\sigma(i)=-1\implies\sigma(i)=\pm i$. So $\sigma$ is determined entirely by where we send $i$ and, having order $2$, $gal(\mathbb{C}:\mathbb{R})=\mathbb{Z}_{2}$.
### Finding Galois Groups
Galois groups must be characterized by elements. Then, by counting elements we can partly characterize the group. If the order of the group does not identify the group, we must rely on other composition rules to characterize the group. (See [[Groups of order n]])
## Permuting Roots (Fundamental Theorem of Galois Theory)
### Lemma
If $u\in E\supseteq F$ and $\sigma \in gal(E:F)$, then for any $f(x)\in F[x]$ with $f(u)=0$, $\sigma(u)$ is also a root of $f$.
### Statement
If $F(u)/F$ is a simple extension, $u$ is algebraic over $F$ with minimal polynomial $m(x)$, and if $u=u_{1},u_{2},\dots,u_{n}$ are all the distinct roots of $m$ in $F[x]$, then $gal(F(u):F)=\{ id,\sigma_{1},\dots,\sigma_{n} \}$ where $\sigma_{i}(u)=u_{i}$.
### Generalization (All finite extensions)
If $E\supseteq F$ is a finite extension with $E=F(u_{1},\dots u_{n})$, where $u_{i}$ is algebraic over $f$ with minimal monic polynomial $m_{i}(x)$. If $\sigma \in gal(E:F)$:
- $\sigma$ is completely determined by each $\sigma(u_{1}),\dots,\sigma(u_{n})$
- $\sigma(u_{i})$ is a root of $m_{i}(x)$. 
In particular, $gal(E:F)$ is finite when $[E:F]$ is finite.
### Theorem
Let $\sigma:F\to \bar{F}$ be a field isomorphism. Let $f(x)\in F[x]$ be separable.
If $E$ is a [[Splitting Fields|Splitting Field]]for $f(x)$ over $F$ and $\bar{E}$ is a splitting field for $\sigma(f(x))=f^\sigma(x)$, then there are exactly $[E:F]$ isomorphisms $\hat{\sigma}:E\to \bar{E}$ extending $\sigma.$
$$
\begin{CD}
E @>\hat{\sigma}>> \bar{E} \\
@|         @| \\
F(u) @>\hat{\sigma}>> K&=\hat{\sigma}(\bar{F}(u)) \\
@|         @| \\
F @>\sigma>\cong> \bar{F} \\
\end{CD}
$$
#### Corollary
If $E$ is a splitting field of a separable polynomial $f(x)\in F[x]$ then  $|gal(E:F)|=[E:F]$