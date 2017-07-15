alphabet = "abcdefghijklmonpqrstuvwxyz"

key = 3

character = input("please enter a character to encript:" )

position = alphabet.find(character)

newposition = (position + key) % 26

encryptedmessage = alphabet[newposition]

print("your encripted letter is" , encryptedmessage)

name = input("what is your name? ")

for char in name:
	print(char)

alphabet = "abcdefghijklmnopqrstuvwxyz"

message = input("please enter a meassage to encrypt: ")

encryptedmessage = ""

for char in message:
	position = alphabet.find(char)
	newposition = (position + key) % 26
	encryptedletter = alphabet[newposition]
	encryptedmessage = encryptedmessage + encryptedletter
	
print(encryptedmessage)
