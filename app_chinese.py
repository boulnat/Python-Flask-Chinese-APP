# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, flash, render_template, request, session
import os, random

app = Flask(__name__)
app.secret_key = os.urandom(12)

tab=[]

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

@app.route('/initiales', methods=['GET', 'POST'])
def initiales(valeur=None, result=None, vue=True):
    tab=random.sample(range(100),4)
    count=len(tab)
    tabResult=[]
    i=0
    if request.method == 'POST':
        while i < count-1:
            if request.form[str(tab[i])] == tab[i]:
                tabResult.append("ok")
            else:
                tabResult.append(goodRequest)
            i+=1
        return render_template("initiales.html",result=tabResult,vue=False) 
    return render_template('initiales.html',valeur=tab,vue=True)

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
    app.run(debug=True)    
