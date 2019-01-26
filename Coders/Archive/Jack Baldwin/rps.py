#!/bin/python3

## Can be found at
## https://trinket.io/embed/python/de918c4f5d

from random import randint

player=input('rock(r),paper(p)orscissors(s)?')
if player == 'r':
  print('0', end=' ')
  
  
print(player,'vs' ,end=' ')
chosen=randint(1,3)

#print(chosen)

if chosen == 1: 
  computer = 'r'
  print('0')
elif chosen == 2:
  computer = 'p'
else:
  computer = 's'
  
print(computer)

if player == computer:
  print('DRAW!')
elif player == 'r' and computer == 's':
  print('player wins!')
elif player == 'r' and computer == 'p':
  print('computer wins!')
elif player == 'p' and computer == 'r':
  print('player wins!')
elif player == 'p' and computer == 's':
  print('computer wins!')
elif player == 's' and computer == 'p':
  print ('player wins!')
elif player == 's' and computer == 'r':
  print ('computer wins!')
