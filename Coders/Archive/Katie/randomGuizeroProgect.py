from guizero import App, Text, TextBox

app = App(title="hi!")

welcome_message = Text(app, text="Welcome to my app" , size=40, font="New Roman", color="purple")

my_name = TextBox(app)

app.display()


