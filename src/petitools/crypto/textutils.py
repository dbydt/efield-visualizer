# Description:
# testutils.py contains simple text-related
# helper functions
# 
# Author:
# Calvin Yeung (dbydt)

# shifts character without bounds (dangerous)
def char_shift(character, shift):
	return chr(ord(character) + shift)

# shifts upper or lower case characters with wrap
def normalized_char_shift(character, shift):
	code = ord(character) + shift
	
	if character.isalpha():
		if character.isupper():
			while code < ord('A'):
				code += 26
			while code > ord('Z'):
				code -= 26
		elif character.islower():
			while code < ord('a'):
				code += 26
			while code > ord('z'):
				code -= 26	
		return chr(code)
	
	else:
		return character