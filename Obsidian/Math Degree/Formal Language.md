---
aliases:
  - Alphabet
  - String
  - Regular Language
---
## Alphabet
An Alphabet $\Sigma$ is considered a set of symbols without $\lambda$. For any $x\in\Sigma$, we call $x$ a symbol. 
We consider only finite alphabets here.
## String
A string is a sequence of symbols in an alphabet $\Sigma$. If $x$ is a string, $|x|$ is the number of symbols in $x$. (We use $\lambda$ to denote an empty string).
A substring $x'$ of a string $x$ is a contiguous sequence of symbols in $x$. 
If $y$ is a substring of $x$, then $|y|\leq|x|$. We may also say $x$ is a superstring of $y$.
### Concatenation
If $x_{1},\dots,x_n=x$ and $y_{1},\dots,y_m=y$ are two strings, we may define $x\circ y= x_{1},\dots,x_n,y_{1},\dots,y_m$.
Strings under concatenation form a [[Monoid]], (not a [[Groups|Group]] since concatenation is not uniquely invertible).
## Language
A formal language $L$ over an alphabet $\Sigma$ is a subset of the set of all strings over $\Sigma$:
$$
L\subseteq S=\{ x|x\text{ is a string over }\Sigma\}
$$
### Positive Closure
We define the positive closure of a language $L$:
$$
L^{+}=\bigcup\limits_{k=1 }^{\infty}L^{k}=L_{1}\cup L_{2}\cup \dots
$$
### Kleene Closure
The Kleene Closure of a string $L$ is defined:
$$
L^{*}=L^{+}\cup \{ \lambda \}
$$
so that empty strings are included in $L^{*}$ even if they are not in $L$.
# Regular Language
A language $L$ over an alphabet $\Sigma$ is regular if it satisfies one of:
- $R=\varnothing$
- $R=\{ \lambda \},R=\{ a \}$ for some $a\in\Sigma$
- $R$ is the concatenation of two regular languages $L_{1},L_{2}$
- $R$ is the Kleene closure or positive closure of a regular language.