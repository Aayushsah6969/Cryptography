# **Symmetric Encryption**

Symmetric encryption is one of the two main types of encryption in cryptography. It protects data by using the same secret key for both encryption and decryption.

Let's understand the important concepts first. After that, we'll implement it in Python using helpful comments for every unfamiliar function and term.

## **1. What is symmetric encryption?**

In symmetric encryption, the sender and receiver share a secret key.

- The sender uses the key to encrypt the original message.
- The receiver uses the same key to decrypt the encrypted message.
- Anyone who obtains the secret key can potentially decrypt the data.

For example, suppose Alice wants to send a confidential message to Bob.

**Alice — Sender**

Plaintext: `HELLO BOB`

Encryption using secret key K

**Ciphertext**

Encrypted message

Decryption using the same secret key K

**Bob — Receiver**

Plaintext: `HELLO BOB`

The key must be kept secret. If Alice sends the key along with the encrypted message without protection, an attacker could obtain both and decrypt the message.

## **2. Important terminology**

| Term                 | Meaning                                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Plaintext            | Original readable data                                                                                            |
| Ciphertext           | Encrypted data                                                                                                    |
| Encryption algorithm | Mathematical procedure that converts plaintext into ciphertext                                                    |
| Secret key           | Shared secret value used by the encryption algorithm                                                              |
| Decryption           | Recovering the original data from ciphertext using the key                                                        |
| Key length           | Size of the key, usually measured in bits                                                                         |
| Nonce                | A value used with certain encryption algorithms; it must be unique for a given key when required by the algorithm |

**Important:** The encryption algorithm does not need to be secret. Security should depend on keeping the key secret.

## **3. How does symmetric encryption work?**

Consider a simplified encryption operation:

\\[ C = E_K(P) \\]

Where:

- \\(P\\) = Plaintext
- \\(C\\) = Ciphertext
- \\(E\\) = Encryption algorithm
- \\(K\\) = Secret key

Decryption reverses the operation:

\\[ P = D_K(C) \\]

The same secret key \\(K\\) is used in both operations.

In real encryption algorithms, the transformation is much more complex than simply shifting letters or replacing characters.

## **4. Types of symmetric encryption**

There are two major categories.

### **A. Block ciphers**

A block cipher encrypts data in fixed-size blocks.

For example, AES processes data in blocks of 128 bits (16 bytes).

If the message is longer than one block, the encryption algorithm uses a method called a mode of operation to handle multiple blocks.

Common block cipher:

\- AES (Advanced Encryption Standard)

### **B. Stream ciphers**

A stream cipher encrypts data as a continuous stream of bits or bytes.

It generates a keystream that is combined with the plaintext to produce ciphertext.

Common stream cipher:

\- ChaCha20

AES and ChaCha20 are both widely used modern encryption algorithms.

## **5. AES: the algorithm we'll use in Python**

AES is a widely used symmetric encryption algorithm.

Important facts:

- AES is a block cipher.
- It supports key sizes of 128, 192, and 256 bits.
- Its block size is always 128 bits, regardless of key size.
- AES-256 uses a 256-bit secret key.

AES is not the same as AES-GCM or AES-CBC. Those are modes of operation that define how AES is used to encrypt data.

### **What is an encryption mode?**

A mode of operation determines how a block cipher processes data, especially when the message is longer than one block.

| Mode | Important characteristic                                            |
| ---- | ------------------------------------------------------------------- |
| ECB  | Encrypts blocks independently; generally insecure for ordinary data |
| CBC  | Uses chaining between blocks; requires padding and a unique IV      |
| CTR  | Converts a block cipher into a stream-like cipher                   |
| GCM  | Provides encryption and authentication                              |

For our Python implementation, we'll use **AES-GCM**.

GCM provides two important security properties:

- Confidentiality: Keeps the original data secret.
- Integrity and authenticity: Detects modifications to the encrypted data and verifies that it was produced by someone with the correct key.

This is important because encryption alone does not necessarily prevent an attacker from modifying ciphertext.

## **6. Key, nonce, and authentication tag**

AES-GCM uses three important values.

| Value              | Purpose                                                                       |
| ------------------ | ----------------------------------------------------------------------------- |
| Key                | Secret value used for encryption and decryption                               |
| Nonce              | A value that must be unique for each encryption under the same key            |
| Authentication tag | Used to verify that the ciphertext and associated data have not been modified |

The nonce does not need to be secret. It is usually stored or transmitted alongside the ciphertext.

**Critical rule:** Never reuse a nonce with the same AES-GCM key. Reusing a nonce can seriously compromise security.

The authentication tag is generated during encryption and checked during decryption. If verification fails, the ciphertext must not be trusted.

## **7. Advantages and limitations**

**Advantages**

- Fast and efficient for encrypting large amounts of data.
- Uses relatively small keys.
- Suitable for file encryption, database encryption, and secure communication.

**Limitations**

- Both parties need access to the same secret key.
- The key must be exchanged and stored securely.
- If the key is compromised, encrypted data may become readable.
- Symmetric encryption does not inherently solve the problem of securely sharing keys.

## **8. Real-world applications**

Symmetric encryption is used in:

- Encrypting files and backups.
- Protecting data stored in databases.
- Encrypting network traffic in HTTPS.
- Protecting sensitive information on computers and mobile devices.

In HTTPS, asymmetric cryptography is commonly used during the handshake to establish shared secrets, while symmetric encryption protects the actual communication.

## **9. What we'll implement next**

Our Python project will use AES-GCM to encrypt and decrypt a message.

We'll learn:

1. Installing the `cryptography` Python library.
2. Generating a secure encryption key.
3. Converting text into bytes.
4. Encrypting plaintext into ciphertext.
5. Decrypting ciphertext back into plaintext.
6. Understanding the nonce and authentication tag.
7. Detecting tampered ciphertext.

We'll use Python's `cryptography` library rather than implementing AES ourselves. Cryptographic algorithms are easy to get wrong, so practical applications should use established libraries.