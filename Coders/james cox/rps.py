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

elif player == 'r'and computer == 's':
    print('player wins!')

elif player =='r' and computer == 'p':
    print('coputer wins!')
    
elif player =='p' and computer == 'r':
    print('player wins!')
    
elif player == 'p' and computer == 's':
    print('computer wins!')
    
elif player == 's' and computer == 'r':
    print('computer wins!')
    
elif player == 's' and computer == 'p':
    print('player wins!')


