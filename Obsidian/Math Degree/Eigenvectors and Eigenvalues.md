## Eigenvalues and vectors
$\lambda$ is an eigenvalue of a [[Linear Operators|Linear Operator]] $T$ if there is some $v \neq{0}$ in V so that $Tv=\lambda v$. In this case $v$ is an eigenvector
### Multiplicities
#### Algebraic multiplicities
Let $\lambda$ be an eigenvalue of a operator $A$. Then $k$ is the algebraic multiplicity of $\lambda$ if and only if $(z-\lambda)^{k}|C_A(z)$ and $(z-\lambda)^{k+1}\not\mid C_A(z)$. Denote this $a_A(\lambda)$ or $a(\lambda)$ if it proves clear enough.
#### Geometric multiplicities
Let $v_{1},\dots,v_n$ be eigenvectors associated with the same eigenvalue $\lambda$, then the geometric multiplicity of $\lambda$ is given by $g_A(\lambda)=\dim \ker(\lambda I-A)$.
Note that for any eigenvalue, the geometric multiplicity must be less than or equal to its algebraic multiplicity;
$$
a(\lambda)\leq g(\lambda)
$$
##### Corollary
$T$ is diagonalizable if and only if $g(\lambda)=a(\lambda)\forall\lambda \in\sigma(T)$.
## Spectrum
The spectrum of $T$ above is:
$$
\sigma(T)=\{ \lambda \in\mathbb{C}|\lambda \text{ Is an eigenvalue of }T \}
$$
For a fixed $\lambda$, the set of eigenvectors associated is the eigenspace $\ker(T-\lambda I)$
## Application of Matrix Representations
Use [[Matrix Representations of Linear Maps]] to represent $T$ as an $n\times n$ matrix $A$. Under this representation we maintain $\sigma(A)=\sigma(T)$
### Characteristic Polynomial
Given the $n\times n$ matrix $A$, the characteristic polynomial is the determinant $C_A(z)=\det(zI-A)$. We can find $\sigma(A)$ as the roots of this polynomial.
#### FTA
Thanks to the [[Fundamental Theorem of Algebra]], this polynomial has $n$ roots over $\mathbb{C}$, counting multiplicities ($\mathbb{C}$ is [[Splitting Fields|Algebraically Closed]]).
#### Corollary
Every $n\times n$ matrix $A$ over $\mathbb{C}$ has exactly $n$ eigenvalues (counting multiplicities).