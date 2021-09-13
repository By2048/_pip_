from flask import Flask, current_app

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask, current_app

app = Flask(__name__)

app1 = Flask('app01')
app2 = Flask('app02')


@app.get('/')
def index():
    pass


@app.post('/')
def index():
    pass


@app.put('/')
def index():
    pass


@app.delete('/')
def index():
    pass


@app1.route('/index')
def index():
    return "app01"


@app2.route('/index2')
def index2():
    return "app2"


# http://localhost:5000/index
# http:/localhost:5000/sec/index2
dm = DispatcherMiddleware(app1, {
    '/sec': app2,
})

if __name__ == "__main__":
    run_simple('localhost', 5000, dm)
