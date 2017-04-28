from flask import Flask, redirect, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('static/ToDoList.html') 
    

toDoList = {
	"list" : [
		{ "name": "Go Shopping" }, 
		{ "name" : "Feed Dog" }, 
		{ "name" : "Pay Bills" }
		]
	}
	
@app.route('/getList', methods=["GET"])
def getToDoList():
	return jsonify(toDoList);

@app.route('/addItem', methods=["POST"])
def addToDo():
	toDoItem = request.form["name"]
	print("To Do Item Added: {}".format(toDoItem))
	toDoList["list"].append({
		"name" : toDoItem
	})
	return '', 201
	
@app.route('/deleteItem', methods=["DELETE"])
def deleteToDo():
	toDoItem = request.form["name"]
	print("To Do Item Removed: {}".format(toDoItem))
	toDoList["list"].remove({
		"name" : toDoItem
	})
	return '', 201
