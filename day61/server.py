from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import LoginForm

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        if email != 'rapet80@gmail.com' or password != '12345678':
            return render_template('denied.html')
        else:
            return render_template('success.html')

    return render_template('login.html', form=login_form)


if __name__ == "__main__":
    app.secret_key = "secret_key"
    app.config['SESSION_TYPE'] = 'filesystem'
    Bootstrap(app)

    app.run(debug=True)