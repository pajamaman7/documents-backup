Given a [[Topology|Topological Space]] $X$, a map $f:X\to Y$, we define the mapping cylinder:
$$
M(f)=(X\times I) \sqcup Y / \sim
$$
Where the relation $\sim$ is defined $(x,t)\in X\times I$, then $(x,1)\sim f(x)$.
## Theorem
$(M(f),X)$ has the [[Homotopy Extension Property]].
## Huh
There is a [[Homotopy]]:
$$
H:M(f)\times I\to M(f)
$$
with
- $H(y,t)=y$
- $H((x,s),t)=(x,(1-t)s)$
