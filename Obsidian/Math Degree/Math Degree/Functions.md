A function defines a conversion between two sets, $A$ and $B$.

Definition: Suppose $A, B$ are sets. A function $f$ from $A$ to $B$ ($f:A\to B$), is a subset of the [[Cartesian Product]] $A\times B$ and for all $x\in A$, there exists a unique $y\in B$ so that $(x,y)\in f$. 

$A$ is called the [[Domain]] of $f$ and B is the [[Codomain]] of $f$.

If $y=f(x)$, we call $y$ the "image of $x$ under $f$."

## Properties of Functions
### Onto (Surjective)
A function is called Onto if every element of the codomain of f is also in the image.
$$\forall b \in B, \exists a \in A \text{ so that } f(a) = b$$
### One-to-one (Injective)
A function is called one-to-one if no two elements of the domain are mapped to the same element of the image.
$$\forall a,b \in A, f(a)=f(b)\implies a=b$$
Or, more intuitively,
$$\forall a,b\in A, a\neq b\implies f(a)\neq f(b)$$
### Bijective
A function is Bijective if it is both injective and surjective. Bijective functions are invertible.
## Identity Map
The Identity map is the function that sends all elements of a set $A$ to itself.
$id_A(x)=x$ for any $x \in A$.
## Inverse functions
A function $f:A\to B$ is said to have an inverse $f^{-1}:B\to A$
## Function Equality
Two functions are equal if and only if they are subsets of each other.