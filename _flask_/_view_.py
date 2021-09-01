from flask import \
    Flask, \
    views, \
    request, \
    jsonify

app = Flask(__name__)


class IndexView(views.MethodView):

    def get(self):
        return 'get'


app.add_url_rule('/', view_func=IndexView.as_view('index'))

if __name__ == '__main__':
    app.run()
