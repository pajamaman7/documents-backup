Partial Differentiation is the [[Differentiation]] of a function which is dependent on multiple variables, with respect to a single variable. The first-order partial derivative is that with respect to a single variable. Because of this, any other variables that the function is dependent on can be treated as constants. 
Partial differentiation is notated as follows, for some function $f$ of two variables, $f(x,y)$.
$$\frac{\partial f}{\partial x}= f_x$$
And for $y$,
$$\frac{\partial f}{\partial y}= f_y$$
Of course, we are also able to take higher level derivatives of multivariable functions. For example, 
$$\begin{align*}
f_{xx}, f_{xy},f_{yx},f_{yy}
\end{align*}$$
Of course, there is a first principles definition of partial derivatives, but in most cases the typical [[Differentiation]] rules such as the chain, product, and quotient rules will still apply and be helpful.
## Multivariable Chain Rule
The multivariable chain rule allows us to take partial derivatives of multivariable compositions of functions.
Suppose $z=f(x,y)$, $x=g(s,t)$ and $y=h(s,t)$. That is, $f$ is a function of $x$ and $y$, and $x,y$ are each functions of $s,t$.
Then:
$$\begin{align*}
\frac{\partial z}{\partial s} &= \frac{\partial f}{\partial x}\frac{\partial x}{\partial s}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial s}\\
\frac{\partial z}{\partial t} &= \frac{\partial f}{\partial x}\frac{\partial x}{\partial t}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial t}
\end{align*}$$
## Properties
For a twice continuously differentiable scalar function $\Phi$, we have equality of second order mixed partials