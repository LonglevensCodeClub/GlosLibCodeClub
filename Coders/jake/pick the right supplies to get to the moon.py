 #!/bin/python3
 
items = [
"A: 3 litres of water",
"B: Shampoo",
"C: An extra Spacesuit",
"D: A shovel",
"E: A 10 day oxygen supply",
"F: Solar panels",
"G: The seeds for your mission",
"H: The soil for your mission",
"I: A 3 day food supply"
]

print("It is the year 2049. You are on a solo mission to restock the base on the moon with soil and seeds to grow more plants.")
print("You have just landed but you are in trouble. You have landed 300 kilometers from the moon base!")
print("You can get to the base in 3 days on your lunar rover")
print("The lunar rover can only fit you in your spacesuit and 4 other items")
print("Out of the items below, which do you bring? \n")

for objects in items:
  print(objects)

print("Type the letter of the 4 items you would like to bring seperated by commas. Do not add spaces \n Ex: A,B,C,D")
 
print("Type the letter of the 4 items?")

user_choice = input("Enter your choice: ")
#print("choice=",user_choice)

user_list = list(user_choice.split(','))
#print(user-list)

if "a" not in user_list:
  print("without a liter of water a day you will dehidrate")
  
if "E" not in user_list:
  print("you will not survive without air")
  
if "F" not in user_list:
  print("without power your rover will not have enough enrgy to get to the moon")
  
if "I" not in user_list:
  print("you will not make it to the moon base without food.you will need enrgy to drive the rover")
  
if "A" in user_list and "E" in user_list and "F" in user_list and "I" in user_list:
  print("hooray! you picked the right 4 items. you will make it safely to the moon base")
else:
  print("you did not pick the correct 4 items for survival. you will not make it safely to the moonbase")
  
