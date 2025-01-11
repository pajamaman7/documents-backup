---
tags:
  - DiffEqns
---
Given a [[Differential Equations|DE]]: 
$$a_{0}(x)y''+a_{1}(x)y'+a_{2}(x)y=0$$
Suppose $x=x_{0}$ is an ordinary point for this DE. The DE then has two linearly independent solutions in powers of $x-x_{0}$, taking the form 
$$y=\sum_{n=0}^{\infty} a_n(x-x_{0})^{n}$$
with $a_{0}\neq 0$ valid for all $x$ such that $|x-x_{0}|<R$ for some $R>0$.
#### Solving for coefficients
To find our coefficients, we substitute $y,y',y''$ into our $DE$ and we obtain an identity. Then we equate all coefficients of $(x-x_{0})$ to 0 and solve the resulting equation.