---
aliases:
  - Partial
  - Partial Derivative
  - Partials
---
Let $f:\mathbb{R}^{n}\to \mathbb{R}$ defined in an open $\Omega \subseteq \mathbb{R}^{n}$, and $c\in\Omega$.
The $i$-th partial derivative of $f$ is given by $$\partial_{x_j}f(c)=\lim\limits_{ t \to 0 } \frac{f(c+te_j)-f(c)}{t}$$ 
If this limit exists.
We may denote:
$$
\partial_{x_j}f(c)=\frac{\partial f}{\partial x_j}=f_{x_j}(c)
$$
If $\partial_{x_j}f(c)$ exists for every $c\in\Omega$ and $j=1,\dots,n$ we have $n$ functions called the first partial derivatives of $f$.
## Theorem
Let $f:\mathbb{R}^{n}\to\mathbb{R}$ defined in $\Omega \subseteq \mathbb{R}^{n}$ with $\frac{ \partial f }{ \partial x_{j} },\frac{ \partial f }{ \partial x_i },\frac{ \partial f }{ \partial x_{i}x_{j} }$ existing and continuous in $\Omega$. Then $\frac{ \partial f }{ \partial x_{j}x_{i} }$ exists and $\frac{ \partial f }{ \partial x_{j}x_{i} }=\frac{ \partial f }{ \partial x_{i}x_{j} }$
### Corollary
For further partials we may switch the order freely as well under the same conditions.
## Multivariable Chain Rule
The multivariable chain rule allows us to take partial derivatives of multivariable compositions of functions.
Suppose $z=f(x,y)$, $x=g(s,t)$ and $y=h(s,t)$. That is, $f$ is a function of $x$ and $y$, and $x,y$ are each functions of $s,t$.
Then:
$$\begin{align*}
\frac{\partial z}{\partial s} &= \frac{\partial f}{\partial x}\frac{\partial x}{\partial s}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial s}\\
\frac{\partial z}{\partial t} &= \frac{\partial f}{\partial x}\frac{\partial x}{\partial t}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial t}
\end{align*}$$
