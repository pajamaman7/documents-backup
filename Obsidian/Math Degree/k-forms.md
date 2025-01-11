- A $0$-form is a function in three variables, usually [[Differentiable]]
- A $1$-form is an expression like $F_{1}(x,y,z)dx+F_{2}(x,y,z)dy+F_{3}(x,y,z)dz$.
- A $2$-form is an expression like $F_{1}(x,y,z)dy \land dz+F_{2}(x,y,z)dz\land dx+F_{3}(x,y,z)dx\land dy$.
- A $3$-form is of the form: $f(x,y,z)dx\land dy\land dz$
## Addition
Addition of k-forms is as follows:
- for $0$-forms, we can add the functions.
- For $1$-forms, the sum of some $\vec{F},\vec{G}$ is $(F_{1}+G_{1})dx+(F_{2}+G_{2})dy+(F_{3}+G_{3})dz$.
- For $2$-forms, the sum of some $\vec{F},\vec{G}$ $(F_{1}+G_{1})dy\land dz+(F_{2}+G_{2})dx\land dz+(F_{3}+G_{3})dx\land dy$
- For $3$-forms, the sum of some $\vec{F},\vec{G}$ is $(f(x,y,z)+g(x,y,z))dx\land dy\land dz$
Only k-forms of the same $k$ can be added.
## Multiplication
Multiplication on k-forms is called the [[Wedge Product]]. It is determined by the following rules:
1. Multiplication by a 0-form distributes; $f\land(F_{1}dx+F_{2}dy+F_{3}dz)=fF_{1}dx+fF_{2}dy+fF_{3}dz$ (This generalizes for any form)
2. The wedge product satisfies the following linear properties:
    - If $\omega_{1}$ and $\omega_{2}$ are k-forms and $f,g$ scalar functions, then $(f\omega_{1}+g\omega_{2})\land \tilde{\omega}= f\omega_{1}\land \tilde{\omega}+g\omega_{2}\land \tilde{\omega}$
3. If $\omega$ is a k-form and $\tilde{\omega}$ a j-form, $k,j\in\{ 0,1,2,3 \}$, then $\omega \land \tilde{\omega}=-1^{kj}\tilde{\omega}\land \omega$.
    - If $jk$ is odd, $\omega \land \tilde{\omega}=-\tilde{\omega}\land \omega$
    - If $k$ is odd, $\omega \land \omega=0$
4. ${\omega}\land(\tilde{\omega}\land \tilde{\tilde{\omega}})=({\omega}\land\tilde{\omega})\land \tilde{\tilde{\omega}}$
5. If $k+j=4$, $\omega \land \tilde{\omega}=0$.
## Derivative
The *Exterior Derivative* acts on [[k-forms]]. It is defined $d:$ $k$-forms $\to\, k+1$ forms
and $d\omega=0$ for any $3$-form.
- $d$ is linear, $d(c_{1}\omega_{1}+c_{2}\omega_{2})=c_{1}d(\omega_{1})+c_{2}d(\omega_{2})$.
- "Graded product rule," for a $k$-form $\omega_{1}$ and a $j$-form $\omega_{2}$: $d(\omega_{1}\land \omega_{2})=d(\omega_{1})\land \omega_{2}(-1)^{k}+\omega_{1}\land d(\omega_{2})$.
- On a $0$-form $\omega$: $d(\omega)=\omega_x dx+\omega_y dy+\omega_z dz$.
- $d(d(\omega))=0$ for any $k$-form.
## Integration
- 0-forms:
    - If $P$ is a point in $\mathbb{R}^{3}$,define:
$$\int_{P}^{} f :=f(P) $$
    More generally for point $P_{1},P_{2},\dots,P_k$ in $\mathbb{R}^{3}$ and integers $n_{1},n_{2},n_{3}$, define
- 1-forms:
    - Let $\omega=F_{1}dx+F_{2}dy+F_{3}dz$,
    $$\int_{C}^{} \omega =\int_{C}^{} \vec{F}\cdot d \vec{r}$$
    Where $C$ is a curve
- 2-forms:
    - Let $\omega=F_{1}dy\land dz+F_{2}dz\land dx+F_{3}dx\land dy$,
$$\int_S\omega:=\iint_S \vec{F}\cdot d \vec{S}$$
- 3-forms:
    - Let $\omega=fdx\land y\land dz$
$$\int_{D}^{} \omega =\iiint_Df(x,y,z)dV $$
    Where $D$ is a solid in $\mathbb{R}^{3}$
    