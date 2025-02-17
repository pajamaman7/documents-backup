This page is currently about $\mathbb{C}^{n}$, some properties will hold in abstract [[Inner Product Space|Inner Product Spaces]]
# Triangulizability
Let $A:V\to V$. $A$ is called upper triangular with respect to an [[Orthogonality|Orthonormal Basis]] $\{ b_{1},\dots,b_n \}$ if:
$$
\begin{align}
Ab_{1}&\in \text{span  }\{ b_{1} \}\\
Ab_{1}&\in \text{span  }\{ b_{1},b_2 \}\\
&\vdots\\
Ab_{n-1}&\in \text{span  }\{ b_{1},\dots,b_{n-1}\}\\ \\
\end{align}
$$
Or equivalently, $A=[a_{ij}]$ has $a_{ij}=0$ if $i>j$
If such a basis exists, we get a lattice of invariant subspaces for $A$:
$$
\{ 0 \}= E_{1}\subseteq\dots\subseteq E_n=V
$$
with $\dim E_j=j$, $E_j=\text{span }\{ b_{1},\dots,b_j \}$, and $AE_j\subseteq E_j$.
# Statement
Let $T:V\to V$ in a [[Vector Spaces|Finite Dimensional]] [[Inner Product Space]] over $\mathbb{C}$. There is an onto $\beta=\{ b_{1},\dots,b_n \}$ so that $[T]_\beta$ is upper triangular.
## Proof
Let $\lambda_{1} \in\sigma(T)$ and $b_{1}$ be a unit eigenvector for $\lambda_{1}$. Extending $b_{1}$ to any orthonormal basis gives the [[Matrix Representations of Linear Maps]]:
$$
[T]=\begin{bmatrix}
\lambda_{1} &*&* \\
0  &A_{2}\\
\vdots& 
\end{bmatrix}
$$
Then continue with $A_{1}$, doing the same process, finding $\lambda_{2}\in\sigma(A_{2})$ and a unit eigenvector orthogonal to $b_{1}$, call it $b_{2}$.
And then we repeat until $\lambda_n$, eventually giving us an upper triangular matrix.
### Notes
- $\sigma(T)=\{ \lambda_{1},\dots,\lambda_n \}$
-  If we write $U = [b_{1} \dots b_n]$, so that $U$ is [[Adjoints|Unitary]], $T\sim_U$ an upper triangular matrix.
- $b_{1}$ is an eigenvector but $b_{2},\dots,b_n$ may not be.
## Applications
If $\sigma(A)=\{ \lambda_{1},\dots,\lambda_n \}$ for some $A\in M_n(\mathbb{C})$, then $\det A=\lambda_{1}\lambda_{2}\dots\lambda_n$. Find a unitary $U$ and upper triangular $T$ so that $U^*AU=T$. We know $\sigma(A)=\sigma(T),$ so 
- $\det T=\lambda_{1}\lambda_{2}\dots\lambda_n=\det A$
- $tr A=tr T$