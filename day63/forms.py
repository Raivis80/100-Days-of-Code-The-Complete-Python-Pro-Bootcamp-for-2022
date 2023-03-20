from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = SelectField('Rating', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])


    submit = SubmitField('Submit')