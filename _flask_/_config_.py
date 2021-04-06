from flask import Flask, request

app = Flask(__name__)
app.debug = True
app.config.from_pyfile()
app.config.from_object()
app.config.from_pyfile()
app.config.from_json()


@app.route('/', methods="get post".split())
def index():
    path = request.path
    return 'index'


if __name__ == '__main__':
    app.run()
