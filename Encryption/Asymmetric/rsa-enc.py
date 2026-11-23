# Import the RSA module for generating RSA keys.
from cryptography.hazmat.primitives.asymmetric import rsa

# Import padding schemes used to make RSA encryption secure.
from cryptography.hazmat.primitives.asymmetric import padding

# Import SHA-256, a cryptographic hash function.
from cryptography.hazmat.primitives import hashes


# ---------------- KEY GENERATION ----------------

def generate_keys():
    """
    Generate an RSA public-private key pair.
    """

    # Generate the private key.
    # 2048 is the key size in bits.
    # public_exponent=65537 is the standard RSA public exponent.
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Extract the public key from the private key.
    # The public key can be shared with others.
    public_key = private_key.public_key()

    return private_key, public_key


# ---------------- ENCRYPTION ----------------

def encrypt_message(message, public_key):
    """
    Encrypt a message using the recipient's public key.
    """

    # RSA works with bytes, so convert the string into bytes.
    message_bytes = message.encode("utf-8")

    # Encrypt the message using the public key.
    ciphertext = public_key.encrypt(
        message_bytes,

        # OAEP is a padding scheme that makes RSA encryption
        # more secure and suitable for modern applications.
        padding.OAEP(

            # MGF1 is a mask generation function used by OAEP.
            # SHA-256 is used as its underlying hash function.
            mgf=padding.MGF1(algorithm=hashes.SHA256()),

            # SHA-256 is also used directly by OAEP.
            algorithm=hashes.SHA256(),

            # No additional application-specific label is used.
            label=None
        )
    )

    return ciphertext


# ---------------- DECRYPTION ----------------

def decrypt_message(ciphertext, private_key):
    """
    Decrypt ciphertext using the recipient's private key.
    """

    # Decrypt the ciphertext using the private key.
    # The padding configuration must match encryption.
    plaintext_bytes = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Convert the decrypted bytes back into readable text.
    return plaintext_bytes.decode("utf-8")


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":

    # Generate the RSA key pair.
    private_key, public_key = generate_keys()

    # Original message.
    message = "Hello Bob! This is my first RSA encryption program."

    print("Original message:", message)

    # Encrypt using the public key.
    ciphertext = encrypt_message(message, public_key)

    # Display ciphertext in hexadecimal format.
    # Hexadecimal makes binary data easier to display.
    print("\nCiphertext:", ciphertext.hex())

    # Decrypt using the private key.
    decrypted_message = decrypt_message(ciphertext, private_key)

    print("\nDecrypted message:", decrypted_message)