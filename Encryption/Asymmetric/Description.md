# **Asymmetric Encryption**

Asymmetric encryption is one of the two main types of encryption in cryptography. Unlike symmetric encryption, which uses one shared secret key, asymmetric encryption uses **two mathematically related keys: a public key and a private key.**

Let's understand the important concepts first. We'll implement it in Python afterward.

## **1. What is asymmetric encryption?**

Asymmetric encryption is also called public-key cryptography.

It uses a pair of keys:

- **Public key:** Can be shared with anyone. It is used to encrypt data or verify digital signatures, depending on the operation.
- **Private key:** Must be kept secret. It is used to decrypt data or create digital signatures.

The two keys are mathematically related, but knowing the public key should not make it practically feasible to calculate the private key.

### **Example: Alice sends a message to Bob**

Suppose Bob wants to receive confidential messages from Alice.

**Bob — Receiver**

Generates a public key and a private key

Shares his public key with Alice

**Alice — Sender**

Encrypts her message using Bob's public key

Sends the ciphertext to Bob

**Bob — Receiver**

Decrypts the ciphertext using his private key

The important point is that Alice does not need to know Bob's private key.

Anyone can encrypt a message using Bob's public key, but only Bob should be able to decrypt it using his private key.

## **2. How does asymmetric encryption work?**

The encryption process can be represented as:

\\[ C = E\_{K\_{pub}}(P) \\]

Where:

- \\(P\\) = Plaintext
- \\(C\\) = Ciphertext
- \\(K\_{pub}\\) = Public key
- \\(E\\) = Encryption algorithm

Decryption uses the private key:

\\[ P = D\_{K\_{priv}}(C) \\]

The public and private keys are different, but mathematically related.

## **3. Symmetric vs asymmetric encryption**

| Feature         | Symmetric                          | Asymmetric                               |
| --------------- | ---------------------------------- | ---------------------------------------- |
| Keys used       | One shared secret key              | Public and private key pair              |
| Key sharing     | Secret key must be shared securely | Public key can be shared openly          |
| Speed           | Generally faster                   | Generally slower                         |
| Best suited for | Large amounts of data              | Key exchange, signatures, and small data |
| Examples        | AES, ChaCha20                      | RSA, ElGamal                             |

Asymmetric encryption solves an important problem in symmetric encryption: how to establish a shared secret without sending that secret directly.

However, asymmetric encryption is generally slower than symmetric encryption, so real-world systems often combine both.

## **4. Important asymmetric algorithms**

### **RSA**

RSA is one of the most widely known asymmetric cryptographic algorithms.

It relies on the mathematical difficulty of factoring large integers.

RSA can be used for encryption and digital signatures.

### **Elliptic Curve Cryptography (ECC)**

ECC is a family of cryptographic techniques based on elliptic curves over finite fields.

It can provide strong security with relatively small keys.

Examples include:

- ECDH — Used for establishing shared secrets.
- ECDSA — Used for digital signatures.

### **Diffie-Hellman**

Diffie-Hellman is a key exchange algorithm.

It allows two parties to establish a shared secret over an insecure communication channel without directly transmitting the secret.

It is not itself an encryption algorithm.

## **5. Public key vs private key**

| Public key                         | Private key                                  |
| ---------------------------------- | -------------------------------------------- |
| Can be shared publicly             | Must remain secret                           |
| Used to encrypt data for its owner | Used to decrypt data encrypted for its owner |
| Used to verify digital signatures  | Used to create digital signatures            |

**Important:** The public key must be authentic. If an attacker replaces Bob's public key with their own, Alice might unknowingly encrypt her message for the attacker.

In real systems, digital certificates and trusted public-key infrastructure help verify that a public key belongs to the intended person or server.

## **6. Digital signatures**

Asymmetric cryptography is also used to create digital signatures.

A digital signature helps verify:

- **Authenticity:** The message was signed using the corresponding private key.
- **Integrity:** The signed data has not been modified.
- **Non-repudiation:** Provides evidence that a particular private key was used to sign the data, though this does not automatically prove the real-world identity of the signer.

For a digital signature:

1. The sender signs the message using their private key.
2. The receiver verifies the signature using the sender's public key.

This is different from encryption.

Encryption protects confidentiality. Digital signatures provide authenticity and integrity.

## **7. Hybrid encryption**

In practice, symmetric and asymmetric encryption are often used together.

For example, in HTTPS:

1. The client and server use asymmetric cryptography and related protocols to establish shared secrets.
2. They derive symmetric encryption keys.
3. Symmetric encryption protects the actual communication.

This approach combines the benefits of both methods.

## **8. What we'll implement next**

We'll create a Python program using the `cryptography` library.

The implementation will use RSA to:

1. Generate a public-private key pair.
2. Encrypt a message using the public key.
3. Decrypt the message using the private key.
4. Save and load keys from files.
5. Understand padding and why it is important for secure RSA encryption.

We'll also explore digital signatures afterward, since they are another major application of asymmetric cryptography.