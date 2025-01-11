(From [[Multivariable Calculus]])
Multiple integrals can be used to find the volume under a curve in three dimensions. That is, multiple integrals can be used on multivariable functions.

The 3-dimensional equivalent to the [[Fundamental Theorem of Calculus]] is as follows.
The area under the curve $f(x,y)$ within the domain $D=[a,b]\times[c,d]$ is:
$$\int\int_{D}f(x,y)dA=\int_{a}^{b}\int_{c}^{d}f(x,y)dy dx=\int_{c}^{d}\int_{a}^{b}f(x,y)dx dy$$
Note that this means that the order of integration can be switched, and that this principle applies to triple and further integrals as well.
Also note that the bounds of integration can be functions as well as constants. If this is the case, we must be more careful when bounding our functions. Always ensure that the outermost integral has constant bounds in order to achieve a constant answer.

## Polar Coordinates for Integration
(See [[Polar Coordinates]])

In two dimensions, we can change our differentials and rewrite our integral to be bounded by $r,\theta$ instead of $x,y$. 
In two dimensions an example can be shown:

Find the area under $f(x,y)=8-x^2-y^2$ above the plane $z=0$.
$$\int_{0}^{2\pi}\int_{0}^{3}(8-r^2)rdrd\theta$$
Note: $x^2+y^2=r^2(sin^2\theta+cos^2\theta)=r^2$  

## Cylidrical Coordinates
Cylindrical coordinates can be thought of as [[Polar Coordinates]] with an added $z$-value.
These are particularly useful for triple integrals where multiple bounds are based circularly, under a sphere or cone for example.

Example in $\mathbb{R}^3$:
Evaluate $\int\int\int_{D} z dV$ where $D$ is the region bounded by the cylinder $x^2+y^2=9$, above by $z=5$ and below by $z=x+y$.

$$\int_{0}^{2\pi}\int_{0}^{3}\int_{r(\sin\theta+\cos\theta)}^{5}zdzdrd\theta$$

## Spherical Coordinates
[[Spherical Coordinates]] can also be used to refactor an integral. 

Note that the volume element in our integral changes.
$$dxdydz=dV=\rho^{2}\sin(\phi) d\phi d\theta d\rho$$

