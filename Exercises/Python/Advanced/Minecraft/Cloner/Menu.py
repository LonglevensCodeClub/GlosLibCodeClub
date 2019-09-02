
class MenuOption:
	def __init__(self, prompt, callback):
		self._prompt = prompt;
		self._callback = callback;
		
	def run(self):
		self._callback();
		
	def getPrompt(self):
		return self._prompt;

class Menu:
	def __init__(self, title="My Cool Menu"):
		self._title = title;
		self._options = []
		
	def addOption(self, option):
		self._options.append(option);

	def run(self):
		while (True):
			print(self._title);
			for o, opt in enumerate(self._options):
				print(str(o) + ": " + opt.getPrompt());
			
			which = input("Select an Option:")
			whichIndex = int(which)
			self._options[whichIndex].run()
