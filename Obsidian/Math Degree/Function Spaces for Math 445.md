Let $(X,d)$ be a [[Metric Spaces|Metric Space]].  Define 
$$\mathcal{F}(\Omega,\mathbb{R})=\{ f:X\to \mathbb{R} : f \text{ is defined in }\Omega\}$$
A function $f:X\to\mathbb{R}$ is said to be bounded in a subset $\Omega \subseteq X$ if $\sup_{x\in\Omega}|f(x)|<M$ for some real $M$.
$$
\mathcal{F}_b(\Omega,\mathbb{R})=\{ f\in\mathcal{F}(\Omega):f\text{ is bounded in }\Omega \}
$$
Recall [[Continuity]] to define continuity for these functions.
$$
C(\Omega,\mathbb{R})=\{ f\in\mathcal{F}(\Omega,\mathbb{R}):f\text{ is continuous} \}
$$
$$
C_b(\Omega,\mathbb{R})=\{ f\in C(\Omega,\mathbb{R}):f\text{ is bounded} \}
$$
### Operations
$\mathcal{F}(\Omega,\mathbb{R})$ will be equipped with the usual addition and scalar multiplication. With these operations $\mathcal{F}(\Omega,\mathbb{R})$ becomes a [[Vector Spaces|Infinite Dimensional]] [[Normed Vector Space]]. (And by [[Stone-Weierstrass Theorem]], an [[Algebra]]). The function $\| \cdot \|:\mathcal{F}_b\to\mathbb{R}$ given by $\| f \|=\sup_{x\in\Omega}|f(x)|$ is a [[Normed Vector Space|Norm]] on $\mathcal{F}_b$, called the norm of uniform convergence.
### Theorem
If $\Omega=K$ is compact, we can say that $C_b(\Omega,\mathbb{R})=C(\Omega,\mathbb{R})$ (by [[Best Approximation]]).
## Sequences
- $\{ f_n \}_{n\geq 1}$, a [[Sequences and Series|Sequence]] of functions in $\mathcal{F}(\Omega,\mathbb{R})$ is said to converge pointwise in $\Omega$, if for each $x\in\Omega$, the sequence of real numbers $\{ f_n(x) \}_{n\geq 1}$ converges.
- $\{ f_n \}_{n\geq 1}$, a [[Sequences and Series|Sequence]] of functions in $\mathcal{F}(\Omega,\mathbb{R})$ with pointwise limit $f$ is said to converge uniformly in $\Omega$, if $\forall\varepsilon>0$, there exists $N$, such that $\forall x\in\Omega$ and $n>N$, 
$$\| f_n(x)-f(x) \|=\sup_{x\in\Omega}| f_n(x)-f(x) |<\varepsilon$$
### Properties
-  $f_n$ converges uniformly to $f$ on $\Omega$, and $f_n\in\mathcal{F}_b(\Omega,\mathbb{R})$, then $f\in\mathcal{F}_b(\Omega,\mathbb{R}).$
-  $f_n$ converges uniformly to $f$ on $\Omega$, and $f_n\in C(\Omega,\mathbb{R})$, then $f\in C(\Omega,\mathbb{R}).$
## Compactness
Let $(E,d)$ a [[Metric Spaces|Metric Space]] and $K$ a [[Compactness|Compact]] subset of $E$. We wish to characterize compact sets in $C(K,\mathbb{R}).$ We use [[Stone-Weierstrass Theorem|Stone-Weierstrass]] to characterize:
