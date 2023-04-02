from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

API_KEY = os.environ.get("API_KEY")
READ_ACCESS_TOKEN = os.environ.get("READ_ACCESS_TOKEN")
URL = "https://api.themoviedb.org/3/search/movie"


def get_movies_from_tmdb(search_term):
    response = requests.get(url=URL, params={
        "api_key": API_KEY,
        "query": search_term
    })
    data = response.json()["results"]
    return data


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


with app.app_context():
    db.create_all()


##CREATE FORM
class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Submit")


class EditForm(FlaskForm):
    rating = StringField("Rating", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])

    submit = SubmitField("Submit")


##CREATE ROUTES
@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()

    return render_template("index.html", movies=movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        try:
            movie_data = get_movies_from_tmdb(movie_title)[0]
            print(movie_data)
        except IndexError:
            return render_template("add.html", form=form)

        new_movie = Movie(
            title=movie_data["title"],
            year=movie_data["release_date"].split("-")[0],
            description=movie_data["overview"],
            rating=movie_data["vote_average"],
            review="This movie was so cool!",
            img_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
        )

        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
