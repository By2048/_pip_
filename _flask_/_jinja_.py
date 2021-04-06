from flask import Flask, render_template, Markup

app = Flask(__name__)
app.template_folder = "."
app.static_folder = "."
app.debug = True


@app.route("/")
def test():
    return render_template("_jinja_.html", name=123)


app = Flask(__name__)
app.template_folder = "."
app.debug = True


@app.template_global()
def test1(a, b):
    return f"{a} {b}"


@app.template_global()
def test11(a, b, c):
    return f"{a} {b} {c}"


@app.template_filter()
def test2(a, b):
    return f"{a} {b}"


@app.route("/")
def index():
    return render_template("_jinja_.html")


if __name__ == '__main__':
    app.run()
