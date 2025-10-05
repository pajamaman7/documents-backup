## Advantage
Adversary sends blocks  $x_{1},x_{2},\dots$ and receives $y_{1},y_2,\dots$ where $y_{1}$ is returned after encrypting $x_{1}$ through DES.
Compare this to $x_{1}$ returning $y_i$ randomly. If the block cipher is secure, the adversary should not be able to tell random $y_i$ versus deterministic.
For an adversary $A$, define:
$$
Adv(A)=|P(A \text{ guesses real}|\text{real})-P(A \text{ guesses rand}|\text{rand})|
$$
This measures how "right" the adversary is.
## Definition
$\{ E_k|k\in\mathcal{K} \}$ is $(t,q,\varepsilon)-$PRF secure, if for any adversary $A$, run on time $<t$, with queries $<q$, we can ensure $Adv(A)<\varepsilon$