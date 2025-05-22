Las Vegas Algorithms are randomized, with no error, and potentially unbounded runtime. If we take a Las
## Example
Assume we have a function `rnd()->{0,1}`. If we run this three times, we can generate an integer $r$ between $0,7$.
Take the algorithm:
- Use `rnd` to generate a number $r'$ between 0 and 7.
- If $r'$ is greater than $5$, go back and generate a new $r'$. Otherwise output $r'$.
## Conversion to [[Monte Carlo Algorithms]]
Let $A$ a LV algorithm, and $X_A$ be the [[Random Variable]] representing the runtime of $A$. Take the algorithm $B$:
- Run $A$ for a certain runtime.
- If $A$ does not terminate after the runtime, stop $A$ and return any arbitrary value.