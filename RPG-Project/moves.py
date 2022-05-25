import time
 #if they type 'go' first
def go(move, rooms, currentRoom):
    
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
        #set the current room to the new room
        currentRoom = rooms[currentRoom][move[1]]
        return currentRoom
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
        return currentRoom
    #if they type 'get' first
def get(move, rooms, currentRoom, inventory):
     
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
def shoot(move, rooms, currentRoom, inventory):
    
        if 'big gun' in inventory:
    #if the room contains an item, and the item is the one they want to get
            if "monster" in rooms[currentRoom] and move[1].lower() in rooms[currentRoom]['monster']:
                i = rooms[currentRoom]['monster'].index(move[1])
                time.sleep(.5)
                           
            #display a helpful message
            print(move[1] + ' is no more!')
            time.sleep(.5)
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

test = "test importing a non function"