
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import base64

# Generate a 2048-bit RSA key pair
key = RSA.generate(2048)

# Separate public and private keys
public_key = key.publickey()
private_key = key

# Original message
message = "Hello! This is my RSA Cryptography Project."

# Encrypt the message using the public key
encrypt_cipher = PKCS1_OAEP.new(
    public_key,
    hashAlgo=SHA256
)

encrypted_message = encrypt_cipher.encrypt(message.encode())

# Display encryption result
print("===== RSA-2048 ENCRYPTION =====")
print("Original Message:", message)
print(
    "Encrypted Message:",
    base64.b64encode(encrypted_message).decode()
)

# Decrypt the message using the private key
decrypt_cipher = PKCS1_OAEP.new(
    private_key,
    hashAlgo=SHA256
)

decrypted_message = decrypt_cipher.decrypt(encrypted_message)

# Display decrypted message
print("\n===== RSA DECRYPTION =====")
print("Decrypted Message:", decrypted_message.decode())

# Verify the result
print("\n===== VERIFICATION =====")

if decrypted_message.decode() == message:
    print("RSA encryption and decryption successful!")
else:
    print("Verification failed!")
