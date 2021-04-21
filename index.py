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
    number = str(Calc.add(10, 25))
    return number


app.run()
