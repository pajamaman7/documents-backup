## 6.1
Let $M_X( t)$ and $M_Y( t)$ denote the moment-generating functions of random variables $X$ and $Y$, respectively. If both moment-generating functions exist and $M_X(t)=M_Y(t)$ for all values of $t$, then $X$ and $Y$ have the same probability distribution.
## 6.2
Let $X_1,X_2,\ldots,X_n$ be independent random variables with moment generating-
functions $M_{X_1}(t),M_{X_2}(t),\ldots,M_{X_n}(t)$, respectively. If $U=X_1+X_2+\cdots+X_{n}, \mathrm{then: }$
$$
M_U(t)=M_{X_1}(t)\times M_{X_2}(t)\times\cdots\times M_{X_n}(t)=\prod_{i=1}^nM_{X_i}(t)
$$
## 6.3
Let $X_1,X_2,\ldots,X_n$ be independent normally distributed random variables with $E( X_i) = \mu_i$ and $V( X_i) = \sigma_i^2,$ for $i= 1, 2, \ldots , n,$ and let $a_1, a_2, \ldots , a_n$ be constants. If $U=\sum_{i=1}^na_iX_i=a_1X_1+a_2X_2+\cdots+a_nX_n$ then $U$ is a normally distributed random variable:

$$
U\sim Norm(\mu_U=E[U],\sigma_U^2=V[U])
$$
with:
$$\begin{array}{ll}\bullet&E[U]=\sum_{i=1}^na_i\mu_i=a_1\mu_1+a_2\mu_2+\cdots+a_n\mu_n\\\bullet&V[U]=\sum_{i=1}^na_i^2\sigma_i^2=a_1^2\sigma_1^2+a_2^2\sigma_2^2+\cdots+a_n^2\sigma_n^2\end{array}$$
## 6.4
Let $X_{1}, X_{2}, \ldots , X_{n}$ be defined as in Theorem 6.3 and define $Z_{i}$ by $Z_{i}=\frac{X_{i}-\mu_{i}}{\sigma_{i}},i=$ $1, 2, \ldots , n.$Then,

$\sum_{i=1}^{n}Z_{i}^{2}$ has a $\chi^{2}$ distribution with $n$ degrees of freedom.
