#Incomplete/Incorrect
Let $A:\mathcal{V}\to \mathcal{W}$, [[Vector Spaces|Finite Dimensional]] [[Inner Product Space|Inner Product Spaces]], and $r:=rank A$, $r\leq\min\{ \dim \mathcal{V},\dim \mathcal{W} \}$. We seek to find [[Orthogonality|Orthonormal]] bases $\{ v_{1},..,v_n \}$ and $\{ w_{1},\dots,w_{n} \}$ so that:
$$
[A]=\begin{bmatrix}
\sigma_{1}&&&0 \\
&\ddots &&0 \\
&&\sigma_r&0 \\
0&0&0&0
\end{bmatrix}
$$
## Construction
Let $\dim \mathcal{V}= n$, $\dim \mathcal{W}=m$. $A^{*}A$ is positive semi-definite, so $\ker A^{*}A=\ker A$, so $r=rankA=rankA^{*}A$ (by rank-nullity). Then we can unitarily diagonalize:
$$
A^{*}A\sim_Udiag\{ \sigma_{1}^{2},\dots,\sigma_n^{2},0,\dots,0 \}
$$
And the matrix norm gives us $|A|\sim_Udiag\{ \sigma_{1},\dots,\sigma_r,0,\dots,0 \}$. Then we take the unitary $U$ so that $\sigma_{i}>\sigma_{i+1}$, and then take $\{ v_{1},\dots,v_r,v_{r+1},\dots,v_n \}$ for the columns of the unitary. Then
$$
\begin{align}
A^{*}Av_j&=\sigma _j^{2}v_j& \\
|A|v_j&=\sigma_jv_j \\
|A|v_j&=0&j=1,\dots
\end{align}
$$
Then define $w_j=\frac{1}{\sigma_j}Av_j$ for $j=1,\dots,r$ in $\mathcal{W}$.
Then our $w_i$'s form an orthonormal set.
# Theorem: Schmidt 
Let $A,\sigma_j,v_j,w_j$ all as above. Then 
$$ A=\sum\limits_{j=1}^{r}\sigma_jw_jv_j^{*} $$
This is called a Schmidt decomposition, and it is not unique.
## Corollary
If $A=\sum\limits_{j=1}^{r}\sigma_jw_jv_j^{*}$ is a Schmidt decomposition for $A$, then $A^{*}=\sum\limits_{j=1}^{r}\sigma_jv_jw_j^{*}$ is a Schmidt decomposition for $A^{*}$.