from random import randint
playername = input('What is your name?')
print('Welcome to ice, fire, earth, air',playername,'.My name is Coderbot')
player = input('Choose ice, fire, earth, water?')
print(player, 'vs', end=' ')

chosen = randint(1,3)
#print(chosen)

if(chosen == 1):
	computer = 'ice'
	
elif(chosen == 2):
	computer = 'fire'

elif(chosen == 3):
	computer = 'earth'
else:
	computer = 'air'

print(computer)

if(player == computer):
	print('DRAW!')

elif(player == 'fire' and computer == 'earth'):
	print(playername,'wins!')

elif(player == 'fire' and computer == 'water'):
	print('Coderbot wins!')
	
elif(player == 'paper' and computer == 'rock'):
	print(playername,'wins!')

elif(player == 'paper' and computer == 'scissors'):
	print('Coderbot wins!')
	
elif(player == 'scissors' and computer == 'paper'):
	print(playername,'wins!')

elif(player == 'scissors' and computer == 'rock'):
	print('Coderbot wins!')

elif(player == 'p' and computer == 'r'):
	print(playername,'wins!')

elif(player == 'p' and computer == 's'):
	print('Coderbot wins!')
