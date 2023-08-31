from flask import Flask,render_template,request

app = Flask(__name__)
Existing_unames=['asd','sed','bob','Hawlk']
@app.route("/register",methods=('GET','POST'))
def default():
    if request.method =='Post':
        uname=request.form.get('name')
        pwd=request.form.get('pwd')
        cpwd=request.form.get('cpwd')
        if uname in Existing_unames:
            print('Username is already taken')
        elif uname not in Existing_unames:
            Existing_unames.append(uname)
        elif pwd==cpwd:
            print('Registered successfully')
        elif pwd != cpwd:
            print('Passwords do not match....enter again')
        
    return render_template("hello.html")