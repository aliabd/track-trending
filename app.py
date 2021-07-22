from flask import Flask, request, render_template
from flask_mail import Mail, Message
import requests

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='githubtrendingtracker@gmail.com',
    MAIL_PASSWORD='github123',
))

mail = Mail(app)

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
    if trending:
        msg = Message("Gradio is trending on Github!",
                      sender="ali.si3luwa@gmail.com",
                      recipients=["ali.si3luwa@gmail.com"])
        mail.send(msg)
    return render_template("index.html", trending=trending)

