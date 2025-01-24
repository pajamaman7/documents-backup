---
aliases:
  - Metric Space
  - Metric
---
A Metric space is one on which a distance function $d$ is defined on any two points $p,q$, satisfying:
- $d(p,q)>0$ provided that $p\neq q$.
- $d(p,q)=d(q,p)$.
- $d(p,q)\leq d(p,r)+d(r,q)$ for any $r$ in the space.
$\mathbb{R}^{n}$ is a metric space for $n\geq 1$, and subsets of metric spaces are also metric spaces.
## Properties and Topology of Metric Spaces
Let $X$ be a metric space, and $E\subseteq X$.
- A *neighbourhood* of $p$ is a set $N_r(p)$ consisting of $q$ so that $d(p,q)<r$ for some $r>0$.
- A point $p$ is a *limit point* of $E$ if any neighborhood of $p$ contains elements $q\in E$ where $q\neq p$.
- A point $p \in X$ is *isolated* if it is not a limit point.
- $E$ is *closed* if it contains all its limit points.
- $p$ is an *interior point* of $E$ if there is a neighborhood $N$ of $p$ so that $N\subseteq E$.
- $E$ is *open* if every point is an interior point.
- The *complement*$E^{c}$ is the set of all $p \in X$, where $p\not\in E$.
- $E$ is *perfect* if it is closed and every point of $E$ is a limit point of $E$.
- $E$ is *bounded* if there exists some real $M$ and $q\in E$ so that $d(p,q)<M$ for every $p \in E$.
    - $E$ is *totally bounded* if for every $\varepsilon>0$ any cover of $E$ by balls of radius $\varepsilon$ has a finite subcover.
- $E$ is *dense* in $X$ if every point of $X$ is a limit point of $E$, or in $E$ (or both).
- A *covering* of $E$ in $X$ is a collection of open subsets $\{ G_{\alpha} \}$ so that $\bigcup_{\alpha}G_{\alpha}\subseteq E$.
- $E$ is *compact* if every open cover of $E$ contains a finite subcover. ($E$ can be finitely covered).
    - See [[Heine-Borel Theorem]]
 