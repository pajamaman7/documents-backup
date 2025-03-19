---
aliases:
  - Local Invertibility Theorem
---
## Single Variable
Let $f: \mathbb{R}\to\mathbb{R}$. If $f$ is invertible on an interval $I$ and differentiable with $f'(x)\neq0$ on $I$, then $f^{-1}$ is differentiable on $f(I)$ and:
$$(f^{-1})'f(x)=\frac{1}{f'(x)}$$
## Multivariable
Let $f:\mathbb{R}^n\to \mathbb{R}^n$ be in $C^{1}(\Omega)$ for some $\Omega \subseteq \mathbb{R}^n$. Let $a\in\Omega$ be such that $df(a)$ is invertible. Then:
- $\exists U\subseteq\Omega$ open that contains $a$ so that $f$ is [[One-to-One]] in $U$ and $V=f(U)$ is open.
- The inverse $g$ of $f$ belongs to $C^{1}(V)$, and $Jg(f(a))Jf(a)=I$