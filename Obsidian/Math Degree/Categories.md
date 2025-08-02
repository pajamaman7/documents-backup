---
aliases:
  - Category
---

A category $C$ is a collection of objects, along with a collection of **morphisms** satisfying:
- Each morphism has domain and codomain objects, denoted as typical; $f:x\to y$.
- Identity: For any object $x,$ there exists a morphism $1_x:x\to x$. This introduces the condition that $1_yf=f,f {1}_x=f$
- Composition: For any $f:x\to y$, $g:y\to z$, there exists a composite morphism, $gf:x\to z$ This introduces the law of associativity, $f(gh)=(fg)h=fgh$.
## Concrete Categories
These categories are those whose underlying objects are sets, and their morphisms are functions between their objects, typically preserving the structure of the object.
 - Set has sets as its objects and [[Functions]], with specified domain and codomain, as its morphisms.
 - Top has [[Topology|Topological Spaces]] spaces as its objects and [[Limits and Continuity in Metric Spaces|Continuous]] functions as its morphisms.
 - Set$_{*}$ and Top$_{*}$ have sets or spaces with a specified basepoint$^6$ as objects and basepoint-preserving (continuous) functions as morphisms.
 - Group has [[Groups]] as objects and [[Group Homomorphism and Isomorphism|Group Homomorphism]]s as morphisms. This example lent the general term “morphisms” to the data of an abstract category. The categories Ring of associative and unital [[Rings]] and [[Ring Homomorphism And Isomorphism|Ring Homomorphisms]] and Field of [[Fields]] and field homomorphisms are defined similarly.
 - For a fixed unital but not necessarily commutative ring R, Mod$_R$ is the category of left R-modules and R-module homomorphisms. This category is denoted by Vect$_k$ when the ring happens to be a field k and abbreviated as Ab in the case of Mod$_Z$, as a Z-module is precisely an abelian group.
 - Graph has graphs as objects and graph morphisms (functions carrying vertices to vertices and edges to edges, preserving incidence relations) as morphisms. In the variant DirGraph, objects are directed graphs, whose edges are now depicted as arrows, and morphisms are directed graph morphisms, which must preserve sources and targets.
 - Man has smooth (i.e., infinitely differentiable) manifolds as objects and smooth maps as morphisms.
 - Meas has measurable spaces as objects and measurable functions as morphisms.
 - Poset has partially-ordered sets as objects and order-preserving functions as morphisms.
 - Ch$_R$ has chain complexes of R-modules as objects and chain homomorphisms as morphisms.$^7$
- For any signature σ, specifying constant, function, and relation symbols, and for any collection of well formed sentences T in the first-order language associated to σ, there is a category Model$_T$ whose objects are σ-structures that model T, i.e., sets equipped with appropriate constants, relations, and functions satisfying the axioms T. Morphisms are functions that preserve the specified constants, relations, and functions, in the usual sense.$^8$ Special cases include (iv), (v), (vi), (ix), and (x).
## Abstract Categories
Abstract categories consist of objects that may not be sets themselves.