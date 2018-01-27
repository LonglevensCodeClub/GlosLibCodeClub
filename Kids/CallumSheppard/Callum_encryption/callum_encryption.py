#!/usr/bin/python3
print("Hello and Welcome to Callum's Encryption Program")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''
message = input('Please enter a message: ')
key = input('Please enter a key: ')
key = int(key)
for character in message:
 if character in alphabet:
  position = alphabet.find(character)
  newPosition = (position + key) % 26
  newCharacter = alphabet [newPosition]
  #print ('The new character is :', newCharacter)
  newMessage += newCharacter
 else:
    newMessage += character

print(' Your new message is: ',newMessage)
