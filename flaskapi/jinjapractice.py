#!/usr/bin/python3
"""Alta3 APIs and HTML"""


from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import random

number = random.randint(1,100)
default_guess = -1
guesses = 0


app = Flask(__name__)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("randomnumjinja.html", guess = default_guess)

@app.route("/user-guess/<int:answer>")
def answer(answer):
    return render_template("randomnumjinja.html", guess = answer, correct = number)

@app.route("/user-guess", methods = ["POST"])
def login():    
    if request.form.get("guess"): 
        (user_guess) = int(request.form.get("guess"))
        return render_template("randomnumjinja.html", guess = user_guess, correct = number)              
    else:
        return redirect(url_for("/start"))
    
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application