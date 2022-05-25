#!/usr/bin/python3
""" Will's RPG Game """
import requests
import os
import time
import roomLogic as rl
import moves
import rooms

# clears console when called
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Greets player when game is ran
def showGreeting():
    print("Welcome to Will's Game\n")
    time.sleep(1)
    print("*distant disembodied voice*")
    time.sleep(2)
    print("Adventurer? Hello? ADVENTURER!!!!")
    time.sleep(2)
    print("You're awake! Phew...the past few weren't so, actually nevermind. Here's the deal, you are trapped in this house and there are two keys you need to get to leave.\nIs it formulaic? Obviously but it's my game so...deal with it. Good luck! I'm rooting for you! Also rooting for the Grue. Oh ya, there are grue here. Do with that information what you will.")
    time.sleep(2)
    print("")

def showInstructions():
  #print a main menu and the commands
  print('''
Commands:
  go [direction]
  get [item]
  shoot [grue name]
''')


def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  print(rooms[currentRoom]['description'])
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print(f"The item(s) you see in the room: {rooms[currentRoom]['item']} ")
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

rooms = rooms.rooms

#start the player in the Hall
currentRoom = 'Hall'

cls()
showGreeting()

#loop forever
while True:

    time.sleep(.5)   
    showStatus()
    showInstructions()

    #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
    move = ''
    while move == '':
        move = input('>')
        cls()

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    
    # move execution
    if move[0] == 'go':
        currentRoom = moves.go(move, rooms, currentRoom)
    if move[0] == 'get':
        moves.get(move, rooms, currentRoom, inventory)
    if move[0] == 'shoot':
        moves.shoot(move, rooms, currentRoom, inventory)

    ## Specific Room Conditions
    if currentRoom == 'Garden':
        end = rl.garden(inventory, rooms, currentRoom)
        if end == "game over":
            break
    if currentRoom == 'Animal Pen':
        end = rl.animalPen(inventory, rooms, currentRoom)
        if end == "game over":
            break
    if currentRoom == 'Beat Lab':
        rl.beatLab(inventory, rooms, currentRoom)

    if currentRoom == 'Exit':
        rl.exit(inventory, rooms, currentRoom)
        if end == "game over":
            break

