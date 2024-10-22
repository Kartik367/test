import random 
def generate_private_key(prime): 
    return random.randint(1, prime - 1) 
 
def compute_public_key(base, private_key, prime): 
    return (base ** private_key) % prime 
 
def compute_shared_secret(public_key, private_key, prime): 
    return (public_key ** private_key) % prime 
 
prime = 29 
base = 5 
private_key_a = generate_private_key(prime) 
public_key_a = compute_public_key(base, private_key_a, prime) 
 
private_key_b = generate_private_key(prime) 
public_key_b = compute_public_key(base, private_key_b, prime) 
 
shared_secret_a = compute_shared_secret(public_key_b, private_key_a, prime) 
shared_secret_b = compute_shared_secret(public_key_a, private_key_b, prime) 
 
print("User A's private key:", private_key_a) 
print("User A's public key:", public_key_a) 
print("User B's private key:", private_key_b) 
print("User B's public key:", public_key_b) 
print("Shared secret (A):", shared_secret_a) 
print("Shared secret (B):", shared_secret_b)
