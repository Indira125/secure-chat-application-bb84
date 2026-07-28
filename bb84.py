import random

def generate_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generate_bases(n):
    return [random.choice(['+', 'x']) for _ in range(n)]

def generate_key(alice_bits, alice_bases, bob_bases):
    key = []
    for i in range(len(alice_bits)):
        if alice_bases[i] == bob_bases[i]:
            key.append(alice_bits[i])
    return key

def detect_eavesdropping(key1, key2, threshold=0.25):
    mismatches = sum(1 for a, b in zip(key1, key2) if a != b)
    error_rate = mismatches / max(1, len(key1))
    return error_rate > threshold
