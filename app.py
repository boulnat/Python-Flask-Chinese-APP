# -*- coding: utf-8 -*-
"""
Boulet Nathan

"""

from flask import Flask, flash, render_template, request, session, redirect, url_for
import os, random, time 
import pinyin as pi
import pinyin.cedict as pc
import itertools

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
    def getSound(self, sound):
        return os.path.join(self.path, sound + self.extension)

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route("/")
def main():
    return render_template("index.html")
@app.route("/stroke", methods=['POST','GET'])
def stroke():
    sound=""
    textPinyin=""
    if request.method == 'POST':
      text = request.form['text']
      textPinyin = pi.get(text,format="numerical", delimiter=" ")
      sound = myPinyin.getSound(textPinyin)
      print(str(sound))
    return render_template('stroke.html', sound=sound, textPinyin=textPinyin, text=text)

@app.route("/translation", methods=['POST','GET'])
def translation():
    words = []
    newwords = []
    text = ""
    textPinyin = ""
    if request.method == 'POST':
        text = request.form['text']
        textPinyin = pi.get(text, delimiter=" ")
        words = list(pc.all_phrase_translations(text))    
        for item in words:
            if item not in newwords:
                newwords.append(item)
        #words.sort()
        #newwords = list(words for words,_ in itertools.groupby(words))
        for a in newwords:
            a.insert(1,pi.get(a[0], delimiter=" ")) 
    return render_template('translation.html', newwords=newwords, text=text, textPinyin=textPinyin)
 
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

@app.route('/finales', methods=['POST','GET'])
def finales(valeur=None, result=None, vue=True,musicFiles=None):
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
    return render_template('finales.html',valeur=myInitiales,musicFiles=myPinyinPath)

@app.route('/tons', methods=['POST','GET'])
def tons(valeur=None, result=None, vue=True,musicFiles=None):
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
    return render_template('tons.html',valeur=myInitiales,musicFiles=myPinyinPath)

@app.route('/fullword', methods=['POST','GET'])
def fullword(valeur=None, result=None, vue=True,musicFiles=None):
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
    return render_template('fullword.html',valeur=myInitiales,musicFiles=myPinyinPath)

@app.route("/answers")
def answers(result=None):
    return render_template("answers.html")

if __name__ == "__main__":
    myPinyin = pinyin()
    app.run(debug=True,host='0.0.0.0')    

