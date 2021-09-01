from flask import \
    Flask, \
    request, \
    jsonify, \
    redirect, \
    Response, \
    session

app = Flask('_test_')
app.secret_key = 'qwe123'


@app.route('/', methods="get post".split())
def index():
    path = request.path
    session['name'] = 123
    return 'index'


if __name__ == '__main__':
    app.run()
