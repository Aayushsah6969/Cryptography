# Import AES-GCM, a symmetric encryption algorithm.
# AES-GCM provides encryption and integrity verification.
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Import os to generate secure random bytes.
import os


# ---------------- ENCRYPTION ----------------

def encrypt_message(message, key):
    """
    Encrypt a plaintext message using AES-GCM.

    message: Original readable text.
    key: Secret key used for encryption.
    """

    # AESGCM requires bytes, not a Python string.
    # encode() converts text into bytes.
    message_bytes = message.encode("utf-8")

    # A nonce is a value used during encryption.
    # AES-GCM requires a unique nonce for every encryption
    # performed with the same key.
    # 12 bytes (96 bits) is the recommended nonce size.
    nonce = os.urandom(12)

    # Create an AES-GCM encryption object using our secret key.
    aesgcm = AESGCM(key)

    # Encrypt the message.
    # encrypt() returns ciphertext + authentication tag.
    # The authentication tag helps detect tampering.
    ciphertext = aesgcm.encrypt(nonce, message_bytes, None)

    # Return both values because decryption needs the nonce.
    return nonce, ciphertext


# ---------------- DECRYPTION ----------------

def decrypt_message(nonce, ciphertext, key):
    """
    Decrypt ciphertext using the same secret key.
    """

    # Create the AES-GCM object with the same key.
    aesgcm = AESGCM(key)

    # Decrypt the ciphertext and verify its authentication tag.
    # If the ciphertext or tag has been modified,
    # decryption will fail.
    plaintext_bytes = aesgcm.decrypt(nonce, ciphertext, None)

    # Convert the decrypted bytes back into readable text.
    return plaintext_bytes.decode("utf-8")


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":

    # Generate a cryptographically secure random AES key.
    # AES-256 uses a 32-byte (256-bit) key.
    key = AESGCM.generate_key(bit_length=256)

    # Our original message.
    message = "Hello Bob! This is my first encryption program."

    print("Original message:", message)

    # Encrypt the original message.
    nonce, ciphertext = encrypt_message(message, key)

    # Print the encrypted data in hexadecimal format.
    # Hexadecimal is a readable representation of binary data.
    print("\nCiphertext:", ciphertext.hex())

    # Decrypt the encrypted message using the same key.
    decrypted_message = decrypt_message(nonce, ciphertext, key)

    print("\nDecrypted message:", decrypted_message)