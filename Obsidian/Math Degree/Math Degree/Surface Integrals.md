---
tags:
  - Calc
aliases:
  - Flux Integrals
---
Let $S$ be a [[Parametric Surfaces|Parametric Surface]] given by $\vec{r}(u,v)$.
## Scalar Functions
Given a scalar function (Always 3 variable), and a domain $D$ which is the set of all $(u,v)$ coordinates for $S$, the *Surface Integral* of $f$ over $S$ is given by:
$$\iint_S f\,dS=\iint_D f(\vec{r}(u,v))\|\vec{n}\|\, du\,dv$$
Where $\|\vec{n}\|$ is the length of the normal vector of the plane spanned by $\vec r_u, \vec{r_v}$.
Hence, $\|\vec{r}_u\times \vec{r}_v\|$
## Vector Fields (Flux integrals)
Given a vector field $\vec{F}$ and a surface $S$ with parameterization $\vec{r}(u,v)$,
$$\iint_S F\cdot d \vec{S}=\iint_D \vec{F}\cdot \vec{n}\,dA$$
