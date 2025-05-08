---
aliases:
  - Continuous
  - Limit
  - Limits
---
A function on [[Topology|Topological Spaces]] $f:X\to Y$ is said to be continuous if, for every $V$ open in $Y$, the preimage $f^{-1}(V)$ is open in $X$.
# In Metric Spaces
## Limits
Let $f:X\to Y$ a function between metric spaces. We say that $\lim\limits_{ x\to p }f(x)=q\iff \forall\epsilon>0 \quad\exists\delta>0$ so that $d_x(x,p)<\delta\implies d_y(f(x),q)<\epsilon$.
### Theorem
Sums, products, and quotients are preserved by limits.
### In $\mathbb{R}$
We say that $\lim\limits_{ x\to p }f(x)=q\iff \forall\epsilon>0 \quad\exists\delta>0$ so that $|x-p|<\delta\implies |f(x)-q|<\epsilon$.
## Continuity
We say $f$ above is continuous at a point $p$ if $\forall\epsilon>0\quad\exists\delta>0:$
$d_x(x,p)<\delta\implies d_y(f(x),f(p))<\epsilon$
Note that if $p$ is isolated, $f$ is continuous at $p$.
We say $f$ is continuous in its domain if $f$ is continuous at every point in its domain.
### Theorem
Let $f:X\to Y$ a function between metric spaces.
Then $f$ is continuous if and only if $f^{-1}(V)$ is open in $X$ for all $V\subseteq Y$ open.
#### Corollary
For the above function $f$, $f$ is continuous in $X \iff f^{-1}(F)$ is closed in $X$ for any closed set $F$ in $Y$.
### Composition
Sums, products, and quotients of continuous functions are continuous; the composition of continuous functions is continuous.
### Coordinate functions
The coordinate function $x_i$ or $z=x+iy$ are continuous.
### Basic continuous functions
- All polynomials are continuous functions.
-  $\left| \cdot \right|$ is continuous in $\mathbb{R}^{k},\mathbb{C}$
### Continuity and Compactness
Let $f$ as above, and let $X$ be [[Compact]] and continuous. Then $f(X)$ is compact in $Y$.
### Boundedness
$f$ is bounded $\iff \exists  M>0$ so that $f(X)\subseteq B_Y(f(x),M)$  for some $x \in M$.
#### Corollary
$f$ is continuous from $X\to \mathbb{R}^{k}$. Then if $X$ is compact, $f(X)$ is closed and bounded.
## Uniform Continuity
$f$ is uniformly continuous on $E\subset X$ if and only if $\forall\varepsilon>0$, $\exists \delta>0$, $d(x,y)<\delta\implies d(f(x),f(y))<\varepsilon$
### On Compact Sets
Continuous functions on compact sets are uniformly continuous
### Easy check
Differentiable functions are continuous when the derivatives are bounded.
