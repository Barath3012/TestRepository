from flask import Flask,render_template, request, flash
from database import database

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

params = {
    "var1":"sabesh",
    "var2":"barath",
    "var3": {
        "barath":1234
             }
          }

@app.route("/",methods=["GET","POST"])
def default():
    if request.method == "POST":
        name = request.form.get("name")
        flash("Welcome, "+name)

    return render_template("hello.html",params=params)
