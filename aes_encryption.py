from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Original message
message = "Hello! This is my Cryptography Project."

# Generate a random 256-bit secret key
key = get_random_bytes(32)

# Create AES-GCM cipher
cipher = AES.new(key, AES.MODE_GCM)

# Encrypt the message
ciphertext, tag = cipher.encrypt_and_digest(message.encode())

# Display encrypted information
print("===== AES-256-GCM ENCRYPTION =====")
print("Original Message:", message)
print("Nonce:", base64.b64encode(cipher.nonce).decode())
print("Encrypted Message:", base64.b64encode(ciphertext).decode())
print("Authentication Tag:", base64.b64encode(tag).decode())

# Decryption
decrypt_cipher = AES.new(
    key,
    AES.MODE_GCM,
    nonce=cipher.nonce
)

decrypted_message = decrypt_cipher.decrypt_and_verify(
    ciphertext,
    tag
)

print("\n===== DECRYPTION =====")
print("Decrypted Message:", decrypted_message.decode())

# Test data integrity
print("\n===== INTEGRITY VERIFICATION =====")

tampered_ciphertext = bytearray(ciphertext)
tampered_ciphertext[0] ^= 1

try:
    test_cipher = AES.new(
        key,
        AES.MODE_GCM,
        nonce=cipher.nonce
    )

    test_cipher.decrypt_and_verify(
        bytes(tampered_ciphertext),
        tag
    )

    print("Data integrity verified.")

except ValueError:
    print("Tampering detected!")
    print("Encrypted data has been modified.")
