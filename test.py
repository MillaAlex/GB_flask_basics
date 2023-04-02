from flask import Flask
app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Hello, world!<h1><br><a href='/index'>visit next page</a>"

@app.route('/index')
def index():
    return "It is my first project<br><a href='/'>return</a><br><a href='/index2'>to calculator</a>"

@app.route('/index2/<x>/<y>')
def index2(x, y):
    return f'Result: {int(x) + int(y)}'

if __name__ == '__main__':
    app.run()
