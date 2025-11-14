'''
Put and Delete HTTP Verbs
Put and Delete HTTP verbs are used to update and delete resources on a server, respectively. 
In Flask, you can handle these verbs by specifying them in the route decorator.    
'''
from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial data in my To-Do List
todo_list = [
    {'id': 1, 'task': 'Buy groceries'},
    {'id': 2, 'task': 'Read a book'},
    {'id': 3, 'task': 'Write code'}
]

@app.route('/')
def home():
    return "Welcome to the To-Do List App"

# GET Req:Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(todo_list)

# GET Req: Retrieve a specific task by ID
@app.route('/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = next((task for task in todo_list if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error":"Task not found"})
    return jsonify(task)

# POST Req: Add a new task
@app.route('/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'task' in request.json:
        return jsonify({"error":"Task not found"})
    new_task = {
        'id': todo_list[-1]['id'] + 1 if todo_list else 1,
        'task': request.json['task']
    }
    todo_list.append(new_task)
    return jsonify(new_task)

# PUT Req: Update an existing task
@app.route('/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task = next((task for task in todo_list if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error":"Task not found"})
    task['task'] = request.json.get('task',task['task'])
    return jsonify(task)

# DELETE Req: Delete a task
@app.route('/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    global todo_list
    todo_list = [task for task in todo_list if task['id'] != task_id]
    return jsonify({"result":"Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)