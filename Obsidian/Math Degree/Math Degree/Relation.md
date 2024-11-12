---
aliases:
  - Equivalence Class
  - Equivalence Relation
---
A relation $\sim$ on a set $A$ is a subset of $A\times A$. We say $a\sim b$ if $(a,b)$ is in this subset.
## Equivalence Relation
An Equivalence relation $R$ on some set $A$ is a relation satisfying:
- Symmetric
    - $\forall a,b\in A, a\sim b\implies b\sim a$
- Reflexive
    - $\forall a\in A, a\sim a$
- Transitive
    - $\forall a,b,c\in A, a\sim b$ and $b\sim c\implies a\sim c$.
[[Modular Arithmetic]] is an example of an equivalence relation.
### Equivalence Class
An equivalence class is a set of objects that are related to another object by a certain [[Relation]].
For some relation $\sim$ on a set $A$, and some element $x$ in $A$, the equivalence class $[x]_R$ is:
$$[x]_r=\{a\in A:a\sim x\}$$
[[Modular Arithmetic]] is built off of these classes.