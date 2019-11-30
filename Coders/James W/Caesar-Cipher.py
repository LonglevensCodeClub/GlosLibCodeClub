class CaesarCipher:
    def _init_(self, key):
        self.key = key

        def encryptLetter(self, plainLetter)
            return 'a'

        def decryptLetter(self, cipherLetter):
            return 'a'

        #Generate all the allowed letters in a list
        allLetterCodes = range(ord('a'), ord('z'))

        #Map the codes to actual letters using the chr() function
        allLetterCodesMapped = map (chr, allLetterCodes)

        #Turn the map into a list
        self.allLetters = list (allLetterCodesMapped)
        
        #We will print it out to demonstrate the alphabet generation works
        print ("All Letters {}" .format(self.allLetters))

#Gives a plain text word
# Encrypts with our key and returns the cipher text
def encryptWord(self, plainText):
    cipherText = ""

    for p in plainText:
        c self.encryptLetter(p)
        ciphertext += c

        return cipherText
    #Given a cipher text word
    #Decrypts with our key and returns the plain text
    def decryptWord(self, cipherText):
        plainText = ""
        return plainText
    
    def testEncryptWord(plainText, key, expected):
        # When
        c = CaesarCipher(key)
        result = c.encryptWord(plainText)

        # Then
        assert expected == result, "Incorrect '{}'!0'".format(expected, result)
        

testEncryptWord("hello", 5, mjqqt")
                
