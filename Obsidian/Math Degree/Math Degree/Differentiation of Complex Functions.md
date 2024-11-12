---
aliases:
  - Cauchy-Riemann Equations
  - Complex Holomorphic Functions
  - Singularities of Complex Functions
  - Holomorphic
---
## At a point
The derivative of a function $f:D\to \mathbb{C}$, with $D$ an open subset of $\mathbb{C}$.
$$f'(c)=\lim\limits_{ z \to c } \frac{f(z)-f(c)}{z-c}$$
If this limit exists, then $f$ is differentiable at $c$.
## In the domain
If this function is differentiable at every point in its domain, we say that it is differentiable.
$$f'(z)=\lim\limits_{ h \to 0 }\frac{(f(z+h)-f(z))}{h} $$
### Properties
- $f(z)=c$ for some constant $c\in \mathbb{C}$, then $f'(z)=0$
- If $g(t)=f(\gamma(t))$, $g'(t)=f'(\gamma(t))\gamma'(t)$.
- $f'(c)$ exists $\implies$ $f$ is continuous at $c$
- $f$ is not continuous at $c\implies$ $f$ is not differentiable at $c$.
## Cauchy-Riemann Equation
Rather than checking restrictions on the limit, we can check:
$$\frac{ \partial f }{ \partial x } =-i\frac{ \partial f }{ \partial y } $$
And if $u(z)=\mathrm{Re}f(z),\,v(z)=\mathrm{Im}f(z)$, we must have
$$\frac{ \partial u }{ \partial x } =\frac{ \partial v }{ \partial y },\quad\frac{ \partial u }{ \partial y } =-\frac{ \partial v }{ \partial x } $$
A consequence of this is that $f$ is differentiable if and only if $u,v$ are differentiable and satisfy the above equality. If this is all satisfied,
$$f'(z)=\frac{ \partial  }{ \partial x } f(z)=-i\frac{ \partial  }{ \partial y } f(z)$$
## Holomorphic and Entire
A function is holomorphic on a subset of its domain $\iff$ it is both [[Differentiation of Complex Functions|Differentiable]] and its derivative is continuous on the subset.

Ratios, products, linear combinations of holomorphic functions are holomorphic.

A function is entire if that subset is its whole domain.
## Singularities
The singularities of some $f:D\to \mathbb{C}, D\subseteq \mathbb{C}$ is the set of cluster points $c\in S\subseteq D$ such that $f$ is not defined at $c$ or $f$ is not differentiable at $c$.
### Isolated
If $c$ is an isolated point of $S$, $c$ is an isolated singularity
#### Removable Singularity
If $c$ is a removable singularity, define $f(c)=l$, where $l=\lim\limits_{ z \to c }f(z)$
$c$ is removable if $\lim\limits_{ z \to c }f(z)=l\in\mathbb{C}$
#### Pole
$c$ is a pole if $\lim\limits_{ z \to c }f(z)=\infty _\mathbb{C}$. Too bad.
#### Essential Singularity
$c$ is an essential singularity if $\lim\limits_{ z \to c }f(z)$ does not exist. 
### Non-isolated
If $c$ is a cluster point of $S$, $c$ is a non-isolated singularity
## Derivatives
- $\frac{d}{dz}e^{z}=e^{z}$
- $\frac{d}{dz}\sinh z=\cosh z$
- $\frac{d}{dz}\cosh z=\sinh z$
- $\frac{d}{dz}\sin z=\cos z$
- $\frac{d}{dz}\cos z=-\sin z$
- $\frac{d}{dz}\alpha ^{z}=\alpha ^{z}\ln \alpha$