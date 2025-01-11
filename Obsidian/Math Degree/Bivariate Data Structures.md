A Bivariate Data Structure is one that can be modeled as a [[Functions|Function]] of two variables. These can be either continuous or discrete. Suppose $X$, $Y$ are random variables.

If $X,Y$ are discrete:
- $P(X=x\cap Y=y)=P(X=x,Y=y)=p(x,y)$
- $P(X\leq x, Y\leq y)=F(x,y)=\sum\limits^{x}\sum\limits^{y}p(x,y)$
- $0\leq p(x,y)\leq1; \: \forall x\in X, y\in Y$
- $\sum\limits_{all x}\sum\limits_{all y}p(x,y)=1$

If $X,Y$ are continuous:
- $f(x,y)\geq0; \: \forall x\in X, y\in Y$
- $\int_{all\: x}\int_{all\: y}f(x,y)dydx=1$
- $P(X\leq x,Y\leq y)=F(x,y)=\int\limits_{-\infty}^{y}\int\limits_{-\infty}^{x}f(x,y)\mathrm{dxdy}$

## Isolating a Cdf

Given a function $f(x,y)$, we can find the following:

If $f$ is continuous:
- $f(x)=\int f(x,y)dy$
- $f(y)=\int f(x,y)dx$

If $f$ is discrete:


 