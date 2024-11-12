A ring homomorphism is a [[Functions|Function]] $\sigma :R\to S$ for [[Rings]] $R,S$ satisfies:
- $\sigma(a+b)=\sigma (a)+\sigma(b)$
- $\sigma(ab)=\sigma (a)\sigma(b)$
## Properties
- $\sigma(0)=0$
- $\sigma(1)$ need not be $1$
- $\sigma(-r)=-\sigma(r)$
- for $k\in \mathbb{Z}$, $\sigma(kr)=k\sigma (r)$
- for $k\in \mathbb{Z}_{\geq 0}$, $\sigma (r^{k})=\sigma (r)^{k}$
- If $u\in U(R)$ then $\sigma(u)\in U(S)$
- If $Char(R)=p$ where $p$ is prime, $(x+y)^{p}=x^{p}+y^p$
## Kernel and Image
### Kernel
$$\ker \sigma=\{ r\in R: \sigma(r)=0 \}$$
Of course $0\in\ker\sigma$. This is not a subring.
$\ker\sigma$ is called an [[Ideals|Ideal]] of $R$.
### Image
$$\mathrm{Im}\sigma=\{ y\in S: \exists x \in R, \sigma(x)=y \}$$
This *is* a subring of $R$.

## Isomorphism
A ring homomorphism is defined identically to a [[Group Homomorphism and Isomorphism|Isomorphism]] on a group; it is a bijective homomorphism.

