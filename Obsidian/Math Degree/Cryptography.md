---
tags:
  - NumThry
---
[[Number Theory]] [[Modular Arithmetic]]
Cryptography refers to techniques of sharing secret messages. Messages are encoded in a certain way and then communicated publicly but no one except for the recipient can decipher it. 
The principle requires three steps:
- Encryption: Reconfigure the message so that it cannot be understood except by the intended recipient.
- Send the message
- Decryption: The recipient deciphers to obtain the original message using a certain "key" piece of information.
## Types of Ciphers
### Caesar Cipher
In this cipher each letter is replaced by the letter down $n$ indices from the letter.
### Permutation ciphers
Divide the alphabet into groups of fixed size:
ABCDE|FGHIJ|KLMNO|$\dots$
And the letters can be switched between groups. $A\iff F$, $B\iff G$.
### Public Key Cryptography
Public Key cryptography is a technique in which the message can be sent out as public information, however only the intended recipient can decrypt the message. 
#### RSA Method
RSA is a cryptography method, where a message is converted to a large natural number $M$. We have many ways of doing this, we can use $A=11, B=12\dots Z=36$ or any other method.

Once we have this large number, we can encrypt it with two other numbers. We take $N=pq$ where $p,q$ are large primes, and encrypt with $E$ (called an encryptor) so that our message is called $R$ and $R\equiv M^{E}\pmod N$.

Note that $E$ is chosen so that we have a decryptor $D:$ $M^{ED}\equiv M\pmod N$.

The recipient can then use $D$ to decrypt the message: $R^{D}\equiv M^{ED}\equiv M\pmod N$.

Finding $D,E$ requires the following theorem:
For any integers $a,k$:
$$a^{k\phi(N)+1}\equiv a \pmod N$$
and so we choose $D,E$ so that $DE=k\phi(N)+1$. This gives:
- $GCD(E,\phi(N))=1$
- $DE\equiv 1 \pmod{\phi(N)}$