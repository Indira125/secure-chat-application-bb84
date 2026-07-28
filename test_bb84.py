from bb84 import generate_bits, generate_bases, generate_key

n = 20

alice_bits = generate_bits(n)
alice_bases = generate_bases(n)
bob_bases = generate_bases(n)

key = generate_key(alice_bits, alice_bases, bob_bases)

print("Shared key:", key)
print("Key length:", len(key))
