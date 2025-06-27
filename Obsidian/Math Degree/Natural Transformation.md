Let $\mathcal{A},\mathcal{B}$ be [[Categories]] and $F,G:\mathcal{A}\to\mathcal{B}$ be [[Functors]]. A natural transformation from $F$ to $G$ is a family of maps $\left(\alpha_A: F(A)\to G(A) \right)_{A\in\mathcal{A}}$, such that the following diagram commutes for any $A,A'\in\mathcal{A}$ and $f\in\mathrm{Hom}(A,A')$
 ```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
  F(A) \arrow[r, "Ff"] \arrow[d, "\alpha_A"] & F(A') \arrow[d, "\alpha_{A'}"] \\
  G(A) \arrow[r, "Gf"] & G(A')
\end{tikzcd}
\end{document}
```