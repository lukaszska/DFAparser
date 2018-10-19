from flask import Flask, render_template, request

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


@app.route('/server', methods=['GET', 'POST'])
def parse_request():
    data = request.data
    return data.form


if __name__ == "__main__":
    app.run(debug=True)
