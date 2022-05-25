#!/usr/bin/env python3

import json
import yaml

with open("classdata.json","r") as jsonfile:
    x= json.load(jsonfile)

# create new python dictionary to be added
new= {
      "name":"Chad",
      "awesome": False,
      "number": 0,
      "favorites":{
          "movie":"The Shawshank Redemption",
          "ice cream":"salted caramel",
          "color":"red"}
     }

# add to data read in from json file
x.append(new)

# open a yaml file and dump the changed data inside it
with open("classdataedit.yml","w") as yamlfile:
    yaml.dump(x, yamlfile)