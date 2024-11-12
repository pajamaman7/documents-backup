Let $\left\{ f_{1}(t),f_{2}(t),\dots,f_n(t) \right\}$ be a given set of $n$ functions defined on some interval $I$. The Wronskian of $f_{1},f_{2},f_{3}\dots f_n$ is the [[Determinant]] of order $n$:
$$W(f_{1},f_{2},\dots f_n)=\det \begin{bmatrix}
f_{1}(t)&f_{2}(t)&\dots &f_n(t)\\ 
f_{1}'(t)&f_{2}'(t)&\dots&f_n'(t) \\
\vdots & & & \vdots\\
f_{1}^{n-1}(t)&f_{2}^{n-1}(t)&\dots&f_n^{n-1}(t)
\end{bmatrix}$$
The value of the Wronskian at $t=t_{0}$ is written $W(f_{1},f_{2},\dots f_n)(t_{0})$.
If $W(f_{1},f_{2},\dots f_n)(t_0)\neq0$ for some $t_{0}$, the set of solutions is linearly independent.