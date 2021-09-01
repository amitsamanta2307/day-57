from flask import Flask, render_template
from datetime import datetime
import random
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url="https://api.agify.io/", params={'name': name})
    response.raise_for_status()
    age_data = response.json()
    age = age_data['age']

    response = requests.get(url="https://api.genderize.io/", params={'name': name})
    response.raise_for_status()
    gender_data = response.json()
    gender = gender_data['gender']

    return render_template('guess.html', name=name.title(), gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)
