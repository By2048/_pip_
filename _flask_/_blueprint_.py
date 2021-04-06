from flask import Flask, url_for, Blueprint, request

app = Flask(__name__)

user = Blueprint("user", __name__, url_prefix="/user")
admin = Blueprint("admin", __name__, url_prefix="/admin")


@user.route('/index')
def index():
    pass


@admin.route('/index')
def index():
    pass


app.register_blueprint(user)
app.register_blueprint(admin)

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('user.index'))
        print(url_for('admin.index'))
