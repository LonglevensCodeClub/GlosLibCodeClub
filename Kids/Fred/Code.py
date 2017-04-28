#!/bin/python3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('enter a number: '))
newMessage = ''
Message= input('Please enter a message: ')
for character in Message:
	position = alphabet.find(character)
	newPosition = (position + key) %26
	newCharacter = alphabet[newPosition]
	newMessage += newCharacter
print("New Encrypted message: %s" % newMessage)	

	
