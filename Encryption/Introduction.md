# Introduction to Encryption

Encryption is a fundamental concept in cryptography and cybersecurity. It is the process of converting readable information into an unreadable format to protect it from unauthorized access.

## 1. Basic Concepts

| Term | Meaning |
|---|---|
| Plaintext | Original, readable data before encryption |
| Encryption | Process of converting plaintext into ciphertext |
| Ciphertext | Encrypted, unreadable data |
| Decryption | Process of converting ciphertext back into plaintext |
| Key | A piece of information used by an encryption algorithm to encrypt or decrypt data |
| Cipher | An algorithm used to perform encryption and decryption |

## 2. How Encryption Works

Encryption transforms readable data into an unreadable format using an encryption algorithm and a key.

```text
                 Encryption
Plaintext --------------------------> Ciphertext
          Algorithm + Encryption Key

                 Decryption
Ciphertext --------------------------> Plaintext
          Algorithm + Decryption Key
````

### **Example**

Suppose we want to encrypt the message:

- Plaintext: `HELLO`
- Cipher: Caesar Cipher
- Encryption Key: 3

Each letter is shifted three positions forward in the alphabet.

```
HELLO → KHOOR
```

The encrypted message `KHOOR` is called ciphertext.

To decrypt it, we shift each letter three positions backward:

```
KHOOR → HELLO
```

This is a simple example of how encryption protects information.

## **3. Types of Encryption**

There are two main types of encryption:

- **Symmetric Encryption:** Uses the same secret key for encryption and decryption.
- **Asymmetric Encryption:** Uses a pair of keys: a public key and a private key.

Both methods protect data, but they work differently and are used in different situations.

## **4. Why Encryption Matters**

Encryption helps protect sensitive information such as:

- Passwords and personal information
- Financial transactions
- Messages and emails
- Files stored on computers
- Data transmitted over the internet

For example, HTTPS uses encryption to protect information exchanged between your browser and a website.

## **5. Important Note**

Encryption is different from hashing.

- Encryption is reversible when the correct decryption key is available.
- Hashing is a one-way process that produces a fixed-length digest and is not designed to be reversed.

Encryption is primarily used to protect the confidentiality of information.

