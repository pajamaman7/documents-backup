---
tags:
  - NumThry
aliases: Quadratic Reciprocity
---
Quadratic Residues can be considered the beginning of modern number theory.
## $x^{2}\equiv a\pmod{p}$
To find solutions to this equation, we consider $U(p)$, all equivalence classes$\pmod{p}$. Exactly half of these classes will be squares.
### Euler's Criteria for Squareness
Given a prime $p>2$, and $a\in\mathbb{Z}_p^{*}$. 
- $a$ is a square $\pmod{p}\iff a^{(p-1)/2}\equiv{1}\pmod{p}$.
- $a$ is not a square $\pmod{p}\iff a^{(p-1)/2}\equiv -1\pmod{p}$.
This can be written using the [[Legendre Symbol]].

## Reciprocity Laws
- $a^{2}\equiv-1\pmod{p}\iff p\equiv{1}\pmod{4}$ .
## Quadratic Reciprocity
IF $p,q$ are odd primes then:
$\left( \frac{p}{q} \right)\left( \frac{q}{p} \right)=(-1)^{(p-1)(q-1)/4}$