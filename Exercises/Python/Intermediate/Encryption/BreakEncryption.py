from CaesarCipher import encryptMessage, decryptMessage

message = 'This is a secret message '
key = 16

cipherText  = encryptMessage(message, key)

print('Encrypted Message: '+ cipherText) 

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''

message = input('Please enter a message: ')

for character in message:
 position = alphabet.find(character)
 print(position)
 newPosition = (position + key) % 26 
 print(newPosition)
 #newCharacter = alphabet[newPosition]
 print('The new message is:', newMessage)

#print (alphabet[0])
#print(alphabet[6])
#print(alphabet[9])
