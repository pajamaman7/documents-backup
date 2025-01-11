## Definition
Let $f(x_1,\ldots,x_n)$ be some scalar function $f: \mathbb{R}^n\to \mathbb{R}$
- The absolute maximum for $f$ is a value $f(a,\ldots,a_n)$ so that $f(a,\ldots,a_n)\geq f(x_1,\ldots,x_n)$ for all $(x_1,\ldots,x_n)$ in $dom(f)$.
- The absolute minimum for $f$ is a value $f(a,\ldots,a_n)$ so that $f(a,\ldots,a_n)\leq f(x_1,\ldots,x_n)$ for all $(x_1,\ldots,x_n)$ in $dom(f)$.
- A local maximum is a value $f(a_1,\ldots,a_n)$ such that there is an [[Open Ball]] $B$ for which $f(a,\ldots,a_n)\geq f(x_1,\ldots,x_n)$ for all $(x_1,\ldots,x_n)$ in $B$.
- A local minimum is a value $f(a_1,\ldots,a_n)$ such that there is an [[Open Ball]] $B$ for which $f(a,\ldots,a_n)\leq f(x_1,\ldots,x_n)$ for all $(x_1,\ldots,x_n)$ in $B$.
## Properties
- In general, we only think of local extrema at [[Interior Point]]s. 
- Global extrema can be interior or on the boundary.
- If $f$ is continuous on a closed and bounded [[Domain]], then it achieves both global maxima and minima on that domain. Moreover, these extrema must occur at:
    - A [[Critical Point]]; where $\nabla f = \vec 0$.
    - A [[Singular Point]]; where $\nabla f$ does not exist.
    - A [[Boundary Point]]