With two-sample hypothesis testing we attempt to create cases in order to use a single [[t Distribution]] or [[Normal Distribution]], etc...
## Testing $\sigma_{1}=\sigma_{2}$
When testing equal variances we let $H_{0}$ be $\sigma_{1}=\sigma_{2}$.
$$F_{calc}=\frac{S_1^2}{S_2^2}\sim F_{n_1-1,n_2-1}$$
#### Using R (raw data):
`var.test(x,y,ratio,alternative,conf.level)`
`ratio` is the ratio between our sample variances, which is 1 (since we are assuming equal variance under the null hypothesis). We can leave this blank since R defaults to 1.
## $\mu_{1}-\mu_{2}$
### $\sigma_{1}=\sigma_{2}$
Our null hypothesis $H_{0}$ is $\mu_{1}-\mu_{2}=d_{0}$.
$$T_{calc}=\frac{(\bar{X}_1-\bar{X}_2)-d_0}{\sqrt{S_p^2\left(\frac1{n_1}+\frac1{n_2}\right)}}\sim t_{n_1+n_2-2}$$
#### Raw Data

### $\sigma_{1}\neq\sigma_{2}$
## $\hat{p}_{1}-\hat{p}_{2}$
### $\hat{p}_{1}-\hat{p}_{2}=0$
$$Z_{calc}=\frac{\widehat{p}_1-\widehat{p}_2}{\sqrt{\widehat{p}(1-\widehat{p})\left(\frac1{n_1}+\frac1{n_2}\right)}}\sim Normal{\left(0,1\right)}$$
In R we use `prop.test` without continuity correction, however our formula above may be simpler.
### $\hat{p}_{1}-\hat{p}_{2}=d_{0}$
$$Z_{calc}=\frac{\left(\widehat{p}_1-\widehat{p}_2\right)-d_0}{\sqrt{\frac{\widehat{p}_1(1-\widehat{p}_1)}{n_1}+\frac{\widehat{p}_2(1-\widehat{p}_2)}{n_2}}}\sim Normal{\left(0,1\right)}$$
Cannot use R for this.