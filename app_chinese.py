# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/logIn")
def logIn():
    return render_template('login.html')

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
    app.run(debug=True)    