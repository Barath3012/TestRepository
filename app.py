from flask import Flask, render_template
app = Flask(__name__)
star={"sathish":12345,"ragul":ragul@123,"sanjay":sanjaymani}
@app.route("/login")
def cric():
    return render_template('hello.html')
