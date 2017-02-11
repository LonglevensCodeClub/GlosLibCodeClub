from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

toDoList = ["Go Shopping", "Feed Dog", "Pay Bills"]

@app.route('/')
def index():
    return render_template('HelloFlask.html')

@app.route('/getToDo', methods=["GET"])
def getToDo():
	return jsonify(toDoList)
	
@app.route('/addToDo', methods=["POST"])
def addToDo():
	toDoItem = request.form["item"]
	print("To Do Item Added: {}".format(toDoItem))
	toDoList.append(toDoItem)
	return '', 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
