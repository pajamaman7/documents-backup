---
aliases:
  - Domain
  - Domains
  - Integral Domain
  - Integral Domains
---
If in a [[Rings|Ring]] $R$, $ab=0$ implies $a=0$ or $b=0$, $R$ is called a domain. In other words, domains do not have zero divisors other than $0$. 
## Cancellation
In domains, cancellation laws hold. Hence if $ab=ac,$ $b=c$. Of course this holds for addition in any ring but in these cases it holds for multiplication as well.
## Integral Domains
Commutative domains are called Integral domains. Every [[Fields|Field]] is an integral domain, and every *finite* integral domain is a [[Fields|Field]].
### Embedding
Every integral domain "sits inside" a field (similarly to [[Cayley's Theorem]]). Precisely, every integral domain is isomorphic to a subring of a field.

$D\hookrightarrow F$ if $\exists$ a one-to-one ring homomorphism so that:
- $\phi:D\to F$
- $\phi:D\to \mathrm{Im}\phi$ is an isomorphism. (We know that $\mathrm{Im}\phi$ is a subring of $F$)
### $\mathbb{Z}_n$
Thanks to [[Euclid's Lemma]], $\mathbb{Z}_n$ is an integral domain $\iff$ $n$ is prime.