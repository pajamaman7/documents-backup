---
aliases:
  - Differentiable
  - Derivative
---
Differentiation is the process of taking the derivative of a function. The derivative of a function gives us the slope of a function at a given point. This can be notated several different ways. In general, when $y=f(x)$,
$$\frac{dy}{dx}=y' = f'(x)$$
Graphically, this can be thought of as the slope of the tangent line to the curve at $(x,f(x))$
## First Principles
The derivative of a function can be found algebraically using [[Limits]], and the formula is given by:
$$\frac{dy}{dx}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$
Note that some derivatives are tedious to obtain through this method. For most polynomials, this section will suffice for differentiation. However, a [[List of Derivatives]] might be needed for some more complicated functions.
## Power Rule
Otherwise, we can use the Power Rule to differentiate a function. For a function of $x$, and some integer $n$, we can say that:
$$\frac{d}{dx}x^{n}=nx^{n-1}$$
Note that derivatives can be distributed across sums. That is, 
$$\frac{d}{dx}(f(x)+g(x))=f'(x)+g'(x)$$
## Product Rule
However, derivatives cannot be distributed across products. In general, 
$$\frac{d}{dx}f(x)g(x) = f'(x)g(x)+f(x)g'(x)$$
## Quotient rule
Likewise, quotients of functions require their own formula.
$$\frac{d}{dx}\frac{f(x)}{g(x)}=\frac{f'(x)g(x)-f(x)g'(x)}{g^2(x)}$$
## Chain rule
Finally, a rule is needed for functions which are nested inside each other.
$$\frac{d}{dx}f(g(x))=f'(g(x))g'(x)$$