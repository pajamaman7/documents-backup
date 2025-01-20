Let $T:V\to V$ be a [[Linear Operators]] with $\dim V=n$. We say that $T$ is diagonal with respect to a basis $\beta=\{ b_{1},\dots,b_n \}$ if the [[Matrix Representations of Linear Maps]] for $T, [T]_\beta$ is a diagonal matrix. Equivalently, there are constants $\lambda_1,...,\lambda_n$ so that $Tb_j=\lambda_j b_j$ for $j=1,\dots,n$, where $[T]_\beta=diag\{ \lambda_{1},\dots,\lambda_n \}$. We say that $T$ is diagonalizable if there is a basis $\beta$ for which $T$ is diagonal with respect to $\beta$.
## Eigenvectors
A diagonalizable matrix $T:V\to V$ is diagonalizable if and only if $V$ has a basis of eigenvectors.
## Theorem
An $n\times n$ matrix $A$ is diagonalizable if and only if there exists an invertible $S$ so that $S^{-1}AS$ is diagonal.
## Nilpotent matrices
Any nonzero nilpotent matrix is not diagonalizable.
## Theorem
If a $n\times n$ matrix $A$ has $n$ distinct eigenvalues, then $A$ is diagonalizable. The converse is false (Example, the zero or identity matrix).
## TFAE
- $T$ is diagonalizable
- $T$ is similar to a diagonal matrix
- $T$ has a basis of eigenvectors
- $g(\lambda)=a(\lambda)\forall\lambda \in\sigma(T)$.
## Cayley-Hamiltion Theorem for Diagonalizable Matrices
If $A$ is diagonalizable, then $C_A(A)=0$.