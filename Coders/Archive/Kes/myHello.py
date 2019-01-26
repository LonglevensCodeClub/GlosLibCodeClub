alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newmesg = ''
mesg=input('please enter a message: ')
for character in message:
position = alphabet.find(character)
print(position)

npos = (position + key) % 26
print(npos)

nc = alphabet[npos]
print('new character is this: ', nc)
