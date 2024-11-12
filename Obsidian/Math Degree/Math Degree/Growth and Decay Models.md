(From [[Applications of Differential Equations]])

The rate at which a radioactive substance decays is proportional to the amount present of the original sample.

$$x(t)=\begin{cases} \frac{dx}{dt} = kx\\x(0)=x_0
 \end{cases}$$
This will give:
$$\ln x = kt+c$$
$$x=ce^{kt}$$
And after applying the initial condition we achieve:
$$x=x_0e^{kt}$$
## Half Life

Let $T$ be the half life of the substance: 
$$x(t=T)=\frac{1}{2}x_0$$
This gives a new formula based on half-life:
$$x(t)=x_0\left(\frac{1}{2}\right)^{\frac{t}{T}}$$