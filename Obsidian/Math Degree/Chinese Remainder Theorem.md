---
tags:
  - NumThry
---
If $m,n$ are coprime integers, then a solution to:
$$\begin{align}
x\equiv a \pmod m\\
x\equiv b\pmod n
\end{align}$$
exists. The solution is unique [[Modular Arithmetic|modulo]] $mn$, and is given by:
$$x_{0}=sna+tmb$$
where $sn \equiv {1}\pmod{m}$, and $tm\equiv 1 \pmod{n}$. That is, $s$ is a multiplicative inverse for $n$ and $t$ is the inverse for $m$.
## As a Homomorphsim
We can think of this as a homomorphism:
$$f:\mathbb{Z}\to \mathbb{Z}_n\times \mathbb{Z}_n$$
$$f(x)=([x]_n,[x]_m)$$
CRT says that this map is onto (when $m,n$ are coprime).
## For a General Ring
Let $R$ be a commutative ring, and $I,J$ be ideals of $R$ such that $I+J=R$. Then
$$R /I\cup J \cong R /I \times R /J$$