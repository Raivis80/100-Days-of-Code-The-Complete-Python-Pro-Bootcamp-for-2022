from flask import Flask, render_template, request, redirect, flash, url_for
import requests
import smtplib
import os

EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
SECRET_KEY = os.environ.get("SECRET_KEY")

posts = requests.get("https://api.npoint.io/6ed5e058357ebbb63f4c").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="rp42dev@gmail.com", password=EMAIL_PASSWORD)
            connection.sendmail(from_addr=email, to_addrs="rp42dev@gmail.com",
                                msg=f"Subject:Blog Contact Form \n\n Name: {name} \n Email: {email} \n Phone: {phone} \n Message: {message}")
            connection.sendmail(from_addr="rp42dev@gmail.com", to_addrs=email,
                                msg=f"Subject:Blog Contact Form \n\n Thank you for contacting me. I will get back to you soon.")

        flash(f"Thanks for contacting us {name}! We will get back to you soon.", "success")
        return redirect(url_for('contact'))
    return render_template("contact.html")


if __name__ == "__main__":
    app.secret_key = SECRET_KEY
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)
