from CommandLineMenu import CommandLineMenu

class CaesarCipher:
	ALL_LETTERS = None
	
	# Singleton to contain the list of ALL_LETTERS
	@staticmethod
	def allLetters():
		if not CaesarCipher.ALL_LETTERS:
			# Generate all the allowed letters in a list
			allLetterCodes = range(ord('a'), ord('z'))
			
			# Map the codes to actual letters using the chr() function
			allLetterCodesMapped = map(chr, allLetterCodes)
			
			# Turn the map into a list
			CaesarCipher.ALL_LETTERS = list(allLetterCodesMapped)
		return CaesarCipher.ALL_LETTERS
	
	def __init__(self, key):
		self.key = key
		
	def encryptLetter(self, plainLetter):
		# find index of the letter
		index = CaesarCipher.allLetters().index(plainLetter) 
		
		# apply the key
		index += self.key 
		
		# wrap around
		index %= len(CaesarCipher.allLetters()) 
		
		# Return the letter identified by the modified index
		return CaesarCipher.allLetters()[index]
		
	def decryptLetter(self, cipherLetter):
		# find index of the letter
		index = CaesarCipher.allLetters().index(cipherLetter)
		
		# apply the key
		index -= self.key 
		
		# force more than zero (in case we wrapped backwards)
		index += len(CaesarCipher.allLetters()) 
		
		# wrap around using modulus
		index %= len(CaesarCipher.allLetters()) 
		
		# Return the letter identified by the modified index
		return CaesarCipher.allLetters()[index]

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

def runTests():
	testEncryptWord("hello", 5, "mjqqt")
	testDecryptWord("mehbs", 15, "world")
	print("All Tests of Caesar Cipher Passed")
runTests()

def encryptWord():
	plainText = input("Enter the word to encrypt: ")
	key = int(input("Enter the key: "))
	c = CaesarCipher(key = key)
	cipherText = c.encryptWord(plainText)
	print("Encrypted cipher text: {}".format(cipherText))

def decryptWord():
	cipherText = input("Enter the word to decrypt: ")
	key = int(input("Enter the key: "))
	c = CaesarCipher(key = key)
	plainText = c.decryptWord(cipherText)
	print("Decrypted plain text: {}".format(plainText))
	
def bruteForceDecryptWord():
	cipherText = input("Enter the word to decrypt: ")
	for key in range(len(CaesarCipher.allLetters())):
		c = CaesarCipher(key = key)
		plainText = c.decryptWord(cipherText)
		print("Decrypted plain text for key {}: {}"\
			.format(str(key).zfill(2), plainText))

menu = CommandLineMenu(title="Caesar Cipher") \
	.withQuitOption('q') \
	.withOption('e', 'Encrypt Word', encryptWord) \
	.withOption('d', 'Decrypt Word', decryptWord) \
	.withOption('b', 'Brute Force Decrypt', bruteForceDecryptWord) \
	.run()

