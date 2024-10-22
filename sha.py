import hashlib

str="onpiece"

result = hashlib.sha384(str.encode())
print("The Hexadecimal equivalent of SHA348 is:")
print(result.hexdigest())
print("\r")

result = hashlib.sha512(str.encode())
print("The Hexadecimal equivalent of SHA512 is:")
print(result.hexdigest())




