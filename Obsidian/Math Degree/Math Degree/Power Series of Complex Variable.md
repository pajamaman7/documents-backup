A power series centered on $c\in \mathbb{C}$ is given by:
$$f(z)=\sum\limits_{n=0 }^{\infty}a_n(z-c)^{n}$$
Where $a_n$ is a complex sequence.
However we can use a change of variable to center the series on 0, giving
$$f(z)=\sum\limits_{n=0 }^{\infty}a_nz^{n}$$
## Radius of convergence
### Abel's Lemma
Abel's lemma says that if the series $\sum\limits_{n=0 }^{\infty}a_nz^{n}$ converges for $w\in \mathbb{C}$, then $\sum\limits_{n=0 }^{\infty }a_nz^{n}$ converges for any $u\in \mathbb{C}$ where $|u|<|w|$.
### Definition
The radius of convergence $R$ is the supremum $R=\sup\left\{  |z|:\,z\in\mathbb{C} \sum\limits_{n=0 }^{\infty}a_nz^{n}\, \text{  converges}  \right\}$
- For $|z|=R$ we cannot say anything about the series
- For $|z|<R$ the series converges absolutely
- For $|z|>R$ the series is divergent.
### Properties
- If the series converges absolutely for some $|z_0|=R$, then the series converges conditionally for any other $|z|=R$.
- If $R$ is finite, there must be a singularity of the series at $|c|=R$.
- Entire functions have infinite radius of convergence.
## Differentiability
If $f(z)=\sum\limits_{n=0 }^{\infty}a_nz^{n}$ has positive radius of convergence $R$, then 
- The series is differentiable in $D(0,R)$
- We define the *formal* derivative of the power series to be:
$$f'(z)=\sum\limits_{n=1 }^{\infty}na_nz^{n-1}$$
- $\sum\limits_{n=1 }^{\infty}na_nz^{n-1}$ has radius of convergence $R$.
In fact, for power series the $k^{th}$ derivative is given by:
$$\sum\limits_{n=k }^{\infty}(nPk)a_nz^{n-k}$$
and is continuous and differentiable in $D(0,R)$ for any $k\in\mathbb{Z}$. Hence they are of class $C^{\infty}$. 
## Abel's Theorem for Series
If a series $f(z)=\sum\limits_{n=0 }^{\infty}a_nz^n$ converges on a point $z$ on the boundary, $|z|=R$, $f$ converges to the function represented by $f$ at $z$.
# Examples/Common Series
## Geometric Series
$$\sum\limits_{n=0 }^{\infty}z^n$$
- Convergent for $|z|<1$
- Divergent for $|z|>1$
- Indeterminate for $|z|=1$
And the sum is given, when the series converges, by 
$$\sum\limits_{n=0 }^{\infty}z^n=\frac{1}{1-z}$$
## Logarithmic Series
$$\sum\limits_{n=1 }^{\infty} \frac{(-1)^{n+1}}{n}z^{n}$$
With the ratio test we can find that the series is:
- Absolutely convergent for $|z|<1$
- Divergent for $|z|>1$
- For $z=1$, the series is convergent for values not equal to $-1$
And when the series converges its sum is given by
$$\sum\limits_{n=1 }^{\infty} \frac{(-1)^{n+1}}{n}z^{n}=\ln(1+z)$$