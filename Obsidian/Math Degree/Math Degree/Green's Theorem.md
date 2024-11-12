Suppose $C$ is a closed curve surrounding a region $D\subset \mathbb{R}^{2}$ (oriented counterclockwise/$D$ is to the left of $C$ while moving along it). For a vector field $\vec{F}=(F_{1},F_{2})^{T}$, we have:
$$\oint_{C}\vec{F} d \vec{r}=\iint_{D}(F_{2})_x-(F_{1})_y\,dA$$
Note that the inside of the right double integral is zero when $F$ is conservative.
### Remarks
- If we regard $\vec{F}$ as $\vec{F}=(F_{1},F_{2},0)^{T}$, then $(F_{2})_x-(F_{1})_y=\text{the z coord of }curl(\vec{F})$.
    From this we also can say that $\iint(F_{2})_x-(F_{1})_ydA$ is the integral over the $z$ component of [[Differential Operators|Curl]].
- $\oint_C \vec{F}\cdot d \vec{r}$ is a measure of the tendency of $\vec{F}$ to "circulate" about $C$. Green's theorem says "The Total circulation around $C=\iint_D \text{local circulation}\; dA$.