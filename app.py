from flask import Flask,render_template,request

app = Flask(__name__)
db={'asd':'123','sed':'234','bob':'345','Hawlk':'456'}
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
        elif pwd != cpwd:
            print('Passwords do not match....enter again')
        
    return render_template("hello.html")
@app.route("/Login",methods=('GET','POST'))
@app.route("/",methods=('GET','POST'))
def default1():
    if request.method =='POST':
        uname=request.form.get('name')
        pwd=request.form.get('pwd')
        if uname in db:
            print('Username is taken')
        elif uname=='' or pwd=='':
            print('Empty password or username')
        
    return render_template("Login.html")