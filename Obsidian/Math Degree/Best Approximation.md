# Metric Spaces
Given a [[Metric Spaces|Metric Space]] $(E,d)$, and a subset $A\subseteq E$. If $x\in E$, then the distance from $x$ to the set $A$ is: $d(x,A)=\inf_{y\in A}d(x,y)$. The general problem of approximation is to determine whether this infimum is reached in $A$.
	If $a\in A$ satisfies $d(x,A)=d(x,a)$, we call it an element of best approximation to the element $x\in E$. 
## Theorem
If $A$ is [[Compactness|Compact]] subset of $E$, then we are guaranteed to have some such $a$ as above, for any $x\in E$.
# Case: Normed Vector Space
Let $(E,\| \cdot \|)$ be a [[Normed Vector Space]]. Then of course $E$ is a [[Metric Spaces|Metric Space]], and the above properties hold. 
## Theorem
Let $A\subseteq E$ be a [[Vector Spaces|Finite Dimensional]] subspace. Then for each $x\in E$, there exists $a\in A$ such that $\| x-a \|=d(x,A)$.