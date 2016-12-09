class CaesarCipher:
	def __init__(self, key):
		self.key = key

		# Generate all the allowed letters in a list
		allLetterCodes = range(ord('a'), ord('z'))
		
		# Map the codes to actual letters using the chr() function
		allLetterCodesMapped = map(chr, allLetterCodes)
		
		# Turn the map into a list
		self.allLetters = list(allLetterCodesMapped)
		
		# We will print it out to demonstrate the alphabet generation works
		#print("All Letters {}".format(self.allLetters))
		
	def encryptLetter(self, plainLetter):
		# find index of the letter
		index = self.allLetters.index(plainLetter) 
		
		# apply the key
		index += self.key 
		
		# wrap around
		index %= len(self.allLetters) 
		
		# Return the letter identified by the modified index
		return self.allLetters[index]
		
	def decryptLetter(self, cipherLetter):
		# find index of the letter
		index = self.allLetters.index(cipherLetter)
		
		# apply the key
		index -= self.key 
		
		# force more than zero (in case we wrapped backwards)
		index += len(self.allLetters) 
		
		# wrap around using modulus
		index %= len(self.allLetters) 
		
		# Return the letter identified by the modified index
		return self.allLetters[index]

	# Given a plain text word
	# Encrypts with our key and returns the cipher text
	def encryptWord(self, plainText):
		cipherText = ""

		for p in plainText:
			c = self.encryptLetter(p)
			cipherText += c
		
		return cipherText
		
	# Given a cipher text word
	# Decrypts with our key and returns the plain text
	def decryptWord(self, cipherText):
		plainText = ""
		
		for c in cipherText:
			p = self.decryptLetter(c)
			plainText += p
			
		return plainText

def testEncryptWord(plainText, key, expected):
	# When
	c = CaesarCipher(key)
	result = c.encryptWord(plainText)
	
	# Then
	assert expected == result, "Incorrect '{}'!='{}'".format(expected, result)

def testDecryptWord(cipherText, key, expected):
	# When
	c = CaesarCipher(key)
	result = c.decryptWord(cipherText)
	
	# Then
	assert expected == result, "Incorrect '{}'!='{}'".format(expected, result)

testEncryptWord("hello", 5, "mjqqt")
testDecryptWord("mehbs", 15, "world")

print("All Tests Passed!")

