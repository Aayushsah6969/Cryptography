import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

#symmetric encryption
def aes_ed(message):
    key = secrets.token_bytes(32)  # Generate a random 256-bit key
    nonce = secrets.token_bytes(12)  # Generate a random 96-bit nonce
    aes = AESGCM(key)

    ciphertext = nonce + aes.encrypt(nonce, message.encode(), None)
    plaintext = aes.decrypt(ciphertext[:12], ciphertext[12:], None)

    return key.hex(), ciphertext.hex(), plaintext.decode()

if __name__ == "__main__":
    message = "This is a secret message."
    key, ciphertext, plaintext = aes_ed(message)
    print("Original Message:", message)
    print("AES Key:", key)
    print("Ciphertext:", ciphertext)