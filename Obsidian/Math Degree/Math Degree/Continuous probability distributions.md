Below are valuable pieces of information about several common continuous probability distributions.

Continuous probability distributions follow the following rules:

Let $P$ be a [[Probability Density Function]] and $F$ a [[Cumulative Distribution Function]]:
- $P(X=x)=0$
- $F(-\infty)=0$
- $F(\infty)=1$
- $F$ is a nondecreasing function of $x$.
- $f(x)=0, \forall x\in\mathbb{R}$
- $\int_{-\infty}^{\infty}f(x)dx=1$

| Distribution | Probability Function | Mean | Variance | Moment function |  |  |  |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| [[Uniform Distribution]] | $f(y)=\frac{1}{\theta_2-\theta_1}$, $\theta_1\leq y\leq\theta_2$ | $\frac{\theta_1+\theta_2}{2}$ | $\frac{(\theta_2-\theta_1)}{12}$ | $\frac{e^{t\theta_2}-e^{t\theta_1}}{t(\theta_2-\theta_1)}$ |  |  |  |
| [[Normal Distribution]] | $f(y)=\dfrac{1}{\sigma\sqrt{2\pi}}\exp\left[-\left(\dfrac{1}{2\sigma^2}\right)(y-\mu)^2\right],\: y\in\mathbb{R}$ | $\mu$ | $\sigma^2$ | $\exp\left(\mu t+\dfrac{t^2\sigma^2}{2}\right)$ |  |  |  |
| [[Exponential Distribution]] | $f(y)=\frac{1}{\beta}\alpha^{-y/\beta}$, $\beta>0, y>0$ | $\beta$ | $\beta^2$ | $(1-\beta t)^{-1}$ |  |  |  |
| [[Gamma Distribution]] | $$f(x)=\frac{x^{\alpha-1}e^{\frac{-x}{\beta}}}{\Gamma(\alpha)\beta^{\alpha}}$$ | $\alpha\beta$ | $\alpha\beta^2$ | $(1-\beta t)^{-\alpha}$ |  |  |  |
| Chi-Square |  |  |  |  |  |  |  |
| [[Beta Distribution]] | $f(y)=$ |  |  |  |  |  |  |
