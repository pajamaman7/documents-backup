A sequence $\{ z_n \}$ is a function from $\mathbb{N}\to \mathbb{C}$. 
## Limits
We say this sequence $\{ z_n \}$ has limit $l\in \overline{\mathbb{C}}$ if there exists $n^{*}$ so that for all $n>n^{*}$, $z_n$ is in any [[Neighbourhood]] of $l$.
### Properties
Let $z_n=u_n+iv_n$
- $\lim\limits_{ n \to \infty }z_n=l\in\mathbb{C}\iff\lim\limits_{ n \to \infty }|z_n-l|=0$
    - Sub-case: $\lim\limits_{ n \to \infty }z_n=0\iff\lim\limits_{ n \to \infty }|z_n|=0$
- $\lim\limits_{ n \to \infty }z_n=\infty_{\mathbb{C}}\iff\lim\limits_{ n \to \infty }\lvert z_n \rvert=+\infty$ 
- $\lim\limits_{ n \to \infty }z_n=l\in\mathbb{C}\iff\lim\limits_{ n \to \infty }u_n=\Re (l)$ and $\lim\limits_{ n \to \infty }v_n=\Im (l)$
- If $u_n$ or $v_n$ diverge, then $\lim\limits_{ n \to \infty }z_n=\infty_{\mathbb{C}}$ *NOT AN IFF*
### Practical tip 
When you have to calculate the limit of a (simple) complex sequence, start by calculating the limits of its real and imaginary part. If they exist, then you can find the limit using the second property above. If they do not, before concluding that the sequence has no limit, remember to check if its modulus diverges!
### Bonus Properties
- $\lim\limits_{ n \to \infty }z_n=l\iff\lim\limits_{ n \to \infty } \overline z_n =\overline l$ with the convention that $\overline\infty_{\mathbb{C}}=\infty_{\mathbb{C}}$ 
- $\lim\limits_{ n \to \infty }z_n=l\implies \lim\limits_{ n \to \infty }|z_n|=|l|$
### Indeterminate forms
???
## Geometric Sequences
Consider the sequence $z_n=\alpha ^{n}$. This follows the conditions:
- $\lim\limits_{ n \to \infty }z_n=0$ if $\lvert \alpha \rvert<1$
- $\lim\limits_{ n \to \infty }z_n=\infty_{\mathbb{C}}$ if $\lvert \alpha \rvert>1$
- $\lim\limits_{ n \to \infty }z_n=1$ if $\alpha=1$ 
- $\lim\limits_{ n \to \infty }z_n$ does not exist if $\alpha \neq 1$ but $\lvert \alpha \rvert=1$