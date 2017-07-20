# -*- coding: utf-8 -*-
"""
Boulet Nathan

"""

from flask import Flask, flash, render_template, request, session, redirect, url_for
import os, random, time

class pinyin:
    def __init__(self,path = "static/music"):
        self.path = path
        self.extension = ".mp3"
        self.listPinyin = [pinyin[:-4] for pinyin in os.listdir(self.path)]
        self.randomList = self.listPinyin
        self.tabInitiales = [("b","p"),("m","f","n","l"),("d","t"),("z","c","s"),("zh","ch","sh","r"),("j","q","x"),("g","k","h")]
        self.tableSoundPath=[]
        
    def setRandomListPinyin(self):
        random.shuffle(self.randomList)
    
    def getRandomListPinyin(self, size):
        return [randomTablePinyin for randomTablePinyin in self.randomList[0:size]]

    def getListPinyin(self, size):
        return [tablePinyin for tablePinyin in self.listPinyin[0:size]]

    def getSoundPathCorrection(self, tableSound):
        tmpTab={}
        for sound in tableSound:
            if sound != "":
                try:
                     tmpTab.update({sound : os.path.join(self.path, sound + self.extension)})
                except:
                    print("error no sound found for" + os.path.join(self.path, sound + self.extension))
        return tmpTab

    def getSoundPath(self, tableSound):
        return [os.path.join(self.path, sound + self.extension) for sound in tableSound]
    
app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route("/")
def main():
    return render_template("index.html")
    
@app.route('/initiales', methods=['POST','GET'])
def initiales(valeur=None, result=None, vue=True,musicFiles=None):
    bonne_reponse = 0
    NUM_OF_EX = 5
    string_value =  []
    index=0

    myPinyin.setRandomListPinyin()
    myPinyinList = myPinyin.getRandomListPinyin(NUM_OF_EX)
    myPinyinPath = myPinyin.getSoundPath(myPinyinList)
    myInitiales = myPinyinList

    if request.method == 'POST':
        myPinyinList = []
        myPinyinPath = []
        for question in request.form.to_dict():
            myPinyinList.append(request.form.to_dict()[question])
            myPinyinList.append(question)

            if request.form.to_dict()[question] == question:
                bonne_reponse+=1 #increment des bonnes répones pour le score final
            index+=1
            string_value=(request.form)
        myPinyinPath = myPinyin.getSoundPathCorrection(myPinyinList)
        return render_template("answers.html",corection=request.form,result=bonne_reponse,musicFiles=myPinyinPath)    
    return render_template('initiales.html',valeur=myInitiales,musicFiles=myPinyinPath)

@app.route("/answers")
def answers(result=None):
    return render_template("answers.html")

if __name__ == "__main__":
    myPinyin = pinyin()
    app.run(debug=True)    

