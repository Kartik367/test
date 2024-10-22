def ceaser_cipher(text,shift):
	result=""
	for char in text:
		if char.isalpha():
			shift_base=65 if char.isupper() else 97
			result += chr((ord(char)-shift_base+shift)%26 +shift_base)
		else:
			result+=char
	return result
text= "Hello, World"
shift= 3
cipher_text = ceaser_cipher(text,shift)
print("Cipher text", cipher_text)
