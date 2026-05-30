from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/add', methods=['GET'])
def add_task():
    task = request.args.get('task')
    if task:
        tasks.append(task)
        return jsonify({'message': f'Task "{task}" added successfully!', 'tasks': tasks}), 201
    return jsonify({'error': 'Task content is required'}), 400

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        deleted_task = tasks.pop(task_id)
        return jsonify({'message': f'Task "{deleted_task}" deleted successfully!', 'tasks': tasks}), 200
    return jsonify({'error': 'Invalid task ID'}), 404

if __name__ == '__main__':
    app.run(debug=True)
