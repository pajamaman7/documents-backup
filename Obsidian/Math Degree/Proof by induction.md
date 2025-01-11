Proof by induction is a useful technique for proving statements that are [[Recursive]], ones that depend on previous statements, as well as being useful when a direct proof is not so trivial. 

## Proving by induction
Proof by induction involves three steps. In general, for a statement $P$ dependent on a variable $n$,
- **Base case:** First, show that the statement $P$ is true for some constant value $a$. This value $a$ is the minimum integer which you are trying to prove $P$ is true. This is often trivial, since you are proving a statement true for a constant value.
- **Inductive Hypothesis:** Next, suppose that the statement $P$ is true for some arbitrary number $k\geq a$. 
- **Inductive step:** Finally, use your inductive hypothesis to show that $P$ is true for $k+1$. This essentially knocks down a domino of statements which will become true to infinity. 
Once you have concluded that $P(k)\implies P(k+1)$, you are done. 

## Strong Induction (uh oh)
Strong induction can be used on statements where $P(k)$ depends on $P(k-1)$ and $P(k-2)$, on recursive statements with more depth, or on statements where it simply might be more useful to prove $P(k+1)$ using several previous instances of $P$. 

Strong induction is incredibly similar to "weak induction" with some strengthening in the base case and inductive hypothesis. 

In particular: 
- **Base case:** The base case must be proven for several values, let's say from $a$ to $b$. These may or may not be evident from the problem, however it should be trivial to go back and add more if necessary. Leave some room on a test for this. 
- **Inductive Hypothesis:** The inductive hypothesis includes another step as well. Once you have your base case set up, you can suppose that $k\geq b$. Then suppose that your statement $P$ is true for all $m$ where $a\leq m\leq k$.
- **Inductive Step:** The inductive step is identical to weak induction in this case. With the setup from the inductive hypothesis and the base cases, it should be possible to prove $P(k+1)$ after assuming $P(k)$. When invoking the inductive hypothesis, it may be necessary to show that the values you invoke it on are between $a$ and $k$, inclusive. 