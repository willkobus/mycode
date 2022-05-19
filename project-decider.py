#!/usr/bin/env python3

name = input("Enter name that you would like to be called!\n>")

print("Welcome to the project decider app!\n")
student = input("Are you a python student being forced by omnipotent instructor to create code that tests your skills with python conditional statements? (this is where you type 'yes' or 'no')\n>")

if student.lower() == "yes":
    print(f"Well you are in luck, {name}! In just 10 questions we will find a project that will knock the socks off your classmates!")

elif student.lower() == "no":
    print(f"Well then what the heck are you doing here then, {name}? You dont have to go home but you can't stay here...")

else:
    print(f"Are you kidding me, {name}? That was not yes or no. In fact it may have even been gibberish!. Good day. I said Good Day!!!!")
