Let $A:\mathbb{R}^{n}\to\mathbb{R}^m$. We can define the matrix norms:
$$ \phi (A)=\max_{1\leq i\leq m}\| R_i(A) \|_\infty=|\| A \| | _{\infty} = \max_{x\in\mathbb{R}^{n}\setminus \{ 0 \}} \frac{\| Ax \| _\infty}{\| x \| _\infty} $$
$$
\psi(A)= \max_{1\leq i\leq n}\| C_i(A) \|_\infty =|\| A \| |_1= \max_{x\in\mathbb{R}^{n}\setminus \{ 0 \}} \frac{\| Ax \| _1}{\| x \| _1}
$$
Where $C_i(A)$ denotes columns of $A$ and $R_i(A)$ denotes rows of $A$.
### Properties
- $\| Ax \|_\infty \leq |\| A \| |_\infty \| x \|_\infty$
- $\| Ax \|_1 \leq |\| A \| |_1\| x \|_1$
## For Linear Transformations
We may define a more general matrix norm on [[Linear Operators]]. For $\| \cdot \|_n,\| \cdot \|_m$ norms on $\mathbb{R}^n,\mathbb{R}^m$ resp, 
$$
\varphi(T)=\sup_{x\in\mathbb{R}^n\setminus \{ 0 \}} \frac{\| Tx \| _m}{\| x \| _n}
$$
is a norm on $L(\mathbb{R}^n,\mathbb{R}^m)$, called the norm induced by $\| \cdot \|_n,\| \cdot \|_m$. We may denote this $|| | \cdot| | |$.
### Properties
- $| | |S\circ T| | |\leq | | | T| | | \cdot| | | S| | |$
- $| | |Tx| | |leq| | |T| | |\cdot\| x \|$.