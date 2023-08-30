from flask import Flask,render_template

app = Flask(__name__)

@app.route("/register")
def default():
    return render_template("hello.html")

