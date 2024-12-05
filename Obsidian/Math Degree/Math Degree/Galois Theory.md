---
aliases:
  - Galois Group
  - Galois Field
  - Separable Polynomial
  - Characters
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
## Character
Let $G$ be a [[Groups|Group]], $E$ a [[Fields|Field]]. Write $E^{*}$ to be the multiplicative group of $E$. A group [[Group Homomorphism and Isomorphism|Homomorphism]] $\sigma:G\to E^{*}$ is called a *Character* of $E$.
A set of characters $\{ \sigma_{1},\dots,\sigma_n \}$is called independent if given $u_{1},\dots,u_n\in E$, $u_{1}\sigma_{1}(g)+\dots+u_n\sigma_n(g)$ for all $g\in G$, $\iff u_{1}=\dots=u_n=0$.
### Lemma (Dedekind's Lemma)
Every finite set $\{ \sigma_{1},\dots,\sigma_n \}$ of distinct characters of a group $G$ in a field $E$ is independent.
#### Corollary 
Any finite set of field automorphisms (any Galois group) is independent
## Theorem
Let $F\supseteq E$ be a finite extension. Let $G=gal(E:F)$. Then $|G|\leq[E:F]$.
## Theorem (Dedekind-Artin)
Let $G\leq Aut(E)$. Then $[E:E_G]=|G|$ is finite when $E_G$ is the set of all fixed points in $E$.
## Main Theorem of Galois Theory
### Preamble
That is, $gal(E:K)$is a subgroup of  $gal(E:F)$.
As well, if $H\leq gal(E:F)$, then $E_H$ (the set of fixed points in $E$) is an intermediate field between $E$ and $F$.
### Lemma
Let $E\supseteq F$ be a field extension and $G=gal(E:F)$. Let $K_{1},K_{2}$ be intermediate extensions and $H_{1},H_{2}\leq G$.
- If $K_{1}\subseteq K_{2}$, then $gal(E:K_{2})\leq gal(E:K_{1})$.
- If $H_{1}\leq H_{2}$, then $E_{H_{2}}\subseteq E_{H_{1}}$.
- $K\subseteq E_{gal(E:K)}$ (Exercise what is this?)
- $H\leq gal(E:E_H)$ (Exercise what is this?)
- $gal(E:K)=gal(E:E_{gal(E:K)})$.
- $E_H=E_{gal(E:E_H)}$ 
These are all proven with the observations above.
### Stable Intermediates and Galois Extensions
- If $K$ is an intermediate extension of $F\subseteq E$, and $\sigma(K)=K$ for all $\sigma \in gal(E:F)$, then $K$ is called Stable
- If $F=E_{gal(E:F)}$ then the extension $E:F$ is Galois
### Statement
Let $F\subseteq E$ be a finite Galois extension. Let $K,K_{1}$ be intermediate fields and $H,H_{1}$ subgroups of the Galois group.
Write $\varphi:$
Write $\psi:$
- $\varphi,\psi$ are inverse and order reversing
- If $K_{1}\subseteq K$, then $[K:K_{1}]=|gal(E:K_{1}):gal(E:K)$
- If $H_{1}\leq H$ then $H:H_{1}=[E_{H_{1}}:E_H]$
- $E / K$ is Galois
- $K / F$ is Galois $\iff$ $K$ is stable in $E /F \iff gal(E:K)\trianglelefteq G$

