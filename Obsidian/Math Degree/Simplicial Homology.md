Let $X$ have some [[Delta complex]] structure:
$$
\{ \sigma_\alpha:\alpha \in J \}
$$
Let $\Delta_n(X)$ be the [[Free Group]] ([[Abelian]]) on the basis $e_\alpha=\Delta ^{n_\alpha o}$, so that $n_\alpha=n$:
$$
\Delta_n(X)=\bigoplus_{\alpha \in J} \mathbb{Z}e_\alpha
=\{ m_{1}e_{\alpha_{1}}+\dots+m_re_{\alpha_r}:m_i\in\mathbb{Z} \}
$$
We call an element $\sum\limits_{i=1}^{r}m_i e_{\alpha_i}$ an $n$-chain of $X$.
## Boundary Maps
We define a boundary map: $\partial_n:\Delta_n(X)\to\Delta_{n-1}(X)$ identifying the boundary of the simplex, and the orientation of faces.
$$
\partial_n(\sigma_a)=\sum\limits_{i=0}^{n}(-1)^{i}\sigma_\alpha|_{[v_{0},\dots,\hat{v}_i,\dots,v_n]}
$$
Defining a [[Group Homomorphism and Isomorphism|Group Homomorphism]].
## Lemma: 
$$
\partial^{2}=0
$$