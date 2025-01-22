## Primitive operations
Each of the following operations takes the same amount of time on a given machine:
- Assigning a value to a variable
- Following an object reference
- Arithmetic operation
- Comparing variables/numbers
- Accessing array index
- Calling a method
- Returning from a method
## Growth rates
We measure an algorithm's time requirement as a function $f$ of the input size $n$. We observe the amount the time requirement of an algorithm grows as $n$ increases.
### Ordered efficiency list
- Super exponential - $n^{n}$
- Factorial - $n!$
- Exponential - $2^{n}$
- Cubic - $n^{3}$
- Quadratic - $n^{2}$
- $n\log_{2} n$
- Linear - $cn$
- $\log_2 n$
- Constant - $c$
#### Base 2 logarithm
Why base 2? Many algorithms such as binary tree search will branch down two paths repeatedly. For this reason it makes sense to abbreviate as $\log_{2}, 2^{n}$, etc.