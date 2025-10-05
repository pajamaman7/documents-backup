## Caesar Cipher
Given the canonical mapping:
$$
\begin{align}
1&\to A\\
2&\to B\\
&\vdots\\
25&\to Y\\
26&\to Z
\end{align}
$$
We encrypt with $E_k(m)=(m+K)\pmod{ n}$, and we decrypt with $D_k(c)=(c-K)\pmod{ n}$.
## General Substitution
Let $\mathcal{P}=\mathcal{C}=\mathbb{Z}_n$, and $\mathcal{K}=S_n$ the [[Symmetric Groups]] on $n$ elements. Then encryption is given:
$$
E_k(x)=k(x), \qquad D_k(y)=k^{-1}(y)
$$
## Vigenere Cipher
Take $\mathcal{P}=\mathcal{C}=\mathcal{K}=\mathbb{Z}^{t}_n$. The key $k$ now takes the form $(k_{1},\dots,k_t)$.
$$E_k(x_{1}\dots x_t)=(x_{1}+k_{1})\pmod{n},\dots,(x_{t}+k_{t})\pmod{n}$$
$$D_k(x_{1}\dots x_t)=(x_{1}-k_{1})\pmod{n},\dots,(x_{t}-k_{t})\pmod{n}$$
## Affine Cipher
Let $\mathcal{P}=\mathcal{C}=\mathbb{Z}_{n}, K=\mathbb{Z}_n^{*}\times \mathbb{Z}_n$.
We take 
$$
E_{(a,b)}(x)\equiv ax+b\pmod{n},\qquad D_{(a,b)}(x)\equiv a^{-1}(x-b)\pmod{n}
$$
## Homophonic Cipher
To each letter, $x\in\mathbb{Z}_n$, we associate a subset of $\mathbb{Z}_m$ for $m>n$. This is in an attempt to flatten the output distribution.
## Permutation Cipher
$\mathcal{P}=\mathcal{C}=\mathbb{Z}^{t}_n$, $\mathcal{K}=S_t$, the [[Symmetric Groups]] on $t$ items,
$$
E_\pi(x_{1},\dots,x_t)=x_{\pi_1},\dots,x_{\pi_t}
$$