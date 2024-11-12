A *Dihedral Group* $D_n$ is a [[Groups|Group]] of reflection and rotation symmetries of a regular $n$-gon. Rotations are given by $\frac{2\pi k}{n}$, and we can find every reflection from a rotation and one reflection.

We can think of elements of $D_n$ as transformations from $\mathbb{C}^{2}\to \mathbb{C}^{2}$. Let $\left< r \right>$ be all rotation symmetries.
$$r=\begin{bmatrix}
e^{2\pi i/n}&0\\0&e^{-2\pi i/n} 
\end{bmatrix},\quad s=\begin{bmatrix}
0 & 1\\
1 & 0
\end{bmatrix}$$
And now we can write
$$D_n=\{ e,r,r^{2}\dots r^{n-1},sr,sr^{2},\dots, sr^{n-1} \}$$
### Properties
- $rs r=s\implies r^{j}s r^{j}=s$
- $D_n$ has $2n$ elements.