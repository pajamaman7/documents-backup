A Turing Machine is uniquely defined as a tuple,
- $Q=\{q_0,q_1,q_2,\dots,q_{\text{a}}\}$,
- $\Sigma$ is a finite input [[Formal Language|Alphabet]] not containing $\perp$.
- $T$ is a finite tape alphabet, satisfying $\Sigma \cup\{ \perp \}\subseteq T$ (with $\perp$ denoting the blank symbol).
- The transition function $\delta$ is defined on some subset of $Q\times T$ to the set $Q\times T\times \{ R,L \}$.
- An initial state $q_{0}$ and accepting state $q_a$.