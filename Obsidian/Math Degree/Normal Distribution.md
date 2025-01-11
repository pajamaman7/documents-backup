(From [[Continuous Probability Distributions]])
The normal distribution is likely the single most useful statistical model. Its shape is a bell curve and it is able to model a number of situations. 

To model this distribution, we will often use the "Standard Normal Distribution," which has an [[Expected Value]] ($\mu$) of 0, and a [[Variance and Standard Deviation]] ($\sigma$) of 1.

To transform any given normal distribution into the standard distribution, we can use 
$$Z=\frac{X-\mu}{\sigma}$$
For a normal distribution, $f(x)=P(X=x)=0$, and $F(x)=P(X\leq x)$ can be represented as the integral of the bell curve up to the point $x$. 

The [[Probability Density Function]]: 
$$f(x)=\dfrac{1}{\sigma\sqrt{2\pi}}\exp\left[-\left(\dfrac{1}{2\sigma^2}\right)(x-\mu)^2\right],\: x\in\mathbb{R}$$
The [[Variance and Standard Deviation]], as well as the [[Expected Value]] are trivially evident in the formula as $\sigma, \mu$ respectively.