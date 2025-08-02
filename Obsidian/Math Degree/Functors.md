---
aliases:
  - Functor
  - Faithful Functor
  - Forgetful Functor
  - Full Functor
---
Let $\mathcal{A},\mathcal{B}$ be [[Categories]]. A functor $F$ from $\mathcal{A}$ to $\mathcal{B}$ consists of:
- A function from $\mathrm{ob}\mathcal{A}$ to $\mathrm{ob}\mathcal{B}$, $A\mapsto F(A)$
- For each $A,A'\in\mathcal{A}$, a function from $\mathrm{Hom}(A,A')$ to $\mathrm{Hom}(F(A),F(A'))$, $f\mapsto F(f)$
Satisfying:
- $F(1_A)=1_{F(A)}$
- $F(fg)=F(f)F(g)$
## Faithful and full
A functor $F$ is called full if it is surjective (with respect to morphisms).
$F$ is faithful if it is injective (with respect to the morphisms)
## Forgetful Functors
A forgetful functor is one that forgets part of the structure. For example, there is a forgetful functor $F:\mathrm{Grp}\to\mathrm{Set}$, which maps a [[Groups|Group]] to its underlying set.