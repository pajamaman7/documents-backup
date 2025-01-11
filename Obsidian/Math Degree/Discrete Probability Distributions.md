(From [[Introduction to Statistics]])
Discrete Probability Distributions occur when the random variable is limited to a countable number of values. 

Discrete distributions must satisfy the following conditions. For some probability function $p(y)$,
1. $0\leq p(y)\leq1$ for all $y$.
2. $\sum_{y}p(y)=1$, summing over all values of $y$.

|Distribution|Probability Mass Function| Expected Value | Variance|Moment Generating Function|
|-|-|-|-|-|
|[[Binomial Distribution]]|$p(x)= {n\choose x}p^x(1-p)^{n-x}$|$np$|$np(1-p)$|$(e^t p+q)^n$|
|[[Negative Binomial Distribution]]|$p(x)=\begin{pmatrix}x-1\\r-1\end{pmatrix}p^r(1-p)^{x-r}$|$\frac{r}{p}$|$\frac{r(1-p)}{p^2}$|
|[[Geometric Distribution]]|$p(y)=(1-p)^{x-1}p$|$\frac{1}{p}$|$\frac{1-p}{p^2}$|
|[[Hypergeometric Distribution]]|$p(x)=\frac{\binom{r}{x}\binom{N-r}{n-\chi}}{\binom{N}{n}}$|$\frac{nr}{N}$|$\sigma^2=n\left({\frac{r}{N}}\right)\left({\frac{N-r}{N}}\right)\left({\frac{N-n}{N-1}}\right)$|
|[[Poisson Distribution]]|$p(x)=\frac{\lambda^x e^{-\lambda}}{x!}$|$\lambda$|$\lambda$|
