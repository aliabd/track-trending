from flask import Flask, request, render_template
import requests

app = Flask(__name__)

URLS = {'daily': 'https://trendings.herokuapp.com/repo?lang=python&since=daily',
         'weekly': 'https://trendings.herokuapp.com/repo?lang=python&since=weekly',
         'monthly': 'https://trendings.herokuapp.com/repo?lang=python&since=monthly'
         }


def trending_github(url):
    response = requests.get(url).json()
    repos = [response["items"][i]["repo"] for i in range(len(response["items"]))]
    return 'gradio-app/gradio' in repos


@app.route("/")
def index():
    trending = [interval for interval in URLS if trending_github(URLS[interval])]
    return render_template("index.html", trending=trending)

