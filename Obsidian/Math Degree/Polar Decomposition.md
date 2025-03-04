Let $A:V\to V$ in a [[Vector Spaces|Finite Dimensional]] [[Inner Product Space]]. There is a [[Adjoints|Unitary]] $U$ so that $A=U|A|$. $U$ may not be unique.
## Diagonal case
If $D=\text{diag}\{ \lambda_{1},\dots,\lambda_n \}$, then $U=\text{diag}\{ c_{1},\dots,c_n \}$ where: 
$$
c_j=\begin{cases}
\frac{\lambda_j}{|\lambda_j|} &\text{if } \lambda_j\neq 0\\ \\
1 & \text{otherwise}
\end{cases}
$$
## Invertibility
If $A$ is invertible, we must have $U=A|A|^{-1}$.
## Normal case
Suppose $N$ is [[Normal Operators|Normal]], and use its [[Diagonalization]] to find a polar decomposition. Then $\exists$ a [[Adjoints|Unitary]] $V$ so that $V^{*}NV=D$ is diagonal. We know that $V|D|V^{*}=|N|$. Let $U|D|=D$ be a polar decomposition. Then $N=VUV^{*}|N|$
## General Construction of $U$
Let $v\in V$ and set $u=|A|v\in \text{ran}A$. Set $U_{0}:\text{ran}|A|\to V$ by $U_{0}u=Av$. 
Since $u=|A|v$ may not have a unique solution $v$, we must verify $U_{0}$ is well-defined.
Suppose $u=|A|v=|A|v_{1}$. Then $|A|(v-v_{1})=0$, and $v-v_{1}\in\ker|A|=\ker A$, and $Av=Av_{1}=U_{0}u$.
$U_{0}$ is linear since $A$ is, and then since $\| U_{0}u \|=\| Av \|=\| |A|v \|=\| u \|$, therefore $U_{0}$ is a well-defined [[Adjoints|Isometry]] defined on $\text{ran}A$. Computing:
$$
Av=U_{0}|A|v
$$
And we have our desired computation. What if $\text{ran}|A|\neq V$?
We have $\text{ran}U_{0}=\text{ran}A$ by definition. Then
$$
U_{0}:\text{ran}|A|\to\text{ran}A
$$, so $U_{0}$ is a unitary from $\text{ran}|A|$ to $\text{ran}A$. 
We have $\text{ran}|A|^{\perp}=\ker|A|$, and $(\text{ran}A)^{\perp}=\ker A^{*}$, and both these pairs have the same dimension. So we can find a unitary from $U_{1}:\text{ker}|A|=\ker A\to\ker A^{*}$, Define $U:V\to V:$
$$
U=\begin{bmatrix}
U_{0}&0\\0&U_{1}
\end{bmatrix}
$$
$U$ is unitary since $U_{0},U_{1}$ are, and for $v\in\text{ran}|A|, w\in\ker A$,
$$
\begin{align}
U|A|(v+w)&=U|A|v+U|A|w \\
&=U|A|v \\
 & =U_{0}|A|v \\
 & =Av +0\\
 & =Av+Aw \\
 & =A(v+w)
\end{align}
$$
