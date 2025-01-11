---
tags:
  - DiffEqns
---
A *Cauchy-Euler* type [[Differential Equations|DE]] is one of the form:
$$a_{0}t^{2}x''+a_{1}tx'+a_{2}x=0$$
with $t<0$ or $t>0$ and all $a\in\mathbb{R}$, $a_{0}\neq 0$. 
## Solutions
Solutions take the form $x(t)=t^{k}$, where $k\in\mathbb{Z}$ and is given by the solutions to the quadratic (known as the indicial equation):
$$a_{0}k(k-1)+a_{1}k+a_{2}=0$$
### Cases
- Two distinct roots $k_{1},k_{2}$:
        The set of solutions is given by: $H=\{ t^{k_{1}},t^{k_{2}} \}$, and the general solution is given by:
        $x(t)=c_{1}t^{k_{1}}+c_{2}t^{k_{2}}$
- One root with multiplicity 2:
        The set of solutions is: $H= \{ t^{k}, t^{k}\ln t \}$ and the general solution is given by: $x(t)=t^{k}(c_{1}+c_{2}\ln t)$.
- Complex conjugate roots $k_{1,2}=a\pm bi$:
        The set of solutions is given by: $H=\{t^{a}\cos(b\ln t), t^{a}\sin (b\ln t)\}$ and the general solution is: $x(t)=c_{1}t^{a}\cos (b\ln t)+c_{2}t^{a}\sin(b\ln t)$.
## Non-Homogenous
If the [[Differential Equations|DE]] is non-homogenous, use Cauchy-Euler to find a homogenous solution, then use [[The Method of Variation of Parameters]] to obtain a general solution.
## Order $n$
The process generalizes to higher order [[Differential Equations|DE]]s as well.