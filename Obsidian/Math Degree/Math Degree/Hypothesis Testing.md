## Null and Alternative Hypothesis
Hypotheses are statements about population parameters. The null hypothesis $H_0$ is assumed to be true, and is a statement that would be most commonly true without some outside information.
By disproving the null hypothesis, we prove the alternative hypothesis $H_a$, the negation of the null.
We have mutually exclusive pairs for $H_0$.
$$\begin{array}{|c|c|c|}\hline\text{Simple ("two-tailed")}&\text{Composite ("left-tailed")}&\text{Composite ("right-tailed")}\\\hline H_0:\theta=\theta_0&H_0:\theta\geq\theta_0&H_0:\theta\leq\theta_0\\\hline H_a:\theta\neq\theta_0&H_a:\theta<{\theta_0}&H_a:\theta>\theta_0\\\hline\end{array}$$
The null will always have equality ($=,\leq,\geq$).
## Test Statistic/$p$-value
We put our available information into a Test Statistic, which must follow some known distribution so we can compute. We calculate this statistic assuming the null hypothesis is true. We convert the statistic into a p-value. This represents how likely a sample we observed could happen again.
### p-value
We choose a level of significance $\alpha$, usually $\alpha=.05$. If:
- $p\geq\alpha$ we fail to reject $H_{0}$.
- $p<\alpha$ we reject $H_{0}$.
The $p$-value is calculated as the area under our pdf, more extreme than our critical value.
### Rejection Region
We can calculate a critical value $X_{crit}$ corresponding to $\alpha$. Our rejection region is the set of values more extreme than our critical value.
## Errors
### Type 1 error
A Type 1 error is one where we reject the null hypothesis when it in fact is true.
$\alpha$ is the probability of committing a type 1 error, given by $\alpha=P(RH_0|H_{0} \text{ is true})$
### Type 2 error
Type 2 error is one where we fail to reject the null hypothesis when it is in fact false. The probability of this happening:
$\beta=P(FTRH_{0}|H_{0} \text{ is false})$
### Power
Power is $1-\beta$ and represents the probability that we reject the null hypothesis given that the null hypothesis is false.
## Large and Normally Distributed Data
### $H_{0}: \mu=\mu_0$, $\sigma$ known
$$Z_{calc}=\frac{\bar{X}-\mu_{0}}{\frac{\sigma}{\sqrt{ n }}}\sim N(0,1)$$
For raw data we use `z.test`, and we use the parameter `alternative` depending on our alternative hypothesis, and set `mu` according to our $\mu_{0}$.
For summary data we do the same with `zsum.test`
### $H_{0}: \mu=\mu_0$, $\sigma$ unknown
$$Z_{calc}=\frac{\bar{X}-\mu_{0}}{\frac{s}{\sqrt{ n }}}\sim T_{df=n-1}$$
For raw data we use `t.test`, and we use the parameter `alternative` depending on our alternative hypothesis, and set `mu` according to our $\mu_{0}$.
For summary data we do the same with `tsum.test`
### $H_{0}: p=p_0$
$$Z_{calc}=\frac{\hat{p}-p_{0}}{\sqrt{ \frac{p_{0}(1-p_{0})}{n} }}\sim N(0,1)$$
We can calculate this with `prop.test(x,n,p,alternative,correct=F)`. However this calculates using a chi-squared distribution, so we must square root our TODO
### $H_{0}: \sigma=\sigma_0$
$$\chi^{2}_{calc}=\frac{(n-1)S^{2}}{\sigma_{0}^{2}}\sim \chi^{2}_{df=n-1}$$
For raw data we can use `varTest(x, alternative, conf.level, sigma.squared)` in the EnvStats package.