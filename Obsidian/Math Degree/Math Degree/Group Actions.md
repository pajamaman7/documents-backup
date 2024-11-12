Given a [[Groups|Group]] $G$, and another set $X$, we say "$G$ acts on $X$", or "$X$ is a $G$-set" and write $G\curvearrowright X$ when there exists a mapping $f$:
$$f:G\times X\to X,\quad (g,x)\mapsto g\cdot x$$
Satisfying:
- $e\cdot x=x$ (Unitality)
- $a\cdot(b\cdot x)=(ab)\cdot x$ (Associativity)
## Properties
- $g\cdot x=g\cdot y\implies x=y$
- $a\cdot x=b\cdot y\implies(b^{-1}a)\cdot x=y$
- For any set $X$ we already have $B(X)$, the group of bijective functions from $X$ to $X$. $B(X)\curvearrowright X$.
- Group actions are essentially homomorphisms from $G$ to $S_X=\{ f:X\to X| f\text{ is a bijection} \}$
## Orbit and Stabilizers
For any $x \in X$, 
### Orbit
$$G\cdot x=Orb(x)=\{ g\cdot x|g\in G \}$$
For any finite group $G$, $|Orb(x)|=[G:Stab(x)]$, or $|G|=|Orb(x)|\cdot|Stab(x)|$
### Stabilizer
$$Stab(x)=\{ g\in G|g\cdot x=x \}$$
Which is a subgroup of G.
### Fixed set
The fixed set of $X$ is 
$$
X_{f}=\{ x \in X|gx=x \forall g\in G \}
$$
### Orbit-Decomposition Theorem
If $G,X$ are finite,
$$|X|=|X_f|+\sum\limits_{\forall! Orb(x)}|Orb(x)|=|X_f|+\sum\limits_{\forall i }^{}|G:Stab(x_i)|$$
Where $X_f$ is the set of all fixed points.
### Orbit-Stabilizer Theorem
Let $G$ be a finite [[Groups|Group]] $G\curvearrowright X$ and $x \in X$. Then
$$
\left| G \cdot x \right|=[G:Stab(x)]=\frac{|G|}{|Stab(x)|} 
$$
### Action by conjugation
Let $G$ act on itself by conjugation. Then $G\cdot h=class(h)$, the conjugacy class of $h$. From Orbit-Decomposition we can reobtain the [[Class Equation]] of $G$:
$$
|G|=|Z(G)|+\sum\limits_{i=1 }^{n}[G:N(g_i)]
$$
## Examples
- The trivial action: $g\cdot x=x$
- $G\curvearrowright G$, $g\cdot x=gxg^{-1}$ is a group action
- $H\leq G$, $H\curvearrowright G,\,h\cdot g= hg$  is a group action
- $S_n\curvearrowright X_n$; $\sigma\cdot x \in X$.
- $D_n\curvearrowright$ vertices of an $n$-gon
- $\mathbb{R} \setminus \{ 0 \}\curvearrowright R^{n}$