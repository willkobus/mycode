#!/usr/bin/python3
"""Alta3 APIs and HTML"""


from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

answer = "ajax"

app = Flask(__name__)
#correct answer route
@app.route("/correct/<answer>")
def correct(answer):
    return f"That's right! {answer.title()} was the correct answer!\n"
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("day9warmuptemplate.html") # look for tday9warmuptemplate.html

@app.route("/wrong") # redirect for wrong answers
def wrong():
    return render_template("day9warmWrongAnstemplate.html") # look for day9warmWrongAnstemplate.html

@app.route("/answer", methods = ["POST", "GET"])
def login():
    
    if request.method == "POST":
        if request.form.get("nm"): 
            user_answer = request.form.get("nm") 
            if user_answer.lower() == answer:
                return redirect(url_for("correct", answer = user_answer)) 
            else:
                return redirect(url_for("wrong"))
        else:
            return redirect(url_for("start"))
    
    elif request.method == "GET":
        if request.args.get("nm"): 
            user_answer = request.args.get("nm") 
        else: 
            user_answer = "defaultuser"
    
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application