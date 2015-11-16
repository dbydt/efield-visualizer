# Description:
# caesar.py contains caesar shift related functions
# 
# Author:
# Calvin Yeung (dbydt)

import textutils

# returns caesar-encrypted text
def encrypt(text, shift):
	message = ""
	
	for c in text:
		message = message + textutils.normalized_char_shift(c, shift)
		
	return message

# decrypts caesar shift	
def decrypt(text, shift):
	return encrypt(text, -shift)
	
# returns list of all possible shifts
def brute_force(text):
	texts = []
	
	for shift in range(26):
		texts.append(encrypt(text, shift))
		
	return texts