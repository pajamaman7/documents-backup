Let $$
\begin{CD}
[a,b) @>f>> \mathbb{R}
\end{CD}
$$
We say that $f$ is differentiable at $x \in[a,b]$ if
$$\lim_{ t \to x } \frac{f(t)-f(x)}{t-x}:=f'(x)$$
### Theorem
If $f:[a,b]\to \mathbb{R}$ and $x \in[a,b]$ is such that $f$ is continuous at $x$, then $f$ is differentiable at $x$.
CONTINUOUS $\implies$ DIFFERENTIABLE but the converse is not necessarily true...
### Theorem
Let $f$ as above, then:
$$
\begin{align}
(f+g)'(x)&=f'(x)+g'(x)\\ 
(fg)'(x)&=f'(x)g(x)+f(x)g'(x) \\
\left( \frac{f}{g} \right) '(x)&= \frac{f'(x)g(x)-f(x)g'(x)}{g^{2}(x)}\\
f(g(x))'&=f'(g(x))g'(x)
\end{align}
$$
See [[List of Derivatives]] for more.
## Increasing and Decreasing
Let $f$ be differentiable on $(a,b)$, and $x\in(a,b)$ arbitrary.Then
- $f(x)>0\implies$ $f$ is increasing
- $f(x)<0\implies$ $f$ is decreasing
- $f(x)=0\implies f$ constant on $(a,b)$ 
### Theorem
If $f$ is differentiable on $[a,b]$, and $f'(a)<\lambda<f'(b)$, then there exists some $c$ so that $f'(c)=\lambda$.