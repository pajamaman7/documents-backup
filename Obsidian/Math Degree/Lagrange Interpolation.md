Given $\{ z_{1},\dots,z_n \}\subseteq \mathbb{C}$, $\{ w_{1},\dots,w_n \}\subseteq\mathbb{C}$ , we wish to find a polynomial of minimal degree so that $p(z_j)=w_j$. First, find a polynomial $p_k$ so that $p_k(z_j)=\delta_{kj}$:
$$
p_k(z)=\frac{(z-z_{1})\dots(z-z_{k-1})(z-z_{k+1})\dots(z-z_n)}{(z_k-z_1)\dots(z_k-z_{k-1})(z_k-z_{k+1})\dots(z_k-z_n)}
$$
Then take:
$$
p(z)=w_{1}p_{1}(z)+\dots+w_np_n(z)
$$
So that $p(z_j)=w_j$.

$\{ p_{1},\dots,p_n \}$ is a [[Vector Spaces|Basis]] for $\mathbb{P}_{n-1}$; if $c_{1}p_{1}(z)+\dots+c_np_n(z)\equiv 0,$ this must hold for all $z$, we plug in $z_j$ for all $j$  and get $c_{1}=\dots=c_n=0$. Then we get a [[Dual Space|Dual Basis]] for $E_a^{*}$ given by the [[Evaluation Map]]s $E_a$.