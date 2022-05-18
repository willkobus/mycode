Deadpool={'Real name':'Wade Winston Wilson','Team Affiliations':['Thunderbolts','X-Force','Agency X','Deadpool Corps.','Great Lakes Initiative','Weapon X','Landau','Luckman, and Lake','Maggia','Frightful Four','Secret Defenders','Heroes for Hire','Six Pack','X-Men'],'Aliases':['Merc with a Mouth','Jack','Wade T. Wilson','Mithras','Johnny Silvini','Thom Cruz (when confused for Tom Cruise after a magic spell restores his face)','Hulkpool (after turned into a hulk)','Wildcard'],'Base of Operations':'Nomadic','Powers':['Accelerated Healing Factor','Extended longevity','Immunity to telepathy','teleportation (aided by machine)','holographic disguise (aided by machine)','Superhuman stamina','agility','flexibility and reflexes','may or may not be aware of the world beyond the fourth wall (IE, might know he is fictional)']}

Deadpool["Celebrity crush"] = "Ryan Reynolds"
print("Want to know more about Deadpool?")
print("Available Keys are: ")
print(Deadpool.keys())

choice = input("Enter a key to see it's associated value.\n>")
x = True
while x == True:
    
    if (Deadpool.get(choice) != None):
        print(Deadpool.get(choice))
        again = input("Enter a Y to see another key's info or any other key to exit.\n>")
        if again.lower() == "y":
            print("Available Keys are: ")
            print(Deadpool.keys())
            choice = input("Enter a key to see it's associated value.\n>")
        else:
            print("Mr. Pool thanks you for you curiosity!")
            break;
    else:
            print(f"Sorry, {choice} isn't an available key. Keys are case sensitive! Try again!")
            print("Available Keys are: ")
            print(Deadpool.keys())
            choice = input("Enter a key to see it's associated value.\n>")

