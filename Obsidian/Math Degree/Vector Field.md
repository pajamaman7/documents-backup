---
tags:
  - Calc
---
A *Vector Field* is a function $\vec F:U\to \mathbb{R}^{n}$ where $U\subset \mathbb{R}^{n}$ is typically [[Open and Closed Sets|open]].
And we will write
$$\vec{F}=\begin{pmatrix}
F_{1}\\F_{2}\\ \vdots
\end{pmatrix}$$
where all $F_i$ are typically twice [[Differentiablility|Differentiable]], and the second order partials are continuous.

If $\phi$ is a scalar function, then $\nabla \phi$ is a vector field.
## Conservative Field
A vector field $\vec{F}$ so that there exists $\phi$ with $\nabla \phi=\vec{F}$ is called a conservative field, with $\phi$ being the *potential* for $\vec{F}$.
### Existence of a potential
To show that a vector field is not conservative, we use the fact:
If a vector field $\vec{F}$ is not conservative, then mixed partials will not be equal. Check:
- 2D: $F_{1,y}=F_{2,x}$
- 3D: $F_{1,y}=F_{2,x}$,$F_{2,z}=F_{3,y}$ $F_{1,z}=F_{3,x}$
### Finding a potential
To find a potential $\phi$ we begin by setting $\phi_x=F_{1}$, $\phi_y=F_{2}$, and $\phi_z=F_{3}$. We solve this not too differently from [[Exact Differential Equations]], integrating for example $\phi_x$, which gives $\phi=\int F_{1} \, dx+f_{1}(y,z)$. Doing this for all three functions will result in a system of equations, either allowing us to solve for $\phi$ or revealing that the field is not conservative.
## Field Line
A *field line* for a vector field $\vec{F}$ is a parametric curve $\vec{r}(t)$ with the property that the velocity vector for $\vec{r}(t)$ is $\vec{F}(\vec{r}(t))$.
