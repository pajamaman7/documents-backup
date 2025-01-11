---
tags:
  - DiffEqns
---
Consider the linear, 2nd order, non-homogenous [[Differential Equations|DE]]:
$$(a_{0}(t)D^{2}+a_{1}(t)D+a_{2}(t))x=E(t)$$
Where all $a$ are continuous for all $t$ in some interval $I$ and $a_{0}(t)\neq 0$, $t\in I$.
If we are given two solutions $h_{1},h_{2}$ or we can find them easily, then the particular solution is given by:

$$x(t)=c_{1}(t)h_{1}(t)+c_{2}(t)h_{2}(t)$$
With:
$$c_{1}(t)=-\int \frac{h_{2}(t)E(t)}{a_{0}(t)W} \, dt\quad c_{2}(t)=\int \frac{h_{1}(t)E(t)}{a_{0}(t)W} \, dt $$
Where $W$ is the [[Wronskian]] of our [[Differential Equations|DE]].
Then our general solution is:
$$x(t)=c_{3}h_{1}+c_{4}h_{2}+c_{1}(t)h_{1}+c_{2}(t)h_{2}$$
### Remarks
- Variation of Parameters cannot be used unless two linearly independent solutions are known
- Variation of Parameters can always be used for second order DEs, but it will typically be more useful to use the methods in [[Linear nth Order Differential Equations]] or [[Differential Equations - Cauchy-Euler]] when applicable.
- We can generalize this method to higher order DEs, however it quickly becomes impractical thanks to the 3x3 or larger [[Wronskian]] we have to calculate.