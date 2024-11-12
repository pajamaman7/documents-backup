---
aliases:
  - sigma(n)
tags:
  - NumThry
---
Arithmetic functions are functions $f:\mathbb{N}\to$ any set.
## $\sigma_0(n)$, divisors of n
The function $\sigma_0(n)$ will be:
$$\sigma_0(n)=\sum_{d|n}1$$
Considering a number $n$'s [[Prime Factorization]]:
$$n=p_1^{\alpha_1}\ldots p_{r}^{\alpha_r}$$
We obtain.
$$\sigma_0(n)=\prod_{i=1}^{r}(\alpha_i+1)$$
## $\sigma_k(n)$
Let the formula $\sigma_k(n)$ sum all the divisors of $n$, each raised to the $k$th power.
$$\sigma_k(n)=\sum_{d|n}d^{k}$$
Again in terms of the [[Prime Factorization]]:
$$\sigma_k(n)=\prod_{i=1}^{r}\frac{p_i^{k(\alpha_i+1)}-1}{p_i^k-1}$$
## Multiplicative Functions
[[Multiplicative Functions]]