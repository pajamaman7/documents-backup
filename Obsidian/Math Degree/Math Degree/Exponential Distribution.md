(From [[Continuous Probability Distributions]])
The exponential distribution is used to model the time between events ($\beta=\frac{1}{\lambda}$) in a [[Poisson Distribution]]. 

Note that an exponential distribution can be also thought of as a [[Gamma Distribution]] with $\alpha=1$ (shape of 1).

The [[Probability Density Function]] is given by: 
$$f(x)=\frac{e^{\frac{-x}{\beta}}}{\beta}=\lambda e^{-x\lambda}$$
The [[Expected Value]]:
$$E[X]=\beta=\frac{1}{\lambda}$$
The [[Variance and Standard Deviation]]:
$$\sigma^2=\beta^2=\frac{1}{\lambda^2}$$

Note that in R, the $\beta$ parameter is given as $\frac{1}{scale}$ so you must use $\lambda$ instead.