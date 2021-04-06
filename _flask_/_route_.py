from flask import Flask, url_for, Blueprint, request

app = Flask(__name__)


# https://dormousehole.readthedocs.io/en/latest/blueprints.html

@app.route('/')
def test_1():
    return 'test_1'


app.add_url_rule(rule='/test_1_copy', endpoint='test_1_copy', view_func=test_1)


@app.route('/test_2')
def test_2():
    return "test_2"


@app.route('/test_3', endpoint='test_3_endpoint')
def test_3():
    return "test_3"


from flask import Flask
from flask import url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super().__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        print("1", value)
        value = int(value) * 2
        return super().to_python(value)

    def to_url(self, value):
        print("2", value)
        value = value * 3
        return super().to_url(value)


app.url_map.converters["re"] = RegexConverter


@app.route(r"/<re('\d+'):value>")
def index(value):
    print("index", value)
    return 'Index'


if __name__ == '__main__':
    with app.test_request_context():
        print("url_for", url_for("index", value=123))
    # app.run()


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for("test_1"))
        print(url_for("test_1_copy"))
        print(url_for('test_2'))
        print(url_for('test_3_endpoint'))

        print(url_for('test_1', next='/'))
        print(url_for('test_1', username='username'))
