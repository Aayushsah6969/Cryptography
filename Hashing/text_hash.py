import hashlib

text = "This is a secret"
hash_object = hashlib.sha256(text.encode())
hash_hex = hash_object.hexdigest()
print("Original Text:", text)
print("SHA-256 Hash:", hash_hex)