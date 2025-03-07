Let $f:\mathbb{R}^n\to \mathbb{R}^m$ be defined in a neighborhood of $c\in\mathbb{R}^{n}$. We say that $f$ is differentiable at $x=c$ if there exists some $T\in L(\mathbb{R}^n,\mathbb{R}^m)$ such that:
$$
F(c+h)=f(c)+T(h)+\| h \|\alpha_c(h)
$$
where $\alpha_c:\mathbb{R}^n\to\mathbb{R}^m$ satisfies $\lim\limits_{h\to_{0}}\alpha_c(h)=0$. The linear transformation $T$ is called the differential of $f$ at $c$ and may be denoted $df_c$ or $Df$.
$$Df(x)=\begin{bmatrix}\frac{\partial f_1}{\partial x_1}(x)&\frac{\partial f_1}{\partial x_2}(x)&\cdots&\frac{\partial f_1}{\partial x_p}(x)\\\frac{\partial f_2}{\partial x_1}(x)&\frac{\partial f_2}{\partial x_2}(x)&\cdots&\frac{\partial f_2}{\partial x_p}(x)\\\vdots&\vdots&\cdots&\vdots\\\frac{\partial f_q}{\partial x_1}(x)&\frac{\partial f_q}{\partial x_2}(x)&\cdots&\frac{\partial f_q}{\partial x_p}(x)\end{bmatrix}$$
## Properties
If $f,g:\mathbb{R}^n\to\mathbb{R}^m$, $u:\mathbb{R}^n\to\mathbb{R}$ are differentiable at the same point $c\in\mathbb{R}^n$, the following are differentiable and satisfy:
- $D(f\pm g)=Df\pm Dg$ 
- $D(uf)=Du\cdot f+uDf$
## Tangent plane
The tangent plane for a point above is given by: 
$$ L( x)= f( x_0)+D f( x_0)( x- x_0)$$
As well, the [[Normal Vector]] for this plane is given by:
$$\overrightarrow n = \pm\begin{bmatrix} f_x\\ f_y\\ -1 \end{bmatrix}$$