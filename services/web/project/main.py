# import basics
import os

from dotenv import load_dotenv
# import stuff for our web server
from flask import Flask, render_template, send_from_directory

load_dotenv()

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STATIC_FOLDER'] = f"{os.getenv('APP_FOLDER')}/project/static"

app.config["UPLOAD_FOLDER"] = f"{os.getenv('APP_FOLDER')}/project/static/uploads"
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024


# set up the routes and logic for the webserver
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)

