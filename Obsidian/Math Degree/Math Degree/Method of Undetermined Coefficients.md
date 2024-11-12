---
tags:
  - DiffEqns
aliases:
  - UC Functions
  - UC Sets
---
The method of undetermined coefficients is used to solve [[Linear nth Order Differential Equations]]. Considering a DE of the form:
$$P(D)x=E(t)$$
## UC functions
We call $E$ a UC function if it takes one of the following forms:
- $e^{at}$
- $\cos\alpha t,\,\sin\beta t$
- $\cosh\alpha t,\,\sinh\beta t$
- Any polynomial in $t$ of finite degree
- A product of the functions above
## UC Sets
The UC set of a single UC function $f$ is all the different derivatives of $f$ up to a constant multiple.
If we have a product of two functions, our UC set is the set of all products of their UC sets.
### Revising the UC set
For a UC set $S$ and a fundamental set $H$, we may not allow the two sets to share a member. ($H\cap S=\varnothing$). To revise the set $S$ we multiply by $t^{k}$ where $k$ is the lowest natural number so that $H$ and $S$ no longer have an element in common.