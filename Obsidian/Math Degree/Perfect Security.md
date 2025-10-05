Suppose we have a [[Symmetric Cryptosystems|Symmetric Cryptosystem]] $G,E,D,\mathcal{P},\mathcal{C},\mathcal{K}$, some distribution $\mathcal{D}$ on $\mathcal{P}$. This, along with $E$ gives some distribution of ciphertext in $\mathcal{C}$.
The system is considered perfect if the following holds.
$$\forall x\in \mathcal{P}, y\in\mathcal{C}:P(x)=P(x|y)\iff P(y)=P(y|x)$$
TLDR: Knowing the ciphertext reveals nothing about the plaintext.
## Equivalent formulation
$\forall x,y$, there exists a unique key $k$ such that $E_k(x)=y$ AND keys are uniformly chosen.
## Property
If the cryptosystem is perfect, we have:
$$
|\mathcal{K}|\geq |\mathcal{C}|\geq |\mathcal{P}|
$$