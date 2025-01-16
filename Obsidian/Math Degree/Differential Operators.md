---
tags:
  - Calc
aliases:
  - Gradient
  - DIvergence
  - Curl
  - Laplacian
---
- There are many identities relating these operators. Two of the most important are
    - $div(curl(\vec{F}))=0$ as long as $\vec{F}$ is sufficiently (twice differentiable).
    - $curl(\nabla \Phi)=\vec{0}$. In fact, if $curl(\vec{F})=0$ at any point $P_{0}\in\mathbb{R}^{3}$, then $\vec{F}$ must be conservative.
## The Gradient - $\nabla$
If $f$ is a scalar function, $\nabla f=(f_x, f_y, f_z)$ (or more in higher dimension).
We think of this symbol as a linear operator taking scalar functions to vector fields.
$\nabla f$ gives a vector field which points to the direction of greatest rate of change on $w=f(x,y,z)$.
## Divergence - $div$
Given a vector field $\vec{F}= (F_{1},F_{2},F_{3}),$ the *Divergence* of $F$ is given by:
$$div(\vec{F})=\frac{ \partial F_{1} }{ \partial x } +\frac{ \partial F_{2} }{ \partial y } +\frac{ \partial F_{3} }{ \partial z } $$
We could consider this similar to "$\nabla \cdot \vec{F}$", with $\nabla\cdot$ as an operator from vector fields to scalar fields.
See also: [[Divergence Theorem]]
### Properties
- $div(\vec{F})$ at a point $P_{0}$ s a signed measure of the degree to which $P_{0}$ is a source or a sink of vectors $\vec{F}$. 
- *Divergence* describes flux density. At some $P_{0}$, Let $B_r$ be the closed ball of radius $r$ around $P_{0}$, and $S_r(P_{0})$ the sphere of radius $r$ around $P_{0}$.
$$div(\vec{F}(P_{0}))=\lim_{ r \to 0 } \frac{1}{vol(B_r)}\iint_{S_r(P_{0})}\vec{F}\cdot d \vec{S}$$
## Curl - $curl$
Curl accepts a vector field and returns another. Consider $curl(\vec{F})$ as "$\nabla \times \vec{F}$"
$$\begin{align}
curl(\vec{F})&=det\begin{bmatrix}
\vec{i}&\vec{j}&\vec{k}\\ 
\frac{ \partial  }{ \partial x } &\frac{ \partial  }{ \partial y } & \frac{ \partial  }{ \partial z }  \\
F_{1} & F_{2} & F_{3}\\
\end{bmatrix}\\
&=\begin{pmatrix}
\frac{ \partial F_{  2} }{ \partial y } -\frac{ \partial F_{2} }{ \partial z }  \\
\frac{ \partial F_{1} }{ \partial x } -\frac{ \partial F_{3} }{ \partial x }  \\
\frac{ \partial F_{2} }{ \partial x } -\frac{ \partial F_{1} }{ \partial y } 
\end{pmatrix}
\end{align}$$
Think of $\nabla \times$ as a linear operator from vector fields to vector fields.
- Suppose we drop a particle into a field $\vec{F}$, following some field line. If the particle follows any kind of positive curvature path then $curl(\vec{F})(P_{0})$ gives the axis of rotation on this path.
## Laplacian - $\Delta$
Given a scalar $f$, the *Laplacian* of $f$ can be considered "$\Delta f=\nabla \cdot \nabla f$".
$$\Delta f=f_{xx}+f_{yy}+f_{zz}$$
Given a vector field $\vec{F}$, 
$$\Delta \vec{F}= \vec{F}_{xx}+\vec{F}_{yy}+\vec{F}_{zz}$$
