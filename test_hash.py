from crypto_utils import hash_key

key = [0, 1, 1, 0, 1]
hashed = hash_key(key)

print("Hashed key:", hashed)
print("Key length:", len(hashed))
