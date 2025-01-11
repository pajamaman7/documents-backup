Consider $f: D\to \mathbb{C}$ where $D\subseteq \mathbb{R}$. Then we can write $f(t)=u(t)+iv(t)$. That is, $\mathrm{Re}f(t)=u(t),\,\mathrm{Im}f(t)=v(t)$. So we can think of $f$ as a [[Parametric Curves|Parametric Curve]] in $\mathbb{R}^{2}$.
Since both functional components of $f$ are functions on ordered sets, it is ordered.
## Limits
The limit of a complex function $f:D\to \mathbb{C}$ with $D\subseteq \mathbb{R}$. The limit as $t$ approaches $c\in\mathbb{R}\cup \{ \infty,-\infty \}$ exists when $c$ is a cluster point in $\mathbb{R}$:
1. $\lim\limits_{ t \to c } f(t)=l\in\mathbb{C}\iff \lim\limits_{ t \to c } u(t)=\mathrm{Re}l$ and $\lim_{ t \to c }v(t)=\mathrm{Im}l$.
2. If $u$ or $v$ diverge as $t\to c$, then $\lim\limits_{ t \to c }f(t)=\infty _\mathbb{C}$.
3. If the limit of $u$ or $v$ does not exist, we check $\lim\limits_{ t \to c }|f(t)|$.
    1. If the modulus diverges, $\lim\limits_{ t \to c }=\infty_\mathbb{C}$
    2. If the modulus is 0, $\lim\limits_{ t \to c }=0$.
    3. If we have some other limit, the modulus test is inconclusive.
### Interesting limits
1. Cluster points of $D$ that are not in the domain (including infinities if they are cluster points).
2. Points where the definition of $f$ changes. (e.g. piecewise)
## Continuity
Consider $f:D\to \mathbb{C}$, and $c\in D$ 
- If $c$ is an isolated point of $D$, then $f$ is a continuous at $c$.
- If $c$ is a cluster point, $f$ is continuous at $c$ if $\lim_{ t \to c }f(t)=f(c)$.
- $f$ is continuous at $c \iff$ $u(t)=\mathrm{Re}f(t)$ and $v(t)=\mathrm{Im}f(t)$ are continuous at $c$. 
## Derivatives
Consider $f:D\to \mathbb{C}$, where $D$ is an open set in $\mathbb{R}$. The derivative of $f$ at $c\in D$ is defined as:
$$f'(c)=\lim_{ t \to c } \frac{f(t)-f(c)}{t-c}$$
Whenever the limit exists and is finite, we say $f$ is differentiable at $c$. This is true$\iff$the real and imaginary parts of $f$ are differentiable at $c$.
### Properties
If $f$ is differentiable at $c$, and $f'(c)\neq 0$, then $f'(c)\in\mathbb{C}$ gives the tangent vector to the curve.

As always, if $f$ is differentiable at $c$, then it is continuous at $c$.

Let $D\subseteq \mathbb{R}$ be open. $f:D\to \mathbb{C}$ is differentiable in $D$ if it is differentiable at every point in $D$.
### Class
#### Class $C^{1}(D)$
Let $f:D\to \mathbb{C}$ where $D\subseteq \mathbb{R}$ and $D$ is open. $f$ is of class $C^{1}(D)$ if:
- $f$ is differentiable in $D$
- $f'$ is continuous in $D$
#### $C^{k}(D)$
A generalization of this to any $k\in\mathbb{Z}_{\geq0}$:
$f$ is of class $C^{k}(D)$ if:
- $f^{(k)}(t)$ exists
- $f^{(k)}(t)$ is continuous
#### $C^{\infty}(D)$
$f$ is of class $C^{\infty}(D)$ if:
- $f$ is infinitely differentiable
- All derivatives of $f$ are continuous.


## Integration
Consider $f(t):D\to \mathbb{C}$ with $D\subseteq \mathbb{R}$. Then the integral of $f$ is:
$$\int_{a}^{b} f(t) \, dt =\int_{a}^{b} u(t) \, dt +i\int_{a}^{b} v(t) \, dt $$
Where $u(t)=\mathrm{Re}f(t)$ and $v(t)=\mathrm{Im}f(t)$.
So:
$$\begin{align}
\mathrm{Re}\int_{a}^{b} f(t) \, dt =\int_{a}^{b} u(t) \, dt&=\int_{a}^{b} \mathrm{Re}f(t) \, dt \\
\mathrm{Im}\int_{a}^{b} f(t) \, dt =\int_{a}^{b} v(t) \, dt&=\int_{a}^{b} \mathrm{Im}f(t) \, dt 
\end{align}$$
A function is integrable when both $u,v$ are integrable over $(a,b)$. 
### Absolutely Integrable
A function $f:I\to \mathbb{C}$ is said to be absolutely integrable if:
$$\int_{I}|f(t)|  \, dt $$
is integrable.
Absolutely integrable functions are also integrable. The converse is not true.
### Abel-Dirichlet Theorem
Let $f:D\to \mathbb{C}$. $f(t)=g(t)h(t)$. To be integrated over $[a,b]$, where $a\in\mathbb{R}$. $f$ may not be well defined at $b$.
1. $g(t)$ has bounded primitive (antiderivative): $|G(t)|<k$ for some $k>0$
2. $h(t)$ is of class $C^{1}([a,b))$ (Differentiable with continuous derivative)
3. The limit $\lim\limits_{ t \to b^{-} }h(t)=0$
4. $h'(t)$ is absolutely integrable over $[a,b)$.
If these conditions are met then we can say $f(t)=h(t)g(t)$ is integrable over $[a,b)$.