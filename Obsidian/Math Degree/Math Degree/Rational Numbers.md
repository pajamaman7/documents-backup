---
tags:
  - NumThry
  - Algebra
---
The set of all *Rational Numbers*, $\mathbb{Q}$ is the set of all numbers $q=\frac{a}{b}$ with $a,b\in\mathbb{Z}$ and $b\neq 0$.
See also: [[Irrational Numbers]]
## Reduced Rational Numbers
Considering the set of *Reduced Rational numbers* (rationals in lowest terms), we add the additional stipulation: $b>0$ and $GCD(a,b)=1$. 
For any $\frac{a}{b}\in\mathbb{Q}$, there exists $\frac{m}{n}\in\mathbb{Q}$ so that $\frac{m}{n}$ is reduced. This reduced form is unique.
To obtain these, we can simply take:
$$m=\frac{a}{GCD(a,b)}\quad n=\frac{b}{GCD(a,b)}$$
## Prime Factorization in $\mathbb{Q}$
Let $r=\frac{m}{n}\in\mathbb{Q}$ be a reduced rational number:
Then the prime factorization of $r$ can be written as:
$$r=p_{1}^{e_{1}}p_{2}^{e_{2}}\dots p_m^{e_m}$$
With all $e_i\in\mathbb{Z}^{*}$.
## Rational Root Theorem
Consider the polynomial $f(x)=c_nx^{n}+c_{n-1}x^{n-1}\dots c_{1}x+c_{0}$ with all $c\in\mathbb{Z}$.
If $\frac{a}{b}$ is a reduced rational root of the polynomial, then:
- $b|c_n$
- $a|c_{0}$
If $f$ is monic (the leading coefficient is 1); then any rational root will be an integer.