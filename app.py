from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "TechTockSync backend is working!"

@app.route("/tiktok/callback")
def callback():
    return "OAuth callback URL reached!"
