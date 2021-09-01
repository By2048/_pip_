import time
import logging

from werkzeug.routing import BaseConverter
from flask import \
    Flask, \
    request, \
    url_for

app = Flask(__name__)


@app.route('/')
def test():
    return 'test'


""" app.route()
flask.scaffold.Scaffold.route
flask.app.Flask.add_url_rule
werkzeug.routing.Rule
"""


@app.route(
    '/',
    redirect='',
    methods='get post'.split()
)
def test_args():
    return 'test'


@app.route('/test_1/<arg>')
def test_1(arg):
    return f"arg {arg} {type(arg)}"


@app.route('/test_2/<string:arg>')
def test_2(arg):
    return f"arg {arg} {type(arg)}"


@app.route('/test_3/<int:arg>', defaults={"arg": 123})
def test_3(arg):
    return f"arg {arg} {type(arg)}"


@app.route('/test_4/<float:arg>')
def test_4(arg):
    return f"arg {arg} {type(arg)}"


@app.route('/test_5/<path:arg>')
def test_5(arg):
    return f"arg {arg} {type(arg)}"


@app.route('/test_6/<uuid:arg>')
def test_6(arg):
    return f"arg {arg} {type(arg)}"


@app.route('/test_7', endpoint='test_7_endpoint')
def test_7():
    return "test_7"


class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super().__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        print("1", value)
        value = int(value) * 2
        value = str(value)
        return super().to_python(value)

    def to_url(self, value):
        print("2", value)
        value = value * 3
        return super().to_url(value)


app.url_map.converters["re"] = RegexConverter

app.add_url_rule(rule='/test_1_copy', endpoint='test_1_copy', view_func=test_1)


@app.route(r"/test_re/<re('\d+'):value>")
def test_re(value):
    print("index", value)
    return 'Index'


if __name__ == '__main__':
    with app.test_request_context():
        print("url_for", url_for("index", value=123))
        print(url_for("test_1"))
        print(url_for("test_1_copy"))
        print(url_for('test_2'))
        print(url_for('test_3_endpoint'))

        print(url_for('test_1', next='/'))
        print(url_for('test_1', username='username'))

    client = app.test_client()
    print("test_1", client.get("/test_1/123").data)
    print("test_2", client.get("/test_2/qwe").data)
    print("test_3", client.get("/test_3/123").data)
    print("test_4", client.get("/test_4/1.23").data)
    print("test_5", client.get("/test_5/1/2/3").data)
    print("test_6", client.get("/test_6/d0248364-b3ec-481e-a725-2846c6e72576").data)
