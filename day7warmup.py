#!/usr/bin/env python3

import requests
import datetime
import sys
import time
import os
import reverse_geocoder as rg

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def west_or_east(longitude):
    if longitude > 0:
        return "E"
    else:
        return "W"

def west_or_east(latitude):
    if latitude > 0:
        return "E"
    else:
        return "W"



def main():
    ISS_API = "http://api.open-notify.org/iss-now.json"
    country_API = "https://restcountries.com/v3.1/alpha/"

    iss_loc_data = requests.get(ISS_API).json()
    iss_epoch_timestamp = iss_loc_data['timestamp']
    iss_standard_timestamp = datetime.datetime.fromtimestamp(iss_epoch_timestamp)
    lat = iss_loc_data['iss_position']['latitude']
    lon = iss_loc_data['iss_position']['longitude']

    coords_tuple = (lat, lon)
    result = rg.search(coords_tuple)

    country_info = requests.get(country_API + result[0]['cc']).json()
    country_name = country_info[0]['name']['common']

    print("Current Location OF THE ISS:")
    print(f"Timestamp: {iss_standard_timestamp}\nLat: {lat}\nLon: {lon}\nCity/Country: {result[0]['name']}, {country_name}({result[0]['cc']})")

if __name__ == "__main__":
    x = 0
    while x < 60:
        cls()
        main()
        x +=1
        time.sleep(2.5)
        