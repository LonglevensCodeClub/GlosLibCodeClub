class CmdOption:
	def __init__(self, text, command=None):
		self.text = text
		self.command = command
		

class CommandLineMenu:
	def __init__(self, title):
		self.title = title
		self.options = dict()
		self.quitOption = None
		
	def withQuitOption(self, char, command=None):
		self.withOption(char, "Quit", command)
		self.quitOption = char
		return self
		
	def withOption(self, char, text, command):
		option = CmdOption(text, command)
		self.options[char] = option
		return self
		
	def run(self):
		while True:
			print("+++++++++++++++++++")
			print("Menu {}".format(self.title))
			for (c, o) in self.options.items():
				print("{}:\t{}".format(c, o.text))
			chosen = input("Please choose an option: ")
			if chosen in self.options:
				option = self.options[chosen]
				if option.command:
					option.command()
				if self.quitOption == chosen:
					print("Now quitting")
					break
			else:
				print("Invalid selection {} expected one of {}".format(chosen, self.options.keys()))


	
