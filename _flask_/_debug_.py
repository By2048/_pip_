from flask import \
    Flask, \
    request, \
    jsonify, \
    redirect, \
    Response, \
    session

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/', methods="get post".split())
def index():
    path = request.path
    session['name'] = 123
    return 'index'


if __name__ == '__main__':
    app.run()
