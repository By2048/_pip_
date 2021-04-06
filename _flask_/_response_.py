from flask import make_response, Flask, request, session

app = Flask(__name__)


@app.route("/index")
def index():
    response = make_response()
    return response


if __name__ == '__main__':
    app.debug = True
    app.run()
