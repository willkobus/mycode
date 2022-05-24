#!/usr/bin/python3
""" Will's RPG Game """
import requests
import os

# link to kanye west api, KanyeREST
kanye_gibberish = "https://api.kanye.rest/"

# clears console when called
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Greets player when game is ran
def showGreeting():
    print("Welcome to Will's Game")

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
                  'description' : '''The hall is the hub of the house. Centrally located it has direct access the Closet (north), Dining Room (east), Kitchen (south), and the Beat Lap (west)''',
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
                  'item' : []
                  
            },
            'Office' : {
                'description' : '''There may be no Jim or Pam but its got the \"old book smell\" you all know and love. The Office has access to the Beat Lab (south).''',
                'south' : 'Beat Lab',
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

showGreeting()

#loop forever
while True:

    
    
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

  #if they type 'go' first
    if move[0] == 'go':
    #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            i = rooms[currentRoom]['item'].index(move[1])
        #add the item to their inventory
            inventory += [move[1]]
        #display a helpful message
            print(move[1] + ' got!')
        #delete the item from the room
            del rooms[currentRoom]['item'][i]
    #otherwise, if the item isn't there to get
        else:
        #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    #if they type shoot and have the anti grue gun
    if move[0] == 'shoot' :
        if 'big gun' in inventory:
    #if the room contains an item, and the item is the one they want to get
            if "monster" in rooms[currentRoom] and move[1].lower() in rooms[currentRoom]['monster']:
                i = rooms[currentRoom]['monster'].index(move[1])
                           
            #display a helpful message
            print(move[1] + ' is no more!')
            # logic for when the player shoots a grue based on what room they are in
            # has grue drop key as long as key is not in inventory
            if currentRoom == 'Garden' and 'exit key 1' not in inventory:
                print(f"{move[1]} dopped exit key 1!")
                rooms[currentRoom]['item'].append('exit key 1')
            if currentRoom == 'Animal Pen' and 'exit key 2' not in inventory:
                print(f"{move[1]} dopped exit key 2!")
                rooms[currentRoom]['item'].append('exit key 2')
            # deletes monster from monster list
            del rooms[currentRoom]['monster'][i]
            # deletes monster key from current room if all monsters in the room have been defeated 
            if len(rooms[currentRoom]['monster']) == 0:
                del rooms[currentRoom]['monster']
        else:
            # tells player they cannot shoot if no gun in inventory
            print("Cannot shoot, you have no gun")
                

    ## Specific Room Conditions
    
    # Handles garden logic
    if currentRoom == 'Garden':
        reward = 'exit key 1'
        if 'big gun' in inventory and 'translator' not in inventory and rooms[currentRoom].get('monster') != None:
            print(f"{rooms[currentRoom].get('monster')[0].title()} stands before and appears to be saying something!")
            print("Wort Wort Wort!!!")
            print("Without a translator you have no idea what the grue is saying. Its time to go or shoot!(type go or shoot!)")
        elif rooms[currentRoom].get('monster') == None:
            print("The still warm body of Elmer Grue is all that remains in the garden")
        elif rooms[currentRoom]['monster'][0] == 'peaceful':
            print(f"Elmer Grue tips his hat from his rocking chair. Only the peaceful grue remains in the garden")
        elif 'big gun' not in inventory and 'translator' not in inventory and rooms[currentRoom].get('monster') != None:
            print(f"{rooms[currentRoom].get('monster')[0].title()} stands before and appears to be saying something!")
            print("Wort Wort Wort!!!")
            print("Without a translator you have no idea what the grue is saying. Its time to go!")
        elif rooms[currentRoom].get('monster') != None and "translator" in inventory and 'corn seeds' in inventory and 'rocking chair' in inventory:
            print("Thank you adventurer! Here is the key as promised!")
            rooms[currentRoom]['monster'].remove('elmer grue')
            rooms[currentRoom]['monster'].append('peaceful')
            inventory.append(reward)
            inventory.remove('corn seeds')
            inventory.remove('rocking chair')
        elif rooms[currentRoom].get('monster') != None and "translator" in inventory and 'corn seeds' in inventory:
            print("So close! Just need the rocking chair now!")
        elif rooms[currentRoom].get('monster') != None and "translator" in inventory and 'rocking chair' in inventory:
            print("So close! Just need the corn seeds now! now!")
        elif rooms[currentRoom].get('monster') != None and "translator" in inventory and rooms[currentRoom].get('monster') != 'peaceful':
            print('Don\'t shoot adventurer!! I am friendly!! I just want to grow some corn and sit in a rocking chair!')
            print('If you bring me what I need I will give you one of the keys to leave this place!')
            choice = input("Accept the grue's quest? Y/N\n>")
            if choice.lower() == 'y':
                print("Thank you adventurer! I just need some corn seeds and a rocking chair! good luck!")
            else:
                print("In a rage the grue kills you. Guess he wasnt so nice...better luck next time!")
                break
    
    # handles Animal Pen Logic
    if currentRoom == 'Animal Pen':
        reward = 'exit key 2'
        if 'big gun' in inventory and 'translator' not in inventory and rooms[currentRoom].get('monster') != None:
            print(f"{rooms[currentRoom].get('monster')[0].title()} stands before and appears to be saying something!")
            print("Warble Warble Warble!!!")
            print("Without a translator you have no idea what the grue is saying. Its time to go or shoot!(type go or shoot!)")
        elif rooms[currentRoom].get('monster') == None:
            print("The still warm body of Gorilla Grue is all that remains in the Animal Pen")
        elif rooms[currentRoom]['monster'][0] == 'peaceful':
            print(f"Gorilla Grue waves from his hammock in the trees. Only the peaceful grue remains in the Animal Pen")
        elif 'big gun' not in inventory and 'translator' not in inventory and rooms[currentRoom].get('monster') != None:
            print(f"{rooms[currentRoom].get('monster')[0].title()} stands before and appears to be saying something!")
            print("Warble Warble Warble!!!")
            print("Without a translator you have no idea what the grue is saying. Its time to go!")
        elif rooms[currentRoom].get('monster') != None and "translator" in inventory and inventory.count('banana') == 2:
            print("Thank you adventurer! Here is the key as promised!")
            rooms[currentRoom]['monster'].remove('gorilla grue')
            rooms[currentRoom]['monster'].append('peaceful')
            inventory.append(reward)
            inventory.remove('banana')
            inventory.remove('banana')
        elif rooms[currentRoom].get('monster') != None and "translator" in inventory and inventory.count('banana') == 1:
            print("Just one more banana and the key is yours!")
        elif rooms[currentRoom].get('monster') != None and "translator" in inventory:
            print('Don\'t shoot adventurer!! I am friendly!! I just need 2 bananas to help me with these awful charlie horses!')
            print('If you bring me what I need I will give you one of the keys to leave this place!')
            choice = input("Accept the grue's quest? Y/N\n>")
            if choice.lower() == 'y':
                print("Thank you adventurer! I just need some corn seeds and a rocking chair! good luck!")
            else:
                print("In a rage the grue kills you. Guess he wasnt so nice...better luck next time!")
                break
  
    # handles Beat Lab logic
    if currentRoom == 'Beat Lab':
        print(f"A wild Kanye has appeared in the {currentRoom}! What wisdom does he have for you adventurer?")
        if "translator" in inventory:
            print("You have found the lair of the all-knowing Yeezy! Let me see how your progress is going so far...")
            if rooms['Animal Pen'].get('monster') == None and rooms['Garden'].get('monster') == None:
                print('You killed both Elmer and Gorilla Grue!?!?! Well I dont know what you are doing here then! You should have the exit keys already. Go on and get...')
            elif rooms['Garden'].get('monster') == None:
                print('You killed Elmer Grue?!?!?! He only wanted to grow corn and sit in his rocking chair! You monster!!!!')
                print('Well at least Gorilla Grue is still alive...get him some bananas and he may offer you a reward')
            elif rooms['Animal Pen'].get('monster') == None:
                print('You killed Gorilla Grue?!?!?! He only wanted bananas for his cramps!!!!')
                print('Well at least Elmer Grue is still alive.' + 
                ' Word on the street is that if you get him top soil, overalls, corn seeds, and a rocking chair he has a special reward!')
            else:
                print('Good to see both the grues are still kicking. They are actually nice dudes')
                print('Word on the street is that if you get Elmer top soil, overalls, corn seeds, and a rocking chair he has a special reward!')
                print('Also heard ol Gorilla Grue is just looking for 2 bananas to cure his charlie horses. Im sure he\'d reward you for your trouble')
        else:
            kanye_quote_getter = requests.get(kanye_gibberish).json()
            kanye_no_translator = kanye_quote_getter["quote"]
            print(kanye_no_translator)
            print("Well...that was utter nonsense...maybe there is a translator somewhere in the house that can help you out.")

    # Handles Exit room and win coditions with all endings good, less bad, bad
    if currentRoom == 'Exit':
        if 'exit key 1' in inventory and 'exit key 2' in inventory:
            if rooms['Animal Pen'].get('monster') == None and rooms['Garden'].get('monster') == None: 
                print("This is the bad ending! You chose to murder the poor grue of this house to gain your freedom. Good riddance!")
                break
            elif rooms['Garden'].get('monster') == None:
                print("This is the less bad ending. You may have murdered poor Elmer Grue but you did not kill Gorilla Grue. Kanye isn\'t mad, just dissappointed. Good day adventurer...")
                break
            elif rooms['Animal Pen'].get('monster') == None:
                print("This is the less bad ending. You may have murdered poor Elmer Grue but you did not kill Gorilla Grue. Kanye isn\'t mad, just dissappointed. Good day adventurer...")
                break
            else:
                print("You unlocked the good ending! Sure it took a lot longer and you don't actually get anything for it but...you can at least say you are a good person!")
                break
        else:
            print('The exit door requires 2 keys to be unlocked. Keep looking adventurer!!')

