from flask import Flask, render_template

server = Flask(__name__)


@server.route('/')
def hello():
    return '''Hello, World!
    <br>
    <a target="_blank" href="index">Index</a>'''


@server.route('/index')
def index():
    name = 'Маша'
    return render_template('index.html')


@server.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')



server.run()

