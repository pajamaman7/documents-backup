---
tags:
  - NumThry
---
Given a set of integer values $a,b,c\ldots$, a *Linear Diophantine Equation* is one which takes the form $ax+by=c$ where $x,y$ must be solved for. (This can be extended to any number of variables). An equation of this form, if solvable, will have infinitely many solutions.
## Solvability
A linear diophantine equation $ax+by=c$ has solutions $x,y\in\mathbb{Z}\iff c|gcd(a,b)$. 
A result of this fact is that if $\gcd(a,b)=1$, or $a,b$ are coprime, then the equation has solutions.
## Finding solutions
A single solution to a linear diophantine equation can be found by performing [[Euclid's Recursive Algorithm]] (Not only is this the first step of the process, this is necessary to determine whether the equation is solvable), then reversing it to find solutions.

Supposing a single solution $x_0,y_0$ has been found to the equation $ax+by=0$, all solutions can be found with the formula:
$$x=x_0+n\cdot\frac{lcm(a,b)}{a},\quad y=y_0-n\cdot\frac{lcm(a,b)}{b}$$