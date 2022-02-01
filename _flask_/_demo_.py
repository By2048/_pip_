from flask import Flask, request, jsonify

app = Flask(__name__)

PORT = 1234


@app.route('/', methods="get post".split())
def index():
    path = request.path
    return 'index'


if __name__ == '__main__':
    print(f'server start at {PORT}')
    app.run(host='0.0.0.0', port=PORT, debug=True)
# set FLASK_APP=hello
# set FLASK_ENV=development
# flask run