#!/usr/bin/python3
print("Hello and Welcome to Callum's Message Program")

while True:
	print("\n1 - encrypt")
	print("2 - decrypt")
	print("3 - force decrypt")
	print("4 - exit")
	mode = input(": ")

	if mode == 1:
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		newMessage = ''
		message = raw_input('Please enter a message: ')
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
		print('Your new message is: ' + newMessage)

	if mode == 2:
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		newMessage = ''
		message = raw_input('Please enter a message: ')
		key = input('Please enter a key: ')
		key = int(key)
		for character in message:
		 if character in alphabet:
		  position = alphabet.find(character)
		  newPosition = (position - key) % 26
		  newCharacter = alphabet [newPosition]
		  #print ('The new character is :', newCharacter)
		  newMessage += newCharacter
		 else:
			newMessage += character

		print(' Your new message is: ' + newMessage)

	if mode == 3:
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		newMessage = ''
		message = raw_input('Please enter a message: ')

		for key in range(1,25):
			for character in message:
				if character in alphabet:
				  position = alphabet.find(character)
				  newPosition = (position + key) % 26
				  newCharacter = alphabet [newPosition]
				  #print ('The new character is :', newCharacter)
				  newMessage += newCharacter
				else:
					newMessage += character
			print(str(key) + ":" + newMessage)
			newMessage = ""

	if mode == 4: break
