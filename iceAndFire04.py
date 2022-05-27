#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def char_titles(name, titles):
        if titles[0] != '':
                print(f"{name} held the following titles:\n---------------------------------------------------")
                for title in titles:
                        print(f">{title}")
        else:
                print(f"{name} did not hold any titles")

def char_aliases(name, aliases):
        if aliases[0] != '':
                print(f"{name} also went by the following aliases:\n----------------------------------------------------------")
                for alias in aliases:
                        print(f">{alias}")
        else:
                print(f"{name} did not have any aliases\n")

def char_info(name, gender, born, titles, aliases):
        if born != '':
                date_born = born
        else:
                date_born = 'DATE NOT AVAILABLE/UNKNOWN'

        print(f"{name}, ({gender}), was born {date_born}.")
        print()
        char_titles(name, titles)
        print()
        char_aliases(name, aliases)
        print()


def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        
        char_info(got_dj['name'], got_dj['gender'], got_dj['born'], got_dj['titles'], got_dj['aliases'])

if __name__ == "__main__":
        main()

