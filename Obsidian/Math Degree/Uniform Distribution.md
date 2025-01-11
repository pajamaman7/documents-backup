A Uniform Distribution is one with a constant [[Probability Density Function]] throughout its [[Domain]] ($x\in[a,b]$). 

The [[Probability Density Function]]:
$$f(x)=\begin{cases}
 \frac{1}{b-a}&a\leq x\leq b\\
 0&elsewhere
 \end{cases}$$
The [[Cumulative Distribution Function]]:
$$F(x)=\begin{cases} 
0&x<a\\
\frac{x-a}{b-a}&a\leq x \leq b \\
 1&x>b\\
 \end{cases}$$
The [[Expected Value]]:
$$E[X]=\frac{a+b}{2}$$
The [[Variance and Standard Deviation]]:
$$V[X]=\frac{(b-a)^2}{12}$$
The [[Moment Generating Functions]]:
 $$ \begin{aligned}
 \\
M_{X}(t) =\frac{e^{t b}-e^{t a}}{t(b-a)} 
\end{aligned}$$