When we order random variables according to their magnitude, we call them *order statistics*.
In R we can order statistics with `ord=sort(x)`, assuming that `x` is our original data set.
For a data set $X_i$ with $i\in\mathbb{Z}, 1\leq i\leq n$, we write $X_{(1)}$ as our lowest, and $X_{(n)}$ as our highest.
### Properties
To find the $1^{st}$ or the $n^{th}$ ordered statistic
$$f_{X_{(n)}}=n[F_X(x)]^{n-1}f_X(x)$$
$$f_{X_{(1)}}=n[1-F_X(x)]^{n-1}f_X(x)$$
The two above allow us to find the distribution of any $k^{th}$ ordered statistic.
$$f_{X_{(k)}}=\frac{n!}{(k-1)!(n-k)!}F_X(x)^{k-1}\left[ 1-F_X(x) \right] ^{n-k}f_X(x)$$
