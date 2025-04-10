---
aliases:
  - Jordan Basis
  - Jordan Decomposition
---
Suppose $N$ is a nilpotent operator. A set of generalized eigenvectors $\{ v_{1},\dots,v_k \}$ is called a cycle of length $k$ if:
$$
\begin{align}
Nv_{1}&=0 \\
Nv_{2}&=v_{1} \\
&\vdots \\ Nv_k&=v_{k-1}
\end{align}
$$
A basis of cycles is called a Jordan Basis for $N$.
## Theorem
Let $N:V\to V$ be nilpotent with $C_{1},\dots,C_m$ cycles of lengths $p_{1},\dots,p_m$. If the initial vectors in each $C_i$ (each in $\ker N$), are [[Vector Spaces|Linearly independent]], then $C_{1}\cup\dots\cup C_m$ is also linearly independent, and the cycles are disjoint.
## Existence of a Jordan Basis
For any $N:V\to V$, there is a Jordan Basis of cycles for $N$.
### Nilpotency
The longest cycle length is the depth of $0$, also equal to the index of nilpotency.
## Matrix Representation
Let $\beta=C_{1}\cup\dots\cup C_d$ be a Jordan basis for $N$. Then when we take the[[Matrix Representations of Linear Maps|Matrix Representation]] of $N$ w.r.t $\beta$ we get a block diagonal matrix with nilpotent diagonal entries like:
$$
B_i=\begin{bmatrix}
0&1&0&\dots&0 \\
&0&1&&\vdots \\
\vdots&&\ \ddots \\
0&&\dots&&0
\end{bmatrix}
$$
A zero matrix with only ones on the superdiagonal. Conventionally we take the blocks in descending size.
A *Jordan cell* is of the form $\lambda I+B_i$, for some $\lambda$, and a Jordan Block is a block diagonal matrix of Jordan cells with the same $\lambda$.
## Jordan Decomposition Theorem
Let $A:V\to V$ be linear, $\sigma(A)=\{ \lambda, \dots,\lambda_n \}$. Then there is a [[Vector Spaces|Basis]] of $V$ consisting of [[Generalized Eigenspace|Generalized Eigenvectors]] of $A$, so that
- $[A]$ is block diagonal of $m$ Jordan blocks, with the $j$th block associated with $\lambda_j$.
- The size of the $j$th block is $a(\lambda_j)=\dim E_{\lambda_j}$
- The size of the largest $\lambda_j$-cell within the $\lambda_j$ block is the depth $d(\lambda_j)$.
- The number of cells within each block is the geometric multiplicity $g(\lambda_j)$.
### Algorithm to find Jordan Form
For $A:V\to V$
- Find $\sigma(A)$
- Compute eigenspaces: $\ker(\lambda I-A)$; $g(\lambda_j)=\dim\ker(\lambda_jI-A)$
- Compute [[Generalized Eigenspace]]s for all $\lambda_j$ where the algebraic multiplicity exceeds the geometric
	- Method 1 (always works): Find $\ker(A-\lambda_jI),\ker(A-\lambda_jI)^{2},\dots$ until they stop getting bigger.
	- Method 2 (sometimes works): If $(A-\lambda_jI)v_{1}=0$, try solving $(A-\lambda_jI)v_{2}=v_{1}$ to generate a cycle.
- Pray this gives a cycle basis for $E_{\lambda_j}$
## Theorem
$A$ and $B$ are similar iff they have the same Jordan form. (Up to reordering of blocks).
## Minimal Polynomial
A minimal polynomial for a [[Linear Operators|Linear Operator]] $A:V\to V$ is a monic polynomial $p(z)$ of minimal degree so that $p(A)=0$.
### Minimal polynomials for Jordan Forms
If we have found a Jordan form for a polynomial with eigenvalues $\lambda_{1},\dots,\lambda _n$, we have a minimal polynomial:
$$
m(z)=(z-\lambda_{1})^{d(\lambda_{1})}\dots(z-\lambda_n)^{d(\lambda_n)}
$$
### Theorem
$A$ is [[Adjoints|Unitarily Diagonalizable]]  if and only if $d(\lambda)=1$, for every eigenvalue $\lambda$.