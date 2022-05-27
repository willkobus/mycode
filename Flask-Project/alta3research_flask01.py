#!/usr/bin/python3
"""JSON Flask App"""


from flask import Flask
from flask import jsonify
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

herodata= [{
   "name": "Deadpool",
   "realName": "Wade Wilson",
   "alsoKnown" : "Merc With a Mouth",
   "since": "Dec, 1990",
   "powers": [
      "foreign chemical resistance",
      "healing factor",
      "disease Immunity",
      "super human strength, agility, reflexes, stamina, and durability"
            ],
   "abilities": [
      "master martial artist",
      "master assassin",
      "multilingual",
      "knows he is a fictional character",
      "unpredictable"
            ],
   "weaknesses" : [
      "volatile mental state",
      "being so annoying even allies hate him",
      "fear of cows, being alone, and possibly chickens"
            ]
            }]

@app.route("/")
def home():
    return render_template("deadpoolfacts.html", dname = None, drealName = None, dAka = None, dsince = None, dpowers = None, dabilities = None, dweaknesses = None)

@app.route("/deadpooljson")
def factsAsJson():
   deadpoolJson = jsonify(herodata)
   return deadpoolJson

@app.route("/deadpooljinja")
def factsAsJinja():
   name = herodata[0]['name']
   realName = herodata[0]['realName']
   alsoKnown = herodata[0]['alsoKnown']
   since = herodata[0]['since']
   powers = herodata[0]['powers']
   abilities = herodata[0]['abilities']
   weaknesses = herodata[0]['weaknesses']

   return render_template("deadpoolfacts.html", dname = name, drealName = realName, dAka = alsoKnown, dsince = since, dpowers = powers, dabilities = abilities, dweaknesses = weaknesses)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application