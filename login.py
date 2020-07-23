from flask import Flask, request, redirect, url_for, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
ids = ['jack', 'adithya', 'tom', 'jill', 'rob','arun']
passwords = [generate_password_hash('jack'), generate_password_hash('adithya'), generate_password_hash('tom'), 
generate_password_hash('jill'), generate_password_hash('rob'),generate_password_hash('arun')]

@app.route('/')
def home():
    return "<h1>Hello</h1>"



@app.route("/login", methods=["GET", "POST"])
def login() :

    if(request.method == "POST") :
        try :
            user = ids.index(request.form['id'])
            if(check_password_hash(passwords[user], request.form['Password']) ==  False) :
                return render_template("wrong.html")
            return render_template("welcome.html")
        except ValueError :
            return render_template("wrong.html")
    
    return render_template("login.html")



if(__name__ == "__main__") :
    app.run()
