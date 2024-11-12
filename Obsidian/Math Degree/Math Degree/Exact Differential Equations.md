Exact [[Differential Equations]] are the most yucky type of first order differential equation. They take the form:
$$M(x,y)+N(x,y)\frac{dy}{dx}=0$$ where $M_x=N_y$. The solution to such equations is given by the function $\Psi(x,y)=c$ where $\Psi_x=M(x,y)$ and $\Psi_y=N(x,y)$.

To find such a function $\Psi$, we take $\int Mdx+h(y)=\Psi$ or $\int Mdy+h(x)=\Psi$, solving for $h$ using the other partial derivative of $\Psi$.

## Non-Exact DEs
Given the non-exact DE:
$$M(t,x)+N(t,x)=0$$
Where $M,N$ have continuous partial derivatives on some domain $D\in\mathbb{R}$.
- Case 1: 
    If the quantity $\frac{1}{N}(\frac{\partial M}{\partial x}-\frac{\partial N}{\partial t})$ is a function of only $t$, the DE has an integrating factor $\mu(t)=e^{\int\frac{1}{N}(\frac{\partial M}{\partial x}-\frac{\partial N}{\partial t})dt}$
- Case2:
    If the quantity $\frac{1}{M}(\frac{\partial M}{\partial x}-\frac{\partial N}{\partial t})$ is a function of only $x$, the DE has an integrating factor $\mu(x)=e^{-\int\frac{1}{M}(\frac{\partial M}{\partial x}-\frac{\partial N}{\partial t})dx}$

