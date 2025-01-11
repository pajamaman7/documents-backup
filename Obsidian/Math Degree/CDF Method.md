---
aliases:
  - Method of Distribution Functions
---
The CDF method uses the [[Cumulative Distribution Function]] of a random variable to determine the [[Probability Density Function]] of another variable.

## Functions of one variable
Consider a continuous random variable $X$ with some PDF $f_{X}(x)$ and a CDF $F_X(x)$. 
Suppose we want the pdf of a new random variable $Y$ which is some function $g(X)$.
1. Find the CDF of $Y: F_Y(y)=P(Y<y)=P(g(X)\leq y)$
    - To do this we solve by integrating the PDF of $X$ over the region where $Y<y$. In other words, find the value of $P(g(X)<y)$
    - Differentiate the CDF $F_Y(y)$ with respect to $y$  to obtain $F_Y(y)$.
## Two Random variables
Let $X_{1},X_{2}$ be continuous random variables with PDFs of $f_{1}(x),f_{2}(x)$ respectively. Let $Y$ be a function of both of these random variables, $Y=g(X_{1},X_{2})$. 
1. Find the joint density function of $X_{1},X_{2}$, as well as its bounds. 
2. Find the CDF of $Y$: $F_Y(y)=P(g(X_{1},X_{2})<y)$. To do this we isolate for either $X_{1}$ or $X_{2}$ and integrate.
3. Differentiate $F_Y$ with respect to $y$ to obtain the PDF
## Method of Transformations for a Single Variable
Generalizing this, we can skip much of the nasty calculus. Let $Y=g(X)$ for random variables $X,Y$. Say we have a PDF $f_X(x)$ and we want to find the PDF $f_Y(y)$.
### One-to-one
If our function $g$ is one-to-one the steps are as follows:
- Find the inverse function so that $X=g^{-1}(Y)$, with support $x \in(x_{1},x_{2})$.
- The PDF of $Y$ is given by: $f_Y(y)=f_X(x) \left| \frac{dx}{dy} \right|=f_X(g^{-1}(y))\left| \frac{d}{dy}g^{-1}(y) \right|$, with support $g(x_{1})<y<g(x_{2})$. 
### Two-to-one
In this case we will split up our function $Y=g(X)$ into two one-to-one invertible functions. We can write this as: $X_1= g_1^{- 1}( Y)$ and $X_2= g_2^{-1}( Y)$. The PDF for the two-to-one part of Y is then:
$$f_{Y}(y)=f_{X_{1}}(g_{1}^{-1}(y))\left|\frac{dx_{1}}{dy}\right|+f_{X_{2}}(g_{2}^{-1}(y))\left|\frac{dx_{2}}{dy}\right|$$

We may have a function that is two-to-one in some parts, and one-to-one in other portions. In this case we split into cases. so we have one case for the one-to-one piece, and one case for the two-to-one piece.
## Method of Transformations for Multiple Variables
### Case 1
The first situation is when we are interested in a single RV that is the function of two other RV's
 Let $X_{1}$ and $X_{2}$ be continuous RV's and $Y=g(X_{1},X_{2})$.
 To find the PDF $f_Y(y)$ of the function $Y = g(X_1,X_2)$ we follow the
 following steps:
- Find the inverse function $X_1= g_{X_1}^{- 1}( X_2, Y)$ or $X_2= g_{X_2}^{- 1}( X_1, Y)$
- Find the joint PDF of $X_1$ and $Y$ or $X_2$ and $Y$
$$\begin{aligned}f_{X_1,Y}(x_1,y)&=f_{X_1,X_2}(x_1,g_{X_2}^{-1}(y,x_1))\left|\frac{d}{dy}g_{X_2}(y,x_1)\right|\\f_{X_2,Y}(x_2,y)&=f_{X_2,X_1}(g_{X_1}^{-1}(y,x_2)),x_2)\left|\frac{d}{dy}g_{X_1}(y,x_2)\right|\end{aligned}$$
- Integrate out the variable we are not interested in to find the PDF of $Y$
### Case 2
 The second situation that we may have is when we are interested in the distribution of random variables $Y_{1}$ and $Y_{2}$ which are both functions of $X_{1}$ and $X_{2}$. $( Y_{1}= g_{1}( X_{1}, X_{2})$ and $Y_{2}= g_{2}( X_{1}, X_{2} )$)

 If we want to find the joint density of $Y_1$ and $Y_2f_{Y_1, Y_2}( y_1, y_2)$:
- Find the inverse functions $x_1= g_1^{- 1}\left ( y_1, y_2\right )$ and $x_2= g_2^{- 1}\left ( y_1, y_2\right )$
- Determine the joint PDF of $Y_{2}$ and $Y_{2}$ by computing $f_{Y_1,Y_2}(y_1,y_2)=f_{X_1,X_2}\left(g_1^{-1}\left(y_1,y_2\right),g_2^{-1}\left(y_1,y_2\right)\right)|J|$
- $|J|$ is the absolute value of the Jacobian, where the Jacobian is
$$\left.J=\det\left|\begin{array}{cc}\frac{\partial g_1^{-1}}{\partial y_1}&\frac{\partial g_1^{-1}}{\partial y_2}\\\frac{\partial g_2^{-1}}{\partial y_1}&\frac{\partial g_2^{-1}}{\partial y_2}\end{array}\right.\right|$$
We can then integrate out the variable we don't want.