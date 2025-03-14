---
aliases:
  - p-adic
  - p-adic integer
---
The $p-$adics are an extension of the [[Rational Numbers]], equipped with a [[Normed Vector Space|norm]] $|\cdot|_p$. $p$-adics take the form:
$$
s=\sum\limits_{i=k}^{\infty}a_ip^{i}=a_kp^{k}+a_{k+1}p^{k+1}+\dots
$$
For some fixed $p$. If $k\geq 0$, we may say that $s$ is a $p$-adic integer.
## Valuation
Let p be a [[Primes|Prime]]. Define the map $v_p : \mathbb{Z}^{*} \to \mathbb{Z}$ by $v_p(n) = e$, if $e$ is the highest exponent with which $p$ occurs in the factorization of $n$. For example $v_2(20) = 2, v_5(-20) = 1$ etc. We can extend this map to $v_p: \mathbb{Q}^* \to \mathbb{Z}$ by  $v_p(\frac{m}{n})=v_p(m)-v_p(n),$ where $m$ and $n$ are at lowest terms, i.e. $GCD(m, n) = 1$.
## Absolute Value
The p-adic absolute value $|\cdot|_p$ as follows : $|\cdot|_p : \mathbb{Q}^{*} \to \mathbb{R}$, given by, $|q|_p = p^{-v_p(q)}$.