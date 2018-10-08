from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/<name>')
def user(name):
    return render_template("user.html", name=name)


@app.route('/index')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
