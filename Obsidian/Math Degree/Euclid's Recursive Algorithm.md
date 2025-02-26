Euclidean recursion is an effective way to solve for a [[GCD and LCM]] of two numbers $a,b$($gcd(a,b)$). The algorithm uses [[Quotient-Remainder Theorem]] along with the following fact:

$$a=bq+r\implies\gcd(a,b)=\gcd(b,r)$$
This fact repeated will give consistently lower values until our $\gcd$ becomes trivial and we are given $\gcd(r,0)$.

