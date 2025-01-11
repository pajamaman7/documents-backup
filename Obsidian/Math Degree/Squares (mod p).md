---
tags:
  - NumThry
---
A *square root* of $a\pmod{m}$ is the solution(s) to $x^{2}\equiv a\pmod{m}$. We have strong techniques to solve for $x$ when $m$ is a prime exponent. 

## Roots of 1 $\pmod{p^{e}}$
Roots of $1$ are critical in order to solve for roots of any other number. We have a few cases.
1. $p^{e}=2$: If this is the case, we have only one root, $1$. 
2. $p^{e}$ is odd: If we have an odd modulus, there will be two roots, $\pm 1$.
3. $p^{e}$ is of the form $2^{e}$, with $e\geq 3$: In this case, there are four roots, $\pm 1$ and $p^{e-1}\pm 1$.
## Roots of $a$
$\zeta^{2}\equiv 1\pmod{p^{e}}$ and $x^{2}\equiv a\pmod{p^{e}}$ $\iff$ $(x\zeta)^{2}\equiv a\pmod{p^{e}}$.
## Lifting Squares 
### Odd primes
Let $p$ be an odd prime, and $x^{2}\equiv a \pmod{p^{e}}$. Let $k$ be such that $x^{2}=a+kp^{e}$ and let $b$ be the inverse for $2x\pmod{p^{e}}$. Finally set $z=x-bkp^{e}$. 
All this gives us $z^{2}\equiv a\pmod{p^{2e}}$.
### $p=2$
If $x^{2}\equiv a \pmod{ p^{e}}$, then either:
- $x^{2}\equiv a \pmod{ p^{e+1}}$.
- $(x+2^{e-1})^{2}\equiv a \pmod{ 2^{e+1}}$.
