## Binary operation
If $f,g$ are paths, with $f(1)=g(0),$ define :
$$
f*g=\begin{cases}
f(2t) & 0\leq t\leq \frac{1}{2}\\
g(2t-1) & \frac{1}{2}\leq t\leq 1
\end{cases}
$$
This operation is associative with respect to homotopy classes.
### On Homotopy Classes
As such, we define the operation on homotopy classes; if $f,g$ are [[Paths and Loops|Paths]], with $f(1)=g(0)$, define:
$$
[f]*[g]=[f*g]
$$
This operation satisfies some familiar properties;
- $([f][g])[h]=[f]([g][h])$
- If $e_c:I\to X$ is the constant point at $c$, we have the identities:
	- $[e_{f_{0}}][f]=[f]$
	-  $[f][e_{f_{1}}]=[f]$
- We define $\bar{f}(t)=f(1-t)$, then take $[f]^{-1}=[\bar{f}]$. This satisfies:
	- $[f][f^{-1}]=[e_{f_{0}}]$ 
	- $[f]^{-1}[f]=[e_{f_{1}}]$
## The Fundamental Group
Define:
$$\pi_{1}(X,p)=\{ f:I\to X |\text{ $X$ is a loop on }p\}$$
With composition as above. Since endpoints will all be at $p$, we have composition well-defined. Associativity follows from above. We define our identity element, the constant map $e(t)=p$ which remains at $p$. And finally to find an inverse for a loop, we simply traverse it backwards.
All this to say $\pi_{1}(X,p)$ is a [[Groups|Group]], called the [[Fundamental Group]].
### Induced Homomorphisms
Let $f:(X,p)\to(Y,q)$ with $f(p)=q$. Take $\gamma$ a loop on $p$.  Then $f\gamma:I \to Y$ is a loop in $Y$. This defines a set mapping, 
$$
F_*:\pi_{1}(X,p)\to \pi_{1}(Y,q)
$$
Since if $H$ is a [[Homotopy]] from $\gamma_{1}$ to $\gamma_{2}$, then $fH$ is a homotopy from $f\gamma_{1}$ to $f\gamma_{2}$.
In fact, the map $f_*$ is a [[Group Homomorphism and Isomorphism|Homomorphism]], satisfying $(fg)_*=f_*g_*$, and $f_*(e)=e$.
### Dependence on Basepoint
Suppose $X$ is [[Path-Connected]]. Then the fundamental group satisfies:
$$
\pi_{1}(X,p)\cong\pi_{1}(X,q)
$$
For any $p,q$ in the space.
### Maps Between Spaces
If $f,g:X\to Y$ are both [[Continuity|Continuous]] maps on [[Topology|Topological Spaces]], and $f(p)=g(p)$ for some basepoint $p$. Suppose $f\simeq g$ relative to $p$. Then $f_*=g_*$ HUH
## Theorem
The fundamental group $\pi_{1}(S^{1})=\mathbb{Z}$