from flask import Flask, jsonify
from .auth import auth_bp
from .scraper import scraper_bp


app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(scraper_bp, url_prefix="/scraper")


@app.route("/")
def read_root():
    return jsonify(message="Sigem 2.0 backend")
