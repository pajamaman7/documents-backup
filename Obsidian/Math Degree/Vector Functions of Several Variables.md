---
aliases: []
---
Let $E\subseteq \mathbb{R}^n$. A function $f:\mathbb{R}^n\to \mathbb{R}^p$ is a vector function of several variables. We may also write 
$$
f(x)=f(x_{1},\dots,x_n)=\begin{pmatrix}
y_{1}\\ \vdots \\ y_p 
\end{pmatrix}=\begin{pmatrix}
f_{1}(x)\\ \vdots \\ f_p(x)
\end{pmatrix}
$$
For [[Real Function of Several Variables]] $f_{1},\dots,f_p$.
## Continuity
Let $f:\mathbb{R}^n\to \mathbb{R}^m$. $f$ is continuous at $c$ if:
$\forall\varepsilon>0\exists\delta>0$, so that $\| x-c \|<\delta\implies \| f(x)-f(c) \|<\varepsilon$.
Thanks to the equivalence of norms in vector spaces, we typically use $\| x \|_\infty=\max \{ |x_{1}|,\dots,|x_n| \}$. This reduces $\| f(x)-f(c) \|<\varepsilon$ to $|f_{i}(x)-f_{i}(c)|<\varepsilon \forall 1\leq i \leq m$.
### Compact Sets
$f:\mathbb{R}^n\to \mathbb{R}^m$ is continuous in a closed and bounded set $E$, then:
- $f(E)$ is bounded and closed.
- $f$ is uniformly continuous on $E$.
### Linear Transformations
See [[Linear Operators|Linear Map]]. Any linear transformation from $\mathbb{R}^n\to\mathbb{R}^m$ is uniformly continuous, [[Limits and Continuity in Metric Spaces|Continuous]], and Lipschitz.
## Differentiation
See [[Jacobian]]