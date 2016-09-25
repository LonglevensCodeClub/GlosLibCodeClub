print( "hello")
from random import randint
alien=input('rock(r),paper(p)or scissors(s)?')

chosen=randint(1,3)
print(chosen)
if(chosen==1):
	computer = 'r'
elif(chosen==2):
	computer = 'p'
elif(chosen==3):
	computer = 's'
print('alien',alien, 'vs',computer)
if (alien == computer):
	print ('THIS WAS A DRAW!!') 
elif(alien == 'r' and computer == 's'):
	print('alien wins!')
elif(alien == 'r' and computer == 'p'):
	print('computer wins!')
elif(alien == 'p' and computer == 'r'):
	print('alien wins!')
elif(alien == 'p' and computer == 's'):
	print('computer wins!')
elif(alien == 's' and computer == 'p'):
	print('alien wins!')
elif(alien == 's' and computer == 'r'):
	print('computer wins!')

