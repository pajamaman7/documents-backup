The Negative Binomial Distribution is similar to the [[Binomial Distribution]] but, instead of our variable representing the number of succeses out of $n$ trials, the negative binomial variable represents the number of trials required for $r$ successes.

The [[Probability Mass Function]] is:
$$p(y)=\begin{pmatrix}y-1\\r-1\end{pmatrix}p^r(1-p)^{y-r}$$
The [[Expected Value]]:
$$E[X]=\frac{r}{p}$$
The [[Variance and Standard Deviation]]:
$$\sigma^2=V[X]=\frac{r(1-p)}{p^2}$$
## Negative Binomial In R
Suppose $X\sim Negative Binomial$.
The pmf of $X$ can be modeled with a regular binomial distribution (in R):
`dbinom(x-1,size-1,p)*p`
With $x$ being our number of successes, size being our desired final choice, and $p$ the probability of success.
This would be equivalent to the R code:
`dnbinom(size-x,x,p)`
