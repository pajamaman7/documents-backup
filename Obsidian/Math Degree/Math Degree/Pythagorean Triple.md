---
tags:
  - NumThry
---
A *Pythagorean Triple* $a,b,c\in\mathbb{Z}$ is a set of integers that satisfy $a^{2}+b^{2}=c^{2}$. If we have a triple of this form, we can associate it with a solution on the [[Unit Circle]] $\left( \frac{a}{c} \right)^{2}+\left( \frac{b}{c} \right)^{2}=1$
## Primitive Triples
A *Primitive Pythagorean Triple* is one where $(a,b,c)$ is a triple and $GCD(a,b,c)=1$. 

If we have a reduced rational solution to $\left( \frac{a}{c} \right)^{2}+\left( \frac{b}{d} \right)^{2}=1$, then $(a,b,c)$ is a primitive Pythagorean triple.
## Finding triples
As above, any triple $a^{2}+b^{2}=c^{2}$ has a rational solution on the [[Unit Circle]] $\left( \frac{a}{c} \right)^{2}+\left( \frac{b}{c} \right)^{2}=1$.

If we draw a line from the point $0,1$ with rational slope $m\in\mathbb{Q}$, $y=mx+1$, any point where it intersects the circle will be a rational solution to $x^{2}+y^{2}=1$.

Through some derivation, we can find that:
$$u=-\frac{2m^{2}}{1-m^{2}},\quad v=\frac{1-m^{2}}{1+m^{2}}$$
And if we are given some $u,v\in\mathbb{Q}$, we can find $$m=\frac{v-1}{u}$$
This implies that all solutions are given by our first formula for $u,v$.
## Properties of Triples
### Scaling
Let $(a,b,c)$ be a Pythagorean triple. Then for any constant $k$, $(ka,kb,kc)$ is also a Pythagorean triple