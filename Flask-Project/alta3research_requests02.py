#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

deadAPI = "http://10.6.163.119:2224/deadpooljson"

def char_powers(name, powers):   
    with open("deadpool_facts.txt", "a") as deadpool_facts:
        deadpool_facts.write(f"{name} has the following powers:\n---------------------------------------------------\n")
        for power in powers:
            deadpool_facts.write(f">{power}\n")
        deadpool_facts.write("\n")

def char_abilities(name, abilities):       
    with open("deadpool_facts.txt", "a") as deadpool_facts:
        deadpool_facts.write(f"{name} has the following abilities:\n---------------------------------------------------\n")
        for ability in abilities:
            deadpool_facts.write(f">{ability}\n")
        deadpool_facts.write("\n")
    


def char_weaknesses(name, weaknesses):      
    with open("deadpool_facts.txt", "a") as deadpool_facts:
        deadpool_facts.write(f"{name} has the following weaknesses:\n---------------------------------------------------\n")
        for weakness in weaknesses:
            deadpool_facts.write(f">{weakness}\n")
        deadpool_facts.write("\n")

def char_info(name, realName, alsoKnown, since, powers, abilities, weaknesses):    
    with open("deadpool_facts.txt", "w") as deadpool_facts:
        deadpool_facts.write(f"{name}, real name ({realName}), also went by \"{alsoKnown}\" and was introduced in {since}.\n\n")
    
    char_powers(name, powers)
    print()
    
    char_abilities(name, abilities)
    print()

    char_weaknesses(name, weaknesses)
    print()

    

def main():
    ## Send HTTPS GET to the custom Deadpool API
    deadresp = requests.get(deadAPI)

    ## Decode the response
    deadInfo = deadresp.json()
    
    char_info(deadInfo[0]['name'], deadInfo[0]['realName'], deadInfo[0]['alsoKnown'], deadInfo[0]['since'], deadInfo[0]['powers'], deadInfo[0]['abilities'], deadInfo[0]['weaknesses'] )
    with open("deadpool_facts.txt", "r") as deadfile:
        for line in deadfile:
            print(line, end="")

if __name__ == "__main__":
    main()