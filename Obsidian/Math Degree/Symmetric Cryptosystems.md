---
aliases:
  - Symmetric Cryptosystem
---
A symmetric cryptosystem is a set of three algorithms, along with a plaintext space $\mathcal{P}$, and a ciphertext space $\mathcal{C}$.
## Key Generation
The algorithm for key generation (randomly) generates a key $k$ in a key space.
## Encryption
Encryption is a (possibly probabilistic) function $E_k:\mathcal{P}\to\mathcal{C}$ that takes plaintext and a key and converts it to ciphertext.
## Decryption
Decryption is a function $D_k:\mathcal{C}\to\mathcal{P}$ that takes ciphertext and a key and converts it to ciphertext.
## Key Property
We wish to always have the property:
$$
D_k(E_k(m))=m
$$