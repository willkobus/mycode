#!/usr/bin/python3
""" Will's RPG Game """
import requests
import os
import time
import roomLogic as rl
import moves

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

## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'description' : '''The hall is the hub of the house. Centrally located it has direct access the Closet (north), Dining Room (east), Kitchen (south), and the Beat Lab (west)''',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west' : 'Beat Lab',
                  'north' : 'Closet',
                  'item'  : ['big gun']
                },

            'Kitchen' : {
                  'description' : '''Ah, the Kitchen. Who wants snacks? Not hungry? No Worries. The kitchen has access to the Hall (north), the Basement (west), the Garden (east), and the oh so wonderful Exit (south).''',
                  'north' : 'Hall',
                  'west' : 'Basement',
                  'east' : 'Garden',
                  'south' : 'Exit',
                  'item'  : ['banana'],
                },
            'Dining Room' : {
                'description' : '''Ye olde Dining Room! Home of the dinner table and where fancy parties are held. The Dining Room has access to the Hall (west), the Pantry (north), the Animal Pen (east), and the beautiful Garden (south).''',
                  'west' : 'Hall',
                  'south': 'Garden',
                  'east' : 'Animal Pen',
                  'north' : 'Pantry',
                  'item' : ['rocking chair'],
               },
            'Garden' : {
                  'description' : '''Plants, flowers, and the occasional grue, welcome to the Garden. The Garden has access to the Dining Room (north) and the Kitchen (west).''',
                  'north' : 'Dining Room',
                  'west': "Kitchen",
                  'item' : [],
                  'monster' : ['elmer grue']
               },
            'Pantry' : {
                  'description' : '''The Pantry, AKA where the food lives. Be polite and remove your shoes. The Pantry has access to the Dining Room (south).''',
                  'south' : 'Dining Room',
                  'item' : ['banana'],
            },

            'Beat Lab' : {
                'description' : '''You hear that? The sound of the bass? The rantings of rapper gone mad? This is the Beat Lab. The Beat Lab has access to The Office (north), the Basement (south), and the Hall (east).''',                  
                  'south': 'Basement',
                  'east' : 'Hall',
                  'north' : 'Office',
                                    
            },
            'Office' : {
                'description' : '''There may be no Jim or Pam but its got the \"old book smell\" you all know and love. The Office has access to the Beat Lab (south).''',
                'south' : 'Beat Lab',
                'item' : ['translator']
            },
            'Closet' : {
                'description' : '''It\'s like the Pantry...but for clothes and junk you want to hide before your parents come over. The Closet has access to the Hall (south).''',
                'south' : 'Hall',
                'item' : ['overalls']
            },
            'Animal Pen' : {
                'description' : '''Doesn\'t every house have an animal pen? No? Well this one does. The Animal Pen has access to the Dining Room (west).''',
                'west': 'Dining Room',
                'item' : [],
                'monster' : ['gorilla grue']
            },
            'Exit' : {
                'description' : '''This is where you leave, if the grues don\'t get you first. Need to get those keys though. The Exit has access to the Kitchen (north).''',
                'north' : 'Kitchen'
            },
            'Basement' : {
                'description' : '''The Basement. It\'s cold, dark, and for some reason is where we store the grain seeds. The Basement has access to the Beat Lab (north) and the Kitchen (east).''',
                'north' : 'Beat Lab',
                'east' : 'Kitchen',
                'item' : ['corn seeds']
            }
         }

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

