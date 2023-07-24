from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []  # List to store the todo items

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append({'text': todo.strip(), 'completed': False})
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    todos.pop(todo_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>', methods=['POST'])
def edit(todo_id):
    todo_text = request.form.get('todo')
    todos[todo_id]['text'] = todo_text
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle(todo_id):
    todos[todo_id]['completed'] = not todos[todo_id]['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
