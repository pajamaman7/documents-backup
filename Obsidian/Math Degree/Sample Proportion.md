For categorical data, we use sample proportion. We sort data into true/false,  and take an IID random sample and think of it as the sum of independent [[Bernoulli Random Variable]]s. 

When $X_i\sim Bernoul li(p)$, $\frac{\sum\limits X_i}{n}$, which is typically called the sample men, is called the sample proportion ($\hat{p}$).
We can also say $\hat{p}\sim N\left( p,\sigma^{2}=\frac{p(1-p)}{n} \right)$.

Sample proportion converges slower than sample mean.

To use CLT, we should have at least 10 successes and 10 failures.
## Unbiased
Sample Proportion is an [[Parameter Estimation|Unbiased Estimator]] for proportion.

## Continuity Correction
When approximating $\hat{p}$ with a continuous distribution, we must adjust probability bounds. We adjust $P(a<\hat{p}<b)$to $P\left( a-\frac{1}{2n}<\hat{p}<b+\frac{1}{2n} \right)$.