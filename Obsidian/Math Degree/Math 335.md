## Final
### Format
~12 MCQ
~2 Proof
### Chapter 1
Construction of reals not tested
### Chapter 2
Topology will be tested
### Chapter 3
- Cauchy criterion for sequences
- Convergence theorems; root ratio test, $2^n$ test, monotonic sequences.
### Chapter 4
Let $f$ continuous:
- $f$(compact) is compact
- $f$(connected) is connected
- $f$ cont. in $X$ iff $f^{-1}(V)$ open for every $V$ open in $Y$. sim. closed...
### Chapter 5
- Derivatives in metric spaces, proof of diff at $x\implies$ cont. at $x$.
- [[Mean Value Theorem]]; Corollary: if $f$ diff in $[a,b]$, and $f'$ is bounded there, then $f$ is uniformly continuous.
	- proof: if $\alpha,\beta \in[a,b]$ then $\frac{f(\beta)=f(\alpha)}{\beta-\alpha}=f'(c)$ for some $c$ between $\alpha,\beta$. Then $\left|\frac{f(\beta)-f(\alpha)}{\beta-\alpha}\right|\leq M$ since div. bounded. Given $\varepsilon,let\delta=\frac{\varepsilon}{M}$. then if $|\beta-\alpha|<\delta$ we have $|f(\beta)-f(\alpha)|<M|\beta-\alpha|<M\delta<\varepsilon$. 
	- Corr: $f'\geq 0$ then $f$ inc. likewise with $f'\leq 0$.
	- Max or min at $c$ means $f'(c)=0$.
- $f:[a,b]\to\mathbb{R}$ has $n-1$ cont derivatives in $[a,b]$ and $f^{(n)}$ exists in $(a,b)$ then $$
f(x)=\sum\limits_{k=0 }^{n-1} \frac{f^{(k)}(\alpha)}{k!}(x-a)^{k}+ \frac{f^{(n)}(\tilde{x})}{n!}(x-\alpha)^{n}
$$
	Where $\tilde{x}$ between $\alpha$ and $x$.
### Chapter 6
- [[Riemann Stieljes Integral]] Given $f:[a,b]\to\mathbb{R}$, and $\alpha$ increasing in the interval, we define $M_i=\sup_{x\in[x_{i-1},x_{i}]} f(x)$, $m_i=\inf{x\in[x_{i-1},x_{i}]} f(x)$. And then, $U(P,f,\alpha)=\sum\limits_{i=1 }^{n}M_i\Delta\alpha_i$, $L(P,f,\alpha)=\sum\limits_{i=1 }^{n}m_i\Delta\alpha_i$. If $P,Q\in\mathcal{P}([a,b])$ and $Q\supseteq P$, then  $U(Q,f,\alpha)\leq U(P,f,\alpha)$, and $L(Q,f,\alpha)\geq L(P,f,\alpha)$
