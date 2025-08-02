(See [[Confidence Intervals]])
## $\sigma^{2}$
A $1-\alpha$ CI for the ratio of variances:
$$\frac{S_1^2}{F_{1-\alpha/2,(n_1-1,n_2-1)}\cdot S_2^2}\leq\frac{\sigma_1^2}{\sigma_2^2}\leq\frac{S_1^2}{F_{\alpha/2,(n_1-1,n_2-1)}\cdot S_2^2}$$
Using R:
`var.test(x,y,conf.level)`
If 1 is in our interval we conclude the variances are equal.
## $\mu_{1}-\mu_{2}$
This method works when we have used the above method and concluded that the variances of the two populations are equal. We get
$\bar{X}_1-\bar{X}_2\sim N(something)$
and a CI of:
$$\bar{X}_1-\bar{X}_2\pm T_{\alpha/2,(df=n_1-1+n_2-1)}\sqrt{S_p^2\biggl(\frac{1}{n_1}+\frac{1}{n_2}\biggr)}$$
Using R:
`t.test,x,y,var.equal=TRUE,conf.level`
Or for summary data:
`tsum.test(mean.x, s.x ,n.x ,mean.y ,s.y , n.y,var.equal = TRUE/FALSE,conf.level)`
If our CI contains 0 we can't say that the means are significantly different.
### $\sigma_{1}\neq\sigma_{2}$
If the variances are not equal, then we have an interval:
$$\bar{X_1}-\bar{X_2}\pm T_{\alpha/2,df}\sqrt{\left(\frac{S_1^2}{n_1}+\frac{S_2^2}{n_2}\right)}$$
Where
$$df\approx\frac{\left(\frac{S_1^2}{n_1}+\frac{S_2^2}{n_2}\right)^2}{\frac1{n_1-1}\left(\frac{S_1^2}{n_1}\right)^2+\frac1{n_2-1}\left(\frac{S_2^2}{n_2}\right)^2}$$
Using R:
`t.test(x,y,var.equal=FALSE,conf.level)`
Or for summary data:
`tsum.test(mean.x, s.x ,n.x ,mean.y ,s.y , n.y,var.equal = TRUE/FALSE,conf.level)`
If our CI contains 0 we can't say that the means are significantly different.
## $\hat{p}$
### $\sigma_{1}\neq\sigma_{2}$
A $1-\alpha$ CI for $\hat{p_{1}}-\hat{p_{2}}$ is given by:
$$(\widehat p_1-\widehat p_2)\pm Z_{\alpha/2}\sqrt{\frac{\widehat p_1(1-\widehat p_1)}{n_1}+\frac{\widehat p_2(1-\widehat p_2)}{n_2}}$$
In R (order matters):
`prop.test(x=c(success1,success2),n=c(n1,n2),conf.level,correct = F)`