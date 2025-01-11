---
tags:
  - DiffEqns
---
Let $f(t)$ be defined for $t>0$, and let $s \in \mathbb{R}$ be a real.
The *Laplace Transform* of $f$ is denoted and defined by:
$$\mathcal{L}\{ f(t) \}=\int_{0}^{\infty} e^{-st}f(t) \, dt$$
for all $s$ in which the improper integral exists. $\mathcal{L}\{ f(t) \}$ is a function of $s$, often denoted by $\mathcal{L}\{ f(t) \}= F(s)$.
## Properties
- Linearity: $\mathcal{L}\{  c_{1}f_{1}(t)+c_{2}f_{2}(t)\}= c_{1}\mathcal{L}\{ f_{1}(t)\}+ c_{2}\mathcal{L}\{f_{2}(t) \}$
## Inverse Laplace Transform
If $\mathcal{L}\{ f(t) \}=F(s)$, then we call $f(t)$ the *Inverse Laplace Transform* of $F(s)$ and write $\mathcal{L}^{-1}\{ F(s) \}=f(t)$
## Shift Formulas
### Shift Formula 1
If $\mathcal{L}\{  f(t)\}=F(s)$, then $\mathcal{L}\{ e^{at}f(t) \}=F(s-a)$, also written as:
$$\mathcal{L}\{ e^{at}f(t) \}=\mathcal{L}\{f(t)\}|_{s\to s-a}$$
### Shift Formula 2
$$\mathcal{L}\{ U_a(t)g(t) \}=e^{-as}\mathcal{L}\{ g(t+a) \}$$
Where $U_a(t)$ is the [[Unit Step Function]]. Again, we can write this as: 
$$\mathcal{L}\{ U_a(t)g(t) \}=e^{-as}\mathcal{L}\{ g(t) |_{t\to t+a}\}$$
## Differentiation Formulas
### Differentiation 1
Postponed
### Differentiation 2
If $\mathcal{L}\{ f(t) \}=F(s)$ then:
$$\mathcal{L}\{  t^{n}f(t)\}=(-1)^{n}\frac{d^{n}}{ds^{n}}\left( F(s) \right)$$
## Laplace Table
$$\begin{align}
\mathcal{L}\{ 1 \}&=\frac{1}{s}\\
\mathcal{L}\{ t^{n} \}&=\frac{n!}{s^{n+1}}\\
\mathcal{L}\{ e^{at} \}&=\frac{1}{s-a}, \quad s>a \\
\mathcal{L}\{ \sin at \}&=\frac{a}{s^{2}+a^{2}} \\
\mathcal{L}\{ \cos at \}&=\frac{s}{s^{2}+a^{2}}\\
\mathcal{L}\{ \sinh at \}&=\frac{a}{s^{2}-a^{2}}\\
\mathcal{L}\{ \cosh at \}&=\frac{s}{s^{2}-a^{2}}\\
\mathcal{L}\{ U_a(t) \}&=\frac{e^{-as}}{s}
\end{align}
$$