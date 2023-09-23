from flask import Flask,render_template,request,redirect,flash
from Database import database
app = Flask(__name__)
app.secret_key='millie'
db=database('db.txt')
@app.route("/Register",methods=('GET','POST'))
def default():
    if request.method =='POST':
        uname=request.form.get('name')
        pwd=request.form.get('pwd')
        cpwd=request.form.get('cpwd')
        if pwd==cpwd:
            if uname in db:
                print('Username is already taken')
                flash('Username is already taken')
            elif uname not in db:
                db[uname]=pwd
                print('Registered successfully')
                print(db)
                database('db.txt','w',username=uname,password=pwd)
                flash('Registered successfully!!')
        elif pwd != cpwd:
            print('Passwords do not match....enter again')
            flash('Passwords do not match....enter again')
        elif pwd=='' or cpwd=='' or uname=='':
            print('Empty password or username')
            flash('Empty password or username')

    return render_template("Register.html")
@app.route("/")
def home():
    return redirect("/Login")

@app.route("/Login",methods=('GET','POST'))
def default1():
    if request.method =='POST':
        uname=request.form.get('name')
        pwd=request.form.get('pwd')
        if uname in db and db.get(uname)==pwd:
            print('Logged in successfully')
            flash('Logged in successfully!!')
        elif uname=='' or pwd=='':
            print('Empty password or username')
            flash('Empty password or username')
        elif uname not in db or db.get(uname)!=pwd:
            print('username or password do not match')
            flash('username or password do not match')

        
    return render_template("Login.html")