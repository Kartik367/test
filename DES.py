from Crypto.Cipher import DES

key = b'8bytekey'  # 8-byte key
cipher = DES.new(key, DES.MODE_ECB)

plaintext = "Hello DES"  # Text to encrypt
padded_text = plaintext + ' ' * (8 - len(plaintext) % 8)  # Padding

encrypted = cipher.encrypt(padded_text.encode())
print("Encrypted:", encrypted)

decrypted = cipher.decrypt(encrypted).decode().strip()
print("Decrypted:", decrypted)
