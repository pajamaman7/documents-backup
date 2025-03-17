We can define the operator norm;
$$ \| A \| _{op}=\max \{ \| Av \| :v\in X,\| v \| =1 \} $$
Which is the largest singular value of $A$, or the greatest [[Normed Vector Space|norm]] $A$ induces to the unit ball.
## Properties
$L(X,Y)$ is a [[Normed Vector Space]] under $\| \cdot \|_{op}$. It satisfies the usual properties, as well as:
- $\| Av \|\leq \| A \|_{op}\| v \|$
- The norm is sub-multiplicative, $\| AB \|\leq\| A \|\| B \|$ ($\| \cdot \|_{op}$ is a [[Banach Norm]])
- $\| A^{*}A \|=\| A \|^{2}=\| A^{*} \|^{2}$, $L(X)$ is a [[C*-algebra]]
## Hilbert-Schmidt Norm
(In this case we discuss $M_n(\mathbb{C})$)
Define the norm 
$$
\| A \| _2=\sqrt{ tr(AA^{*}) }=\sqrt{ tr(A^{*}A) }=\sqrt{ \sum\limits_{}^{}\sigma_i }
$$
Where $\sigma_i$ are singular values of $A$.