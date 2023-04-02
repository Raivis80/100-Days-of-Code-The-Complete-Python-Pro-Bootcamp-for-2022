from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])

    submit = SubmitField("Done")


class AddForm(FlaskForm):
    id = StringField("Movie ID", validators=[DataRequired()])
    title = StringField("Movie Title", validators=[DataRequired()])
    year = StringField("Movie Year", validators=[DataRequired()])
    description = StringField("Movie Description", validators=[DataRequired()])
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    ranking = StringField("Your Ranking", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    img_url = StringField("Movie Image URL", validators=[DataRequired()])
    submit = SubmitField("Add Movie")
