---
tags:
  - Calc
aliases:
  - Parametric Curve
---
A Parametric Curve $C$ is the range of a vector-valued, $\vec r(t):\mathbb{R}\to \mathbb{R}^n$. 
$\vec r$ is called a parametrization of $C$. ($\vec r$ is not unique). 
## Velocity/speed
Velocity at time $t$ of $\vec v(t) = \vec r' (t)$ is $D\vec r(t)$.
The speed at time $t$ is $v(t)=||\vec v(t)||$.
### Arc Length
The arc length from $t=t_0$ to $t=t_1$ is given by:
$$\int_{t_0}^{t_1}v(t)dt$$
This quantity is independent of parameterization.
From time $t_0$ this can be called $s(T)$.
$$s(T)=\int_{t_0}^{T} v(t)dt$$
### Rectifiable Length
Given $t_{0}\in I$, the rectifiable length from a curve $\alpha:I\to \mathbb{R}^{3}$ is given by
$$
l(\alpha,P):=\sum\limits_{k=1 }^{n}|\alpha(t_k)-\alpha(t_{k-1})|
$$
Where $P$ is a partition of $[a,b]$ given by the points $a=t_{0}<t_{1}<\dots<t_n=b$. $|.|$ denotes Euclidean distance.
#### Error
Let $\alpha:I\to \mathbb{R}$ be a regular parameterized curve.
Given $\epsilon>0$, there exists $\delta>0$ so that 
## Acceleration
The acceleration of a parametric curve given by $\vec r(t)$ is $\vec a(t)=D\vec v(t)=\vec r''(t)$.
### Tangential and Normal Components
Our acceleration vector can be decomposed with [[Tangent, Normal, Binormal Vectors]].
$$\vec{a}=(\vec{a}\cdot \vec{T})\vec{T}+(\vec{a }\cdot\vec{N})\vec{N}$$
(Note that our decomposition of $\vec{a}$ does not include a $\vec{B}$ component since $\vec{a}\cdot \vec{B}=0$).

We can write both parts of this sum as components of acceleration; giving the following:
- $\vec{a}=a_T\cdot \vec{T}+a_N\cdot \vec{N}$
- $a_T=\vec{a}\cdot \vec{T}=v(t)'=\lvert \vec{r}(t) \rvert'$ is the *tangential component of acceleration*
- $a_N=\vec{a}\cdot \vec{N}=v^{2}\kappa$ is the *normal component of acceleration*
(See below, $\kappa$ is curvature)

It may be useful to find $a_N$ with $a_T$ or vice versa. We find using Pythagoras
$$a_N=\sqrt{ \lvert\lvert \vec{a} \rvert \rvert ^{2}-(a_T)^{2} }$$
## TNB
For tangent, normal, and binormal vectors, see [[Tangent, Normal, Binormal Vectors]].
## Torsion
Let $\tau$ be the constant so that 
$$\frac{d\vec{B}}{ds}=-\tau \vec{N}$$
We call $\tau$ torsion. We know it exists and is given by:
$$\tau=\frac{(\vec{v}\times \vec{a})\cdot \vec{a}'}{\left| \left| \vec{v}\times \vec{a} \right|  \right| ^{2}}$$
If $\tau>0$ motion twists counterclockwise.
if $\tau<0$, motion twists clockwise.
## Curvature
Given a curve $C$, the curvature at some point $p_0$ is the absolute rate of change of the tangent vector with respect to the position on the curve. This is given by:
$$\kappa = \left|\left|\frac{d\vec T}{ds}\right|\right|=\frac{1}{v^3}\left|\left|\vec   v \times \vec a\right|\right|$$
Note $\kappa\geq0$ and is strictly positive when the curve is non-linear.

### Curvature of Planar Functions
If we consider a planar function $y=f(x)$, we will obtain: 
$$\kappa=\frac{f''(t)}{{ (1+f'(t)^{2} })^\frac{3}{2}}$$
## Radius of Curvature
The Radius of curvature is $\rho=\frac{1}{\kappa}$.
## Product rules for parametric curves
Let $\vec r_1, \vec r_2$ be parametric curves and $f$ a scalar function.
- $(f(t)\vec r(t))'=f'(t)\vec r(t)+f(t)\vec v(t)$
- $(r_1\dot r_2)'=r_1'\cdot\vec r_2 + \vec r_1\cdot \vec r_2'$.
