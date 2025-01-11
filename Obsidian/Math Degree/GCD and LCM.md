---
tags:
  - NumThry
---
The Greatest Common Divisor of two integers $a,b$ is the greatest $d$ so that $d|a,d|b$.

In general: 
- $\gcd(a,0)=a$
- $\gcd(a,1)=1$
- $\gcd(a,b)=\gcd(b,a)$
- $\gcd(ga,gb)=g\gcd(a,b)$

Simply, the greatest common divisor of two numbers can be found by checking all natural numbers up to $\min(a,b)$. However this is quite slow. The most effective way to solve for a greatest common divisor may be [[Euclid's Recursive Algorithm]].

## Diophantine Theorem
If $gcd(a,b)=d$, then there exist integers $x,y$ so that $ax+by=d$. These can be obtained by reversing [[Euclid's Recursive Algorithm]].

## The GCD and LCM
A useful identity with the [[Lowest Common Multiple]] exists. The $lcm$ of two integers $a,b\neq0$ can be given by: $$lcm(a,b)=\frac{gcd(a,b)}{ab}$$