def gcd(a, b): 
    while b: 
        a, b = b, a % b 
    return a 
 
def mod_inverse(e, phi): 
    for d in range(1, phi): 
        if (e * d) % phi == 1: 
            return d 
def generate_keys(): 
    p, q = 61, 53 
    n = p * q 
    phi = (p - 1) * (q - 1) 
    e = 17 
    d = mod_inverse(e, phi) 
    return (e, n), (d, n) 
 
def encrypt(message, public_key): 
    e, n = public_key 
    return [(ord(char) ** e) % n for char in message] 
 
def decrypt(cipher, private_key): 
    d, n = private_key 
    return ''.join([chr((char ** d) % n) for char in cipher]) 
 
# Example usage 
public_key, private_key = generate_keys() 
message = "HELLO" 
encrypted = encrypt(message, public_key) 
decrypted = decrypt(encrypted, private_key) 
 
print("Original:", message) 
print("Encrypted:", encrypted) 
print("Decrypted:", decrypted)
