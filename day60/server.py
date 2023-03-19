from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def receive_data():
    return f"Hello {request.form['name']} {request.form['password']} Ha Ha Ha"


if __name__ == "__main__":
    app.run(debug=True)