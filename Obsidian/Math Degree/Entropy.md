Let $X$ be a [[Random Variable]], which takes outcomes $x_{1},\dots,x_n$ with probabilities $p_{1},\dots,p_n$. Then the entropy of $X$ is measured in bits, denoted and defined by:
$$
H(X)=\sum\limits_{i=1}^{n}p_i\log_2\left( \frac{1}{p_i} \right)
$$
If we have an outcome with $p(x)=0,$ we take the convention $0\log \frac{1}{0}=0$.
## Shannon's Postulate
If some event $A$ occurs with probability $p$, and you learn that $A$ occurred, you learned $\log_2\left( \frac{1}{p} \right)$ bits of information.
## Properties
- $H(X)\geq0$
- $H(X)=0\iff$ some $p_i=1$
- $H(X)\leq\log_2n$  (Equality is satisfied if and only if $p_i$'s are all constant)
## On two RVs
Let $X,Y$ be [[Random Variable|Random Variables]]. We can define $H(X,Y)$ as follows. Define $r_{ij}=P(X=x_i,Y=y_{i}).$ Then we have:
$$ H(X,Y)=\sum\limits_{i,j}^{}r_{ij} \log_2\left( \frac{1}{r_{ij}} \right)  $$
### Properties
If $X,Y$ are independent, we have $H(X,Y)=H(X)+H(Y).$
In general, $H(X,Y)\leq H(X)+H(Y)$
## Conditional Entropy
Let $X,Y$ be [[Random Variable|Random Variables]], potentially dependent. Define:
$$
H(X|Y=y_j)=\sum\limits_{x_j}^{}P(X=x_{i}|Y=y_j)\log \frac{1}{P(X=x_{i}|Y=y_{j})}
$$
And,
$$
H(X|Y)=\sum\limits_{y_{i}}^{}P(Y=y_{i})H(X|Y=y_{i})
$$
