For installation:

```bash
git clone https://github.com/kanan-garayzada/Cryptography.git
cd Cryptography


###### **GCD**



This program calculates the greatest common divisor of two integers using the Euclidean algorithm.



The user enters two numbers. The program repeatedly replaces the pair (a, b) with (b, a mod b). This process continues until b becomes zero. At that point, a is the GCD. The result is printed.



The main idea is that gcd(a, b) = gcd(b, a mod b), which reduces the problem step by step.



###### **Caesar and Affine Ciphers**



This program implements two classical encryption methods.



For the Caesar cipher, the input text is converted to uppercase. Each letter is shifted by a fixed value inside the alphabet. The position of the letter is found, the shift is added, and modulo 26 is applied. Decryption is done by using the negative shift.



For the Affine cipher, each letter is first converted to its index in the alphabet. Encryption uses the formula E(x) = (ax + b) mod 26. Decryption requires the modular inverse of a and uses D(y) = a^(-1)(y - b) mod 26. If the inverse does not exist, the program reports an error.



The Caesar cipher is a simple shift, while the Affine cipher combines multiplication and addition in modular arithmetic.



###### **OTP**



This program demonstrates the One-Time Pad idea using XOR.



The user enters a message, which is converted into bytes. A random key of the same length is generated using os.urandom. Each byte of the message is XOR-ed with the corresponding byte of the key to produce ciphertext.



The ciphertext is displayed in binary form. Decryption is done by XOR-ing the ciphertext with the same key again, which returns the original message.



The main property used is that XOR is reversible.



###### **OTP + PRG**



This program combines OTP with a pseudorandom generator.



The user provides a message and a seed. The seed is given to Python’s random generator. Based on this seed, a sequence of bytes is generated with the same length as the message.



This generated sequence acts as the key. The message is XOR-ed with this key to produce ciphertext. During decryption, the same seed generates the same key again, allowing the original message to be recovered.



The main idea is that instead of storing a full random key, a shorter seed is expanded into a longer key.



###### **Frequency Analysis Attack**



This program performs a simple attack on Caesar cipher using letter frequency.



The ciphertext is converted to uppercase. The program counts how many times each letter appears and finds the most frequent one. It assumes that this letter corresponds to the letter E in English.



Using this assumption, the shift is estimated and the ciphertext is decrypted. The result is printed.



This method works better for longer texts and may not always give the correct answer.



###### **CPA-secure OTP**



This program builds a randomized encryption scheme using a pseudorandom function based on AES.



A random AES key is generated. The message is converted into bytes. A random nonce is also generated for each encryption.



Using the key and nonce, the program generates a pseudorandom byte stream by repeatedly applying AES with a counter. This stream is used as a pad.



The message is XOR-ed with this pad to produce ciphertext. For decryption, the same key and nonce regenerate the same pad, and XOR returns the original message.



Because a new random nonce is used every time, the same message produces different ciphertexts, making the scheme randomized.



###### **Extended Euclidean Algorithm**



This program calculates not only gcd(a, b) but also integers x and y such that ax + by = gcd(a, b).



If b is zero, the result is gcd = a, x = 1, y = 0. Otherwise, the program computes q = a // b and r = a - q\*b, then recursively solves the problem for (b, r).



After returning from recursion, it computes x = y1 and y = x1 - q\*y1.



The result includes gcd, x, y, and also verifies the equation ax + by = gcd.



###### **RSA Encryption Scheme**



This program implements basic RSA encryption and decryption.



The user enters p, q, e, and a message m. The program computes N = pq and phi(N) = (p-1)(q-1).



It checks that e is coprime with phi(N). It also ensures that the message satisfies 0 < m < N and gcd(m, N) = 1.



The program then computes d as the modular inverse of e modulo phi(N).



Encryption is done using c = m^e mod N. Decryption is done using m = c^d mod N.



The program prints the keys, ciphertext, and the decrypted message.



###### **Diffie-Hellman Key Exchange**



This program implements the Diffie-Hellman key exchange process.



The user provides q and g, which are public parameters. Then Alice chooses a private value x and Bob chooses a private value y.



Alice computes her public key hA = g^x mod q. Bob computes his public key hB = g^y mod q.



Alice then computes the shared key using kA = hB^x mod q. Bob computes kB = hA^y mod q.



Both values are equal because they both compute g^(xy) mod q. The program prints the public keys and verifies that the shared keys match.



This allows two parties to establish a shared secret without directly transmitting it.



###### **PRG based on Discrete Log**



This program implements a pseudorandom generator based on the discrete logarithm idea.



The user enters a seed, a prime number p, a generator g, and the desired output length. The seed is reduced modulo p to ensure it is inside the group.



The generator works iteratively. At each step, it checks whether the current value is greater than (p-1)/2. If it is greater, it outputs bit 1, otherwise it outputs bit 0.



After generating the bit, the state is updated using the formula:



x = g^x mod p



This new value becomes the input for the next iteration. The process repeats until the required number of bits is produced.



The final output is a sequence of bits printed as a binary string.



The main idea is that exponentiation modulo a prime is easy to compute, but reversing it (discrete logarithm) is computationally hard, which makes the output appear pseudorandom.



The correctness of the implementation can be checked in the file.

