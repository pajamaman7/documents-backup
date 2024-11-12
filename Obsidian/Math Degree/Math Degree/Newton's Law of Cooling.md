(From [[Applications of Differential Equations]])

Newton's law of cooling states that the rate of change of an object's temperature is proportional to the difference between its temperature and the temperature of the medium in which the object is situated. 

(Note that Newton's law of Heating is identical)
## Formula
Let $x=x(t)$ be the object's temperature at time $t>0$ and let $m$ be constant, the temperature of the medium.
The law states literally:
$$\begin{cases}  x'=k(x-m)\\
x(0)=x_0
 \end{cases}$$
However, this [[Differential Equations|Differential Equation]] can be solved to give:
$$x=m+Ce^{kt}$$
And the IVP $x(0)=x_0$ is all that must be solved for, giving:
$$x(t)=(x_0-m)e^{kt}+m$$
The constant $k$ can be found from an additional supplementary condition.