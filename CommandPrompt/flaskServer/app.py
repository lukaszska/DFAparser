from flask import Flask
from flask import render_template
from flask import request
from dfa_class_system import DFA
from regexEnumArgs import get_information
import json

app = Flask(__name__)
users = {}   #   key: IP, Value: DFA


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<name>')
def user(name):
    return render_template("user.html", name=name)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.remote_addr
        if user not in users:
            users[user] = DFA()
        users[user].tuple_reader(get_information(request.form['script']))
        print(users[user].dfa_dict)
        output = json.dumps(users[user].dfa_dict)
        users[user].dfa_dict['result'] = None
        return output
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
