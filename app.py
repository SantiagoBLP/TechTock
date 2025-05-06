from flask import Flask, redirect, request
import os
import requests

app = Flask(__name__)

# Variables de entorno
APP_ID = os.getenv("TIKTOK_APP_ID")
APP_SECRET = os.getenv("TIKTOK_APP_SECRET")
REDIRECT_URI = os.getenv("TIKTOK_REDIRECT_URI")

@app.route("/")
def home():
    return '''
        <h2>TechTockSync backend is working!</h2>
        <a href="/auth">Connect to TikTok Shop</a>
    '''

@app.route("/auth")
def auth():
    auth_url = (
        "https://auth.tiktok-shops.com/oauth/authorize"
        f"?app_id={APP_ID}&state=init&redirect_uri={REDIRECT_URI}&response_type=code"
    )
    return redirect(auth_url)

@app.route("/tiktok/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "No code provided", 400

    token_url = "https://auth.tiktok-shops.com/api/token"
    payload = {
        "app_id": APP_ID,
        "app_secret": APP_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
    }
    response = requests.post(token_url, json=payload)
    return response.json()
