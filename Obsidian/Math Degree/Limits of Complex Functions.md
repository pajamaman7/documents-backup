Limits on complex functions are defined similarly to limits in $\mathbb{R}^{2}$:
$$\begin{align}
\lim\limits_{ z \to c }f(z)=l&\iff \lim\limits_{ z \to c }\lvert f(z)-l \rvert=0\\
\lim\limits_{ z \to c }f(z) =\infty_\mathbb{C}&\iff \lim\limits_{ c \to \infty }|f(z)|=\infty \end{align}$$
We have a familiar property, for $u(z)=\mathrm{Re}f(z)$ and $v(z)=\mathrm{Im}f(z)$:
- $\lim\limits_{ z \to c }f(z)=l\iff \lim\limits_{ z \to c }u(z)\mathrm{Re} l$ and $\lim\limits_{ z \to c }v(z)=\mathrm{Im}l$.
- If $u(z)$ or $v(z)$ diverge as $z\to c$, then $\lim\limits_{ z \to c }f(z)=\infty_\mathbb{C}$.
## Proving Limits do not exist
Take two paths through the point $c$. If the limit differs at the two points, then it does not exist.
## Proving Limits
To prove limits in the complex case we use [[Polar Coordinates]] and [[Squeeze Theorem]].
### $c$ finite
When $c$ is finite, we write $z=c+r e^{i\theta}$. Then we get $f(c+ r e^{i\theta})=\tilde{f}(r,\theta)$, and we can take $\lim\limits_{ r \to 0 }\tilde{f}(r,\theta)$
#### $l$ finite
When $l$ is finite, we use squeeze theorem and find some $g$ so that: 
$$\lim\limits_{ r \to 0^{+} } g(r)=0$$
and
$$\left| f(c+r e^{i\theta})-l \right| \leq g(r)$$
In an neighbourhood of $r=0$.
#### $l=\infty_{\mathbb{C}}$
Find $g(r)$ so that $\lim\limits_{ r \to \infty }g(r)=\infty$ and
$$|f(c+r e^{i\theta})|\geq g(r)$$
in a neighbourhood of $r=0$.
### $c\to \infty_{\mathbb{C}}$
For infinite cases we write $z=r e^{i\theta}$ and we obtain $f(re^{i\theta})=\tilde{f}(r,\theta)$.
#### $l$ finite
Find some real function $g(r)$ and show that:
$$\lim\limits_{ r \to \infty }g(r)=0$$
and
$$\left| f(r e^{i\theta})-l \right|\leq g(r) $$
in a neighbourhood of $r=\infty$.
#### $l$ infinite
Find $g(r):\lim\limits_{ r \to \infty }g(r)=\infty$ and
$$f(r e^{i\theta})\geq|g(r)|$$
In a neighbourhood of $r=\infty$.