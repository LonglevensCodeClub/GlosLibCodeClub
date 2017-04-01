alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[0])
print(alphabet[6])
print(alphabet[9])
key = 3
character = input ( 'please enter a character' )
position  = alphabet.find(character)
print(position)
newPosition = position + key % 26
print(newPosition)
