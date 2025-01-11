---
tags:
  - DiffEqns
  - Needs_Rewrite
---
A linear $n$th order differential equation in the dependent variable $x$ and independent $t$ is of the form (Written with $D$ as the [[Differential Operators]]):
$$a_{0}(t) D^nx+a_{1}(t) D^{n-1}x\dots a_{n}(t)x=E(t)$$
To ensure existence of a solution in some interval $I$, Assume all $a(t)$ and $E(t)$ are coefficient for all $t\in I$, and that $a_{0}\neq 0$.
We write $L=a_{0}(t) D^n+a_{1}(t) D^{n-1}\dots a_{n}(t)$. 
If $L$ is linear, then $L(c_{1}h_{1}+c_{2}h_{2})=c_{1}L(h_{1})+c_{2}L(h_{2})$.
## Characteristic Polynomial
A linear non-homogenous $n$th order DE $Lx=E(t)$:
$$L=a_{0}D^{n}+a_{1}D^{n}\dots a_{n-1}D+a_n$$
where all $a$ are constant real numbers, will be denoted by $L=P(D)$. Therefore the DE becomes $P(D)x=E(t)$. Since $P(D)$ is a polynomial in $D$ of degree $n$, we can replace $D$ with say $r$ and solve the polynomial. We call $P(r)=0$ the characteristic polynomial.

If our solutions to the polynomial $P(r)$ are given by $r_{1},r_{2}\dots r_n$, then our solutions are given below:
## Homogenous solutions
- If the characteristic equation $P(r)=0$ has distinct roots $r_{1},r_{2},\dots,r_k$, then the DE has $k$ linearly independent solutions:
$$h_i(t)=e^{r_it}:\quad i=1,2,\dots,k$$
- The characteristic equation $P(r)=0$ has a real root $r=r_{0}$ of multiplicity $m$. Then the DE has $m$ linearly independent solutions: $$t^0e^{r_{0}t},t^{1}e^{r_{0}t},\dots,t^{m-1}e^{r_{0}t}$$
- The characteristic equation $P(r)=0$ has complex conjugate roots $r_{1,2}=a\pm bi$. Then $$h_{1}(t)=e^{at}\cos bt,\quad h_{2}(t)=e^{at}\sin bt$$
- If the characteristic equation $P(r)=0$ has complex conjugate roots $r_{1,2}=a\pm bi$ of multiplicity $m$, the DE has $2m$ linearly independent solutions:$$t^0e^{at}\cos bt,t^1e^{at}\cos bt ,\dots,t^{m-1}e^{at}\cos bt$$
$$t^{0}e^{at}\sin bt,t^1e^{at}\sin bt , \dots,t^{m-1}e^{at}\sin bt$$
#### Special Cases
- If the characteristic equation $P(r)=0$ has only *imaginary roots*, $r_{1,2}=\pm bi$, the linearly independent solutions are given by:$$h_{1}(t)=\cos bt,\quad h_{2}(t)=\sin bt$$
- If the characteristic equation $P(r)=0$ has *real roots* $r_{1,2}=\pm k$, then either $$h_{1}(t)=e^{kd},\quad h_{2}(t)=e^{-kd}$$ or $$h_{1}(t)=\cosh kt,\quad h_{2}(t)=\sinh kt$$
### Fundamental Set
A *Fundamental Set* for a linear nth order homogenous DE is a set of $n$ functions:
$$\{h_{1}(t),h_{2}(t),h_{3}(t)\dots h_n(t)\}$$
Provided that:
- $h_{1},h_{2}\dots h_n$ are solutions to the DE 
- The set is linearly independent
### Homogenous solutions
Let $h_{1}(t),h_{2}(t)\dots h_m(t)$ be solutions to a linear and homogenous DE $L(x)=0$ on an interval $I$.
Any linear combination of these $m$ solutions is also a solution to the DE on $I$. 

Let $h_{1}(t),h_{2}(t)\dots h_n(t)$ be solutions to a [[Linear nth Order Differential Equations]] on an interval $I$. The set of solutions is Linearly independent if the [[Wronskian]] is nonzero: $W(f_{1},f_{2},\dots f_n)(t_{0})\neq 0$ for some $t_{0}$.
## Particular Solutions
A particular solution to a linear, non-homogenous DE is a solution that does not contain arbitrary constants, denoted $x_p(t)$.

To find a particular solution, we suppose that $E(t)$ is a linear combination of $m$ [[Method of Undetermined Coefficients|UC Functions]]: $f_{1},f_{2}\dots f_m$.
- Find the fundamental set $H$; all linearly independent solutions to $P(D)x=0$.
- Find the [[Method of Undetermined Coefficients|UC Sets]] for $E(t)$ and revise if needed into sets $S_{1},S_{2},\dots$ 
- Take the collection of revised and unrevised sets and create a linear combination: $x_p(t)=$linear combination of sets (use constant $k$'s, not $c$).
- Find $k_{1},k_{2}\dots$ by substituting $x_p,x_p'\dots$ into the non-homogenous DE $P(D)x=E(t)$. Expand and collect like terms until it becomes clear the value of each $k$.
## General Solution
The general solution to the linear $n$ th order non-homogenous DE:
$$Lx=E(t)$$
is of the form
$$x=x_h(t)+x_p(t)$$
where $x_h(t)$ is the solution to the DE $Lx=0$ and $x_p(t)$ is a particular solution.
