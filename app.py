from flask import Flask, request, jsonify, abort
from tasks import TMS

app = Flask(__name__)
task_manager = TMS()

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = task_manager.get_all_tasks()
    return jsonify(tasks), 200

@app.route('/api/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'due_date': request.json.get('due_date', "")
    }
    new_task = task_manager.create_task(task)
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_manager.get_task_by_id(task_id)
    if task is None:
        abort(404)
    return jsonify(task), 200

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if not request.json:
        abort(400)
    task = task_manager.get_task_by_id(task_id)
    if task is None:
        abort(404)
    updated_task = {
        'title': request.json.get('title', task['title']),
        'description': request.json.get('description', task['description']),
        'due_date': request.json.get('due_date', task['due_date'])
    }
    task = task_manager.update_task(task_id, updated_task)
    return jsonify(task), 200

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = task_manager.delete_task(task_id)
    if not result:
        abort(404)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
