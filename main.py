#need to: work on error/exception handling

from flask import Flask
from flask import render_template, request
from news import search

app = Flask(__name__)

images = dict(business = "https://imageio.forbes.com/blogs-images/alejandrocremades/files/2018/07/desk-3139127_1920-1200x773.jpg?format=jpg&width=960", technology = "https://www.onlinetoolsexpert.com/wp-content/uploads/2020/08/Technology-news.jpg", entertainment = "https://kstp.com/kstpImages/800EntertainmentNewsGfx.jpg", health = "https://www.mobihealthnews.com/sites/default/files/world%20health.jpg", sports = "https://ak.picdn.net/shutterstock/videos/29587630/thumb/3.jpg")

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/results', methods = ["GET", "POST"])
def results():
  if request.method == "POST":
    q = request.form["search_term"]
    category = request.form["search_category"].lower()
    results = search(q, category)
    return render_template("results.html", q = q, category = category, results = results, default_images = images)

app.run(host = "0.0.0.0", port = 81, debug = True)