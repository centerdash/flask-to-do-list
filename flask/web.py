from flask import Flask, render_template

app = Flask(__name__)

tasks = []

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html')

@app.route('/add/<task>')

def add(task):
    global tasks
    tasks.append(task)
    return render_template('main.html', tasks=tasks)

@app.route('/delete/<task>')

def remove(task):
    global tasks
    tasks.remove(task)
    return render_template('main.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)