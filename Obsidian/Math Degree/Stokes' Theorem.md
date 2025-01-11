Let $S$ be an orientable surface with boundary curve $C$. Then we can relate the [[Line Integrals|Line Integral]] of $\vec{F}$ with its [[Differential Operators|Curl]].
$$\oint_C \vec{F}\cdot d\vec{r}=\iint_S curl(\vec{F})\cdot d\vec{S}$$
### Remarks
- If $\vec{F}=(F_{1}, F_{2},0)$, this is Green's theorem.
- If $S$ is closed, we know from the [[Divergence Theorem]] that 
$$\iint_S curl(\vec{F})\cdot d\vec{S}=\iiint_Ddiv(curl(\vec{F}))dV=0$$
    So $S$ has no boundary curves.
- If two surfaces $S_{1},S_{2}$ share a boundary $C$, then 
$$\iint_{S_{1}}curl(\vec{F})\cdot d\vec{S}=\iint_{S_{2}}curl(\vec{F})\cdot d\vec{S}$$