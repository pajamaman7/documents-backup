---
aliases:
  - Galois Group
---
## Galois Group
 If $E\supseteq F$ are fields, Galois theory is concerned with the automorphisms $\sigma{:}E\to E$ that fix $F$ in the sense that $\sigma(a)=a$ for all $a\in F.$ In this case, $\sigma$ is called an $F$-automorphism $E$.
 The set of all these automorphisms on a particular field form a group; $gal(E:F)=\{ \sigma:E\to E| \sigma \text{ is an automorphism},  \forall a\in F,\sigma(a)=a \}$
### Examples
$gal(\mathbb{C}:\mathbb{R})$ must have $\sigma(x)=x$ for real $x$. Then $\sigma(a+bi)=\sigma(a)+\sigma(i)b$. But $\sigma(i^{2})=\sigma(i)\sigma(i)=-1\implies\sigma(i)=\pm i$. So $\sigma$ is determined entirely by where we send $i$ and, having order $2$, $gal(\mathbb{C}:\mathbb{R})=\mathbb{Z}_{2}$.
### Finding Galois Groups
Galois groups must be characterized by elements. Then, by counting elements we can partly characterize the group. If the order of the group does not identify the group, we must rely on other composition rules to characterize the group. (See [[Groups of order n]])
