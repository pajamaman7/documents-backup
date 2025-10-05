---
aliases: []
tags:
  - ComplexAnalysis
al:
---
This whole page is made irrelevant by [[Topology of R^n]], [[Topology]] or [[Normed Vector Space]], save for the section on complex infinity.
## Neighbourhood of Infinity
$\infty_ \mathbb{C}$ is not a number, and is not in the set $\mathbb{C}$. Think of it as a circle with infinite radius about the plane.
We write $\bar{\mathbb{C}}=\mathbb{C}\cup \{ \infty _\mathbb{C} \}$
A *Basic Neighbourhood of Infinity* is:
$$U=\{ z\in\mathbb{C}:\lvert z \rvert>M \}$$
For $M>0$. This is also the complement of a closed disc centered at the origin.
A neighbourhood of $\infty_{\mathbb{C}}$ is any set that contains a basic neighbourhood of infinity.
$\infty _\mathbb{C}$ is a cluster point of $A\subseteq \mathbb{C}$ if for all basic neighbourhoods of $\infty_ \mathbb{C}$ we can find points of $A$. Hence, $A$ is unbounded.
## Open Disc
The open disc of center $z_{0}\in\mathbb{C}$ and radius $r>0$ is denoted and defined by:
$$D(z_{0},r)=\{ z\in\mathbb{C}: |z-z_{0}|<r \}$$
In the complex plane this forms a circle around $z_{0}$ of radius $r$ with the boundary not included.
## Open Set
A set $A\subseteq \mathbb{C}$ is open if for every $x \in A$, there exists an open disc $D$ centered on $x$ with arbitrary radius so that $D\subset A$ .
The sets $\varnothing, \mathbb{C}$ are considered trivially open.
The above definition is equivalent to:
$A$ is open $\iff$ $A$ can be written as a union of open discs.
## Closed Disc
The open disc of center $z_{0}\in\mathbb{C}$ and radius $r>0$ is defined by:
$$\{ z\in\mathbb{C}:|z-z_{0}|\leq r \}$$
or, an open disc with the included boundary.
## Neighbourhood
A neighbourhood of $z_{0}$ is a set $U\subset \mathbb{C}$ which contains an Open Disc centered on $z_{0}$.
Trivially, $D(z_{0},r)$ is a neighbourhood of $z_{0}$. This is called a basic neighbourhood.
## Cluster Point
(aka limit or accumulation point)
A point $z_{0}\in\mathbb{C}$ is a cluster point of the set $A\subseteq \mathbb{C}$ if in any neighbourhood of $z_{0}$ we find elements of $A$ that are not $z_{0}$. 
Note that $z_{0}$ is not necessarily in $A$.
Equivalently, for any $r>0$, there exists some point $z$ so that $\lvert z-z_{0} \rvert<r$.
## Isolated point
A point $z_{0}\in\mathbb{C}$ is an isolate point of $A\subseteq C$ if there exists a neighbourhood of $z_{0}$ with no elements of $A$ other than $z_{0}$.
## Closed set
A closed set $S\subseteq \mathbb{C}$ is a set that contains all its closure points (cluster and isolated points). The isolated points are trivially in $S$, however cluster points of $S$ may not be in $S$.
$\infty_\mathbb{C}$ can be ignored when checking if a set is closed. Though it may be a cluster point, it cannot be contained within $S$.
## Bounded Set
A set $A\subseteq \mathbb{C}$ is bounded if there exists some $M>0$ so that for all $z\in A$, $\lvert z \rvert<M$.
## Compact Set
A bounded and closed set is called Compact.
