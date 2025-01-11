Linear [[Differential Equations]] are ones that take the form:
$$y'+p(x)y=f(x)$$
To solve a linear differential equation we assume the existence of a function $\mu(x)$, called the *integrating factor*. We also suppose that this function has the property: $\mu(x)p(x)=\mu'(x)$ (which further implies that $\mu(x)=e^{\int p(x)dx}$). We then multiply our original equation by $\mu(x)$. 
$$\begin{align*} 
\mu(x)y'+\mu(x)p(x)y&=\mu(x)f(x)\\
\mu(x)y'+y\mu'(x)&=\mu(x)f(x)\\
(\mu(x)y)'&=\mu(x)f(x)\\
\mu(x)y&=\int\mu(x)f(x)dx+C
 \end{align*}$$
 And in the end we are given:
$$y=\frac{\int\mu(x)f(x)dx+C}{\mu(x)}$$
 