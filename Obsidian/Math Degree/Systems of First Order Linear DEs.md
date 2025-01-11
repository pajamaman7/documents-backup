---
tags:
  - DiffEqns
---
## Constant Coefficients - 2 equations
Consider the system of equations:
$$\begin{align}
Dx&=\alpha x+\beta y+f_{1} \\
Dy&=\gamma x+\delta y+f_{2} \\
\end{align}$$
With $\alpha,\beta,\gamma,\delta \in\mathbb{R}$ not all zero, and $f_{1},f_{2}$ functions of our independent $t$. We must solve for $x$ as well as $y$.
These two equations become
$$\begin{align}
(D-\alpha)x-\beta y&=f_{1} \\
-\gamma x+(D-\delta)y&=f_2
\end{align}$$
We can solve using [[Gaussian Elimination]], giving us a [[Linear nth Order Differential Equations|Linear 2nd order Differential Equation]]. Then once we have solved for one dependent variable, we can differentiate and substitute back into our original equations to solve for the other variable.
*note that this is an outline of the process which will vary greatly for every problem*
### Homogenous
The system is homogenous if and only if $f_{1}=f_{2}=0$.