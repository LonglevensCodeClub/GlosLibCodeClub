#!/bin/python3
from random import randint
print ('rock, paper scissors 3 rounds winner takes all')

numberOfDraws = 0
numberOfComputer = 0
numberOfPlayer = 0


for x in range(3):
	player=input('rock (r), paper (p) or scissors (s) lizard (l) spock (k)?')
	#print(player, 'vs')
	chosen = randint(1,3)
	#print(chosen)
	if(chosen == 1):
		computer = 'r'
	elif(chosen == 2):
		computer = 'p'
	elif(chosen == 3):
		computer = 'l'
	elif(chosen == 4):
		computer = 'k'
	else:
		computer = 's'
	#print (computer)		

	if(player == computer):
		print('DRAW!')
		numberOfDraws += 1
		## if player chooses rock
	elif(player == 'r' and computer == 's'):
		print('Player wins! rock crushes scissors')
		numberOfPlayer += 1
	elif(player == 'r' and computer == 'p'):
		print('computer wins! paper covers rock')
		numberOfComputer += 1
	elif(player == 'r' and computer == 'l'):
		print('player wins!rock crushes lizard ')
		numberOfPlayer+= 1
	elif(player == 'r' and computer == 'k'):
		print('computer wins! spock vaprises rock')
		numberOfComputer += 1
		## if player chooses paper
	elif(player == 'p' and computer == 'r'):
		print('player wins! paper covers rock')
		numberOfPlayer += 1
	elif(player == 'p' and computer == 's'):
		print('computer wins! scissors cuts paper')
		numberOfComputer += 1
	elif(player == 'p' and computer == 'l'):
		print('computer wins! lizard eats paper')
		numberOfComputer += 1
	elif(player == 'p' and computer == 'k'):
		print('player wins! paper dissproves spock')
		numberOfPlayer += 1
		## if player chooses scissors
	elif(player == 's' and computer == 'r'):
		print ('computer wins! rock crushes sissors ')
		numberOfPlayer += 1
	elif(player == 's' and computer == 'p'):
		print('player wins! sissors cuts paper')
		numberOfComputer += 1
	elif(player == 's' and computer == 'l'):
		print('player wins! sissors dicapetates lizard')
		numberOfPlayer += 1
	elif(player == 's' and computer == 'k'):
		print('computer wins! spock smashes scissors')
		numberOfComputer += 1
		## if player chooses lizard
	elif(player == 'l' and computer == 'r'):
		print('computer wins! rock crushes lizard')
		numberOfComputer += 1
	elif(player == 'l' and computer == 'p'):
		print('player wins! lizard eats paper')
		numberOfPlayer += 1
	elif(player == 'l' and computer == 's'):
		print('computer wins! scissors decapetats lizard')
		numberOfComputer += 1
	elif(player == 'l' and computer == 'k'):
		print('player wins! lizard poisens spock')
		numberOfPlayer += 1
		## if player chooses spock
	elif(player == 'k' and computer == 'r'):
		print('player wins! spock vaprises rock')
		numberOfPlayer += 1
	elif(player == 'k' and computer == 'p'):
		print('computer wins! paper dissproves spock')
		numberOfComputer += 1
	elif(player == 'k' and computer == 's'):
		print('player wins! spock smashes scissors')
		numberOfPlayer += 1
	elif(player == 'k' and computer == 'l'):
		print('computer wins! lizard poisens spock')
		numberOfComputer += 1

#print ('number of computer wins is ' + str(numberOfComputer))
#print ('number of player wins is ' + str(numberOfPlayer))
#print ('number of draws is ' + str(numberOfDraws))
print ('over all:')
if numberOfPlayer == numberOfComputer:
	print('it is a draw')
if numberOfComputer > numberOfPlayer:
	print('computer wins!')
if numberOfPlayer > numberOfComputer:
	print('player wins!')
