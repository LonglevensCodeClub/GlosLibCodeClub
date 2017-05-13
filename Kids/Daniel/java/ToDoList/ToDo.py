from flask import Flask, redirect, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
	return redirect('static/ToDoList.html')
	
ToDoList = {
	"list" : [
		]
	}

@app.route("/getList", methods=["GET"])
def getToDoList():
	return jsonify(ToDoList);

@app.route("/additem", methods=["POST"])
def addToDo():
	ToDoitem = request.form["name"]
	print("To Do List Added: {}".format(ToDoitem))
	ToDoList["list"].append({
		"name" : ToDoitem
	});
	return "", 201

if __name__ == "__main__":
    app.run()
