from random import randint

player = input('rock (r), paper (p) or scissors (s)?')

print(player, 'vs' , end='')

chosen = randint(1,3)
#print(chosen)

if chosen == 1:
    computer = 'r'

elif chosen == 2:
    computer = 'p'

else:
    computer = 's'

#computer = 'r'

print(computer)

if player == computer:
    print('DRAW!')


