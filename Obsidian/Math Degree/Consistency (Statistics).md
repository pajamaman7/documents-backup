An estimator is said to be consistent if, for any positive integer $\epsilon$,
$$\lim\limits_{ n \to \infty } P(|\hat{\theta}_n-\theta|\leq\epsilon)=1$$
or,
$$\lim\limits_{ n \to \infty } P(|\hat{\theta}_n-\theta|>\epsilon)=0$$
## Consistency of unbiased estimators
An unbiased estimator $\hat{\theta}$ is a consistent estimator for $\theta$ if:
$$\lim\limits_{ n \to \infty } Var(\hat{\theta})=0$$
## Properties
Let $\hat{\theta}_n\to^p\theta$ and $\hat{\theta ^{*}}\to^p\theta ^{*}$.
- $\hat{\theta}_n+\hat{\theta}^*_n\to^p\theta+\theta^*$
- $\hat{\theta}_n\hat{\theta}^*_n\to^p\theta\theta^*$
- $\frac{\hat{\theta}_n}{\hat{\theta}^*_n}\to^p \frac{\theta}{\theta^*}$
- If $g$ is a real valued function continuous at $\theta$,  $g(\widehat{\theta}_n)\overset{p}{\operatorname*{\to}}g(\theta)$
### More
- $\overline{X}-\overline{Y}\stackrel{p}{\to}?$
- $\frac{S_{1}^{2}}{S_{2}^{2}}\xrightarrow{p}?$
 - An unbiased consistent estimator for the mean of a Poisson random variable is $\bar{X}$ or $S^{2}$
 - $\frac{S}{\bar{X}}$ is a consistent estimator for $\frac\sigma\mu.[\frac\sigma\mu$ is called the coefficient of variation]