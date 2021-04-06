from flask import Flask, flash, get_flashed_messages

app = Flask(__name__)

app.secret_key = __name__


@app.route("/index1")
def index1():
    flash("message-content")
    pass


@app.route("/index2")
def index2():
    data = get_flashed_messages()
    pass


if __name__ == '__main__':
    app.debug = True
    app.run()
