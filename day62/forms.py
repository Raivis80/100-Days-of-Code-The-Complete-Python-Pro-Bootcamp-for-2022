from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CafeForm(FlaskForm):
    COFFE_RATINGS = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
    WIFI_RATINGS = ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
    POWER_RATINGS = ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']

    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[(rating, rating) for rating in COFFE_RATINGS])
    wifi_rating = SelectField('Wifi Strength Rating', choices=[(rating, rating) for rating in WIFI_RATINGS])
    power_rating = SelectField('Power Socket Availability', choices=[(rating, rating) for rating in POWER_RATINGS])

    submit = SubmitField('Submit')