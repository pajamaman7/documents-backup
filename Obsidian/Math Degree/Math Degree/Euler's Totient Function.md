---
tags:
  - NumThry
---
Euler's Totient function $\phi(n)$ denotes the number of natural numbers $a$ up to $n$ so that $GCD(a,n)=1$.
Let $n=p_{1}^{\alpha_{1}}p_{2}^{\alpha_{2}}\dots p_n^{\alpha_n}$. Since $\phi$ is a [[Multiplicative Functions|Multiplicative Function]], we can see:
$$\phi(n)=\phi(p_{1}^{\alpha_{1}})\phi(p_{2}^{\alpha_{2}})\dots \phi(p_n^{\alpha_n})$$
## Properties
- For a prime $p$, we say that $\phi(p)=p-1$.
- $\phi$ is also multiplicative.
- In relation to [[U(n)]], we can write that $\phi(n)=|U(n)|$.
- For a prime $p$ and exponent $e\in\mathbb{N}$, $\phi(p^{e})=p^{e}-p^{e-1}$. This allows us to decompose a number $n=p_{1}^{\alpha_{1}}p_{2}^{\alpha_{2}}\dots p_r^{\alpha_r}$ as:
  $$\phi(n)= (p_{1}^{e}-p_{1}^{e-1})(p_{2}^{e}-p_{2}^{e-1})\dots (p_r^{e}-p_r^{e-1}) =n\left( 1-\frac{1}{p_{1}} \right)\left(1-\frac{1}{p_{2}}\right)\dots \left( 1-\frac{1}{p_r} \right) $$
