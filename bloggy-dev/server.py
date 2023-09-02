from flask import Flask, render_template
import requests

app = Flask(__name__)

fake_blogs = "https://api.npoint.io/c790b4d5cab58020d391"


def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data

@app.route("/")
def home():
    all_blog = get_data(fake_blogs)
    return render_template("index.html", blogs=all_blog)


