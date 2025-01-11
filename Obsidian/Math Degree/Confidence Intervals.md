Confidence intervals for a given parameter $\theta$ have two properties:
- It will contain $\theta$
- It will be narrow
The endpoints will likely vary from sample to sample.

A $100(1-\alpha)\%$ confidence interval is defined by:
$$P(\hat{\theta}_L<\theta <\hat{\theta}_U)=1-\alpha$$
## Pivotal Quantity
This method depends on finding a pivotal quantity $g(\hat{\theta})$:
- $g(\hat{\theta})$ is a function of the sample $X_{1},X_{2},\dots$ and of the targeted parameter $\theta$
- $g(\hat{\theta})$'s probability function does not depend on $\theta$.
Once we have a pivotal quantity, we can find our confidence interval by transforming $g(\hat{\theta})$ into $\theta$ within our probability statement.
## For Large or Normally Distributed Samples
This technique works for normal samples or sufficiently large samples, where we can approximate $\bar{X}$ as normal with [[Central Limit Theorem]]. 

If we have a distribution $\frac{\bar{X}-\mu}{\frac{\sigma}{\sqrt{ n }}}$, we can find a symmetric interval of confidence $\alpha$:
$$\bar{X}\pm \frac{Z_{\frac{\alpha}{2}}\sigma}{\sqrt{ n }}$$
With the second term called the *margin of error*.
For a [[t Distribution]], when we don't know $\sigma$:
$$\bar{X}\pm t_{\frac{\alpha}{2},df=n-1} \frac{S}{\sqrt{ n }}$$

For Bernoulli/qualitative data:
$$\hat{p}\pm Z_{\frac{\alpha}{2}}\sqrt{ \frac{\hat{p}(1-\hat{p})}{n}}$$