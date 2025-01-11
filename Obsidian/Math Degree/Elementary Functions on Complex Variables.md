For all the following let $z\in \mathbb{C},\,z=x+iy$
## Exponential
The exponential function on $z$ is given by:
$$e^{z}=\exp(z)=\exp(x)(\cos y+i\sin y)$$
Or the following:
$$e^{z}=\lim\limits_{ n \to \infty }\left( 1+\frac{z}{n} \right)^{n}$$
$$e^{z}=\sum\limits_{n=0 }^{\infty} \frac{z^{n}}{n!}$$
### Properties
- $\exp(z_{1}+z_{2})=\exp z_{1}\exp z_{2}$
- $e^{-z}=\frac{1}{e^{z}}$
- $e^{z}$ is nonzero
- $|e^{z}|=e^{\mathrm{Re}z}$, and if $\mathrm{Im}z=0$, then $|e^{z}|=1$.
## Trigonometric Functions
To find trigonometric functions of complex variables, we plug $z$ in for $x$ within a familiar formula:
$$\sin z=\frac{e^{iz}-e^{-iz}}{2i},\quad\cos z=\frac{e^{iz}+e^{-iz}}{2}$$
### Properties
- $\cos z$ is even, $\cos(-z)=\cos z$
- $\sin z$ is odd, $\sin(-z)=-\sin z$
- $e^{iz}=\cos z+i\sin z$
- $\cos ^{2}z+\sin ^{2}z=1$
- $\cosh iz=\cos z$
- $-i\sinh iz=\sin z$
### Series expansion
$$\cos z=\sum\limits_{n=0 }^{\infty} (-1)^{n} \frac{z^{2n}}{(2n)!} ,\quad\sin z=\sum\limits_{n=0 }^{\infty}(-1)^{n} \frac{z^{2n+1}}{(2n+1)!}$$
### Special Cases of Complex Trigonometry
In fact, $\sin,\cos$ are unbounded in the complex case.
### In Terms of $x+iy$
$$\begin{align}
\cos (x+iy)&=\cos x\cosh y-i\sin x\sinh y\\
\sin(x+iy)&=\sin x\cosh y+i\cos x\sinh y
\end{align}$$
## Hyperbolic Trigonometric Functions
Hyperbolic trigonometric functions of complex variables are obtained simply by replacing the typical real variable $x$ with the complex variable $z$:
$$\sinh z=\frac{e^{z}-e^{-z}}{2},\quad\cosh z=\frac{e^{z}+e^{-z}}{2},\quad\tanh z=\frac{\sinh z}{\cosh z}$$
### Properties
- $\cosh z$ is even, $\cosh(-z)=\cosh z$
- $\sinh z$ is odd, $\sinh(-z)=-\sinh z$
- $e^{z}=\cosh z+\sinh z$
- $\cosh ^{2} z-\sinh ^{2}z=1$
- $\cosh iz=\cos z$
- $-i\sinh iz=\sin z$
### Series Expansion
$$\cosh z=\sum\limits_{n=0 }^{\infty}\frac{z^{2n}}{2n!},\quad\sinh z=\sum\limits_{n=0 }^{\infty} \frac{z^{2n+1}}{(2n+1)!}$$
## Logarithm
The logarithm of $z$ is not well defined as the inverse of $\exp$. This is because the exponential is neither injective nor surjective.
To solve surjectivity, we simply remove $0$ from the domain of $ln$.

We say that the *principal natural logarithm* of $z\neq 0$ is written as:
$$\ln z=\ln|z|+i\arg z$$
Where we take:
$$\arg z=\begin{cases}
\arccos \frac{\mathrm{Re}z}{|z|} &\mathrm{Im}z\geq 0 \\
-\arccos \frac{\mathrm{Re}z}{|z|}&\mathrm{Im}z<0
\end{cases}$$
Other values can be given by:
$$\ln z=\ln|z|+i(\arg z+2\pi k)$$
However, we typically take the principal case.
### Properties that no longer hold for $\ln$
- $\ln zw\neq \ln z+\ln w$
- $w\ln z\neq \ln z^{w}$
and many more, do not fuck with real properties of $\ln$
## Complex Powers
For a nonzero $z\in \mathbb{C}$, and $w\in\mathbb{C}$:
$$z^{w}=e^{w\ln z}$$
Of course we typically take the primitive natural logarithm, however infinite solutions are given with the periodic formula.
If $w$ is an integer, $z^{w}$ takes the usual definition of power with an integer exponent.
### Limits
Consider $\lim\limits_{ n \to \infty }n^{\alpha}$. We have the following cases:
- $|\alpha|>0$: $\lim\limits_{ n \to \infty }n^{\alpha}=\infty _{\mathbb{C}}$
- $\alpha=0$: $\lim\limits_{ n \to \infty }n^{\alpha}=1$
- The limit is not defined if $\mathrm{Re}\alpha=0$ but $\alpha \neq 0$.
### Properties that do not hold
- $(ab)^{c}\neq a^{c}a^{c}$
## Nth Roots
The $n$th root of a complex $z=re^{i\theta}\in\mathbb{C}$ is:
$$\sqrt[n]{ z }\in\left\{  \sqrt[n]{ r }\exp\left( {i\left( \frac{\theta}{n}+\frac{2k\pi}{n} \right)} \right) :\,k\in 0,1,\dots,n-1 \right \}$$
or:
$$\sqrt[n]{ z }=\sqrt[n]{ |z| }\exp\left( {\frac{i}{n}\arg z} \right)$$
The "principal root" is again given when $k=0$, and $\theta$ given by the principal argument of $z$.
### Fractional Exponents
Consider $z^{m/n}$ with $m,n$ coprime. This equals
$$z^{m/n}=(\sqrt[n]{ z })^{m}\neq\sqrt[n]{ z^{m} }$$
