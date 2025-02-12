A real function of several variables is simply a [[Functions|Function]] $f:\mathbb{R}^{n}\to \mathbb{R}$.
Recall [[Functions|Domain]], [[Functions|Range]], etc as usually defined for functions.
## Graph
The set $G$ of all points $(x,f(x))=(x_{1},\dots,x_n,f(x))$ is called the graph of $f$.
## Continuity 
Continuity in this case is defined identically as for [[Limits and Continuity in Metric Spaces]].
$f$ is continuous at $c$ if, $\forall\varepsilon>0\,,\exists\delta>0: \| x-c \|<\delta\implies|f(x)-f(c)|<\varepsilon$. This turns out to be equivalent regardless of the norm chosen.
### Equivalent definitions
TFAE to the above definition
- $f$ is continuous if the preimage of every open set in $\mathbb{R}$ is open in $\mathbb{R}^{n}$.
- For any [[Sequences and Series|Sequence]] $\{ a_{k} \}_{k\geq 1}$ convergent to $a$, the sequence $\{ f(a_k) \}_{k\geq 1}$ converges to $f(a)$.
### Properties
Sums, differences, quotients, products, scalar multiples, and composition maintain continuity as per the usual conditions.