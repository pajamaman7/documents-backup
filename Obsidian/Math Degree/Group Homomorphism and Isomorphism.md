---
aliases:
  - Isomorphic
  - Isomorphism
  - Homomorphism
  - Group Homomorphism
---
Now we study the structure of groups in relation to each other.
## Homomorphism
If $G, H$ are two [[Groups]], then a homomorphism is a [[Map]] $f: G\to H$ so that
- $h(e_G)=e_{H}$
- $f(a\circ_{G}b)=f(a)\circ_{H}f(b)$
### Properties
For any $g\in G$:
- $f(e_G)=e_H$
- $f(g^{-1})=f(g)^{-1}$
- $\forall k\in \mathbb{Z}:\,f(g)^{k}=f(g^{k})$
- [[Groups|Order]]: If $o(g)=n\in \mathbb{Z}_{> 0}$,  $o(f(g))|o(g)$. 
### Kernel, Image
The Kernel of a homomorphism $f$ is the subgroup:
$$\ker(f)=\{ g\in G: f(g)=e_H \}$$
(Think [[Null Space]])
The Image of $f$ is the subgroup:
$$\mathrm{Im}(f)=\{ h\in H : \exists g\in G, f(g)=h \}$$
(Of course this is [[Image Space]])
### Onto
An onto homomorphism has:
$$\mathrm{Im}f=H$$
### One-to-one
An one-to-one homomorphism has:
$$\ker f=\{ e_G \}$$
## Isomorphism
If a homomorphism $f$ is a [[Bijection]] we call it an isomorphism. We say $G\cong H$, $G$ is isomorphic to $H$. 
### Up to Isomorphism
Two groups are said to be the same up to isomorphism, if they are in the same equivalence class (or there exists an isomorphism between them).
### Properties
- The identity map $id_G:G\to G$ is an isomorphism $G\cong G$.
Let $f:G\to H$ be an isomorphism.
- If $G$ is cyclic, so is $H$.
- If $G$ is abelian, so is $H$.
- $f^{-1}:H\to G$ is also an isomorphism
- If $g:H\to K$ is another isomorphism, then $f\circ g$ is an isomorphism.
- If $G$ is a group of order $2p$ for a prime $p$, then $G$ is isomorphic to $C_{2p}$ or $D_p$.
## Automorphism
An automorphism is an isomorphism $f:G\to G$. Write:
$$Aut(G)=\{ f:G\to G:\text{$f$ is an isomorphism} \}$$
The set of all isomorphisms on a group forms its own group under composition.
Automorphisms must send generators to generators; since $o(g)=o(f(g))$.