For any differentiable function $F:U\to\mathbb{R}$ with $F(x_1,\ldots,x_n)=0$, we have $\frac{\partial x_i}{\partial x_j}=\frac{-F_{x_j}}{F_{x_i}}$  

Suppose $f_1,\ldots,f_n$ are differentiable scalar functions in the variables $y_1\ldots y_n,x_1\ldots x_n$ and consider the equations:
$$\begin{align*} f_1(b_1,\ldots,b_n,a_1,\ldots,a_m)&=c_1\\
\vdots\\
f_w(b_1,\ldots,b_n,a_1,\ldots,a_m)&=c_n
\end{align*}$$
Write $\vec F=\begin{pmatrix}f_1&\ldots&f_n\end{pmatrix}^T$ 
and $DF(b_1,\ldots,b_n,a_1,\ldots,a_m)=\begin{bmatrix} B&|&A \end{bmatrix}$
If $B$ is invertible then we can locally solve for $y_1,\ldots,y_n$ in terms of $x_1,\ldots,x_m$ as 
$$\vec g(x_1,\ldots,x_m)=\begin{pmatrix}y_1&\ldots&y_n\end{pmatrix}^T$$
and $D\vec g(a_1,\ldots, a_m)= -B^{-1}A$.