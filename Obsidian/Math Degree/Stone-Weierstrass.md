# Original formulation (Weierstrass)
If $f:[a,b]\to \mathbb{R}$ is continuous, then for any $\varepsilon>0,$ there exists some $N$ and a polynomial $p_N$ of degree at most $N$ so that $\| p_n-f \|=\sup_{x\in[a,b]}|p_n(x)-f(x)|<\varepsilon$.
## Corollaries
(Refer to [[Function Spaces for Math 445]] for notation)
- The subspace $\mathcal{P}\subseteq C([a,b],\mathbb{R})$ of polynomials with real coefficients is dense in $C([a,b],\mathbb{R}).$
- The subspace $\mathcal{P}_\mathbb{Q}\subseteq C([a,b],\mathbb{R})$ of polynomials with rational coefficients is dense in $C([a,b],\mathbb{R}).$
- $C([a,b],\mathbb{R})$ is [[Connectedness|Separable]]; it contains a countable dense set.
# Stone-Weierstrass (Real version)
Algebras are defined strangely in Math 445; I will be defining them here to avoid conflict. 
For a [[Metric Spaces|Metric Space]] $X\supseteq\Omega$, we define the algebra on $C(\Omega,\mathbb{R})$, by functional and scalar multiplication. A subalgebra is defined typically.
## Statement
Let $(E,d)$ be a metric space; and $K$ a [[Compactness|Compact]] subset of $E$. Let $G$ be a subalgebra of $C(K,\mathbb{R})$. Suppose $C,G$ are equipped with the norm of uniform convergence. If:
- The unit function $1\in C(K,\mathbb{R})$ defined by $1(x)=1$, $x\in K$ belongs $G$
- $G$ separates the points of $K$, given any distinct $x,y\in K$, there exsts $g\in G$ so that $g(x)\neq g(y)$
Then $G$ is dense in $C(K,\mathbb{R})$; if $f\in C(K,\mathbb{R})$, then $\forall\varepsilon>0,\exists f_\varepsilon \in G$, so that $\| f-f_\varepsilon \|\leq K$.
# Alternate Statement
Let $(E,d)$ be a metric space; and $K$ a [[Compactness|Compact]] subset of $E$. Let $G$ be a subalgebra of $C(K,\mathbb{R})$. Suppose $C,G$ are equipped with the norm of uniform convergence. If:
- $G$ doesn't vanish at any point in $K$, $\forall x\in K$, $\exists f\in G: f(x)\neq 0$
- $G$ separates the points of $K$, given any distinct $x,y\in K$, there exists $g\in G$ so that $g(x)\neq g(y)$
Then $G$ is dense in $C(K,\mathbb{R})$; if $f\in C(K,\mathbb{R})$, then $\forall\varepsilon>0,\exists f_\varepsilon \in G$, so that $\| f-f_\varepsilon \|\leq K$.