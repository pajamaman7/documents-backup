The formula for sample variance is given by:
$$S^{2}=\frac{\sum_{i=1 }^{n}(X_i-\bar{X})^{2}}{n-1}$$
The distribution of $\frac{(n-1)S^{2}}{\sigma^{2}}$ is $\chi ^{2}$ with $n-1$ degrees of freedom. (when $X_i$ is exactly normal or the sample size is big enough for [[Central Limit Theorem]]).
## Theorem 7.2 
The distribution of the sum of $n$ squared independent Standard Normal random variables is Chi-Square with the degree of freedom $n.$
$$
\sum_{i=1}^nZ_i^2\sim\chi_{df=n}^2
$$
## Cochran's Theorem
If a I.I.D. random sample of Chi-Square random variables $(Z_1^2,Z_2^2,\ldots,Z_n^2)$ each with their own respective degrees of freedom$(\nu_1,\nu_2,\ldots,\nu_n)$ is taken and summed $\sum_{i=1}^nZ_i^2.$ Then,
$$
\sum_{i=1}^nZ_i^2\sim\chi_{df=\sum_{i=1}^n\nu_i}^2
$$

