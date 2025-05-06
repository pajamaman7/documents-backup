Let $\mathfrak{R}$ be a $\sigma$-[[Algebra]] in a set $X$ and $\mu$ a positive measure on $\mathfrak{R}$.
If $s:X\to[0,\infty]$ is a [[Measure|Measurable]] [[Simple Functions|Simple Function]], taking the form
$$
s=\sum\limits_{i=1}^{n}\alpha_i\chi_{A_i}
$$
where $\alpha_i$ are distinct values of $s$, and:
$$
\chi_A(x)=\begin{cases}
0&\text{if }x\not\in A\\
1&\text{if }x\in A
\end{cases}
$$
Then we define:
$$
\int _E s\, d\mu =\sum\limits_{i=1}^{n}\alpha_i\mu(A_i\cap E)
$$
If it happens that $\mu$ takes an infinite value at some point we may require the convention $0\cdot \infty=0$.
Then for a general measurable function $f:X\to [0,\infty]$, we define the Lebesgue Integral:
$$
\int_{E}^{} f \, d\mu =\sup_{s\in S}\int_{E}^{} s \, d\mu 
$$
Where $S$ is the set of all measurable functions $s$ with $0\leq s\leq f$.
## Properties of the Lebesgue Integral
- If $0\leq f\leq g$, then $\int_{E}^{} f \, d\mu\leq\int_{E}^{} g \, d\mu$.
- If $A\subseteq B$ and $f\geq 0$, then $\int_{A}^{} f \, d\mu\leq\int_{B}^{} f \, d\mu$.
- If $c\in\mathbb{R}$, then $\int_{E}^{} cf \, d\mu=c\int_{E}^{} f \, d\mu$
- If $f$ is identically zero on $E$, then $\int_{E}^{} f \, d\mu=0$.
- If $\mu(E)=0$, then $\int_{E}^{} f \, d\mu=0$.