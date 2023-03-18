from flask import Flask
from speed_cals_decorator import main

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>{}</p>".format(main())


@app.route("/bye")
def bye():
    return "<h1>Bye</h1>"


if __name__ == "__main__":
    app.run(debug=True)