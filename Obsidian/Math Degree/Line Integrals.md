---
tags:
  - Calc
---
## Scalar Functions
Line integrals require the integration of a function $f(x,y)$ or $f(x,y,z)$ along a 2d or 3d curve $C$. These integrals take the form:
- 2D: $\int_{C} f(x,y) ds$
- 3D: $\int_{C}^{}  f(x,y,z) ds$
where $s$ denotes arc-length. This implies some chosen [[Parametric Curves|parameterization]] for $C$, say $\vec{r}(t)$.
Recall $\frac{ds}{dt}=v(t)$, which implies $ds=v(t)dt$.
This allows us to evaluate:
- 2D: $\int_{C} f(x,y) ds=\int_{a}^{b} f(x(t),y(t)))v(t)dt$
- 3D: $\int_{C} f(x,y,z) ds=\int_{a}^{b} f(x(t),y(t),z(t))v(t)dt$
This again does not depend on the chosen parameterization.
## Vector fields
Let $\vec{F}$ be a [[Vector Field]] in $\mathbb{R}^{2}$ or $\mathbb{R}^{3}$ and $C$ a [[Parametric Curves|Parametric Curve]] (with parameterization $\vec{r}(t)$). in the same space. We can take the line integral of $\vec{F}$ along $C$, given by the integral of $\vec{F}\cdot \vec{T}$ along $C$:
$$\int_{C}^{} \vec{F} \, d \vec{r} =\int_{a}^{b} \vec{F}(\vec{r}(t))\cdot \vec{v} \, dt $$
### On parameterization
If we take $\vec{r_{1}}(t)$ which travels in one direction along $C$ and $\vec{r_{2}}(t)$ in the other direction, the line integrals will be equal up to sign.

Otherwise the integral does not depend on parameterization.

### On decomposition
If we write:
$$\vec{F}=\begin{pmatrix}
F_{1}\\F_{2}\\F_{3}
\end{pmatrix}$$
then the line integral can be written as:
$$\int_{C}^{} \vec{F} \, d \vec{r}=\int_{c}^{} F_{1} \, dx+\int_{C}^{} F_{2} \, dy+\int_{C}^{} F_{3} \, dz$$
### On conservative fields
Let $\vec{F}=\nabla \phi$ and $C$ as above.
Then our integral can be written according to the chain rule and [[Fundamental Theorem of Calculus]] as:
$$\int_{C}^{} \vec{F} \, d \vec{r}=\phi(\vec{r}(b))-\phi(\vec{r}(a))$$
This means that for a line integral in a conservative vector field, only the endpoints of $C$ and the integral. The value of the integral is not dependent on the path $C$ takes.
If the starting and ending point ($C$ will be called *closed*) are equal of course our integral is $0$.

### "Almost" Conservative Fields
If we can find a potential $\phi$ for a field $F$ that differs only slightly from the original function, that is:
$$\vec{F}=\nabla \phi+\vec{G}$$
Then we can simplify a line integral using conservative properties as follows:
$$\int_{C}^{} \vec{F} \, d \vec{r}=\phi(\vec{r}(b))-\phi(\vec{r}(a))+\int_{C}^{} \vec{G} \, d \vec{r} $$
## Circulation
The line integral over a closed curve (that is, the start and end point are the same is notated by:
$$\oint_C \vec{F}\,d \vec{r}$$