(From [[Primes]])
## Witness
If $n$ is a positive integer such that there exists $a, GCD(a,n)=1$ and $a^{n-1}\not\equiv 1\pmod n$, then $n$ is not prime. We say that $a$ witnesses non-primality of $n$.

There exist composite numbers for which finding a witness is impossible. These are called Carmichael Numbers.
### Carmichael Numbers
A composite number $N$ which satisfies, for any positive $a\in\mathbb{Z}$, 
$$GCD(a,n)=1\implies a^{N-1}\equiv 1 \pmod N$$
There are infinitely many Carmichael Numbers.
#### Theorem: (Korselt, 1899)
A positive composite $N$ is a Carmichael number $\iff$ $N$ is [[Squarefree]] and for every prime divisor $p$ of $N$, $p-1|N-1$.  

## Square test
We use the fact that $\pmod p$, $x^{2}\equiv 1\iff x\equiv1$ or $x\equiv-1\pmod{p}$.

