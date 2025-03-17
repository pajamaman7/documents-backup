---
tags:
  - NumThry
---
[[Factorials]]
The number of zeroes at the end of some $N!$ is given by the sum of the highest power of $5$ that divides each term in the expansion: $N(N-1)(N-2)\dots 2\cdot 1$.
This works since, if a term $k$ which is divisible by 5, is not already divisible by 10, the term $k-1$ will be divisible by $2$.
### Ex:
Find the number of zeroes at the end of $1000!$.
We begin by finding the number of times that $5|1000!$ This can be given by $\frac{1000}{5}=200$. Then we add the number of times $25|1000!$; $\frac{1000}{25}=40$. $\frac{1000}{125}=8$, $\frac{1000}{625}=1$. Summing all these gives 249 zeroes at the end of $1000!$.