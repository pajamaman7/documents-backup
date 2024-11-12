We use this method in order to find a point estimator $u(X_{1},X_{2},\dots,X_n)$ for some parameter $\theta$. It revolves around maximizing the likelihood that a sample we observed happened.
Suppose we have a random sample $X_1,X_2,\ldots,X_n$ for which the probability density (or mass) function of each $X_{i}$ is $f( x_{i}|\theta) .$
 The joint probability mass (or density) function of $X_1,X_2,\ldots,X_n$, which we'll call $L(\theta)$ is:
$$
{L}(\theta)=P(X_1=x_1,X_2=x_2,\ldots,X_n=x_n)=f(x_1|\theta)f(x_2|\theta)\cdots f(x_n|\theta)=\prod_{i=1}^nf(x_i|\theta)
$$
We then take this as a function of $\theta$ and maximize the function at some $\hat{\theta}_{MLE}$
Often we take $\ln(L(\theta))$, since it is increasing monotonically and by maximizing this will maximize $L(\theta)$
## Process
- Find pdf
- Find the likelihood function ${L}(\theta)=\prod_{i=1}^nf(x_i|\theta)$
- Optional: take $\ln$ of the function
- Take the first derivative and set it to 0
- Ensure that the zero is a maximum and not a minimum
## MLE for >1 parameter
Let $X_1,X_2,\ldots,X_n$ be a random sample from a distribution that depends on one or more unknown parameters $\theta_1,\theta_2,\ldots,\hat{\theta}_m$ with probability density (or mass) function $f(x_{i}|\theta_{1},\theta_{2},\ldots,\theta_{m}).$
 Suppose that $(\theta_1,\theta_2,\ldots,\theta_m)$ is restricted to a given parameter space $\Omega$. Then:
 As a function of $\theta_1,\theta_2,\ldots,\theta_m$, the joint probability density (or mass) function of
 $X_{1}, X_{2}, \ldots , X_{n}\mathrm{~is: }$
$$
\begin{aligned}L(\theta_1,\theta_2,\ldots,\theta_m)=\prod_{i=1}^nf(x_i|\theta_1,\theta_2,\ldots,\theta_m)\end{aligned}
$$
This is the likelihood function If$[ u_1( x_1, x_2, \ldots , x_n) , u_2( x_1, x_2, \ldots , x_n) , \ldots , u_m( x_1, x_2, \ldots , x_n) ]$ is the vector that maximizes the likelihood function, then $\hat{\theta}_i=u_i(X_1,X_2,\ldots,X_n)$ is the maximum likelihood estimator of $\theta_i,$ for $i= 1, 2, \ldots , m.$
 The corresponding observed values of the statistics in $(2)\colon[u_1(x_1,x_2,\ldots,x_n),u_2(x_1,x_2,\ldots,x_n)$
 $,\ldots,u_m(x_1,x_2,\ldots,x_n)]$ are called the maximum likelihood estimates of $\theta_i,$for $i=1,2,\ldots,m.$
## More Information
The Parameter space $\Omega$ is the set of possible values for a parameter.