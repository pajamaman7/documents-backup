## Bivariate Data
Bivariate data comes from a sample from which two measurements are observed.
We represent bivariate data as ordered pairs $(X_i,Y_i)$.
## Covariance
From [[Covariance and Correlation]]: 
$$COV[X,Y]=E[XY]-E[X]E[Y]$$
and
$$COR=\frac{COV[X,Y]}{\sigma_x\sigma_y}$$
However, for our sample covariance, we would use:
$$\frac{S_{XY}}{n-1}=\frac{\sum_{i=1 }^{n}(\bar{X}-X_i)(\bar{Y}-Y_i)}{n-1}$$
Covariance is a measure of dependence, and is scaled by the standard deviation. Instead we use correlation, which is the covariance divided by the product of standard deviations of both samples.
R can simply calculate sample correlation and covariance;
`cor(X,Y)` and `cov(X,Y)`.
For notation, $r$ is our sample correlation, and $\rho$ is our population correlation.
### Analyzing Correlation
$r=1$ means we have a perfect positive relationship.
$r=-1$ means we have a perfect negative relationship
$r=0$ means no linear relationship.
Positive values mean positive relationships, and negative means negative. The closer to $\pm 1$ we are, the stronger the linear relationship.
## Formulas
## Sum of Squares Total
