The Gamma Distribution is always right-skewed with parameters $\beta$ and $\alpha$, representing scale and skewness respectively. 
The [[Probability Density Function]]:
$$f(x)=\frac{x^{\alpha-1}e^{\frac{-x}{\beta}}}{\Gamma(\alpha)\beta^{\alpha}}$$ The [[Expected Value]]:
$$E[X]=\alpha\beta$$
The [[Variance and Standard Deviation]]:
$$\sigma^{2}=\alpha\beta^2$$
Note that in R, the $\beta$ parameter is given as $\frac{1}{scale}$ so you must use $\lambda$ instead. 