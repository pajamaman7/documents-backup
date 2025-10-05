Define Real projective space, $\mathbb{R}P^{n}=S^{n} / \sim$ where $a\sim-a$ defines $\sim.$
## Compactness
This space is compact Hausdorff, take $\pi:S^{n}\to\mathbb{R}P^{n}$ which is surjective, and $S^{n}$ is compact so $\mathbb{R}P^{n}$ is compact. 
By a usual argument we can say $\mathbb{R}P^{n}$ is Hausdorff.
## Inductive construction
Let $a\sim\pi(a)$ exactly when $a\in S^{n-1}$
$$
\mathbb{R}P^{n}\cong \mathbb{R}P^{n-1}\sqcup D^{n} / \sim
$$
Using the map $f:\mathbb{R}P^{n-1}\sqcup D^{n}\to \mathbb{R}P^{n}$ defined by:
$$
f(x_{1},\dots,x_{n-1})=\begin{cases}
\frac{(x_{1},\dots,x_n-1,\sqrt{ 1-|x|^{2} })}{|(x_{1},\dots,x_n-1,\sqrt{ 1-|x|^{2} })|} &x\in D^{n}\\ 
(x_{1},\dots,x_n-1,0)\not \in D^{n}
\end{cases} 
$$
## Cell Complex
The structure of $\mathbb{R}P^{n}$ as a [[CW Complex]] can be constructed by taking one cell in each dimension from $0$ to $n$.