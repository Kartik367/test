import hashlib 
 
string = "Darshan"
encoded=string.encode()
result=hashlib.md5(encoded)
print("Hash value", result)
print("Hexadecimal equvalent:",result.hexdigest())
