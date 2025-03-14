Let $f:\mathbb{R}^n\to \mathbb{R}^m$ be defined in a neighborhood of $c\in\mathbb{R}^{n}$. We say that $f$ is differentiable at $x=c$ if there exists some $T\in L(\mathbb{R}^n,\mathbb{R}^m)$ such that:
$$
F(c+h)=f(c)+T(h)+\| h \|\alpha_c(h)
$$
where $\alpha_c:\mathbb{R}^n\to\mathbb{R}^m$ satisfies $\lim\limits_{h\to_{0}}\alpha_c(h)=0$. The linear transformation $T$ is called the differential of $f$ at $c$ and may be denoted $df_c$ or $Df(c)$.
$$Df(x)=\begin{bmatrix}\frac{\partial f_1}{\partial x_1}(x)&\frac{\partial f_1}{\partial x_2}(x)&\cdots&\frac{\partial f_1}{\partial x_p}(x)\\\frac{\partial f_2}{\partial x_1}(x)&\frac{\partial f_2}{\partial x_2}(x)&\cdots&\frac{\partial f_2}{\partial x_p}(x)\\\vdots&\vdots&\cdots&\vdots\\\frac{\partial f_q}{\partial x_1}(x)&\frac{\partial f_q}{\partial x_2}(x)&\cdots&\frac{\partial f_q}{\partial x_p}(x)\end{bmatrix}$$
## Properties
If $f,g:\mathbb{R}^n\to\mathbb{R}^m$, $\varphi:\mathbb{R}^n\to\mathbb{R}$ are differentiable at the same point $c\in\mathbb{R}^n$, and $\alpha \in\mathbb{R}$, the following are differentiable and satisfy:
- $D(f\pm g)=Df\pm Dg$ 
- $D(uf)=D\varphi \cdot f+\varphi Df$
- $D(\alpha f)=\alpha Df$
If $f:\mathbb{R}^n\to \mathbb{R}^m$, $g:\mathbb{R}^m\to \mathbb{R}^p$ are differentiable, $gf:\mathbb{R}^n\to\mathbb{R}^p$ is differentiable and:
$$ D(gf(x))=Dg(f(x)) Df(x) $$
## Continuously Differentiable
Let $U$ be open in $\mathbb{R}^{n}.$ Let $f:\mathbb{R}^n\to \mathbb{R}^m$ be differentiable in $U$. We say that $f$ is continuously differentiable in $U$ if the function $Df:\mathbb{R}^n\to L(\mathbb{R}^{n},\mathbb{R}^m)$ is [[Limits and Continuity in Metric Spaces|Continuous]] in $U$.
### Theorem
Let $U$ be open in $\mathbb{R}^n$, and $f:\mathbb{R}^n\to \mathbb{R}^m$. Then $f$ is continuously differentiable in $U$ if and only if $\partial_{x_{i}}f_j$ is continuous in $U$
### Mean Value Theorem
Let $f:\mathbb{R}^n\to \mathbb{R}^m$ be differentiable in $U\subseteq \mathbb{R}^n$ open. If $x,x+h\in U$ are such that the line segment from $x$ to $x+h$ is contained within $U$, then 
$$
\| f(x+h)-f(x) \| \leq \left(\sup \| | df_{x+h}-df_x | \|_\infty\right)\| h \| _{\infty} 
$$
provided that the supremum exists.
$$
f(x+h)-f(x)=\begin{bmatrix}
\sum\limits_{i=1}^{n}\partial_{x_{i}}f_{1}(x+\theta_{1}h)\cdot h_i\\
\vdots \\
\sum\limits_{i=1}^{n}\partial_{x_{p}}f_{m}(x+\theta_{m}h)\cdot h_i
\end{bmatrix}
$$
## Tangent plane
The tangent plane for a point above is given by: 
$$ L( x)= f( x_0)+D f( x_0)( x- x_0)$$
As well, the [[Normal Vector]] for this plane is given by:
$$\overrightarrow n = \pm\begin{bmatrix} f_x\\ f_y\\ -1 \end{bmatrix}$$