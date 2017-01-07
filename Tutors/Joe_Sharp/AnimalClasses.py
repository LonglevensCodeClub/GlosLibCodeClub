
print("Hello");

class Animal:	
	def speak(self):
		pass
		
class Dog(Animal):
	def speak(self):
		print("Woof");
		
class Cat(Animal):
	def speak(self):
		print("Meow");
		
animals = []
animals.append(Dog());
animals.append(Cat());
animals.append(Dog());
animals.append(Dog());

for a in animals:
	a.speak()
