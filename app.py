from flask import Flask,render_template
from database import database

app = Flask(__name__)

@app.route("/")
def default():
    return render_template("hello.html")
