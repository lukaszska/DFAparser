from flask import Flask, render_template, request

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
        return return_string()
    return render_template("index.html")


def return_string():
    return "Hello!"


if __name__ == "__main__":
    app.run(debug=True)
