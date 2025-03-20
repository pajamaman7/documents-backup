Let $f:\mathbb{R}^{n+p}\to \mathbb{R}^{p}$ in $C^{1}(E)$ for $E\subseteq \mathbb{R}^{n+p}$ open. Write $f=(f_{1},\dots,f_p)$. Consider the system $f(x,y)=0$ If $(a,b)\in E$ is such that $f(a,b)=0$ and $\partial_yf(a,b)$ is invertible, then there exists $\Omega_a\subseteq \mathbb{R}^{n}$ an open neighborhood of $a$, $W_b\subseteq \mathbb{R}^{p}$ an open neighborhood of $b$, and a unique function $\varphi:\mathbb{R}^{n}\to\mathbb{R}^{p}$ in $C^{1}(\Omega_a)$ so that $\varphi(a)=b$, $f(x,\varphi(x))=0$, $\forall x\in\Omega_a$, 
$$\partial_x\varphi(x)=-\left( \partial_yf(x,\varphi(x)) \right)^{-1}\partial_xf(x,\varphi(x)),\forall x\in\Omega_a$$ 
$$
Jf(x,y)=\begin{bmatrix}
\frac{ \partial f_{1} }{ \partial x_{1}} & \dots & \frac{ \partial f_{1} }{ \partial x_n } &\frac{ \partial f_{1} }{ \partial y_{1} } & \dots & \frac{ \partial f_{1} }{ \partial y_p } \\  
\vdots &  & \vdots & \vdots &  & \vdots \\
\frac{ \partial f_{q} }{ \partial x_{1}} & \dots & \frac{ \partial f_{q} }{ \partial x_n } &\frac{ \partial f_{q} }{ \partial y_{1} } & \dots & \frac{ \partial f_{q} }{ \partial y_p } 
\end{bmatrix}=\begin{bmatrix}
\partial_xf&\partial_yf
\end{bmatrix}
$$