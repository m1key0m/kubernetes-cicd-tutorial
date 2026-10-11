from flask import Flask, render_template, request, redirect
from todo.tasks import load_tasks, save_tasks

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tasks=load_tasks())

@app.route('/add', methods=['POST'])
def add():
    new_task = request.form.get('newTask')
    tasks = load_tasks()
    tasks.append(new_task)
    save_tasks(tasks)
    return redirect('/')

@app.route('/complete', methods=['POST'])
def complete():
    task_index = int(request.form.get('taskIndex')) - 1
    tasks = load_tasks()
    tasks[task_index] = f'[✔] {tasks[task_index]}'
    save_tasks(tasks)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    task_index = int(request.form.get('taskIndex')) - 1
    tasks = load_tasks()
    del tasks[task_index]
    save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
