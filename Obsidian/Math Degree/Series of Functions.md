## Pointwise convergence
Let $\{ f_n \}$ be a [[Sequences of Functions|Sequence of Functions]] from $E\subseteq \mathbb{R}$ to $\mathbb{R}$. We say that the series $\sum\limits_{k=1 }^{\infty}f_k=f$ converges pointwise on $E$ if the sequence of partial sums $\sum\limits_{k=1 }^{N}f_k$ converges pointwise.
## Uniform convergence
Let $\{ f_n \}$ be a [[Sequences of Functions|Sequence of Functions]] from $E\subseteq \mathbb{R}$ to $\mathbb{R}$. We say that the series $\sum\limits_{k=1 }^{\infty}f_k=f$ converges uniformly on $E$ if the sequence of partial sums $\sum\limits_{k=1 }^{N}f_k$ converges uniformly.
A uniformly convergent series is convergent pointwise in the same interval.
## Absolute convergence
We say that $\sum\limits_{n=1 }^{\infty}f_n$ is absolutely convergent in $E\subseteq \mathbb{R}$ if $\sum\limits_{n=1 }^{\infty}|f_n|$ converges pointwise in $I$. If a series converges absolutely in $I$, it must be pointwise convergent in $I$.
## Cauchy Criterion
The series $\sum\limits_{n=1}^{\infty}f_n(x)$ converges uniformly in $E\subseteq \mathbb{R}$ if and only if: For ever $\varepsilon>0$, there exists $N\in\mathbb{N}$: $m>n\geq N\implies \left|\sum\limits_{k=n}^{m}f_k(x)\right|<\varepsilon \forall x\in E$.
## Weierstrass Comparison Test
Let $\{ f_n \}$ be a [[Sequences of Functions|Sequence of Functions]] from $E\subseteq \mathbb{R}$ to $\mathbb{R}$. If there exists a sequence of positive numbers $\{ u_n \}$ such that $|f_n(x)|<u_n$, $\forall n\geq N_{0}\forall x\in E$, and $\sum\limits_{n=1}^{\infty}u_n$ converges.