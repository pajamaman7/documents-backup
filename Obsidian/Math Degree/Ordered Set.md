---
aliases:
  - Supremum
  - Bounded
  - Infimum
  - Order
  - Partial Order
---
Let $S$ be a set. A total order $<$ is a [[Relation]] on $S$ with the properties:
- If $x,y\in S$, either $x<y,y<x$, or $x=y$.
- If $x,y,z\in S$ then if $x<y$ and $y<z$, $x<z$. ($<$ is transitive)
An ordered set is one on which an order is defined.
A partial order $\leq$ follows:
- $a\leq a$, it is reflexive
- $a\leq b$ and $b\leq a\implies a=b$, $\leq$ is antisymmetric
- $a\leq b$ and $b\leq c\implies a\leq c$, transitivity.  
## Bounded
A set $E\subseteq S$ is bounded above if there exists some $\beta \in S$ so that for all $\alpha \in E$, $\alpha\leq\beta$.
A set is bounded below identically with $\geq$.
## Supremum and Infimum
$\alpha$ is a supremum for a set $E$ which is bounded above, or $\alpha=\sup E$ if:
- $\alpha$ is an upper bound for $E$.
- If $\gamma<\alpha$, then $\gamma$ cannot be an upper bound for $E$.
$\alpha$ is a infimum for a set $E$ which is bounded below, or $\alpha=\inf E$ if:
- $\alpha$ is a lower bound for $E$
- If $\gamma>\alpha$, $\gamma$ is not a lower bound for $E$.
Note that infimums and supremums may or may not be contained in $E$.
## Least upper bound property
A set $S$ is said to have the least upper bound property if: For any nonempty $E\subseteq S$ that is bounded above, $\sup E\in S$.
$$

$$