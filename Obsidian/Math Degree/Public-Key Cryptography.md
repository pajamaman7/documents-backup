A public key cryptosystem is a tuple, $(G,E,D)$. Importantly, it has $G$ generate both a public and secret (private) key. Encryption uses the public key and decryption uses the secret key.
## Diffie-Hellman
### One-way Trapdoor Function
$f:X\to Y$ be an [[One-to-One|Injective]] function on [[Countable and Uncountable sets|Finite]] sets. A one-way function is simple to compute $f(x)$, but difficult to compute $f^{-1}(y)$.
The trapdoor should give $f^{-1}$.
With this, we have a cryptosystem, with $f$ the public key, and $\mathrm{trapdoor}(f)$ the secret key.