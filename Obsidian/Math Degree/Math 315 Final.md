Priority of content is on the after-midterm content
(20%) Pre-midterm will mainly focus on Lagrange, or small subgroup tests; Normal subgroups, Dihedral and Symmetric Groups, Cauchy's theorem and Class Equations.
(10%) Group Actions
(10%) Quotient Groups, isomorphism theorems
(15%) Ring Basics, integral domains, ideals; questions from definitions.
(15%) Prime and maximal ideals; quotient rings, ring isomorphism theorem
(15%) Polynomial Rings
## Review
-  Normal Subgroups; remember to show subgroup, that it is nonempty, then show one of:
    - $aN=Na$ for all $a\in G$
    - $gNg^{-1}\subseteq H$ for all $g\in G$
    - $gNg^{-1}= H$ for all $g\in G$
- $D_n=\left< r,s|r^{n}=e,s^{2}=e, r^{2}=s \right>$
    - $rs=s r^{n-1}$
- $A_n=$ even permutations in $S_n$
- Cauchy's theorem, if $G$ a finite group, for every divisor $p|G$, prime, there is a subgroup of order $p$. (likewise with order)
- $|G|=\sum\limits_{ }^{}Cl(a)$
- $|G|=|Cl(a_i)| |C(a_i)|$ where $C(a_i)=\{ g\in G : ga_i=a_ig \}$
- Group action $G\curvearrowright X$:
    - $e\cdot x=x$
    - $a\cdot(b\cdot x)=ab\cdot x$
    - $Orb(x)=\{ g\cdot x:g\in G \}\subseteq X$
        - Orbits partition $X$
    - $Stab(x)=\{ g\in G: g\cdot x \}\leq G$
- Class equation is a special case of orbit-decomposition theorem:
    - $G\curvearrowright X$ then $|Orb(x)| |Stab(x)|$; $Orb(x)=[G:Stab(x)]$
### Rings!
- Show identity to show ring
- Zero divisors are those that appear in a zero product
- Units have multiplicative inverses
- Domains have no zero divisors, and integral domains are commutative domains. If $R$ satisfies both of these and every element is a unit, it is a field.
- Integral domains can be embedded inside a field, called a field of fractions.
- Check well-definedness for multiple representations
- Prime, maximal ideals - check $I\neq R$ for both cases.
    - prime: $R /P$ is an integral domain
        - $\{ 0 \}$ prime ideal $\iff$ $R$ is an ID
    - maximal: $R / M$ is a field
        - $\{ 0 \}$ maximal ideal $\iff R$ is a field.
- In a field $F$, $\{ 0 \},F$ are the only ideals.