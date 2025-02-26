A real function of several variables is simply a [[Functions|Function]] $f:\mathbb{R}^{n}\to \mathbb{R}$.
Recall [[Functions|Domain]], [[Functions|Range]], etc as usually defined for functions.
## Graph
The set $G$ of all points $(x,f(x))=(x_{1},\dots,x_n,f(x))$ is called the graph of $f$.
## Continuity 
Continuity in this case is defined identically as for [[Limits and Continuity in Metric Spaces]].
$f$ is continuous at $c$ if, $\forall\varepsilon>0\,,\exists\delta>0: \| x-c \|<\delta\implies|f(x)-f(c)|<\varepsilon$. This turns out to be equivalent regardless of the norm chosen.
### Equivalent definitions
TFAE to the above definition
- $f$ is continuous if the preimage of every open set in $\mathbb{R}$ is open in $\mathbb{R}^{n}$.
- For any [[Sequences and Series|Sequence]] $\{ a_{k} \}_{k\geq 1}$ convergent to $a$, the sequence $\{ f(a_k) \}_{k\geq 1}$ converges to $f(a)$.
### Properties
Sums, differences, quotients, products, scalar multiples, and composition maintain continuity as per the usual conditions.
## Lipschitz
$f:\mathbb{R}^{n}\to \mathbb{R}$ is said to be Lipschitz in $E\subseteq \mathbb{R}^{n}$ if there exists $k>0$, $|f(x)-f(y)|\leq k\| x-y \|$.
Any Lipschitz function is continuous in $E$.
## Uniform Continuity
Let $f:\mathbb{R}^{n}\to \mathbb{R}$ defined in $E\subseteq \mathbb{R}^{n}.$ We say that $f$ is uniformly continuous in $E$ if $\forall\varepsilon>0\exists\delta$ so that $\| x-y \|<\delta\implies | f(x)-f(y) |<\varepsilon$. This $\delta$ is independent of $x,y$.
### Theorem
If $f:\mathbb{R}^{n}\to \mathbb{R}$ is continuous in a compact set $E\subseteq \mathbb{R}^{n}$, then $f$ is uniformly continuous in $E$.
## Differentiability
Let $f:\mathbb{R}^{n}\to \mathbb{R}$ defined in a neighborhood of $c\in\mathbb{R}^{n}$. We say that $f$ is differentiable at $c$ if there exists a [[Linear Operators|Linear Transformation]] $T:\mathbb{R}^{n}\to\mathbb{R}$ such that for $h$ small, $f(c+h)=f(c)+T(h)+\| h \|\alpha_c(h)$, where $\lim\limits_{h\to{0}}\alpha_c(h)=0$
### The Gradient - $\nabla$
If $f$ is a scalar function, $\nabla f=(f_x, f_y, f_z)$ (or more in higher dimension).
We think of this symbol as a linear operator taking scalar functions to vector fields.
$\nabla f$ gives a vector field which points to the direction of greatest rate of change on $w=f(x,y,z)$.
### Theorem
Let $f:\mathbb{R}^{n}\to \mathbb{R}$ defined in a neighborhood of $c\in\mathbb{R}^{n}$. If $f$ is differentiable at $c$, then 
- $T=df_c(h)=\partial x_{1}h_{1}+\dots+\partial_{x_n}f(c)h_n=\nabla f\cdot h$
- $f$ is continuous at $c$.
### Equivalent (more helpful definition)
Let $f:\mathbb{R}^{n}\to \mathbb{R}$ defined in a neighborhood of $c\in\mathbb{R}^{n}$. We say that $f$ is differentiable at $c$ if 