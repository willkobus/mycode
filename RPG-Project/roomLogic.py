import requests
import os
import time

# link to kanye west api, KanyeREST
kanye_gibberish = "https://api.kanye.rest/"

# Handles garden logic
def garden(inventory, rooms, currentRoom):
        # reward for completing Elmer Grue Quest
        reward = 'exit key 1'
        # logic for if plater has the big gun in inventory but does not have the translator and monster is in the room
        if 'big gun' in inventory and 'translator' not in inventory and rooms[currentRoom].get('monster') != None:
            print(f"{rooms[currentRoom].get('monster')[0].title()} stands before and appears to be saying something!")
            time.sleep(2)
            print("Wort Wort Wort!!!")
            time.sleep(2)
            print("Without a translator you have no idea what the grue is saying. He seems dangerous! Its time to go or shoot!(type go or shoot!)")
        # logic for if the player has killed the monster and returns to the room    
        elif rooms[currentRoom].get('monster') == None:
            print("The still warm body of Elmer Grue is all that remains in the garden")
        # logic for if the player completed the monster's quest and returns to the room     
        elif rooms[currentRoom]['monster'][0] == 'peaceful':
            print(f"Elmer Grue tips his hat from his rocking chair. Only the peaceful grue remains in the garden")
        # logic for if the player enters the garden without the big gun and the translator while monster is still in it and not peaceful
        elif 'big gun' not in inventory and 'translator' not in inventory and rooms[currentRoom].get('monster') != None:
            print(f"{rooms[currentRoom].get('monster')[0].title()} stands before and appears to be saying something!")
            time.sleep(2)
            print("Wort Wort Wort!!!")
            time.sleep(2)
            print("Without a translator you have no idea what the grue is saying. He seems dangerous! Better go!")
        #logic for if the player 
        elif rooms[currentRoom].get('monster') != None and "translator" in inventory and 'corn seeds' in inventory and 'rocking chair' in inventory:
            print("Thank you adventurer! Here is the key as promised!")
            rooms[currentRoom]['monster'].remove('elmer grue')
            rooms[currentRoom]['monster'].append('peaceful')
            inventory.append(reward)
            inventory.remove('corn seeds')
            inventory.remove('rocking chair')
        elif rooms[currentRoom].get('monster') != None and "translator" in inventory and 'corn seeds' in inventory:
            print("The Key is almost yours! Just need the rocking chair now!")
        elif rooms[currentRoom].get('monster') != None and "translator" in inventory and 'rocking chair' in inventory:
            print("The Key is almost yours! Just need the corn seeds now!")
        elif rooms[currentRoom].get('monster') != None and "translator" in inventory and rooms[currentRoom].get('monster') != 'peaceful':
            print('Don\'t shoot adventurer!! I am friendly!! I just want to grow some corn and sit in a rocking chair!')
            time.sleep(2)
            print('If you bring me what I need I will give you one of the keys to leave this place!')
            time.sleep(2)
            choice = input("Accept the grue's quest? Y/N\n>")
            if choice.lower() == 'y':
                print("Thank you adventurer! I just need some corn seeds and a rocking chair! good luck!")
            else:
                print("In a rage the grue kills you. Guess he wasnt so nice...better luck next time!")
                return "game over"
    
# handles Animal Pen Logic
def animalPen(inventory, rooms, currentRoom):
    if currentRoom == 'Animal Pen':
        reward = 'exit key 2'
        if 'big gun' in inventory and 'translator' not in inventory and rooms[currentRoom].get('monster') != None:
            print(f"{rooms[currentRoom].get('monster')[0].title()} stands before and appears to be saying something!")
            time.sleep(2)
            print("Warble Warble Warble!!!")
            time.sleep(2)
            print("Without a translator you have no idea what the grue is saying. He seems dangerous! Its time to go or shoot!(type go or shoot!)")
        elif rooms[currentRoom].get('monster') == None:
            print("The still warm body of Gorilla Grue is all that remains in the Animal Pen")
        elif rooms[currentRoom]['monster'][0] == 'peaceful':
            print(f"Gorilla Grue waves from his hammock in the trees. Only the peaceful grue remains in the Animal Pen")
        elif 'big gun' not in inventory and 'translator' not in inventory and rooms[currentRoom].get('monster') != None:
            print(f"{rooms[currentRoom].get('monster')[0].title()} stands before and appears to be saying something!")
            time.sleep(2)
            print("Warble Warble Warble!!!")
            time.sleep(2)
            print("Without a translator you have no idea what the grue is saying. Better go!")
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
            time.sleep(2)
            print('If you bring me what I need I will give you one of the keys to leave this place!')
            time.sleep(2)
            choice = input("Accept the grue's quest? Y/N\n>")
            if choice.lower() == 'y':
                print("Thank you adventurer! I just need some corn seeds and a rocking chair! good luck!")
            else:
                print("In a rage the grue kills you. Guess he wasnt so nice...better luck next time!")
                return "game over"
  
# handles Beat Lab logic
def beatLab(inventory, rooms, currentRoom):
    if currentRoom == 'Beat Lab':
        print(f"A wild Kanye has appeared in the {currentRoom}! What wisdom does he have for you adventurer?")
        time.sleep(2)
        if "translator" in inventory:
            print("You have found the lair of the all-knowing Yeezy! Let me see how your progress is going so far...")
            time.sleep(2)
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
            time.sleep(2)
            print("Well...that was utter nonsense...maybe there is a translator somewhere in the house that can help you out.")

def exit(inventory, rooms, currentRoom):
    # Handles Exit room and win coditions with all endings good, less bad, bad
    if currentRoom == 'Exit':
        if 'exit key 1' in inventory and 'exit key 2' in inventory:
            if rooms['Animal Pen'].get('monster') == None and rooms['Garden'].get('monster') == None: 
                print("This is the bad ending! You chose to murder the poor grue of this house to gain your freedom. Good riddance!")
                return "game over"
            elif rooms['Garden'].get('monster') == None:
                print("This is the less bad ending. You may have murdered poor Elmer Grue but you did not kill Gorilla Grue. Kanye isn\'t mad, just dissappointed. Good day adventurer...")
                return "game over"
            elif rooms['Animal Pen'].get('monster') == None:
                print("This is the less bad ending. You may have murdered poor Elmer Grue but you did not kill Gorilla Grue. Kanye isn\'t mad, just dissappointed. Good day adventurer...")
                return "game over"
            else:
                print("You unlocked the good ending! Sure it took a lot longer and you don't actually get anything for it but...you can at least say you are a good person!")
                return "game over"
        else:
            print('The exit door requires 2 keys to be unlocked. Keep looking adventurer!!')