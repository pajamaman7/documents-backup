Let $\{ f_n \}$ be a [[Sequences of Functions|Sequence of Functions]] that are [[Riemann Integral|Riemann Integrable]] in $[a,b]$.
If:
- $\exists M>0$ so that $|f_n(x)|<M$, for all $x\in[a,b]$ and $n\in\mathbb{N}$
- $f_n$ converges pointwise to $f$, and $f$ is Riemann integrable in $[a,b]$
Then:
$$
\lim\limits_{ n \to \infty } \int_{a}^{b} f_n(x) \, dx =\int_{a}^{b} \lim\limits_{ n \to \infty } f_n(x) \, dx =\int_{a}^{b} f(x) \, dx 
$$