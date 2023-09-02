from flask import Flask, render_template,request
app = Flask(__name__)
db={"sathish":"12345","ragul":"ragul@123","sanjay":"sanjaymani"}
@app.route("/register",methods=('GET','POST'))
def cric():
    if request.method =='POST':
        username=request.form.get('name')
        password=request.form.get('password')
        if username in db:
            if password == db[username]:
                print("login successful")
            else:
                print("login unsuccessful")
        else:
            print("login unsuccessful")
    return render_template('hello.html')
