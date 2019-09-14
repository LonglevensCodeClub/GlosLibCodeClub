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



print("Type the letter of the 4 items you would like to bring seperated by commas. Do not add spaces \n Ex: A,B,C,D")
user_choice =input("Enter your choice: ")
#print(user_choice)
user_list= list(user_choice.split(','))
#print(user_list)
if "A" not in user_list:
    print("Without a litre of water a day you will dehydrate")

if "E" not in user_list:
        
    print ("Without oxygen you will not have any air to breathe!")

if "F" not in user_list:
    print("Without solar panels your lunar rover will not have enough power to make it to the base")

if "I" not in user_list:
    print("You will not be able to make it to the moon base without food you need your energy to drive the rover.")
if "A" in user_list and "E" in user_list and "F" in user_list and "I" in user_list:
    print ("Hooray! You picked the correct 4 items. You will make it to the moonbase safely")
else:
    print("You did not pick the correct 4 items for survival. You will not make it to the moonbase safely")


