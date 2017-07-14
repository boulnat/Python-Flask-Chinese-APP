# -*- coding: utf-8 -*-
"""
Boulet Nathan

"""
from flask import Flask, flash, render_template, request, session, redirect, url_for
import os, random

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route("/")
def main():
    return render_template("index.html")
    
@app.route('/initiales', methods=['POST','GET'])
def initiales(valeur=None, result=None, vue=True):
    initiale_q=None
    initiale_q=random.sample(range(100),2)      #initialise des valeurs pour l'exercices
    string_value =  []
    i=1
    if request.method == 'POST':
        #while i <= len(initiale_q):
        #for v in request.form:
        #    for a in v:
        #        key, ans = v, a
        #        string_value[key] = ans
        string_value=(request.form)
        #    i=i+1
        #return redirect(url_for('answers',result=string_value))
        return render_template("answers.html",result=string_value)

    return render_template('initiales.html',valeur=initiale_q)

@app.route("/answers")
def answers():
    return render_template("answers.html")

if __name__ == "__main__":
    app.run(debug=True)    

