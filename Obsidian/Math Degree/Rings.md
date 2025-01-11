---
aliases:
  - Ring
---
A *Ring* $(R,+,\cdot)$ is an abelian [[Groups|Group]] $(R,+)$ together with an additional operation $\cdot$, which satisfies the additional axioms:
- Closure of $R$ under $\cdot$
- Associativity of $\cdot\,$: $a\cdot (b\cdot c)=(a\cdot b)\cdot c$
- Existence of the multiplicative identity element: $1\cdot a = a$
- Distribution of multiplication over addition: $a\cdot(b+c)=ab+ac$, and: $(b+c)\cdot a=ab+ac$ 
Multiplication is not necessarily commutative.
Note that sometimes a ring does not necessarily contain $1$.
### Notation
In a ring, we often write additive identity as $0$ or $0_R$, and multiplicative identity as $1$ or $1_R$.
To differentiate additive and multiplicative exponentiation, we use
- $a+a+=\dots=na$
- $a\cdot a\cdot\dots =a^{n}$, here $n\geq 0$ unless $R$ is commutative ring
### Properties
- $0\cdot r=0=r\cdot0$
- The only ring with $0=1$ is the zero ring, $R=\{ 0 \}$.
### Examples
- $\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$ are all infinite rings with the expected operations
- $\mathbb{Z}_n$ is a finite ring.
- $M_n(\mathbb{R})$ form rings with matrix addition and multiplication.
- Polynomial rings $\mathbb{Z}[x]$:
$$a_nx^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}$$
        With coefficients in $\mathbb{Z}$. $\mathbb{R}[x]$ is similar, with coefficients in $\mathbb{R}$.
- Real valued functions. $f:X\to \mathbb{R}$
## Commutative Ring
$R$ is a commutative ring if $\cdot$ is commutative.
### Binomial Theorem
The [[Binomial Theorem]] holds in commutative rings.
$$(a+b)^{n}=\sum\limits_{k=0 }^{n} {n \choose k}a^{n-k}b^{k}$$
Which requires [[Pascal's Identity]]:
$${n\choose k}+{n\choose k-1}={n+1\choose k}$$
## Units
$a\in R$ is called a unit if it has a multiplicative inverse. $\exists b\in R: ab=1$.
The set of all units of a ring $R$, denoted $U(R)$ forms a [[Groups|Group]].
If every element of $R$ is a unit, $R$ is a [[Field|Fields]].
## Zero-Divisors
$a\in R$ is called a zero-divisor when there exists $b\in R$, $b\neq 0$ so that $ab=0$ or $ba=0$. In some cases $0$ is not considered a zero-divisor.

## Characteristic
The characteristic of a ring $R$ is:
- If $o(1)=n$ in $R$, the characteristic of $R$, $char(R)=n$.
    - In this case the smallest subring of $R$, say $A\cong \mathbb{Z}_n$.
- If $o(1)=\infty$ in $R$ the characteristic of $R$, $char(R)=0$.
    - In this case the smallest subring of $R$, say $A\cong \mathbb{Z}$.
### Theorem
If $R$ is an integral domain, then $char(R)=0$ or $char(R)=p$ for some prime $p$.
#### Properties
- If $F$ is a field, $Char(F)=0$ or $p$, prime.
- If $char(R)=n$, then $nr=0$ for any $r\in R$.
    - Every element in the ring $R$ has additive order dividing $n$.