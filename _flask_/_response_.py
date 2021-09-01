from flask import \
    Flask, \
    make_response, \
    request, \
    session, \
    flash

app = Flask(__name__)


@app.route("/index")
def index():
    response = make_response()
    response.set_cookie('k', 'v')
    return response


if __name__ == '__main__':
    app.debug = True
    app.run()
