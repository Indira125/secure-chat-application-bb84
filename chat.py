from bb84 import generate_bits, generate_bases, generate_key, detect_eavesdropping
from crypto_utils import hash_key, encrypt_message, decrypt_message

# Number of qubits
n = 100

print("🔐 Starting Quantum Key Distribution (BB84)...")

# Alice (Sender)
alice_bits = generate_bits(n)
alice_bases = generate_bases(n)

# Bob (Receiver)
bob_bases = generate_bases(n)

# Generate keys
alice_key = generate_key(alice_bits, alice_bases, bob_bases)
bob_key = generate_key(alice_bits, alice_bases, bob_bases)

print("🔑 Raw key length:", len(alice_key))

# Detect eavesdropping
if detect_eavesdropping(alice_key, bob_key):
    print("❌ Eavesdropping detected! Session aborted.")
    exit()

print("✅ Secure key established!")

# Strengthen key
secure_key = hash_key(alice_key)

# Secure message exchange
message = "Hello Bob, this is a quantum-secure message!"
nonce, ciphertext, tag = encrypt_message(message, secure_key)

print("\n📨 Encrypted message sent...")
print("Ciphertext:", ciphertext)

# Bob decrypts
decrypted_message = decrypt_message(nonce, ciphertext, tag, secure_key)
print("\n📩 Decrypted message received:")
print(decrypted_message)
