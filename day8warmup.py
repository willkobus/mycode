#!/usr/bin/env python3

zodiac = [
    'your chinese zodiac sign is Monkey, you are sharp, smart, curious, and mischievious.',
    'your chinese zodiac sign is Rooster, you are hardworking, resourceful, courageous, and talented.',
    'your chinese zodiac sign is Dog, you are loyal, honest, cautious, and kind.',
    'your chinese zodiac sign is Pig, you are a symbol of wealth, honesty, and practicality.',
    'your chinese zodiac sign is Rat, you are artistic, sociable, industrious, charming, and intelligent.',
    'your chinese zodiac sign is Ox, you are strong, thorough, determined, loyal, and reliable.',
    'your chinese zodiac sign is Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader.',
    'your chinese zodiac sign is Rabbit, you are vigilant, witty, quick-minded, and ingenious.',
    'your chinese zodiac sign is Dragon, you are talented, powerful, lucky, and successfull.',
    'your chinese zodiac sign is Snake, you are wise, like to work alone, and determined.',
    'your chinese zodiac sign is Horse, you are animated, active, and energetic.',
    'your chinese zodiac sign is Sheep, you are creative, resilient, gentle, mild-mannered, and shy.'
]


def main():    
    usr_name = input("Please enter your name:\n>") 
              
    usr_name = usr_name.title()    
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
    theNumber = usr_date % 12
    

    
    print(f"{usr_name}, {zodiac[theNumber]}")

main()