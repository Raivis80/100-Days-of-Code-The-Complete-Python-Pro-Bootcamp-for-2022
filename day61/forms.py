from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8)])
    submit = SubmitField('Login')

