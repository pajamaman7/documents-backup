A series of complex numbers is defined and denoted by:
$$\sum_{n=0}^{\infty}z_n=\lim_{ k \to \infty } \sum\limits_{n=0 }^{k}z_n=\lim_{ k \to \infty } s_k$$
If this limit exists and is equal to some $s\in \mathbb{C}$, we say that it is convergent. If it equals $\infty_{\mathbb{C}}$, we say it is divergent. And if the limit does not exist, we say that it is indeterminate.
## Divergence and Convergence
$\sum\limits_{n=0 }^{\infty}z_n$ is convergent if and only if both its real and imaginary parts converge. We can use typical [[Convergence tests]] on each part.
### Absolute Convergence
A series $z_n$ is absolutely convergent if $\sum\limits_{n=0 }^{\infty}|z_n|$ is convergent. If this is the case, the series $\sum\limits_{n=0 }^{\infty}z_n$ is convergent as well.
## Geometric Series
Consider the convergence of $\sum\limits_{n=0 }^{\infty}q^{n}$ with $q \in \mathbb{C}$. If $q\neq 1$ then its $k$th partial sum is given by $\sum\limits_{n=0 }^{k}q^{k}=\frac{1-q^{k+1}}{1-q}$. 
The infinite series:
- Diverges if $\lvert q \rvert>1$ 
- Converges to $\frac{1}{1-q}$ if $\lvert q \rvert<1$ or $q=1$
- Is indeterminate if $\lvert q \rvert=1$ but $q\neq 1$
## Exponential Series
Consider the series $\sum\limits_{n=0 }^{\infty} \frac{z^{n}}{n!}$ with $z\in\mathbb{C}$. This series is conveniently convergent for any $z$, by the absolute ratio test.