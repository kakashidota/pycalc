from flask import Flask

app = Flask(__name__)


class Calc:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

@app.route("/")
def home():
    return "hello"


@app.route("/add")
def add():
    number = str(Calc.add(10, 25))
    return number

@app.route("/sub")
def sub():
    number = str(Calc.add(10, 25))
    return number


app.run()
# py -m pip freeze > requirements.txt // Fixar en req
# py -m flake8 --statistics //linter
# py -m pip install flake8 pytest pytest-cov flask// paket som behövs
# pytest -v --cov kör tester