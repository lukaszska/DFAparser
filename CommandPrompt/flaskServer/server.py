from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/<name>')
def user(name):
    return render_template("user.html", name=name)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return return_string(request.form['script'])
    return render_template("index.html")


def return_string(input):
    return "You typed:%s" % input


if __name__ == "__main__":
    app.run(debug=True)
