An Ordinary Differential Equation (Also known as a ODE) is a [[Differential Equations|Differential Equation]], containing an unknown function of a single variable together with its derivative with respect to that variable. In other words, it is not a [[Partial Differential Equation]].

The Order of an ODE is the order of the highest derivative in the equation.
## Solutions to ODEs
A solution to an ODE on an interval $I$ is a function having sufficient derivatives (matching the order of the ODE), that satisfies the Differential Equation on the interval $I$.
## Existence of a solution - FODE
Consider 
$$\begin{cases} 
\frac{dy}{dx}=f(x,y)\\
 y(x_0)=y_0\\
 \end{cases}$$
This IVP may have one, zero or infinitely many solutions.

If $f(x,y), f_y(x,y)$ are both be continuous for all $(x,y)$ in a rectangular region $R$ that contains the point $(x_0,y_0)$, then the DE has a unique solution. The converse however does not hold.

If the function is continuous on some $R\subset \mathbb{R}^2$, but $f_y(x,y)$ is not, then the solution exists but is not unique.