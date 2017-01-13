class Person():
	def __init__(self, name):
		self.name = name
		
	def introduceSelf(self):
		print("Hello, my name is {}".format(self.name))
		
		
me = Person("Joe Sharp")

me.introduceSelf()

james = Person("James Bond")
jason = Person("Jason Bourne")
neo = Person("Neo")

james.introduceSelf()
jason.introduceSelf()
neo.introduceSelf()
