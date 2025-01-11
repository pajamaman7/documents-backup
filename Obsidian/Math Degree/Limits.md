A limit follows the idea of finding a value of a [[Functions|Function]] that is "sufficiently close" to a point. The notation is as follows:
$$\lim_{x\to a}f(x)=L$$
Where $f$ is our function, $a$ is the point we are getting close to, and $L$ is the evaluated result.

## Delta-Epsilon Proofs
A Delta-Epsilon proof restricts the range of our function to a small radius $\epsilon$ around $L$. Then, we prove that there is a related, similarly small radius $\delta$ that the domain of $f$ must also be restricted to. As $\delta$ gets "sufficiently small," so will $\epsilon$.

$$\lim_{x\to a}f(x)=L\iff \forall \epsilon>0,\exists \delta>0: \forall x, |x-c|<\delta\implies|f(x)-L|<\epsilon$$
