from random import *

print("Play Your Cards Right")

answer = randint(0, 10)

print("Try and guess %d" % answer)

while True:
	guess = int(input("Input your guess: "))
	if (guess == answer):
		break
	elif (answer < guess):
		print("The real answer is lower")
	else:
		print("The real answer is higher")
		
print("You win!")