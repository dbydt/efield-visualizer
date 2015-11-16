# Description:
# vigenere.py contains encrypt and decrypt
# functions using the vigenere encryption
# method
# 
# Author:
# Calvin Yeung (dbydt)

import textutils

# returns encrypted text using vigenere
def encrypt(text, key):
	key = key.upper()
	message = ""
	index = 0
	
	for c in text:
		if c.isalpha():
			message = message + textutils.normalized_char_shift(c, ord(key[index]) - ord('A'))
			index += 1
		else:
			message = message + c
		if index == len(key):
			index = 0
	
	return message
	
# returns decrypted text using vigenere
def decrypt(text, key):
	key = key.upper()
	message = ""
	index = 0
	
	for c in text:
		if c.isalpha():
			message = message + textutils.normalized_char_shift(c, ord('A') - ord(key[index]))
			index += 1
		else:
			message = message + c
		if index == len(key):
			index = 0
	
	return message