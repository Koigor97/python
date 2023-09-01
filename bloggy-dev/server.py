from flask import Flask, render_template
import requests

app = Flask(__name__)

agify = "https://api.agify.io?name="
genderfy = "https://api.genderize.io?name="

def get_data(url, user):
    response = requests.get(f"{url}{user}")
    response.raise_for_status()
    data = response.json()
    return data

@app.route("/<name>")
def home(name):
    age = get_data(url=agify, user=name)["age"]
    gender = get_data(url=genderfy, user=name)["gender"]
    return render_template("index.html", age=age, gender=gender, user=name)


