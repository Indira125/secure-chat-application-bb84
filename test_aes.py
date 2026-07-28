from crypto_utils import hash_key, encrypt_message, decrypt_message

# Sample BB84 key
bit_key = [1, 0, 1, 1, 0, 1]

# Strengthen key
secure_key = hash_key(bit_key)

# Encrypt
message = "Hello, this is quantum secure!"
nonce, ciphertext, tag = encrypt_message(message, secure_key)

print("Ciphertext:", ciphertext)

# Decrypt
decrypted = decrypt_message(nonce, ciphertext, tag, secure_key)
print("Decrypted:", decrypted)
