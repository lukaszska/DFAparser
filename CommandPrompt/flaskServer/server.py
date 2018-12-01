from flask import Flask
from flask import render_template
from flask import request
from dfa_class_system import DFA
from regexEnumArgs import get_information
import json

app = Flask(__name__)
dfas = {}   #   key: IP, Value: DFA


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<name>')
def user(name):
    return render_template("user.html", name=name)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.remote_addr not in dfas:
            dfas[request.remote_addr] = DFA()
        dfas[request.remote_addr].tuple_reader(get_information(request.form['script']))
        print(type(dfas[request.remote_addr]))
        return json.dumps(dfas[request.remote_addr].dfa_dict)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
