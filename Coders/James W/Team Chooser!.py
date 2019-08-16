
from random import choice 

players = []
file = open('player.txt', 'r')
players = file.read().splitlines()
print(players)

teamA= []
teamB= []
 
while len(players) > 0: 
 playerA = choice(players)
 print(playerA)
 teamA.append(playerA)
 players.remove(playerA)
 print('Players Left:', players)


 if players ==[]:
   break

 playerB = choice(players)
 print(playerB)
 teamB.append(playerB)
 players.remove(playerB)
 print('Players Left:', players)
 
 print('TeamA:', teamA)
 print('TeamB:', teamB)
 
 
Harry
Hermione
Neville
Ginny
Luna
