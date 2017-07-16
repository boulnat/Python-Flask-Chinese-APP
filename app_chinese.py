# -*- coding: utf-8 -*-
"""
Boulet Nathan

"""
from flask import Flask, flash, render_template, request, session, redirect, url_for
import os, random, time, pygame

pygame.mixer.init()
path = "E:\MUSIC\pinyin"
#path = os.path.join(os.getcwd(),os.listdir(os.getcwd())[1])
initial_tab = [("b","p"),("m","f","n","l"),("d","t"),("z","c","s"),("zh","ch","sh","r"),("j","q","x"),("g","k","h")]

class pinyin:
    def __init__(self,path = "E:\MUSIC\pinyin"):
        print("in class pinyin")
        self.path = path
        self.extension = ".mp3"
        self.listPinyin = [pinyin[:-4] for pinyin in os.listdir(self.path)]
        self.randomList = self.listPinyin
        random.shuffle(self.randomList)
        self.tabInitiales = [("b","p"),("m","f","n","l"),("d","t"),("z","c","s"),("zh","ch","sh","r"),("j","q","x"),("g","k","h")]
        self.tableSoundPath=[]
        
    def getRandomListPinyin(self, size):
        return [randomTablePinyin for randomTablePinyin in self.randomList[0:size]]

    def getListPinyin(self, size):
        return [tablePinyin for tablePinyin in self.listPinyin[0:size]]

    def getSoundPath(self, tableSound):
        return [os.path.join(self.path, sound + self.extension) for sound in tableSound]

class initialesQuestions:
    def __init__(self,tabInitiales):
        self.tabInitiales=tabInitiales
    def showInitiales(self):
        tmpTab=[]
        for valueInitiale in self.tabInitiales:
            if valueInitiale[0:2] in ("zh","ch","sh"): #détermine si le mot commence par des initiales composés
                tmpTab.append(valueInitiale[2:]) #selection sans les 2 premiers caractere
            else:
                tmpTab.append(valueInitiale[1:]) #selection sans le 1er caractere
        return tmpTab
    
app = Flask(__name__)
app.secret_key = os.urandom(12)
"""
class questions:
    def __init__(self, number)
        self.number = number
    
    def setNumber(self, number):
        self.number = number
        
    def getNumber(self):
        return self.number

class createInitiales(questions):
    def __init__(self, number):
        questions.__init__(self, number)
        
    def numberEx():
        return random.sample(range(100),self.getNumber())      #initialise des valeurs pour l'exercices
"""
@app.route("/")
def main():
    return render_template("index.html")
    
@app.route('/initiales', methods=['POST','GET'])
def initiales(valeur=None, result=None, vue=True):
    bonne_reponse = 0
    NUM_OF_EX = 5
    
    myPinyin = pinyin()
    myPinyinList = myPinyin.getRandomListPinyin(NUM_OF_EX)
    myPinyinPath = myPinyin.getSoundPath(myPinyinList)
    myInitiales = initialesQuestions(myPinyinList)
    
    #####
    string_value =  []
    index=0
    if request.method == 'POST':
        print(request.form.to_dict())
        print(myPinyinList)
        while index < len(myPinyinList):
            if myPinyinList[index] == request.form.to_dict(str(myPinyinList[index])):
                bonne_reponse+=1 #increment des bonnes répones pour le score final
            else:
                print("ok")
            index+=1
            string_value=(request.form)
        print(bonne_reponse)
        return render_template("answers.html",result=request.form)
       
    return render_template('initiales.html',valeur=myInitiales.showInitiales())

@app.route("/answers")
def answers():
    return render_template("answers.html")

if __name__ == "__main__":
    app.run(debug=True)    

