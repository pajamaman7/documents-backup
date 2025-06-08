---
aliases:
  - Deterministic Finite Automata
---
# DFA (Deterministic Finite Automata)
A Deterministic Finite Automata is defined by a 5-tuple $(Q,\Sigma)$
- $Q$, the set of states
- $\Sigma$, an input [[Formal Language|Alphabet]]
- $\delta$, a transition [[Functions|Function]] defined $\delta:Q\times\Sigma\to Q$
- $q_{0}\in Q$, an initial state
- $A\subseteq Q$ a set of acceptable states.
When processing a string $s \in\Sigma ^{*}$,