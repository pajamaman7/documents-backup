Given the [[DE]]:
$$a_{0}(x)y''+a_{1}(x)y'+a_{2}(x)y=0$$
Assume the DE has a regular, singular point at $x=x_{0}$. Then the DE has at least one non-trivial series solution of the form:
$$y=|x-x_{0}|^{r}\sum_{n=0}^{\infty}a_n(x-x_{0})^{n}$$
with $a_{0}\neq 0$, and $r\in\mathbb{C}$ is a constant to be determined. The solution $y$ is valid for all $x$ such that $0<|x-x_{0}|<R$ for some $R>0$.
### Comments and Assumptions
- $r$ can be determined from the indicial equation, whose roots $r_{1},r_{2}$ are called the exponents. It will be assumed that that $r_{1},r_{2}$ are real with $r_{1}\geq r_{2}$ (for math 387).
- We suppose that the DE has a regular singular point at $x_{0}=0$. If the DE has a regular singular point at $x_{0}\neq 0$, we make the change of independent variable $t=x-x_{0}$.
- The solution is valid when $0<|x-x_{0}|<R$. When splitting the absolute value we take $0<x-x_{0}<R$, and since we translate until $x_{0}=0$, this gives $0<x<R$ as our interval of validity.
Based on these assumptions we are given: 
$$y=\sum_{n=0}^{\infty}a_n\ x^{n+r}$$
## The Frobenius Method
Take the DE at the beginning of the section:
$$a_{0}(x)y''+a_{1}(x)y'+a_{2}(x)y=0$$
### Cases:
- If $r_{1}-r_{2}\not\in \mathbb{N}\cup \{ 0 \}$, the [[Differential Equations|DE]] has two linearly independent solutions:
$$y_{1}(x)=\sum_{n=0}^{\infty}a_nx^{n+r}\quad y_{2}(x)=\sum_{n=0}^{\infty}b_nx^{n+r}$$
    with $0<x<R$ and $R>0$.
- If $r_{1}=r_{2}=r$ then our DE still has two linearly independent solutions:
$$y_{1}(x)=\sum_{n=0}^{\infty}a_nx^{n+r}\quad y_{2}(x)=\sum_{n=0}^{\infty}b_nx^{n+r+1}+y_{1}(x)\ln x$$
    again with $0<x<R$ and $R>0$.
- If $r_{1}-r_{2}\in\mathbb{N}$ then the $DE$ has two linearly independent solutions:
$$y_{1}=\sum_{n=0}^{\infty}a_nx^{n+r_{1}}\quad y_{2}(x)=\sum_{n=0}^{\infty}b_nx^{n+r_{2}}+Cy_{1}(x)\ln x$$
    again with $0<x<R$ and $R>0$. $C\in\mathbb{R}$.
