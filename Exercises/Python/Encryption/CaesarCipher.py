
ALL_LETTERS = None

# Generate all the allowed letters in a list
allLetterCodes = range(ord('a'), ord('z') + 1)

# Map the codes to actual letters using the chr() function
allLetterCodesMapped = map(chr, allLetterCodes)

# Turn the map into a list
ALL_LETTERS = list(allLetterCodesMapped)

def encryptLetter(plainLetter, key):
	try:
		# find index of the letter
		index = ALL_LETTERS.index(plainLetter) 
		
		# apply the key
		index += key 
		
		# wrap around
		index %= len(ALL_LETTERS) 
		
		# Return the letter identified by the modified index
		return ALL_LETTERS[index]
	except ValueError:
		# Default to returning the letter unmodifed
		return plainLetter
		
def decryptLetter(cipherLetter, key):
	try:
		# find index of the letter
		index = ALL_LETTERS.index(cipherLetter)
		
		# apply the key
		index -= key 
		
		# force more than zero (in case we wrapped backwards)
		index += len(ALL_LETTERS) 
		
		# wrap around using modulus
		index %= len(ALL_LETTERS) 
		
		# Return the letter identified by the modified index
		return ALL_LETTERS[index]
	except ValueError:
		# Default to returning the letter unmodifed
		return cipherLetter

# Given a plain text message
# Encrypts with our key and returns the cipher text
def encryptMessage(plainText, key):
	cipherText = ""

	for p in plainText.lower():
		c = encryptLetter(p, key)
		cipherText += c
	
	return cipherText
		
# Given a cipher text message
# Decrypts with our key and returns the plain text
def decryptMessage(cipherText, key):
	plainText = ""
	
	for c in cipherText.lower():
		p = decryptLetter(c, key)
		plainText += p
		
	return plainText
