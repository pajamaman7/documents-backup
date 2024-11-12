---
tags:
  - DiffEqns
---
Consider the Linear 2nd order homogenous [[Differential Equations|DE]]:
$$a_{0}(x)y''+a_{1}(x)y'+a_{2}(x)y=0$$
where $a_{0}(x),a_{1}(x),a_{2}(x)$ are continuous for all $x$ in an interval $I$ and $a_{0}(x)\neq 0$ on $I$.
Assume a first solution $y_{1}(x)$ is known. We must find a second solution $y_{2}(x)$. Suppose this takes the form $y_{2}=y_{1} v(x)$. Through some derivation we obtain: 
$$a_{0}y_{1}v''+(2a_{0}y_{1}'+a_{1}y_{1})v'=0$$
And letting $u=v'$, $u'=v''$. We obtain a [[Separable First Order Differential Equations|Separable FODE]] in $u$:
$$a_{0}y_{1}u'+(2a_{0}y_{1}'+a_{1}y_{1})u=0$$
With a solution given by:
$$v'=u=y_{1}^{-2}e^{-\int \frac{a_{1}}{a_{0}} \, dx }$$
And this allows us to solve for $y_{2}$:
$$y_{2}=y_{1}\int \frac{\exp\left( -\int \frac{a_{1}}{a_{0}} \, dx  \right)}{y_{1}^{2}} \, dx $$
### SPECIAL CASE: TOMMYBUCKETS FIND!!
IF we have a common case (thanks to professors and TAs making the questions easy) where $a_{1}=-a_{0}'$, then our solution $y_{2}$ is given by:
$$y_{2}=y_{1}\int \frac{a_{0}}{{y_{1}}^{2}} \, dx $$
wow!