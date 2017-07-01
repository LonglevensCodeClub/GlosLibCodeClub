from random import randint
playername = input('What is your name?')
print('Welcome to Elemental battles',playername,'.My name is Coderbot')
print('Water beats Fire, Fire beats Air, Air beats Earth, Earth beats Water.') 
player = input('Choose air, fire, earth, water?')
print(player, 'vs', end=' ')

chosen = randint(1,3)
#print(chosen)

if(chosen == 1):
	computer = 'water'
	
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
	
elif(player == 'water' and computer == 'fire'):
	print(playername,'wins!')

elif(player == 'water' and computer == 'earth'):
	print('Coderbot wins!')
	
elif(player == 'earth' and computer == 'water'):
	print(playername,'wins!')

elif(player == 'earth' and computer == 'air'):
	print('Coderbot wins!')

elif(player == 'air' and computer == 'earth'):
	print(playername,'wins!')

elif(player == 'air' and computer == 'fire'):
	print('Coderbot wins!')

print('Thank you for playing!')
