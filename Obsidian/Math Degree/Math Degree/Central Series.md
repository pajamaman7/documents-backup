---
aliases:
  - Ascending Central Series
  - Descending Central Series
---
## Ascending
Ascending central series are used to construct a [[Series of Subgroups]] starting from $\{ e \}$ and going to $G$. Construct the series as follows:
$$Z_{0}(G)=\{ e \},\quad Z_{1}(G)=Z(G)$$
And the subgroup $Z_{i+1}$ is the unique subgroup containing $Z_i$ and satisfying ${Z_i}/{Z_{i+1}}=Z\left( \frac{G}{Z_i(G)} \right)$. 
For some groups, this series starts and ends with $\{ e \}$. If this series terminates, that is for some $i$, $Z_i(G)=G$, we say that $G$ is a [[Nilpotent Groups|Nilpotent Group]]
## Descending
These are constructed by starting at $G$ and identifying subgroups, hopefully ending at $\{ e \}$. 
If $H,K$ are subgroups of $G$, define $[H,K]=\left< [h,k]:h\in H, k\in K \right>$.
Denote the series: $\Gamma_{0}(G)=G$, $\Gamma_{1}(G)=[G,G]$, and $\Gamma_{i+1}(G)=[\Gamma_i(G),G]$
This interestingly resembles the ascending series, since
$\Gamma_i(G) /\Gamma_{i+1}(G)\leq Z(G / \Gamma_{i+1}(G))$
## Theorem
If $G$ is a [[Groups|Group]], the following are equivalent:
- There exists an $n>0$ such that $\Gamma_n(G)=\{ e \}$
- $Z_n(G)=G$
- There exists a [[Series of Subgroups|Subnormal Series]] $G=G_{0}\geq\dots\geq G_n=\{ e \}$ so that $G_i /G_{i+1}\leq Z(G/G_{i+1})$.
- $G$ is a [[Nilpotent Groups|Nilpotent Group]].