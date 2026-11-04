
import hashlib

# Original message
message = "Hello! This is my Cryptography Project."

# Generate SHA-256 hash
hash_object = hashlib.sha256(message.encode())
hash_value = hash_object.hexdigest()

# Display the result
print("===== SHA-256 HASHING =====")
print("Original Message:", message)
print("SHA-256 Hash:", hash_value)
print("Hash Length:", len(hash_value), "characters")

# Demonstrate that a small change creates a different hash
modified_message = "Hello! This is my Cryptography Project!"
modified_hash = hashlib.sha256(
    modified_message.encode()
).hexdigest()

print("\n===== HASH COMPARISON =====")
print("Original Hash:", hash_value)
print("Modified Hash:", modified_hash)

if hash_value != modified_hash:
    print("Different messages produce different hashes.")
else:
    print("Hashes are identical.")
