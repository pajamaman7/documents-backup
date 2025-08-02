(See [[Taylor Series]])
Let $f:\mathbb{R}^n\to \mathbb{R}$, so that $f$ has $p$ continuous derivatives, and the $p+1$th derivative of $f$ exists.
$\forall x\in\Omega,h\in\mathbb{R}^n$. If the line segment from $x$ to $x+h$ is contained in $\Omega$, then $\exists\theta \in(0,1)$ so that:
$$
f(x+h)=f(x)+\left(\sum\limits_{k=1}^{p}\frac{1}{k!}\left( \sum\limits_{i=1}^{n}h_i\frac{ \partial  }{ \partial x_{i} }  \right) ^{(k)}f(x)\right)+\frac{1}{p!}\left(\sum\limits_{i=1}^{n}h_i\frac{ \partial  }{ \partial x_i } \right)^{(p+1)}f(x+\theta h)
$$