# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, flash, render_template, request, session
import os

app = Flask(__name__)

@app.route("/")
def main(name="Unknown"):
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return render_template('index.html', name=name)

@app.route("/login", methods=["POST"])
def login():
    if request.method == 'POST':
        if request.form["username"] == "boulnat" or request.form["password"] == "boulnat":
            session["logged_in"] = True
            loggedInName = "boulnat"
        else:
             print ("error")
        return main(name=loggedInName)          

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return main()

@app.route("/singUp")
def signUp():
    return render_template('signup.html')

@app.route('/initiales')
def initiales():
    return render_template('initiales.html')

@app.route('/finales')
def finales():
    return render_template('finales.html')

@app.route('/tons')
def tons():
    return render_template('tons.html')

@app.route('/statistiques')
def statistiques():
    return render_template('statistiques.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)    