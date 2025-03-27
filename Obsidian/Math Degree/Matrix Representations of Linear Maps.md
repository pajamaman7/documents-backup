---
aliases:
  - Matrix Representation
---
## Basis Coordinates
Suppose $\dim V=n$ and $\dim W=m$ and let $\beta=\{ b_{1},\dots,b_n \}$ a [[Vector Spaces|Basis]] for $V$, $\Delta=\{ d_{1},\dots,d_m \}$ a basis for $W$. If $V=\alpha_{1}b_{1}+\dots+\alpha_nb_n$, then we write:
$$
[v]_\beta=\begin{bmatrix}
\alpha_{1}\\ 
\vdots\\
\alpha_n
\end{bmatrix}
$$
where the map $[\cdot]_\beta$ is an isomorphism from $V$ to $\mathbb{C}^{n}$.
## Matrix of a Linear Transformation 
If $T:V\to W$ is a [[Linear Operators|Linear Transformation]] then the basis representation of $T$w.r.t $\beta,\Delta$ is 
$$
[T]_{\beta\Delta}=\begin{bmatrix}
\begin{bmatrix}
Tb_{1}
\end{bmatrix}_\Delta  
&\dots&\begin{bmatrix}
Tb_n
\end{bmatrix}_{\Delta}
\end{bmatrix}
$$
Which is a $m\times n$ matrix in $\mathbb{M}_{mn}(\mathbb{C})$. The map $T\mapsto [T]_{\beta\Delta}$ is also an isomorphism.