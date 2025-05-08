## Constructions
Given the set $\mathbb{Q}$ of [[Rational Numbers]], we have several constructions which can produce the reals, with the desired properties:
- $\mathbb{R}$ is an ordered field.
- $\mathbb{R}$ contains $\mathbb{Q}$.
- $\mathbb{R}$ has the [[Least Upper Bound Property]].
### By cuts
#### Definition
By Dedekind, we define $x\in\mathbb{R}$ as a subset of $\mathbb{Q}$ which is:
- Unbounded below (or above if we so choose)
- Not empty or equal to $\mathbb{Q}$
- If $p\in x$, then $\forall q<p$ in $\mathbb{Q}$, $q\in x$.
- For any $p\in x$, there is another $q\in x$ greater than $p$.
#### Order
A [[Ordered Set|Partial Order]] is defined on these cuts, $a\subseteq b\iff a\leq b$
#### Operations
We define addition and multiplication:
- $a+b=\{ r+s:r\in a, s \in b \}$
- Multiplication is defined more uncomfortably; define, for $\alpha,\beta>0$, define $\alpha\beta=\{ rs:r\in\alpha,s\in\beta \}$. Then if one of $\alpha,\beta$ is negative, 
$$
\alpha\beta=
\begin{cases}
(-\alpha)(-\beta) & \mathrm{if~}\alpha<0^*,\beta<0^*, \\
-[(-\alpha)\beta] & \mathrm{if~}\alpha<0^*,\beta>0^*, \\
-[\alpha\cdot(-\beta)] & \mathrm{if~}\alpha>0^*,\beta<0^*. & 
\end{cases}
$$
#### Inclusion of $\mathbb{Q}$
For any $r\in\mathbb{Q}$, we define $\varphi(r)\in\mathbb{R}$ to be the cut:
$$
\varphi=\{ s\in\mathbb{Q}:s<r \}
$$
This gives an injection, allowing for our desired inclusion of $\mathbb{Q}$ in $\mathbb{R}$.
### By Cauchy Sequences
#### Definition
We define $x\in\mathbb{R}$, to be a sequence $\{ x_n \}_{n\in\mathbb{N}}$ of [[Rational Numbers]].