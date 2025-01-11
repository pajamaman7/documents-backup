## Tangent Vector and Line
The tangent vector at $t$ is:
$$\vec T(t)=\frac{\vec v(t)}{v(t)}$$ which is a unit vector expressing the direction of travel.
The tangent line at $t_1$ is the line with direction $\vec T(t_1)$ containing the point $\vec r(t_1)$
$$L(t)=\vec r(t_1)+t\vec T(t_1)$$
## Normal Vector
It is useful to note that $\vec T'$ is [[Orthogonal]] to $\vec T$.
Normalizing this derivative gives us the *Normal Vector*.
$$\vec N=\frac{\vec T'}{||\vec T'||}$$
Using the below facts and properties of the [[Cross Product]], we may also find
$$\vec{N}=\vec{B}\times\vec{T}$$
## Binormal Vector
To find this, we assume the parametric curve $\vec{r}\in\mathbb{R}^{3}$.
We define $\vec{B}=\vec{T}\times\vec{N}$. Since both $\vec{T},\vec{N}$ are unit vectors, the binormal vector will be perpendicular to both vectors and will be a unit vector as well.

We can also find that $$\vec{B}=\frac{\vec{v}\times\vec{a}}{\left| \left| \vec{v}\times\vec{a} \right| \right| }$$
## TNB
A curve is uniquely determined by $\vec{T},\vec{N},\vec{B}$. $\{\vec{T},\vec{N},\vec{B}\}$ is called a frame and is an [[Orthonormal Basis]] for $\mathbb{R}^{3}$.

## TNB decomposition
Any vector $\vec{u}=(u_{1},u_{2},u_{3})$ can be expressed in terms of TNB, as:
$$u=(\vec{u}\cdot \vec{T})\vec{T}+(\vec{u}\cdot \vec{N})\vec{N}+(\vec{u}\cdot \vec{B})\vec{B}$$