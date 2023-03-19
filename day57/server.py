from flask import Flask
from flask import render_template
import datetime
import requests

app = Flask(__name__)

GENDERIZE_API_URL = "https://api.genderize.io/?name="
AGE_API_URL = "https://api.agify.io/?name="
NPOINT_API_URL = "https://api.npoint.io/6ed5e058357ebbb63f4c"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/guess/<name>')
def guess(name):
    gender = requests.get(GENDERIZE_API_URL + name).json()
    age = requests.get(AGE_API_URL + name).json()

    print(gender['gender'])
    print(age['age'])
    return render_template('index.html', age=age['age'], gender=gender['gender'], name=name)


@app.route('/blog')
def blog():
    blog_posts = requests.get(NPOINT_API_URL).json()
    return render_template('blog.html', blog_posts=blog_posts)


@app.route('/blog/<num>')
def get_blog(num):
    blog_posts = requests.get(NPOINT_API_URL).json()
    post = blog_posts[int(num)]
    return render_template('get-blog.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)
