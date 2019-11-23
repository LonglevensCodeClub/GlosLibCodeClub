from CaesarCipher import encryptMessage, decryptMessage

message = 'This is a secret message '
key = 16

cipherText  = encryptMessage(message, key)

print('Encrypted Message: ') + cipherText

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print (alphabet[0])
print(alphabet[6])
print(alphabet[9])
