from CaesarCipher import encryptMessage, decryptMessage

message = 'This is a secret message '
key = 19

cipherText = encryptMessage(message, key)

print('Encrypted Message: '+ cipherText) 

# should decrypt to 'hello' with a key of 7

cipherText = 'olssv'
key = 7

plainText = decryptMessage(cipherText, key)

print ('Decrypted Message: ' + plainText)

cipherText = ' xubbe, mubsecue je setu sbkr'
for x in range(0, 26):
  plainText = decryptMessage(cipherText, x )
  print('Key: {} - {}' .format(x, plainText))
