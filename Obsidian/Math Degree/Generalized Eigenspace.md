---
aliases:
  - Generalized Eigenvectors
---
Motivation: Find a subspace that includes the eigenspace, behaves like one, and has dimension equal to the algebraic multiplicity of the eigenvalue.

Let $\dim V=n,$ $A:V\to V$ is a [[Linear Operators|Linear Operator]]. Write $\sigma(A)=\{ \lambda_{1},\dots,\lambda_m \}$ for some $m\leq n$. 
Let $\lambda \in\sigma(A)$. The generalized eigenspace for $\lambda$ is given by 
$$E_\lambda=\bigcup_{k=1}^{\infty}\ker(A-\lambda I)^{k}=\ker(A-\lambda I)\cup\ker(A-\lambda I)^{2}\cup\dots$$
## Remarks
- $E_\lambda \neq\{ 0 \}$ since it contains the eigenspace $\ker(A-\lambda I)$.
- $E_\lambda$ is a [[Vector Spaces|Subspace]] since for all $k$, $\ker(A-\lambda I)^{k}\subseteq \ker(A-\lambda I)^{k+1}$. 
- In a [[Vector Spaces|Finite Dimensional]] space, the containment cannot be strict for all $k$, so our union must be finite; there is a $k$ so that $E_\lambda=\ker(A-\lambda I)^{k}$. This $k$ is called the depth of $\lambda$, denoted here as $d(\lambda)$.
## Proposition
- $E_\lambda=\ker(A-\lambda I)^{d(\lambda)}$.
- $E_\lambda$ is invariant for $A$.
- $(A-\lambda I)^{d(\lambda)}|_{E_\lambda}=0$.
- $\sigma(A|_{E_\lambda})=\{ \lambda \}.$
## Theorem
There is a diagonalizable $D$ and a nilpotent $N$ so that:
$$ A=D+N; \quad DN=ND $$
# Decomposition
See [[Block Diagonalization]] 