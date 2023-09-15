from flask import Flask,render_template,request,redirect,flash
from Database import database
app = Flask(__name__)

@app.route("/Register",methods=('GET','POST'))
def default():
    if request.method =='POST':
        uname=request.form.get('name')
        pwd=request.form.get('pwd')
        cpwd=request.form.get('cpwd')
        if pwd==cpwd:
            if uname in db:
                print('Username is already taken')
            elif uname not in db:
                db[uname]=pwd
                print('Registered successfully')
                print(db)
                database('db.txt','w',username=uname,password=pwd)
        elif pwd != cpwd:
            print('Passwords do not match....enter again')
        
    return render_template("Register.html")
@app.route("/")
def home():
    return redirect("/Login")

@app.route("/Login",methods=('GET','POST'))
def default1():
    if request.method =='POST':
        uname=request.form.get('name')
        pwd=request.form.get('pwd')
        if uname in db:
            print('Username is taken')
        elif uname=='' or pwd=='':
            print('Empty password or username')

        
    return render_template("Login.html")