## Contours/Paths
A path or contour on $\mathbb{C}$ is a function $\gamma:[a,b]\to \mathbb{C}$ where
- $\gamma$ is continuous
- $\gamma$ is piecewise of class $C^{1}$.
A contour is closed if $\gamma(a)=\gamma(b)=z_{0}$. Intuitively, it forms a loop in $\mathbb{C}$. A contour is constant if $\gamma(t)=z_{0}$. 
### Parameterization
If we change parameter, we look at $\gamma\circ p$. Sometimes the extremes are in the same order, sometimes they can be switched.
### Segment
The parameterization of a connection from $z_{0}$ to $z_{1}$ is given by $\gamma(t)=z_{0}+t(z_{1}-z_{0})$, with $t\in [0,1]$. (or $t\in\mathbb{R}$ if we want the entire line through $\mathbb{C}$). We can see this is a contour since it is continuous and differentiable.
### Opposite Contour
Let $\gamma:[a,b]\to \mathbb{C}$ is a contour. Then $\tilde{\gamma}:[a,b]\to \mathbb{C}$, $\tilde{\gamma}(t)=\gamma(a+b-t)$.
### Joining Contours
Let $\gamma:[a,b]\to \mathbb{C}$ and $\delta:[c,d]\to \mathbb{C}$, so that $\gamma(b)=\delta(c)$.
## Topology of Contours
### Path-Connected
$A\subseteq \mathbb{C}$ is path-connected if for every pair of $z_{0},z_{1}\in A$, we can find a continuous path $\gamma$ with extremes $z_{0}$ and $z_{1}$, fully contained in $A$ ($\gamma(t)\in A$ for any $t$ for which the path is defined).
### Homotopy
$\gamma,\delta$ are homotopic if:
Start with a closed contour $\gamma \in A$ where $A$ is path connected, apply a continuous deformation of $\gamma$ to obtain another closed contour $\delta$ with
- Never cut the contour, the contour is closed when deformed
- At every step the contour will always be in $A$
### Simply-Connected
$A\subseteq \mathbb{C}$ is called simply-connected if $A$ is path-connected, and every closed contour in $A$ is homotopic to a constant.
## Integration
### Continuous
Take $f:D\to \mathbb{C}$, with $D\subseteq \mathbb{C}$, $f$ continuous on $D$, and $\gamma:[a,b]\to D$. Then 
$$\int_{\gamma}^{} f(z) \, dz =\int_{a}^{b} f(\gamma(t))\gamma'(t) \, dt $$
If $\gamma$ is a closed contour, then we instead write:
$$\oint_\gamma f(z)dz$$
### Properties
- $\int_{\gamma}^{} af+bg \, dz=a\int_{\gamma}^{} f \, dz+b\int_{\gamma}^{} g \, dz$
- $\int_{\gamma}^{} f(z) \, dz=\pm \int_{\gamma}^{} f(z) \, dz$
    - +ive if the extremes are left the same, -ive if they are switched.
- $\int_{\tilde{\gamma}}^{} f(z) \, dz=-\int_{\gamma}^{} f(z) \, dz$
- $\int_{\gamma\delta}^{} f(z) \, dz=\int_{\gamma}^{} f(z) \, dz+\int_{\delta}^{} f(z) \, dz$
- If we have a constant contour, the integral becomes 0
### Cauchy Theorem
If $f$ is holomorphic, and $\gamma, \delta$ are closed and homotopic, then
$$\oint_{\delta}^{} f(z) \, dz=\oint_{\gamma}^{} f(z) \, dz  $$
In particular, if $D$ is simply-connected, every contour is homotopic to a constant contour, and every integral becomes zero.
### Equivalent for open contours
$$\oint_\gamma f(z)\,dz=0,\,\forall\gamma \iff \int_{\gamma_{1}}^{} f(z) \, dz=\int_{\gamma_{2}}^{} f(z) \, dz,\,\, \gamma_{1}(a)=\gamma_{2}(a) ,\gamma_{1}(b)=\gamma_{2}(b) $$
## Primitive
$f:D\to \mathbb{C}$,$D$ open, has a primitive in $D$ if we can find a function $F:D\to \mathbb{C}$ such that $F'(z)=f(z)$ for any $z\in D$.
### Properties
- If $D$ is path-connected, and $G$ and $F$ are primitives for $f$, $G(z)=F(z)+c$ for some $c\in\mathbb{C}$.
- If $f$ has a primitive $F$, $\int_\gamma f(z)dz=F(z_{1})-F(z_{0})$
#### TFAE
- $f$ has a primitive
-  $\oint_\gamma f(z)dz=0$
- $\int_{\gamma_{1}} f(z) \, dz=\int_{\gamma_{2}}^{} f(z) \, dz$
### Finding A Primitive
If we know $f$, one of the above is satisfied, and $D$ is path-connected, we can find a primitive $F: F'=f$ with:
$$F(z)=\int_{\gamma}^{} f(w) \, dw $$
Where $\gamma:[a,b]\to D$, and $\gamma(a)=z_{0}$, $\gamma(b)=z$. It may be simplest to choose $\gamma(a_{0})=0$.
## Jordan Curve
A Jordan Curve is a contour that is closed and simple:
- $\gamma:[a,b]\to\mathbb{C}$
- $\gamma(a)=\gamma(b)$
- If $\gamma(t_{1})=\gamma(t_{2})$ then $t_{1},t_{2}=a,b$.
A Jordan Curve is positively oriented if it's traversed counterclockwise.
### Theorem
A Jordan curve divides $\mathbb{C}$ into 2 regions, one bounded, enclosed by the curve, and the other unbounded outside the curve.
## Cauchy Integral Formula
Let $f:D\to \mathbb{C}$ with $D$ open, and $f$ holomorphic in $D$. Consider $\gamma$, positively oriented Jordan curve in $D$. Suppose $\gamma$ does not enclose any singularity of $f$. Then for any $z_{0}$ in the region enclosed by $\gamma$, 
$$f(z_{0})=\frac{1}{2\pi i}\oint_{\gamma} \frac{f(z)}{z-z_{0}}\,dz$$
If $\gamma$ is not positively oriented ($\gamma$ is clockwise), 
$$f(z_{0})=-\frac{1}{2\pi i}\oint_{{\gamma}} \frac{f(z)}{z-z_{0}}\,dz$$
It follows with a change of variable;
$$f(z)=\frac{1}{2\pi i}\oint \frac{f(w)}{w-z}$$
And a property of differentiation:
$$f^{(n)}(a)=\frac{n!}{2\pi i}\oint_{\gamma} \frac{f(z)}{(z-a)^{n+1}}dz$$
Which implies that all complex holomorphic functions are infinitely differentiable.