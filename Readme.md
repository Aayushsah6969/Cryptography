# Cryptography

A practical learning repository focused on understanding cryptography and implementing its fundamental concepts using Python.

This repository contains small, hands-on implementations of cryptographic algorithms and techniques, exploring how they work and how they are used to protect information.

## Topics Covered

### 1. Hashing
Learn how cryptographic hash functions transform data into fixed-length digests.

- Text hashing using SHA-256.
- File hashing and integrity verification.
- Comparing file hashes to detect changes in content.

### 2. Encryption
Introduction to the fundamentals of encryption, including plaintext, ciphertext, encryption, decryption, and cryptographic keys.

### 3. Symmetric Encryption
Implementation of AES-GCM, a symmetric encryption algorithm that uses the same secret key for encryption and decryption.

- Generating a secure encryption key.
- Encrypting and decrypting messages.
- Understanding nonces and authentication tags.
- Detecting unauthorized modifications to encrypted data.

### 4. Asymmetric Encryption
Implementation of RSA, a public-key cryptographic algorithm that uses a public-private key pair.

- Generating RSA keys.
- Encrypting messages using a public key.
- Decrypting messages using a private key.
- Understanding the role of OAEP padding.

### 5. Steganography
Implementation of image-based steganography using the Least Significant Bit (LSB) technique.

- Hiding secret messages inside images.
- Extracting hidden messages from images.
- Understanding pixels, RGB values, and binary data.
- Exploring the relationship between encryption and steganography.

## Technologies Used

- **Python 3** — Implementation language.
- **cryptography** — Library for cryptographic algorithms and encryption.
- **Pillow** — Library for image processing and steganography.
- **Linux / Ubuntu** — Development environment.

## Getting Started

Clone the repository:

```bash
git clone git@github.com:Aayushsah6969/Cryptography.git
cd Cryptography
````

Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install the required libraries:

```
pip install cryptography Pillow
```

## **Learning Objectives**

The goal of this repository is to develop a practical understanding of cryptography and its applications in cybersecurity.

Through these implementations, I aim to understand how data is protected, how cryptographic algorithms operate, and how Python can be used to build basic security tools.

## **Disclaimer**

This repository is intended for educational purposes and hands-on learning. The implementations demonstrate fundamental cryptographic concepts and are not intended for production use.
