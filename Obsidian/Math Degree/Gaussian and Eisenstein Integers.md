---
tags:
  - NumThry
  - Needs_Rewrite
---
Extensions of the [[Complex Numbers]]
## Gaussian Integers
The Gaussian Integers are given by the set 
$$\mathbb{Z}[i] = \{a+bi|a,b\in \mathbb{Z}\}.$$
### Divisibility
We say, for some $u,v\in\mathbb{Z}[i]$, $u|v\iff \exists z\in\mathbb{Z}[i]: zu=v$.
- If $u|v$, then $\lvert u \rvert\leq \lvert v \rvert$.
### Modulus
See [[Complex Numbers]].
The modulus of any $z\in\mathbb{Z}[i]$ is always greater than 0.
### Inverses/Units
If $u\in\mathbb{Z}[i]$ has an inverse, then there exists a $v\in\mathbb{Z}[i]$ so that $uv=1 (+0i)$.
$u$ will have an inverse $\iff$ $\lvert u \rvert=1$, or $u$ is on the unit circle. So $U(\mathbb{Z}[i])= \{ \pm 1,\pm i \}$.
Units divide every member of $\mathbb{Z}[i]$
## Eisenstein Integers
The Eisenstein Integers are given by the set 
$$\mathbb{Z}[\omega]= \{ a+b\omega: a,b\in\mathbb{Z} , \omega=e^{2\pi i/3}\}.$$
Note that $\omega$ is a cube root of $1$, and can be written $\omega^{3}=1$. $\omega$ also has the property that $\omega^{2}=\bar{\omega}$.
### Divisibility
We say, for some $u,v\in\mathbb{Z}[\omega]$, $u|v\iff \exists z\in\mathbb{Z}[\omega]: zu=v$.
Again, if $u|v$, then $\lvert u \rvert\leq \lvert v \rvert$.
### Modulus
The modulus of an Eisenstein integer is **Not** given by $a^{2}+b^{2}$. Instead we take:
$$\lvert a+b\omega \rvert=\sqrt{(a+b\omega)(a+b\bar{\omega})}=\sqrt{a^{2}-ab+b^{2}}$$
The modulus of any $z\in\mathbb{Z}[\omega]$ is always greater than 0.
### Inverses/Units
If $u\in\mathbb{Z}[\omega]$ has an inverse, there exists a $v\in\mathbb{Z}[\omega]$ so that $uv=1$.
Again, if $u$ has an inverse, then $\lvert u \rvert=1$. This means that the set of inverses $U(\mathbb{Z}[i])=\{ \pm 1,\pm \omega,  \pm \omega^{2}\}$.
Units divide every member of $\mathbb{Z}[\omega]$
## Division Algorithm and GCD
[[Euclid's Recursive Algorithm]] can be extended to both Gaussian and Eisenstein Integers.
### Gaussian
Statement:
- For $a,b \in\mathbb{Z}[i]$; with $b\neq 0$, there exists $q,r\in\mathbb{Z}[i]$ such that $a=bq+r$ and $0\leq |r|\leq|b|$.
Procedure:
- 
### Eisenstein
Statement:
- For $a,b \in\mathbb{Z}[\omega]$; with $b\neq 0$, there exists $q,r\in\mathbb{Z}[\omega]$ such that $a=bq+r$ and $0\leq |r|\leq|b|$.
### GCD
$d$ is said to be the greatest common divisor of $a,b\in\mathbb{Z}[i]\iff$:
1. $d|a$ and $d|b$
2. If $c|a$ and $c|b$ then $c|d$.
#### Other properties of GCD
- Consider $a,b,d\in\mathbb{Z}[i]$ so that $GCD(a,b)=d$. Then there exists $m,n\in\mathbb{Z}[i]$ so that $d=am+bn$.
- If $a|xy$ in $\mathbb{Z}[i]$ and $GCD(a,x)=u$ where $u$ is a unit in $\mathbb{Z}[i]$, then $a|y$.
## Primes
A number $p\in\mathbb{Z}[i]$ is called prime $\iff$
- $p$ is not a unit.
- If $p=uv$ for some $u,v\in\mathbb{Z}[i]$ then either $u$ or $v$ is a unit.
[[Euclid's Lemma]] also holds in this setting.
if $p$ is a prime, then $p|ab$ $\implies p|a \lor p|b$. The converse holds so long as $p$ is not a unit.
### Prime Factorization
Every Gaussian or Eisenstein integer can be written uniquely (up to order and units) as a product of Gaussian or Eisenstein primes.
### Other Properties
- If $q$ is a prime and $u$ is a unit, then $uq$ is also a prime.
- If $q$ is a prime, so is $\bar{q}$.