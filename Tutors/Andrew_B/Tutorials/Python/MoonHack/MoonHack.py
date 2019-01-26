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

answers = 0

while answers != 4:

    print("It is the year 2049. You are on a solo mission to restock the base on the moon with soil and seeds to grow more plants.")
    print("You have just landed but you are in trouble. You have landed 300 kilometers from the moon base!")
    print("You can get to the base in 3 days on your lunar rover")
    print("The lunar rover can only fit you in your spacesuit and 4 other items")
    print("Out of the items below, which do you bring? \n")

    for objects in items:
        print(objects)

    print("Type the letter of the 4 items you would like to bring seperated by commas. Do not add spaces \n Ex: A,B,C,D")

    user_choice = input("Enter your choice:")

    print("You chose", user_choice)

    user_list = list(user_choice.split(','))
    print(user_list)

    answers = len(user_list)

    if answers != 4:
        print('You have selected the wrong number of items. Try again \n')

correct_items = 0

if "A" not in user_list:
    print("Without a litre of water a day you will dehydrate")
else:
    correct_items += 1

if "B" in user_list:
    print("I shouldn't care about how your hair will look, this is survival time!")
    
if "C" in user_list:
    print("You already have a spacesuit, no room for a spare. Be careful not to puncture the one you are wearing!")
    
if "D" in user_list:
    print("There's no room in the rover for the shovel along with the 4 items needed to survive. Just don't get stuck in any craters!")

if "E" not in user_list:
    print("Without oxygen you will not have any air to breathe!")
else:
    correct_items += 1

if "F" not in user_list:
    print("Without solar panels your lunar rover will not have enough power to make it to the base.")
else:
    correct_items += 1

if "G" in user_list:
    print("If you don't make it back to base alive there will be no mission, so the seeds can wait!")
    
if "H" in user_list:
    print("The soil can wait for the seeds.")

if "I" not in user_list:
    print("You will not make it to the moon without food. You will need your energy to drive the rover.")
else:
    correct_items += 1

if correct_items == 4:
    print("Hooray! You picked all 4 correct items. You will make it to moonbase safely!")
else:
    print("Your choice did not include the correct items necessary for survival. You will not make it safely to moonbase.")